# Object-Detection

Real-Time Object Detection with Voice Feedback
This project uses OpenCV, cvlib, YOLOv3, and gTTS (Google Text-to-Speech) to detect objects in real time using your webcam and announce them aloud.

📸 Demo
✅ Detects objects like person, chair, bottle, cell phone, etc.
🗣️ Speaks: "I see a bottle", "I see a person"...
📋 Summarizes: "I found a person, a chair, and a laptop"

🧰 Requirements
Make sure Python 3.11+ is installed.

📦 Install dependencies:
pip install opencv-python cvlib gTTS playsound
💡 cvlib will automatically download YOLOv3 model files (.cfg, .weights, .txt) on first run, or you can manually place them in your working directory:

yolov3.cfg
yolov3.weights
yolov3.txt

🧠 How It Works
Opens your default webcam.
Detects objects using YOLOv3.
Draws bounding boxes and shows video in a live window.
Speaks out each newly detected object.
On pressing q, prints and speaks a final summary of detected objects.

▶️ Run the Project
python objDetection.py
Press q to stop the webcam and hear the final summary.

📁 Project Structure

├── objDetection.py         # Main Python script
├── yolov3.cfg              # YOLOv3 config file
├── yolov3.weights          # YOLOv3 weights
├── yolov3.txt              # COCO labels
├── /sounds/                # (Auto-created) temporary mp3 files for speech
🎤 Voice Output
Uses gTTS to convert text to speech.
Plays audio using playsound.
Temporary .mp3 files are cleaned up automatically.

💡 Notes
Requires internet connection for gTTS.
If you want offline TTS, consider replacing gTTS with pyttsx3.
Works best with a well-lit webcam feed.


