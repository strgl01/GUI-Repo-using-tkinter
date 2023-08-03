from tkinter import *


class NLPApp:

    def __init__(self):
        self.root= Tk()
        self.root.title("NLPApp")
        self.root.geometry("400x500") 
        self.__register()
        self.root.mainloop()
        

    def __register(self):
        
        self.__clear()

        email_label=Label(self.root,text='Enter your email',bg='silver',fg='white').pack(pady=10)
        email_entry=Entry(self.root,width=50).pack(pady=10)

        name_label=Label(self.root,text='Enter your name',bg='silver',fg='white').pack(pady=10)
        name_entry=Entry(self.root,width=50).pack(pady=10)

        password_label=Label(self.root,text='Enter your Password',bg='silver',fg='white').pack(pady=10)
        password_entry=Entry(self.root,width=50,show='*').pack(pady=10)

        btn=Button(self.root,text='Already a member? Login',activebackground='blue',command=self.__login).pack(pady=10)

    def __clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def __login(self):

        self.__clear()
        
        email_label=Label(self.root,text='Enter your email',bg='silver',fg='white').pack(pady=10)
        email_entry=Entry(self.root,width=50).pack(pady=10)

        password_label=Label(self.root,text='Enter your Password',bg='silver',fg='white').pack(pady=10)
        password_entry=Entry(self.root,width=50,show='*').pack(pady=10)


        btn=Button(self.root,text='Not a member? Register',activebackground='blue',command=self.__register).pack(pady=10)



obj=NLPApp()
