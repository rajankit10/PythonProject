from tkinter import *
from tkinter import messagebox
from random import *
from pyperclip import *

#-------------------------------------------------Save Password---------------------------------

def save():

	website=website_entry.get()
	email=email_entry.get()
	password=password_entry.get()

	if len(website)==0 or len(password)==0:
		messagebox.showinfo(title="Oops",message="Please Make sure you haven't left any feild Empty")

	else:

		is_ok=messagebox.askokcancel(title=website, message="The details are \n \n Website: "+website+"\n\n"+"Email: "+email+"\n\n"+"Password: "+password+"\n\n"+"Is it OK to save?")
		if is_ok:
			with open('data.txt','a') as data_file:
				data_file.write(website+" --> "+email+" --> "+password+"\n")
				website_entry.delete(0, END)
				password_entry.delete(0, END)

#-------------------------------------------------Password Generator-----------------------------
def generate_pass():
	letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	numbers=["0","1","2","3","4","5","6","7","8","9"]
	symbols=["!","@","#","$","%","^","&","*","?","|","(",")","{","}","[","]"]

	nr_letters=randint(8,10)
	nr_numbers=randint(2,4)
	nr_symbols=randint(2,4)

	password_letters=[choice(letters) for _ in range(nr_letters)]
	password_symbols=[choice(symbols) for _ in range(nr_symbols)]
	password_numbers=[choice(numbers) for _ in range(nr_numbers)]

	password_list=password_letters+password_symbols+password_numbers

	shuffle(password_list)

	password="".join(password_list)
	password_entry.insert(0, password)
	copy(password)

#--------------------------------------------------GUI------------------------------------------------

window=Tk()
window.title("Password Maneger")# to give name to the GUI
window.config(padx=50,pady=50)#use for padding

canvas=Canvas(height=200, width=200)
logo_image=PhotoImage(file="logo.png")# use to assign logo

canvas.create_image(100,100,image=logo_image)# specify image name with a proper height and width. 100 because half of 200 is 100. 
canvas.grid(row=0,column=1)


#labels

website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)


email_label=Label(text="Email/UserId: ")
email_label.grid(row=2,column=0)


password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)


#Entries

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()


email_entry=Entry(width=35)
email_entry.grid(row=2,column=1)
email_entry.insert(0, "abc0@gmail.com")


password_entry=Entry(width=35)
password_entry.grid(row=3,column=1)

#Buttons

generate_password_button = Button(text="Generate Password",command=generate_pass)
generate_password_button.grid(row=4,column=1)


add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=5,column=1)


window.mainloop() # used to start the window