from tkinter import *
root = Tk()
root.geometry("700x400")
root.title("My GUI")

# Important Lable Options
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font=("comicsansms 19 bold")
# padx = x padding
# pady = y padding
# relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_lable = Label(text="Ready", bg = "red",fg="white", padx=23, pady=10, font=("comicsansms 19 bold"), borderwidth=3, relief=SUNKEN)


# Important pack options
# anchor = nw
# 1. title_lable.pack(anchor="nw")
# 2. title_lable.pack(anchor="ne")
# side = top, bottom, left, right
# fill
# padx
# pady


title_lable.pack(side="left", fill=X, padx=120, pady=100)
root.mainloop()