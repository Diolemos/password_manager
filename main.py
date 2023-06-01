from tkinter import *



#------------UI ----------------------------------------#

#create main window
window = Tk()
window.config(padx=50,pady=50)

#create canvas that will hold the image
logo = PhotoImage(file="./images/logo.png")
canvas = Canvas(width=200, height=200)
main_image = canvas.create_image(100,100,image=logo)


canvas.grid(row=0,column=1)





window.mainloop()