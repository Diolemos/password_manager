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

#Labels
website_label = Label(text="Website")

email_label = Label(text="Email/Username:")

password_label = Label(text="Password:")


#Entries
website_entry = Entry()

email_entry = Entry()

password_entry = Entry()

#Buttons

search_button = Button(text="Search")
generate_button = Button(text="Generate")
save_button = Button(text="Save")




window.mainloop()