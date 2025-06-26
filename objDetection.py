import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
import os, time

def speech(text):
    print(text)
    os.makedirs("sounds", exist_ok=True)
    filename = f"./sounds/{int(time.time() * 1000)}.mp3"
    gTTS(text=text, lang="en", slow=False).save(filename)
    playsound(filename)
    try: os.remove(filename)
    except: pass

# Initialize webcam
video = cv2.VideoCapture(0)
labels = []

if not video.isOpened():
    print("❌ Could not open webcam")
    exit()

while True:
    ret, frame = video.read()
    if not ret: break

    bbox, label, conf = cv.detect_common_objects(frame, model='yolov3', confidence=0.5)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("Object Detection", output_image)

    for item in label:
        if item not in labels:
            labels.append(item)
            print("🔍 Detected:", item)
            speech(f"I see a {item}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()

# Final spoken summary
sentence = "I found " + ", ".join([f"a {l}" for l in labels[:-1]]) + (f", and a {labels[-1]}" if len(labels) > 1 else "")
print("\n🧾 Final labels detected:", labels)
print("🗣️ Summary:", sentence)
speech(sentence)
