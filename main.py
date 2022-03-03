from cgitb import text
from hashlib import sha224
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import messagebox
from turtle import width
from httpx import request
import requests
from api_key import api_key
from tkinter.filedialog import asksaveasfile

# root window
root = Tk()
root.geometry("600x400")

# canvas
canvas = Canvas(root, background="blue")
canvas.pack(fill=tk.BOTH, expand=True)

# "DejaVu Sans Mono", 16 font
dejavu_font = "DejaVu Sans Mono", "16"

# input label
input_label = canvas.create_text((300,50), text="Input a URL to shorten: ", font=dejavu_font)

# output label
output_label = canvas.create_text((300,160), text="Your output URL is: ", font=dejavu_font)

# input textbox
url_input = Entry(canvas)
url_input.place(x=50, y=100)
url_input.configure(width=41, font=dejavu_font, justify=CENTER)
url_input.focus()

# output url
output_url = Entry(canvas)
output_url.place(x=50, y=200)
output_url.configure(width=41, font=dejavu_font, justify=CENTER)

# given a input url, it takes the url and shortens it
def generate_url(url):
    url_to_short = url_input.get()
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url_to_short}"
    data = requests.get(api_url).json()["url"]

    # if data status is "OK", then shorten url
    if data["status"] == 7:
        short_url = data["shortLink"]
        output_url.delete(0, END)
        output_url.insert(0, short_url)
    else:
        messagebox.showwarning("Connection Failed", "Connection has failed, try again")

# generate url button
url_gen_button = Button(canvas, text="Generate URL")
url_gen_button.place(x=50, y=300)
url_gen_button.config(width=20, height=1, font=dejavu_font)
url_gen_button.bind("<Button-1>", generate_url)

# if save_url_button is pressed, then a open file dialog will open and the user will need to choose
# a location to save the file
def save_url(file_to_save):
    filesave = asksaveasfile(mode="w", defaultextension=".txt")

    # if file save is cancelled, then return to the program
    if filesave == None:
        return
    else:
        text_to_save = str(output_url.get())
        filesave.write(text_to_save)
        filesave.close()


# save url in a file button
save_url_button = Button(canvas, text="Save URL")
save_url_button.place(x=300, y=300)
save_url_button.config(width=20, height=1, font=dejavu_font)
save_url_button.bind("<Button-1>", save_url)

# mainloop
root.mainloop()