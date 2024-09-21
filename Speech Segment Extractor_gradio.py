import gradio as gr
import os
import shutil
import whisper
import torch
import subprocess

def process_video(input_video, model_size='base', merge_threshold=0.3):
    try:
        # Ensure the input_video is a valid file path
        if not os.path.isfile(input_video):
            return "Invalid file path."

        # Limit file size (e.g., 100MB)
        max_file_size = 100 * 1024 * 1024  # 100MB
        if os.path.getsize(input_video) > max_file_size:
            return "File size exceeds the maximum allowed limit of 100MB."

        # Load Whisper model
        device = 'cpu'  # Hugging Face Spaces free tier doesn't support GPU
        model = whisper.load_model(model_size, device=device)

        # Transcribe audio and get word-level timestamps
        result = model.transcribe(input_video, word_timestamps=True)
        segments = result['segments']

        # Extract speech intervals from words
        speech_intervals = []
        for segment in segments:
            words = segment.get('words', [])
            for word_info in words:
                start = word_info.get('start')
                end = word_info.get('end')
                if start is not None and end is not None:
                    speech_intervals.append((start, end))

        # Merge speech intervals
        speech_intervals = merge_speech_intervals(speech_intervals, merge_threshold)

        # Extract speech segments
        output_dir = 'output_segments'
        extract_speech_segments(input_video, speech_intervals, output_dir)

        # Zip the output directory
        shutil.make_archive('speech_segments', 'zip', output_dir)

        # Clean up temporary files
        shutil.rmtree(output_dir)

        # Return the path to the ZIP file
        return 'speech_segments.zip'

    except Exception as e:
        return f"An error occurred: {str(e)}"

def merge_speech_intervals(speech_intervals, merge_threshold):
    if not speech_intervals:
        return []
    speech_intervals.sort(key=lambda x: x[0])
    merged_intervals = [speech_intervals[0]]
    for current in speech_intervals[1:]:
        previous = merged_intervals[-1]
        if current[0] - previous[1] <= merge_threshold:
            merged_intervals[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged_intervals.append(current)
    return merged_intervals

def extract_speech_segments(input_video, speech_intervals, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for idx, (start, end) in enumerate(speech_intervals):
        if end <= start:
            continue
        output_file = os.path.join(output_dir, f'segment_{idx+1:03d}.mp4')
        duration = end - start
        command = [
            'ffmpeg', '-y', '-ss', f"{start:.3f}", '-i', input_video,
            '-t', f"{duration:.3f}",
            '-c', 'copy', output_file
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

iface = gr.Interface(
    fn=process_video,
    inputs=[
        gr.File(label="Input Video", type="filepath", file_count="single", file_types=['.mp4', '.mkv', '.avi', '.mov']),
        gr.Dropdown(choices=['tiny', 'base'], value='base', label="Model Size"),
        gr.Slider(0.0, 1.0, step=0.1, value=0.3, label="Merge Threshold (seconds)")
    ],
    outputs=gr.File(label="Download Speech Segments"),
    title="Speech Segment Extractor",
    description="Upload a video file (max 100MB) to extract speech segments by removing silences."
)

if __name__ == "__main__":
    iface.launch()
