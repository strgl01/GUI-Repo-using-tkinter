from tkinter import *
import tkinter
from db import Database_
from tkinter import messagebox

class NLPApp:

    def __init__(self):
        self.root= Tk()
        self.db=Database_()
        self.root.title("NLPApp")
        self.root.geometry("400x500") 
        self.__register()
        self.root.mainloop()
        

    def __register(self):
        
        self.__clear()
        self.email=tkinter.StringVar()
        self.name_=tkinter.StringVar()
        self.password=tkinter.StringVar()

        email_label=Label(self.root,text='Enter your email',bg='silver',fg='white').pack(pady=10)
        email_entry=Entry(self.root,width=50,textvariable=self.email).pack(pady=10)
        
        name_label=Label(self.root,text='Enter your name',bg='silver',fg='white').pack(pady=10)
        name_entry=Entry(self.root,width=50,textvariable=self.name_).pack(pady=10)

        password_label=Label(self.root,text='Enter your Password',bg='silver',fg='white').pack(pady=10)
        password_entry=Entry(self.root,width=50,show='*',textvariable=self.password).pack(pady=10)

        btn=Button(self.root,text='Register',activebackground='blue',command=self.__perform_registration).pack(pady=10)

        btn=Button(self.root,text='Already a member? Login',activebackground='blue',command=self.__login).pack(pady=10)

    def __perform_registration(self):
        name1=self.name_.get()
        email1=self.email.get()
        password1=self.password.get()

        response=self.db.add(name1,email1,password1)
        if response:
            messagebox.showinfo("Success",'Registration Done')
        else:
            messagebox.showerror('Error','Try Again')


    def __clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def __login(self):

        self.__clear()

        self.email1=tkinter.StringVar()
        self.password1=tkinter.StringVar()
        
        email_label=Label(self.root,text='Enter your email',bg='silver',fg='white').pack(pady=10)
        email_entry=Entry(self.root,width=50,textvariable=self.email1).pack(pady=10)

        password_label=Label(self.root,text='Enter your Password',bg='silver',fg='white').pack(pady=10)
        password_entry=Entry(self.root,width=50,show='*',textvariable=self.password1).pack(pady=10)

        btn=Button(self.root,text='Login',activebackground='blue',command=self.__perform_login).pack(pady=10)

        btn=Button(self.root,text='Not a member? Register',activebackground='blue',command=self.__register).pack(pady=10)

    def __perform_login(self):
        
        email1=self.email1.get()
        password1=self.password1.get()

        response=self.db.login(email1,password1)
        if response:
            messagebox.showinfo("Success",'Login Done')
            self.__home()
        else:
            messagebox.showerror('Error','Try Again')


    def __home(self):

        self.__clear()
        
        NER_btn=Button(self.root,text='Named Entity Recognistion',width=50,activebackground='blue',command=self.__NER).pack(pady=20)

        Semantic_btn=Button(self.root,text='Semantic Analysis',width=50,activebackground='blue',command=self.__Sentiment_Analysis).pack(pady=20)

        Emotion_btn=Button(self.root,text='Emotin Detector',width=50,activebackground='blue',command=self.__Emotion_Analysis).pack(pady=20)


    def __NER(self):
        self.__clear()

        Text_label=Label(self.root,text='Enter your string here',width=50,bg='silver',fg='white').pack(pady=20)
        string_entry=Entry(self.root,width=50).pack(pady=20)
        Analyse=Button(self.root,text='Analyse',width=50,activebackground='blue').pack(pady=20)
        response=Label(self.root,text='A').pack(pady=20)
        Back=Button(self.root,text='Home',width=50,activebackground='blue',command=self.__home).pack(pady=20)

    def __Sentiment_Analysis(self):
        self.__clear()

        Text_label=Label(self.root,text='Enter your string here',width=50,bg='silver',fg='white').pack(pady=20)
        string_entry=Entry(self.root,width=50).pack(pady=20)
        Analyse=Button(self.root,text='Analyse',width=50,activebackground='blue').pack(pady=20)
        response=Label(self.root,text='A').pack(pady=20)
        Back=Button(self.root,text='Home',width=50,activebackground='blue',command=self.__home).pack(pady=20)

    def __Emotion_Analysis(self):
        self.__clear()

        Text_label=Label(self.root,text='Enter your string here',width=50,bg='silver',fg='white').pack(pady=20)
        string_entry=Entry(self.root,width=50).pack(pady=20)
        Analyse=Button(self.root,text='Analyse',width=50,activebackground='blue').pack(pady=20)
        response=Label(self.root,text='A').pack(pady=20)
        Back=Button(self.root,text='Home',width=50,activebackground='blue',command=self.__home).pack(pady=20)








obj=NLPApp()
