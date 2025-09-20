import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dimensions = (width, height)
f = cv2.VideoWriter_fourcc(*"mp4v")
name = input('Enter the name of the file which you want to save : ') # Taking input from the user for the name of the file
file_name = f"{name}.mp4"  # Appending .mp4 to the file name
output = cv2.VideoWriter(file_name, f , 30, dimensions)

obj= input('Enter the second you wnat to record: ') # Taking input from the user for the number of seconds to record
now_time = time.time()
duration = int(obj) # seconds
print("Recording started...")
end_time = now_time + duration

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    remaining = int(end_time - time.time())
    print(f"\rRecording... {remaining}s left", end='')
    current_time = time.time()
    if current_time > end_time:
        break
output.release()

print(f"Recording finished and store where you save this exe file and saved as {name}.mp4")

