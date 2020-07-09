import tkinter as tk
from PIL import Image, ImageDraw
width = 100
height = 100
white = (255, 255, 255)
green = (0,128,0)

def save():
    filename = "image.png"
    image1.save(filename)
    root.destroy()

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1) 
    x2, y2 = (event.x + 1), (event.y + 1) 
    cv.create_oval([x1, y1, x2, y2],fill = "black", width=5)
    draw.line([x1, y1, x2, y2], fill = "black", width=5)

root = tk.Tk()

cv = tk.Canvas(root, width=width, height=height, bg='white')
cv.pack()

image1 = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

cv.pack(expand=tk.YES, fill=tk.BOTH)
cv.bind("<B1-Motion>", paint)

button = tk.Button(text="Save", command = save)
button.pack()
root.mainloop()