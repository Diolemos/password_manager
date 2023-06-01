from tkinter import *
from tkinter import messagebox
import json

#-----------??------------------------------------------#
default_email = ''
EMAIL_FILE_PATH = './data/default_email.txt'
USER_DATA_PATH = './data/user_data.json'
try:
    with open(EMAIL_FILE_PATH, "r") as file:
        default_email = file.read()
except FileNotFoundError:
    with open(EMAIL_FILE_PATH,'w+') as file:
        default_email = 'default@email.com'
        file.write(default_email)






def set_default_email():
     #-----Create a new window for input
    input_window = Toplevel(window)
    input_window.title("Set Default Email")
    
    # Create a label and entry widget for email input
    email_label = Label(input_window, text="Email:")
    email_label.pack()
    
    email_entry = Entry(input_window, width=25)
    email_entry.pack()
    
    # Create a button to save the email
    save_button = Button(input_window, text="Save", command=lambda: save_default_email(email_entry.get(), input_window))
    save_button.pack()

def save_default_email(email,input_window):
   
   if len(email) == 0:
       messagebox.showwarning(message="Please, Don't this field empty")
   else:
    with open(EMAIL_FILE_PATH, 'w') as file:
        file.write(email)
    email_entry.delete(0,END)
    email_entry.insert(0,email)    
    input_window.destroy()    
   

##------ SAVE PASSWORD ---------------------------------##
def clear_app():
    website_entry.delete(0,END)
    password_entry.delete(0,END)


def save_data():
    #-----get data from entries
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    
    data = {website:{'email':email,'password':password}}
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please, don't leave any field empty")
    
    elif messagebox.askokcancel(title="Save data?",message=f"Would you like to add?\nemail:{email}\nwebsite:{website},password:{password}?") :    
    ## try to read and update the json file
        try:
            with open(USER_DATA_PATH,'r') as file:
                file_data = json.load(file)
                file_data.update(data)
            with open(USER_DATA_PATH, 'w') as file:
                json.dump(file_data,file,indent=4)
        except FileNotFoundError:
            with open(USER_DATA_PATH,'w+') as file:
                json.dump(data,file)            
        
        finally:
            clear_app()
    
    ##except filenotfounderror createone and insert the brandnew data



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
email_entry.insert(0,default_email) #to be replace by variable 'default_email'
email_entry.grid(column=1,row=2,columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(column=1,row=3)

##----Buttons-----##

search_button = Button(text="Search") #this will fetch user data, if there is any
search_button.grid(row=1,column=2) 
generate_button = Button(text="Generate")
generate_button.grid(row=3,column=2)
save_button = Button(text="Save",width=35, command=save_data)
save_button.grid(column=1, row=4, columnspan=2)


###-----Create menubar------###

menubar = Menu(window)

#------Create the settings menu
settings = Menu(menubar, tearoff=0)
settings.add_command(label="Set Default Email", command=set_default_email)

#------- Add the settings menu to the menubar
menubar.add_cascade(label="Settings", menu=settings)

#------- Configure the window to use the menubar
window.config(menu=menubar)



window.mainloop()