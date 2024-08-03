import tkinter
from tkinter import Tk
import json
import pyperclip

WIN = Tk()
WIN.geometry("400x400")
WIN.title("Password Manager")


def saving_password():
    with open("manager.json", "r") as file:
        data = json.load(file)

    with open("manager.json", "w") as file:
        data[software.get()] = insert_password.get()
        json.dump(data, file, indent=4)


    message =tkinter.Label(WIN,text="Password saved for: " + software.get() + " software.")
    message.pack()
    insert_password.delete(0,tkinter.END)
    software.delete(0,tkinter.END)





def saved_password():

    def copy():
        Password = data.get(copy_entry.get())

        if Password is not None:
            pyperclip.copy(Password)

    def delete():
        service_name = dlt_entry.get()
        with open("manager.json", "w") as saved_pass:
            if service_name in data:
                del data[service_name]
            json.dump(data,saved_pass,indent=4)


    WIN2 = Tk()
    WIN2.geometry("650x500")
    WIN2.title("Saved Passwords")
    with open("manager.json", "r") as saved_pass:
            data = json.load(saved_pass)

    for software_name, password in data.items():
        newlabel = tkinter.Label(WIN2,text= software_name + ": " + password)
        newlabel.pack()

    copy_label = tkinter.Label(WIN2, text="If you want to copy a password enter the service name then click copy")
    copy_label.pack()
    copy_entry = tkinter.Entry(WIN2)
    copy_entry.pack()
    copy_btn = tkinter.Button(WIN2, text="Copy", bg="#cce3e6", fg="black",command=copy)
    copy_btn.pack()

    dlt_label = tkinter.Label(WIN2, text="If you want to delete a password enter the service name then click delete")
    dlt_label.pack()
    dlt_entry = tkinter.Entry(WIN2)
    dlt_entry.pack()
    dlt_btn = tkinter.Button(WIN2, text="Delete", bg="#cce3e6", fg="black", command=delete)
    dlt_btn.pack()






    WIN2.mainloop()


label = tkinter.Label(WIN,text="Enter Password")
label.pack()

insert_password= tkinter.Entry(WIN)
insert_password.pack()

label = tkinter.Label(WIN,text="Service Name")
label.pack()

software= tkinter.Entry(WIN)
software.pack()

btn = tkinter.Button(WIN, text="Enter", bg="#cce3e6", fg="black", command= saving_password)
btn.pack()
btn = tkinter.Button(WIN, text="Saved passwords", bg="#cce3e6", fg="black", command= saved_password)
btn.pack()

WIN.mainloop()
