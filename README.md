# 🎥 Python Screen Recorder

A lightweight **screen recording tool** built in Python using **OpenCV**, **PyAutoGUI**, and **Win32 API**.  
This program captures your screen and saves it as an **MP4 video file**.

---

## ✨ Features
- 📺 Records the **entire screen**  
- ⏱️ User can set **custom recording duration** (in seconds)  
- 💾 Saves the recording as `.mp4` with a **user-defined filename**  
- 📊 Displays remaining recording time in real-time  

---

## 🛠️ Requirements
Make sure you have the following installed:

```bash
pip install opencv-python numpy pyautogui pywin32
```
🚀 How to Run

Clone the repository:
```bash
git clone https://github.com/swapnanil99/py_screen_recoder.git
cd py_screen_recorder
```
Run the script:
```bash
python py_screen_recorder.py
```
💻 Example Usage
- Enter the name of the file which you want to save : demo
- Enter the second you want to record: 10
- Recording started...
- Recording... 9s left
- Recording... 8s left
...
- Recording finished and saved as demo.mp4
