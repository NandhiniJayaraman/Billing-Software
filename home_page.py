from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
from restratunt_page import Bill

root=Tk()
root.title('Login')
root.geometry('925x500+0+0')
root.configure(bg='#fff')
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='nandhini' and password=='1234':
        Bill(root)
    elif username!='nandhini' and password!='1234':
        messagebox.showinfo("Invalid","Invalid username and password")
    elif password!='1234':
        messagebox.showwarning("Warning","Invalid Password")
    elif username!='nandhini':
        messagebox.showwarning("Warning","Invalid Username ")
#=======================================================================
img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=100,y=100)

frame=Frame(root,width=300,height=350,bg='white')
frame.place(x=480,y=50)
'''url=PhotoImage("login1.png")
canvas1=Canvas(frame,width=400,height=400)
canvas1.pack(fill='both',expand=True)
canvas1.create_image(0,0,image=url,anchor='nw')'''
#-------------------------------------------------------------------
heading=Label(frame,text='LOG-IN',fg='black',bg='white',font=('Times',23,'bold'))
heading.place(x=100,y=5)
#==============================================================
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Times',13))
user.place(x=30,y=80)
user.insert(0,'UserName')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#=====================================================================
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Times',13),show='*')
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#=========================================================================
# sign up button

Button(frame,width=39,pady=7,text='Sign In',fg='black',bg='blue',border=0,command=signin).place(x=35,y=250)
#label=Label(frame,text="Don't have an Account?",fg='black',bg='white',font=('Times',9))
#label.place(x=75,y=270)

#sign_up=Button(frame,width=6,text='Sign-up',border=0,bg='white',fg='blue')
#sign_up.place(x=215,y=270)
root.mainloop()

