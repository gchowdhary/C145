# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:55:06 2021

@author: hp
"""

#add tkinter basic template
from tkinter import *
root=Tk()
root.title("Driving License")
root.geometry("500x400")

root.configure(bg="white")
canvas = Canvas(root, width=500, height=600)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 500, 55, fill="red")
# canvas.create_retangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(220, 25, font=('Times', '24', 'bold italic'), text="Driving License")
label_ID_tag = canvas.create_text(50, 75, font=('Times', '16', 'bold'), text="ID :")
label_name_tag = canvas.create_text(60, 125, font=('Times', '16', 'bold'), text="Name :")
label_DOB_tag = canvas.create_text(90, 150, font=('Times', '16', 'bold'), text="Date of Birth :")
label_Pincode_tag = canvas.create_text(65, 175, font=('Times', '16', 'bold'), text="Pin No. :")
label_address_tag = canvas.create_text(65, 200, font=('Times', '16', 'bold'), text="Address :")
label_vehicle_tag = canvas.create_text(200, 225, font=('Times', '16', 'bold'), text="Authorisation to drive following vehicle :")

#Create a label
label_id = Label(root)
label_name=Label(root)
label_dob=Label(root)
label_pincode=Label(root)
label_address=Label(root)
label_vehicle=Label(root)


#add function
def cardId():
    id=38843784347
    name="Apras"
    dob="20 August 2012"
    pincode=110088
    address="abc, def road"
    vehicle=["two","four"]
    
    print(type(id))
    print(type(name))
    print(type(dob))
    print(type(pincode))
    print(type(vehicle))

# update the label created    
    label_id['text']=id
    label_name['text']=name
    label_dob['text']=dob
    label_address['text']=address
    label_pincode['text']=pincode
    label_vehicle['text']=vehicle
    

#add button
button1=Button(root, text="click me",command=cardId)


button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)

label_id_window = canvas.create_window(120, 75, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(120, 125, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(200, 150, anchor=CENTER, window=label_dob)
label_address_window = canvas.create_window(155, 175, anchor=CENTER, window=label_address)
label_pincode_window = canvas.create_window(155, 200, anchor=CENTER, window=label_pincode)
label_vehicle_window = canvas.create_window(420, 225, anchor=CENTER, window=label_vehicle)
canvas.pack()

#tkinter basic template end statement
root.mainloop()

