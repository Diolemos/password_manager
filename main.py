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

###-----Labels------###

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)


###---Entries---###

website_entry = Entry(width=25)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.insert(0,"default@email.com") #to be replace by variable 'default_email'
email_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(column=1,row=3)

##----Buttons-----##

search_button = Button(text="Search") #this will fetch user data, if there is any
search_button.grid(row=1,column=2) 
generate_button = Button(text="Generate")
generate_button.grid(row=3,column=2)
save_button = Button(text="Save",width=35)
save_button.grid(column=1, row=4, columnspan=2)



window.mainloop()