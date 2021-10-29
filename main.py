import tkinter
import time
import threading


def hi():
    time.sleep(2)
    print("hi")
    
    
mainwindow = tkinter.Tk()
mainwindow.title("Best Discord Token Generator | hCaptcha Bypass *Latest Method | 2022")
mainwindow.geometry("720x720") 
mainwindow.configure(bg="#141414")


label = tkinter.Label(mainwindow, text="Updated: 28/10/2021 | Source for sale", borderwidth=3, relief="solid", padx=5, pady=10).pack(padx=5, pady=10)
label = tkinter.Label(mainwindow, text="Discord Token Generator", font=("Arial", 33))
label.pack()
button = tkinter.Button(mainwindow, text="discord.gg/FQTfmdbWhG", command=threading.Thread(target=hi).start())
button.pack()

mainwindow.mainloop()
