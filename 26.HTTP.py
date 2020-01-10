import tkinter as UI
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
import requests

imagePath = 'Files/bg.jpg'
url = "https://api.jsonbin.io/b/"
bin = "5e16b6865df6407208323019"
key = "$2b$10$FyY1CLUHl52Ca9Fa3ZIFe.bsjMxgxyYy85TZonNJEUtv/p6.TaN7m"

# window
window = UI.Tk()                # Create window
window.title('HTTP Request')           # Define Title
window.geometry("400x300")      # Define window size
window.resizable(False, False)  # Disable resizing

# Preparing structure
header = UI.Frame(window, bg='green', height=30)
content = UI.Frame(window)
footer = UI.Frame(window, bg='green', height=30)

# text message
ResponseText = UI.Message(content, text="", width=400, font=("Courier", 15))
Title = UI.Message(header, text="HTTP Request", width=400)
Title.config(bg='green', foreground='white', font=("Courier", 15))

# image
img = Image.open(imagePath)
img = img.resize((400, 190), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = UI.Label(content, image=img)


def httpGet():
    response = requests.get(url+bin, headers={"secret-key": key})
    response = response.text
    print("get", response)
    btn.config(text='POST https://api.jsonbin.io/', command=httpPost)
    footer.update()
    ResponseText.config(text=response)
    content.update()


def httpPost():
    data = {
        "source": "https://jsonbin.io/",
        "method": "POST"
    }
    headers = {"secret-key": key, "Content-Type": "application/json"}
    response = requests.post(url, data=data, headers=headers)
    response = response.text
    print("post", response)
    btn.pack_forget()
    footer.update()
    ResponseText.config(text=response+"\n Can you fix this?")
    content.update()


# buttons
btn = UI.Button(footer, text='GET https://api.jsonbin.io/')
btn.config(bg='green', width=400, command=httpGet)

# pack
btn.pack()
ResponseText.pack()
Title.pack()
header.pack(fill='both', side='top')
content.pack(fill='both')
footer.pack(fill='both', side='bottom')
panel.pack(side="bottom", fill="both", expand="no")

# start program
window.mainloop()
