import tkinter as tk
import tkinter.ttk
import sys
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import PIL
from PIL import ImageTk, Image
from twilio.rest import Client
import random
from random import randrange
import  mysql.connector as sql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


con=sql.connect(host="",user="",passwd="",database="") #enter details
cursor1=con.cursor()

inimain=tk.Tk()
inimain.title("E&S")
inimain.geometry("500x300")
inimain.resizable(height=0,width=0)

mf=Frame(inimain,background="white", highlightthickness=0, width=500, height=300)

welimg=Image.open("logo_small.png")
welimage1=welimg.resize((1000,820),Image.ANTIALIAS)
imgwel=ImageTk.PhotoImage(welimage1)

lbimg=Label(inimain,image=imgwel,highlightthickness=0,bg="white")
lbimg.image=imgwel
lbimg.place(x=-265,y=-260)

mf.grid(pady=0)

def Sign():
          iniframe=Frame(inimain,highlightthickness=3,width=1366,height=40, bd= 0)
          iniframe.place(x=110,y=160)
          iniframe.tkraise()          
          

          lb1=Label(iniframe,text="User ID")
          lb1.grid(row=0,column=0)
          lb2=Label(iniframe,text="Password")
          lb2.grid(row=1,column=0)
          e1=Entry(iniframe)
          e1.grid(row=0,column=1)
          e2=Entry(iniframe,show="*")
          e2.grid(row=1,column=1)

          def loginfunc():
          
                    cursor2=con.cursor(buffered=True)
                    cursor3=con.cursor(buffered=True)
                    cursor2.execute("SELECT User_ID from project WHERE User_ID =%s",(e1.get(),))
                    cursor3.execute("SELECT Password from project WHERE User_ID =%s",(e1.get(),))
                    userverify=cursor2.fetchone()                               
                    passverify=cursor3.fetchone()

                    if (e1.get(),)==userverify:
                              if (e2.get(),)==passverify:
                                        messagebox.showinfo("Login","Successfully logged in")
                                        inimain.destroy()
                                        select=tk.Tk()
                                        select.title("E&S")
                                        select.geometry("500x300")
                                        select.resizable(height=0,width=0)
                                        
                                        mycolor='#FFFFFF'
                                        frame1 = Frame(select, highlightbackground=mycolor, background="grey", highlightthickness=3, width=1366, height=100, bd= 0)
    
                                        frame1.grid(pady=0)
                                        image=Image.open("logo_small.png")
                                        image1=image.resize((1100,900),Image.ANTIALIAS)
                                        img=ImageTk.PhotoImage(image1)
                                        
                                        logo=Label(frame1,image=img,highlightthickness=0,bd=0)
                                        logo.image=img
                                        logo.place(x=-310,y=-385)
                                        mycolor2='#177565'
                                        frame2 = Frame(select, highlightbackground="white", background="white", highlightthickness=3, width=1366, height=400, bd= 0)
                                        frame2.grid(pady=0)
                                        onglb=Label(frame2,text="Select Service",bg="white",fg='Black',relief=FLAT,font=(("FranklinGothic"),14))
                                        onglb.place(x=0,y=0)
                                        frame2.grid_propagate(False)

                                        def email():
                                            class emailGui:
                                                def __init__(self):
                                                    self.root = tkinter.Tk()
                                                    self.root.geometry("800x500")
                                                    self.root.title("EMAIL CLIENT")
                                                    self.top_frame = tkinter.Frame(self.root,width=500,height=100)
                                                    self.bottom_frame = tkinter.Frame(self.root,width=500,height=100)
                                                    self.top_frame.pack_propagate(0)
                                                    self.bottom_frame.pack_propagate(0)
                                                    self.header = tkinter.Label(self.top_frame, text = "Bulk Email Service")
                                                    self.header.pack(side = 'top')
                                                    self.to = tkinter.Label(self.top_frame, text = "")
                                                    self.to.place(x=0,y=75)
                                                    self.message = tkinter.Entry(self.bottom_frame, width = 100)
                                                    self.subject = tkinter.Entry(self.bottom_frame, width = 100)
                                                    self.send = tkinter.Button(self.bottom_frame, text = "Send Email", command = self.sendEmail)
                                                    self.msg = tkinter.Label(self.bottom_frame, text = "Message:")
                                                    self.sub = tkinter.Label(self.bottom_frame, text = "Subject:")
                                                    self.sub.place(x=0,y=0)
                                                    self.msg.place(x=0,y=30)

                                                    self.message.place(x=80,y=30)
                                                    self.subject.place(x=80,y=0)
                                                    self.send.place(x=0,y=70)
                                                    self.top_frame.pack()
                                                    self.bottom_frame.pack()
                                                    self.browse = tkinter.Label(self.top_frame, text = "Select contact file:")
                                                    self.browse.place(x=0,y=50)
                                                    self.button_explore = tkinter.Button(self.top_frame,text = "Browse 🔍",command = self.browseFiles)
                                                    self.button_explore.place(x=103,y=47)
                                                    tkinter.mainloop()
                                                def browseFiles(self):
                                                    
                                                    self.filename = filedialog.askopenfilename(initialdir = "/",
                                                                                            title = "Select a File",
                                                                                            filetypes = (("Text files",
                                                                                                            "*.txt*"),
                                                                                                           ("all files",
                                                                                                            "*.*")))
                                                    self.to.configure(text="Path → "+self.filename)

                                                def sendEmail(self):
                                                    with open(self.filename) as f:
                                                        contents = f.read()
                                                        email = contents.splitlines()
                                                    mail_content = str(self.message.get())
                                                    subject_mail=str(self.subject.get())
                                                    
                                                    with open("email.txt") as f:
                                                        contents = f.read()
                                                        lst = contents.splitlines()
                                                        dict1 = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
                                                        emails_lst=[lst[i] for i in range(0,len(lst),2)]

                                                    for address in email:
                                                        random_index = randrange(len(emails_lst))
                                                        i=emails_lst[random_index]
                                                        sender_address=i
                                                        sender_pass = dict1[i]
                                                        receiver_address = address                  
                                                    #Setup the MIME
                                                        message = MIMEMultipart()
                                                        message['From'] = sender_address
                                                        message['To'] = receiver_address
                                                        message['Subject'] = subject_mail  #The subject line
                                                    #The body and the attachments for the mail
                                                        message.attach(MIMEText(mail_content, 'plain'))
                                                    #Create SMTP session for sending the mail
                                                        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                                                        session.starttls() #enable security
                                                        session.login(sender_address, sender_pass) #login with mail_id and password
                                                        text = message.as_string()
                                                        session.sendmail(sender_address, receiver_address, text)
                                                        session.quit()
                                                        print('Mail Sent')

                                                        val=(sender_address,receiver_address,subject_mail)

                                                        cursor_info=con.cursor(buffered=True)
                                                        cursor_info.execute('INSERT INTO email_info(Sender_Mail,Receiver_Mail,Mail_Subject) VALUES (%s,%s,%s)' , val)
                                                        con.commit()
                                                        
                                                        
                                                        
        
                                            GUI = emailGui()

                                                


                                        def sms():
                                            class SMSGUI:
                                                def __init__(self):
                                                    self.root = tkinter.Tk()
                                                    self.root.geometry("800x500")
                                                    self.root.title("SMS CLIENT")
                                                    self.top_frame = tkinter.Frame(self.root,width=500,height=100)
                                                    self.bottom_frame = tkinter.Frame(self.root,width=500,height=100)
                                                    self.top_frame.pack_propagate(0)
                                                    self.bottom_frame.pack_propagate(0)
                                                    self.header = tkinter.Label(self.top_frame, text = "Bulk SMS Service")
                                                    self.header.pack(side = 'top')
                                                    self.to = tkinter.Label(self.top_frame, text = "")
                                                    self.to.place(x=0,y=75)
                                                    self.message = tkinter.Entry(self.bottom_frame, width = 100)
                
                                                    self.send = tkinter.Button(self.bottom_frame, text = "Send SMS", command = self.sendSms)
                                                    self.msg = tkinter.Label(self.bottom_frame, text = "Message:")
         
                          
                                                    self.msg.place(x=0,y=0)

                                                    self.message.place(x=80,y=0)
                            
                                                    self.send.place(x=0,y=30)
                                                    self.top_frame.pack()
                                                    self.bottom_frame.pack()
                                                    self.browse = tkinter.Label(self.top_frame, text = "Select contact file:")
                                                    self.browse.place(x=0,y=50)
                                                    self.button_explore = tkinter.Button(self.top_frame,text = "Browse 🔍",command = self.browseFiles)
                                                    self.button_explore.place(x=103,y=47)
                                                    tkinter.mainloop()
                                                def browseFiles(self):
                                                    
                                                    self.filename = filedialog.askopenfilename(initialdir = "/",
                                                                                            title = "Select a File",
                                                                                            filetypes = (("Text files",
                                                                                                            "*.txt*"),
                                                                                                           ("all files",
                                                                                                            "*.*")))
                                                    self.to.configure(text="Path → "+self.filename)

                                                def sendSms(self):
                                                    account_sid = 'Your Twilio SID'
                                                    auth_token = 'Your Twilio Auth_Token'
                                                    client = Client(account_sid, auth_token)
                                                    msg = str(self.message.get())
                                                    with open(self.filename) as f:
                                                        contents = f.read()
                                                        phone_num = contents.splitlines()
                                                    

                                                    
                                                    msg = str(self.message.get())

                                                    for rec in phone_num:
                                                        message = client.messages.create(body=msg,from_='Twilio Phone Number',to= rec)
                                                        print(message.sid) 
                                                        tkinter.messagebox.showinfo('Success', 'Message sent successfully')

                                                        val=(rec,str(current_time))

                                                        cursor_sms=con.cursor(buffered=True)
                                                        cursor_sms.execute('INSERT INTO sms(Contact_Number,Time) VALUES (%s,%s)' , val)
                                                        con.commit()
                                    
    
                                            gui = SMSGUI()
                                         
                                                

                                        Button(frame2,text="E-Mail",height= 2, width=10,command=email).place(x=100,y=70)
                                        Button(frame2,text="SMS",height= 2, width=10,command=sms).place(x=300,y=70)


                                

                                        


                              else:
                                        messagebox.showinfo("Login","Invalid Credentials")
                    else:
                              messagebox.showinfo("Login","Invalid Credentials")
                    
                                                                                                    

          def exitfunc():
                     inimain.destroy()
          
                              

          def register():
                    regis=tk.Tk()
                    regis.title("Register")
                    regis.geometry("500x300")

                    lb3=Label(regis,text="User ID")
                    lb3.grid(row=0,column=0)
                    lb4=Label(regis,text="Password")
                    lb4.grid(row=1,column=0)
                    lb7=Label(regis,text="Confirm Password")
                    lb7.grid(row=2,column=0)
                    e3=Entry(regis)
                    e3.grid(row=0,column=1)
                    e4=Entry(regis,show="*")
                    e4.grid(row=1,column=1)
                    e5=Entry(regis,show="*")
                    e5.grid(row=2,column=1)

          
          
                    def register1():
                              cursor4=con.cursor(buffered=True)
                              cursor4.execute("SELECT User_ID from project WHERE User_ID =%s",(e3.get(),))
                              usercheck=cursor4.fetchone()

                              if (e3.get(),)==usercheck:
                                        messagebox.showinfo("Login","User already exists, Please choose another User ID")
                              else:
                                        if e4.get()==e5.get():
                                                  messagebox.showinfo("Register","Registeration Complete")
                                                  
                                                  l=e3.get()
                                                  m=e4.get()
                                        
                                                  val=(l,m)
                                                  cursor1.execute('INSERT INTO project(User_ID,Password) VALUES (%s,%s)' , val) 
                                                  con.commit()
                                                  print(cursor1.rowcount, "record inserted.")
                                                  regis.destroy()
                                                 
                                        
                                        else:
                                                  messagebox.showinfo("Register","Passwords do not match. Please Check again")


                    def exitfunc2():
                              regis.destroy()
                    Button(regis,text="Confirm",command=register1).grid(row=3,column=1)
                    Button(regis,text="Cancel",command=exitfunc2).grid(row=3,column=0)
                    
          Button(iniframe,text="Cancel",command=exitfunc).grid(row=3,column=0)
          Button(iniframe,text="Login",command=loginfunc).grid(row=3,column=1)
          Button(iniframe,text="Sign Up",command=register).grid(row=3,column=2)

Button(inimain,text="Sign In/Sign Up",command=Sign).place(x=190,y=200)



          
          

   