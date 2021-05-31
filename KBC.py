from tkinter import *
import pygame

pygame.init()
root = Tk()
root.title("""******Quiz zoMania"******""")
root.geometry('1352x652+0+0')
root.configure(background='Black')
Frame_background = Frame(root, bg="Black")
Frame_background.grid()
Frame_left = Frame(root, bg="black", width=452, height=600)
Frame_left.grid(row=0, column=0)
Frame_bottom = Frame(root, bg="black", width=452, height=600)
Frame_bottom.grid(row=0, column=1)
option1 = Frame(Frame_left, bg="black", bd=20, padx=130, width=900, height=200)
option1.grid(row=0, column=0)
option2 = Frame(Frame_left, bg="Black", bd=20, width=900, height=200)
option2.grid(row=1, column=0)
option3 = Frame(Frame_left, bg="black", bd=20, width=900, height=200)
option3.grid(row=2, column=0)
"""option4 = Frame(root, bg="Black", width=900, height=200)
option4.grid(row=1, column=1)"""
"""......................images......................................"""
CentreImage = PhotoImage(file="Logo.png")
LogoCentre = Button(option2, image=CentreImage, bg="Black", width=290, height=280)
LogoCentre.grid()
lifetime_50_50 = PhotoImage(file="download (1).png")
Lifeline50_50 = Button(option1, image=lifetime_50_50, bg="Black", width=110, height=78)
Lifeline50_50.grid(row=0, column=0, padx=15)
Audience = PhotoImage(file="audiece.png")
audience_vote = Button(option1, image=Audience, bg="Black", width=110, height=78)
audience_vote.grid(row=0, column=1, padx=15)
phone = PhotoImage(file="phonecall.png")
phone_call = Button(option1, image=phone, bg="Black", width=110, height=78)
phone_call.grid(row=0, column=2, padx=15)
lists = PhotoImage(file="Slide1.PNG")
amount_list = Button(Frame_bottom, image=lists, bg="Black", width=260, height=800)
amount_list.grid()
"""......................Question .............................."""
Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()
Question5 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()

Question1.set("Q1 Which of these Hindi phrases is used to denote high inflation?")
Answer1.set("Fasal Bikau Mehngaai")
Answer2.set("Padgi Chor Mehngaai")
Answer3.set("Aankhfod Mehngaai")
Answer4.set("Kamartod Mehngai")
"""............................................................."""

questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                  textvariable=Question1)
questions.grid(row=0, column=0, columnspan=12, pady=4)
optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
optionA.grid(row=1, column=0, pady=4, sticky=E)
questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                    justify=CENTER, textvariable=Answer1)
questions1.grid(row=1, column=1, pady=4)
optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
optionB.grid(row=1, column=2, pady=4, sticky=E)
questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                    justify=CENTER, textvariable=Answer2)
questions2.grid(row=1, column=3, pady=4)

optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
optionC.grid(row=2, column=0, pady=4, sticky=E)
questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                    justify=CENTER, textvariable=Answer3)
questions3.grid(row=2, column=1, pady=4)

optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
optionD.grid(row=2, column=2, pady=4, sticky=E)
questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                    justify=CENTER, textvariable=Answer4)
questions4.grid(row=2, column=3, pady=4)
root.mainloop()
