"""
Paul Deater
SDEV245
RBAC and Authentication Mini-App
8/31/2026
Application has a login screen and has two path ways depending the users role.
Answer to part 4:
This app shows the Confidentiality aspect of the CIA triad, through its use distinct protected routes depending the role of the individual logging in. 
Keeping users and administrators separate in the information they can view and interact with, which is indicative of confidentiality. 
"""
import tkinter as tk
from tkinter import messagebox

# dictionary format: Username, password, role- True == Admin  False == User
Users = {
    "Matt@company.com" : ["short124", True],
    "Tom@company.com" :["tall124", False]
}

# creates a window
root = tk.Tk()
root.title("Mini-App")
root.geometry("720x720") 
root.configure(bg="gray85")

# Entry boxes
Login_Entry_Username = tk.Entry(root, width = 20)
Login_Entry_Username.pack(pady=5)

Login_Entry_Password = tk.Entry(root, width = 20)
Login_Entry_Password.pack(pady=5)

# Separate pathes depending on the login
def Admin_Page(x,y,z):
    for widget in root.winfo_children():
        widget.destroy()
    Admin_Button = tk.Button(root, text = "This does nothing but you are an Admin")
    Admin_Button.pack(pady=10)

def User_Page(x,y,z):
    for widget in root.winfo_children():
        widget.destroy()
    User_Button = tk.Button(root, text = "This does nothing but you are a User")
    User_Button.pack(pady=10)

#Checks the input for the username and password
def Check_Login():
    input_Username = Login_Entry_Username.get()
    input_Password = Login_Entry_Password.get()

    #validation
    if input_Username in Users:
        if input_Password == (Users[input_Username])[0]:
            if (Users[input_Username])[1]:
                Admin_Page(input_Username, input_Password, True)
            elif not((Users[input_Username])[1]):
                User_Page(input_Username, input_Password, False)
        else:
             messagebox.showerror("Login Failed", "Invalid Password.")
    else:
         messagebox.showerror("Login Failed", "Invalid User Name.")


Login_Button = tk.Button(root, text = "Login", command=Check_Login)
Login_Button.pack(pady=10)

root.mainloop()
