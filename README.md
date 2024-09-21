# **Speech Segment Extractor**

### **Overview**

**Speech Segment Extractor** is a Python-based web application that allows users to upload a video file and extract only the segments that contain speech. The application removes silent sections, processes the video using OpenAI's Whisper model, and outputs the segments with speech as a downloadable file.

The project is built using **Gradio** for the web interface, **FFmpeg** for video processing, and **OpenAI's Whisper** model for speech detection.

### **Features**

- Upload video files in various formats (MP4, MKV, AVI, etc.).
- Extract only the segments where speech occurs, removing silences.
- Download the speech segments as a ZIP file containing individual video files.
- Supports configurable Whisper model sizes and customizable speech merge thresholds.

---

## **Table of Contents**

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Customization](#customization)
- [License](#license)

---

## **Requirements**

Before running the application, ensure you have the following dependencies installed:

- Python 3.7 or higher
- FFmpeg (for video processing)
- Torch (PyTorch)
- OpenAI Whisper
- Gradio

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/speech-segment-extractor.git
cd speech-segment-extractor
```

### **2. Create and Activate a Virtual Environment (Optional but Recommended)**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### **3. Install the Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Install FFmpeg**

You need to install FFmpeg for video processing. Here’s how to install it:

- **macOS** (using Homebrew):

  ```bash
  brew install ffmpeg
  ```

- **Windows**:

  1. Download FFmpeg from [the official site](https://ffmpeg.org/download.html).
  2. Extract the files and add the `bin` folder to your system's PATH.

- **Linux**:

  ```bash
  sudo apt install ffmpeg
  ```

---

## **Usage**

### **1. Run the Application**

After installing the dependencies, run the application with:

```bash
python app.py
```

### **2. Access the Web Interface**

Once the application is running, open your browser and go to:

```
http://127.0.0.1:7860/
```

### **3. Upload a Video File**

- Use the file uploader to upload a video (max 100MB).
- Choose the Whisper model size (e.g., `tiny`, `base`).
- Set the merge threshold to adjust how close speech segments should be merged.

### **4. Download Speech Segments**

After processing, you will receive a ZIP file containing the speech segments extracted from the video.

---

## **Deployment**

### **Hugging Face Spaces**

This application can easily be deployed on Hugging Face Spaces:

1. **Create a Hugging Face Account**: If you don’t already have one, sign up at [Hugging Face](https://huggingface.co).
2. **Create a New Space**: In your Hugging Face account, create a new Space.
3. **Connect GitHub Repository**: Set up your Space to pull code directly from this GitHub repository.
4. **Deployment**: Hugging Face will automatically install the dependencies and deploy your application.

### **Other Hosting Options**

You can deploy the app on platforms like Heroku, AWS, DigitalOcean, etc. Refer to the platform's documentation for specific deployment instructions.

---

## **Customization**

You can customize the following aspects of the application:

1. **Model Size**: Modify the default Whisper model by changing the `model_size` parameter in the app.
2. **Merge Threshold**: Adjust the `merge_threshold` slider to control how close speech segments should be merged.
3. **UI Customization**: You can modify the Gradio interface by editing the layout in `app.py`. If you want more control over the frontend design, consider using frameworks like Flask or FastAPI with a custom frontend.

---

## **Contributing**

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Contributions are welcome!

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any issues or inquiries, feel free to open an issue on GitHub or contact me directly.

---

### **Final Notes**

Remember to update the repository URL, and any other personal contact or customization info as needed. This README file provides a comprehensive guide to your application and should make it easy for others to use, install, and contribute to the project.

Let me know if you need any further customization!
