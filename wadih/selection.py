import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.attributes("-fullscreen", True)

imagePath = "plz.png"

# Open the image using Pillow
originalImage = Image.open(imagePath)

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Resize the image to the screen size
resizedImage = originalImage.resize((screen_width, screen_height))

# Convert the Pillow image to a Tkinter-compatible format
tkImage = ImageTk.PhotoImage(resizedImage)

# Create a label with the resized image
backgroundLabel = tkinter.Label(window, image=tkImage)
backgroundLabel.place(relwidth="1", relheight="1")



miniGame1 = tkinter.Button(window,text="test", width=40, height=10, bg="red" )
miniGame2 = tkinter.Button(window,text="test", width=40, height=10, bg="red" )
miniGame3 = tkinter.Button(window,text="test", width=40, height=10, bg="red" )
miniGame4 = tkinter.Button(window,text="test", width=40, height=10, bg="red" )

miniGame1.place(rely= 0.3, relx=0.3)
miniGame2.place(rely= 0.3, relx=0.5)
miniGame3.place(rely= 0.5, relx=0.3)
miniGame4.place(rely= 0.5, relx=0.5)

window.mainloop()