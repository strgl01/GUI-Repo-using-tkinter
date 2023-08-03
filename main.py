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

        btn=Button(self.root,text='Register',activebackground='blue').pack(pady=10)

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

        btn=Button(self.root,text='Login',activebackground='blue',command=self.__home).pack(pady=10)

        btn=Button(self.root,text='Not a member? Register',activebackground='blue',command=self.__register).pack(pady=10)


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
