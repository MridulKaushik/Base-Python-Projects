from tkinter import *
import requests


# ---------------- API REQUEST FUNCTION-------------------#

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    can.itemconfig(quote_text, text=data["quote"], fill='white')


# ------------------- USER INTERFACE-----------------------#

win = Tk()
win.title("Kanya Says.....")
win.configure(padx=50, pady=50)

can = Canvas(width=300, height=415)
try:  # For vs code editor
    background_image = PhotoImage(file="Day33_Python/background.png")
except:
    background_image = PhotoImage(file="background.png")
can.create_image(150, 212, image=background_image)
quote_text = can.create_text(150, 207, width=250, fill='red', text="Kanya quote goes here", font=("Arial", 16, "bold"))
can.grid(row=0, column=0)

try:
    kanya_image = PhotoImage(file="Day33_Python/kanye.png")
except:
    kanya_image = PhotoImage(file="kanye.png")
but = Button(image=kanya_image, bd=0, height=140, highlightthickness=0, command=get_quote)
but.grid(row=1, column=0)

win.mainloop()
