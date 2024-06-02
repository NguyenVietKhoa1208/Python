from tkinter import *

count = 0 

def click():
    global count
    count+=1 
    print("You click the button ",count,"time!")

def submit():
    username = entry.get()
    print("Hello, ",username)
    
def delete():
    entry.delete(0,END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)
    

window = Tk()
window.geometry("900x900")
window.title("first GUI program")

icon = PhotoImage(file='dog.PNG')
window.iconphoto(True, icon)
window.config(background="White")

photo = PhotoImage(file = 'dog.PNG')


label = Label(window,text= "Dũng the Dog", 
              font= ('Arial', 40,'bold'), 
              fg= 'Black', 
              bg='#5cfcff',
              relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

entry = Entry(window,
              font=("Arial", 40),
              fg="#00FF00",
              bg="black",
              show="*"
              )
entry.pack()

submit_button = Button(window, text= "submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text= "delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text= "backspace", command=backspace)
backspace_button.pack(side=RIGHT)

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="Red",
                activeforeground=("#00FF00"),
                activebackground=("Red"),
                image=photo,
                compound='left'
                )
button.pack(side=BOTTOM)

def display():
    if(x.get()== 1):
        print("You agree!")
    else:
        print("You gay!")
        
x= IntVar()

check_button = Checkbutton(window,
                           text= " I agree with something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left'
                           )
check_button.pack()

    
window.mainloop()