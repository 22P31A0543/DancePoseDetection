# 💃 Dance Pose Detection with MediaPipe & OpenCV

A real-time **pose detection system** that captures and visualizes full-body human movement through your webcam. Built using **MediaPipe** and **OpenCV**, this project can be extended to applications like dance tracking, gesture control, fitness posture correction, and more!

---

## 🔍 Overview

This project detects body landmarks from a webcam video stream, flips the view like a mirror, and overlays pose connections to visualize real-time human movement. It’s designed to run fast and smooth using TensorFlow Lite and XNNPACK delegate.

---

## 🎯 Features

- 🔵 Real-time pose tracking using webcam
- 🔄 Mirror (flipped) video feed for natural interaction
- 🔺 Draws pose landmarks and connections on the body
- 📊 Displays frame rate (FPS) live
- 🧠 Uses MediaPipe's built-in pose estimation model

---

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**: MediaPipe, OpenCV, NumPy
- **Model**: MediaPipe Pose Landmark model (TensorFlow Lite backend)

---

## ▶️ How to Run

### 🔹 Prerequisites

Install dependencies:

```bash
pip install mediapipe opencv-python numpy
