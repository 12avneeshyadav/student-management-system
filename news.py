from tkinter import *
from PIL import ImageTk, Image
import textwrap

root = Tk()
root.title("Chutiyapa News")
root.geometry("1000x800")

texts = []
photos = []

# Title
f0 = Frame(root, width=1000, height=70)
Label(f0, text="Avneesh News", font="lucida 33 bold").pack()
f0.pack()

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(textwrap.fill(text, 40))  # better wrapping

    image = Image.open(f"{i+1}.jpg")
    image = image.resize((400, 250))
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)

# News blocks
for i in range(3):
    f = Frame(root, width=900, height=200, padx=100)
    Label(f, text=texts[i], padx=22, pady=22, font=("comicsansms 19 bold")).pack(side="left")
    Label(f, image=photos[i]).pack(side="right")
    f.pack(anchor="w", pady=10)

root.mainloop()