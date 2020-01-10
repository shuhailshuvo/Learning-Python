import tkinter as UI
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep

imagePath = 'Files/bg.jpg'

# window
window = UI.Tk()                # Create window
window.title('Clock')           # Define Title
window.geometry("400x300")      # Define window size
window.resizable(False, False)  # Disable resizing

# Preparing structure
header = UI.Frame(window, bg='green', height=30)
content = UI.Frame(window)
footer = UI.Frame(window, bg='green', height=30)

# text message
Date = UI.Message(content, text="", width=400, font=("Courier", 15))
Title = UI.Message(header, text="Clock", width=400)
Title.config(bg='green', foreground='white', font=("Courier", 15))

# image
img = Image.open(imagePath)
img = img.resize((400, 210), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = UI.Label(content, image=img)


def count():
    showBtn.pack_forget()
    Date.config(text=datetime.now())
    content.update()
    sleep(1)
    count()


# buttons
showBtn = UI.Button(footer, text='SHOW CLOCK')
showBtn.config(bg='green', width=400, command=count)

# pack
showBtn.pack()
Date.pack()
Title.pack()
header.pack(fill='both', side='top')
content.pack(fill='both')
footer.pack(fill='both', side='bottom')
panel.pack(side="bottom", fill="both", expand="no")

# start program
window.mainloop()
