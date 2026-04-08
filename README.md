# 🤖 Real-Time Object Detection (YOLOv8 + OpenCV)

A Python-based **AI Object Detection System** that uses **YOLOv8** to detect and label objects in real-time using your webcam.

This project demonstrates **state-of-the-art deep learning** used in real-world applications like autonomous driving and surveillance.

---

# 🚀 Features

✔ Real-time object detection using webcam
✔ Uses YOLOv8 (Ultralytics) model
✔ Detects multiple objects simultaneously
✔ Displays bounding boxes with labels
✔ Fast and efficient detection
✔ Easy to upgrade to higher accuracy models

---

# 🛠 Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* Deep Learning (Computer Vision)

---

# 📂 Project Structure

```id="q8m2zl"
yolov8-object-detection
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for clean structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="x3n7kl"
pip install opencv-python ultralytics
```

---

# ▶️ How to Run

```bash id="k2p9zl"
git clone https://github.com/ravigautam7739/yolov8-object-detection.git
cd yolov8-object-detection
python main.py
```

---

# 🧠 How It Works

1. Loads **YOLOv8 model (yolov8n.pt)**
2. Webcam captures live video
3. Each frame is passed to the model
4. Model detects objects using deep learning
5. Bounding boxes + labels are drawn on screen

---

# 💻 Example Output

```id="m7p2wl"
Detected Objects:

Person 🧍
Laptop 💻
Mobile 📱
Bottle 🧴
```

Displayed with bounding boxes in real-time.

---

# ⚙️ Model Options

You can switch models for better performance:

```id="p9k3xt"
yolov8n.pt → Fast (default)
yolov8s.pt → Better accuracy
yolov8m.pt → High accuracy
```

---

# 🎯 Use Cases

* Smart surveillance systems
* Autonomous vehicles
* Security monitoring
* Retail analytics
* AI learning projects

---

# ⚠️ Notes

* Requires webcam
* First run may download YOLO model
* GPU improves performance (optional)
* Works on CPU as well

---

# 🔮 Future Improvements

* Custom object detection
* Train your own model
* Object tracking
* Save detection results
* GUI dashboard

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and advanced computer vision projects**.

Stay tuned 🚀
