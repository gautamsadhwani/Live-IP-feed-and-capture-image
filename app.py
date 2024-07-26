

import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import datetime
import threading

HTTP_URL = 'http://mmb.aa1.netvolante.jp:1025/mjpg/video.mjpg?resolution=640x360&compression=50'

class WebcamApp:
    def __init__(self, window):
        self.window = window
        self.window.title = ("WebCam App")

        self.video_capture = cv2.VideoCapture(HTTP_URL)

        self.current_image = None
        self.canvas = tk.Canvas(window, width=640, height= 480)
        self.canvas.pack()

        self.download_button = tk.Button(window, text="Capture", command= self.download_image)
        self.download_button.pack()

        self.update_webcam()

    def update_webcam(self):
       ret, frame = self.video_capture.read()

       if ret:
          self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
          self.photo = ImageTk.PhotoImage(image= self.current_image)
          self.canvas.create_image(0,0, image=self.photo, anchor= tk.NW)
         
          self.window.after(15, self.update_webcam)
    
    def download_image(self):
        if self.current_image is not None:
            file_path = os.path.expanduser("~/Downloads/captures_image.jpg")
            self.current_image.save(file_path)
            os.startfile(file_path)



root = tk.Tk()
url = 'http://mmb.aa1.netvolante.jp:1025/mjpg/video.mjpg?resolution=640x360&compression=50'
app = WebcamApp(root)
root.mainloop()