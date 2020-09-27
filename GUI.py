import cv2
import pytesseract
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

#windows display functions
window = tkinter.Tk()
window.title("Image2Text")
window.geometry("800x800")

l = Label(window, text = "Extracted Text") 
l.config(font =("Courier", 14))
l.place(x=530, y=20)

l1 = Label(window, text = "Image") 
l1.config(font =("Courier", 14))
l1.place(x=150, y=20)


def UploadAction():
	global filename
	filename = filedialog.askopenfilename(filetypes=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif','.tiff', '.tif', '.bmp'])])
	im = Image.open(filename).resize((400,400))
	photo = ImageTk.PhotoImage(im)
	text1 = tkinter.Label(window, image = photo)
	text1.image = photo
	text1.place(x=20, y=50)
    
def GenerateText():
	text = list(pytesseract.image_to_string(filename).split('\n'))
	while("" in text):
		text.remove("")
	text =''.join(text)
	label = Text(window, height = 25, width = 44)
	label.insert(tkinter.END, text)
	label.place(x=440, y=50)


button = tkinter.Button(window, text='UploadFile', command = UploadAction)
button1 = tkinter.Button(window, text='GenerateText', command= GenerateText)
button.place(x=180, y=500)
button1.place(x=600, y=500)

window.mainloop()

