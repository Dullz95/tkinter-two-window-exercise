from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x200")

# Create Labels and entries

user_label=Label(root, text= "please enter Username: ")
user_label.place(x=20, y=5)
user_entry=Entry(root)
user_entry.place(x=250, y=5, width=100)

pass_label=Label(root, text="please enter Password: ")
pass_label.place(x=20,y=50)
pass_entry=Entry(root)
pass_entry.place(x=250, y=50, width=100)


# clear_button=Button(root,text="clear", command=clear)
# clear_button.place(x=370, y=100)
# exit_button=Button(root,text="exit", command=exit)
# exit_button.place(x=450, y=100)


def login():
    usernames = ["Aisaacs", "Jsmith", "Bblack", "Karnold", "Lmorgan"]
    password = ["12548", 85296, 14725, 96385, 78945]
    found=False
    for x in range(len(usernames)):
        if user_entry.get()==usernames[x] and pass_entry.get()==password[x]:
            found=True
    if found==True:
        messagebox.showinfo("STATUS", "Access Granted")
        root.destroy()
        import next_window
    else:
        messagebox.showinfo("STATUS","Access not granted")


submit_button=Button(root,text="Submit", command=login)
submit_button.place(x=300, y=100)

root.mainloop()



