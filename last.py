from tkinter import *
import pygame

pygame.init()
root = Tk()
root.title("""******Quiz zoMania"******""")
root.geometry('1920x1040+0+0')
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
"""-------------------------------------------------------------------------"""


def Change50_50():
    canvas = Canvas(option1, bg="Black", width=110, height=78)
    canvas.grid(row=0, column=0, padx=15)
    canvas.delete("all")
    image1 = PhotoImage(file="del50-50.png")
    canvas.create_image(55, 40, image=image1)
    canvas.image = image1


def Peoplechange():
    canvas = Canvas(option1, bg="Black", width=110, height=78)
    canvas.grid(row=0, column=1, padx=15)
    canvas.delete("all")
    image1 = PhotoImage(file="del_audience.png")
    canvas.create_image(55, 40, image=image1)
    canvas.image = image1


def Phonechange():
    canvas = Canvas(option1, bg="Black", width=110, height=78)
    canvas.grid(row=0, column=2, padx=15)
    canvas.delete("all")
    image1 = PhotoImage(file="del_call.png")
    canvas.create_image(55, 40, image=image1)
    canvas.image = image1


def Millionpicture1():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide2.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture2():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide3.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture3():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide4.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture4():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide5.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture5():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide6.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture6():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide7.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture7():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide8.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture8():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide9.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture9():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide10.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture10():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide12.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1


def Millionpicture11():
    canvas = Canvas(Frame_bottom, bg="Black", width=260, height=800)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image1 = PhotoImage(file="Slide13.png")
    canvas.create_image(130, 400, image=image1)
    canvas.image = image1
    won()


def lost():
    canvas = Canvas(Frame_left, bg="Black", width=800, height=450)
    canvas.grid(row=1, column=0)
    # canvas.delete("all")
    image1 = PhotoImage(file="you_lost2.png")
    canvas.create_image(400, 260, image=image1)
    canvas.image = image1


def won():
    canvas = Canvas(Frame_left, bg="Black", width=800, height=450)
    canvas.grid(row=1, column=0)
    # canvas.delete("all")
    image1 = PhotoImage(file="you-won.png")
    canvas.create_image(400, 289, image=image1)
    canvas.image = image1


"""......................images......................................"""
CentreImage = PhotoImage(file="Logo1.png")
LogoCentre = Button(option2, image=CentreImage, bg="white", width=290, height=280)
LogoCentre.grid()
lifetime_50_50 = PhotoImage(file="download (1).png")
Lifeline50_50 = Button(option1, image=lifetime_50_50, bg="Black", width=110, height=78, command=Change50_50)
Lifeline50_50.grid(row=0, column=0, padx=15)
Audience = PhotoImage(file="audiece.png")
audience_vote = Button(option1, image=Audience, bg="Black", width=110, height=78, command=Peoplechange)
audience_vote.grid(row=0, column=1, padx=15)
phone = PhotoImage(file="phonecall.png")
phone_call = Button(option1, image=phone, bg="Black", width=110, height=78, command=Phonechange)
phone_call.grid(row=0, column=2, padx=15)
lists = PhotoImage(file="Slide1.PNG")
amount_list = Button(Frame_bottom, image=lists, bg="Black", width=260, height=800)
amount_list.grid(padx=155)

"""......................Question .............................."""
Question1 = StringVar()
Question2 = StringVar()
Question3 = StringVar()
Question4 = StringVar()
Question5 = StringVar()
Question6 = StringVar()
Question7 = StringVar()
Question8 = StringVar()
Question9 = StringVar()
Question10 = StringVar()
Question11 = StringVar()

Answer1 = StringVar()
Answer2 = StringVar()
Answer3 = StringVar()
Answer4 = StringVar()


def question1():
    Question1.set("Q1 Which of these Hindi phrases is used to denote high inflation?")
    Answer1.set("Fasal Bikau Mehngaai")
    Answer2.set("Padgi Chor Mehngaai")
    Answer3.set("Aankhfod Mehngaai")
    Answer4.set("Kamartod Mehngai")

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question1)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=question2)
    questions4.grid(row=2, column=3, pady=4)


def question2():
    Question2.set("Which one of these four birds has the longest beak and feet?")
    Answer1.set("Heron")
    Answer2.set("Parrot")
    Answer3.set("Crow")
    Answer4.set("Pigeon")
    Millionpicture1()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question2)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=question3)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question3():
    Question3.set("Which of these formulae is used to calculate area of a rectangular field?")
    Answer1.set("breadth-length")
    Answer2.set("length * breadth * height")
    Answer3.set("length * breadth")
    Answer4.set("breadth/length")
    Millionpicture2()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question3)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=question4)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question4():
    Question4.set("Which one of these festivals is celebrated during winter in India?")
    Answer1.set("Baisakhi")
    Answer2.set("Makar Sankanti")
    Answer3.set("Naag Panchami")
    Answer4.set("Ganesh Chaturthi")
    Millionpicture3()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question4)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=question5)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question5():
    Question5.set("Which of these Hindi idioms means to defame someone ?")
    Answer1.set("Keechad Uchaalna")
    Answer2.set("Paani Daalna")
    Answer3.set("Mitti Khodna")
    Answer4.set("Rang Lagaana")
    Millionpicture4()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question5)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=question6)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question6():
    Question6.set("Which of the following was once a lifeline on the TV show 'K.B.C'?")
    Answer1.set("Tridev")
    Answer2.set("Triguni")
    Answer3.set("Trimurti")
    Answer4.set("Baba ji ki bhuti")
    Millionpicture5()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question6)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=question7)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question7():
    Question7.set("What time corresponds to 23:23 hours ?")
    Answer1.set("1:23 AM")
    Answer2.set("11:23 AM")
    Answer3.set("11:23 PM")
    Answer4.set("12:00 AM")
    Millionpicture6()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question7)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=question8)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question8():
    Question8.set("Who is the best Underground Rapper?")
    Answer1.set("Divine")
    Answer2.set("Naezy")
    Answer3.set("Emiway")
    Answer4.set("Kr$na")
    Millionpicture7()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question8)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=question9)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question9():
    Question9.set("Which of these diseases is caused by bacteria, not viruses ?")
    Answer1.set("Konkan")
    Answer2.set("Paani Daalna")
    Answer3.set("Mitti Khodna")
    Answer4.set("Rang Lagaana")
    Millionpicture8()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question9)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=question10)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question10():
    Question10.set("Who played the role of Maqbool in Mirzapur ?")
    Answer1.set("Shajhi Chaudhary")
    Answer2.set("Pankaj Triphati")
    Answer3.set("Mua Triphati")
    Answer4.set("Ali Fazal")
    Millionpicture9()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question10)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=question11)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=lost)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


def question11():
    Question11.set("Between whom the First day_night test match was played?")
    Answer1.set("Australia vs India ")
    Answer2.set("New Zealand vs Australia")
    Answer3.set("New Zealand vs West Indies")
    Answer4.set("Banladesh vs Sri Lanka")
    Millionpicture10()

    questions = Entry(option3, font=('arial', 20, 'bold'), bg="blue", fg='white', bd=5, width=70, justify=CENTER,
                      textvariable=Question11)
    questions.grid(row=0, column=0, columnspan=12, pady=4)
    optionA = Label(option3, font=('arial', 14, 'bold'), text="A", bg="black", fg='white', bd=5, justify=CENTER)
    optionA.grid(row=1, column=0, pady=4, sticky=E)
    questions1 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer1, command=lost)
    questions1.grid(row=1, column=1, pady=4)
    optionB = Label(option3, font=('arial', 14, 'bold'), text="B", bg="black", fg='white', bd=5, justify=LEFT)
    optionB.grid(row=1, column=2, pady=4, sticky=E)
    questions2 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer2, command=Millionpicture11)
    questions2.grid(row=1, column=3, pady=4)

    optionC = Label(option3, font=('arial', 14, 'bold'), text="C", bg="black", fg='white', bd=5, justify=LEFT)
    optionC.grid(row=2, column=0, pady=4, sticky=E)
    questions3 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer3, command=lost)
    questions3.grid(row=2, column=1, pady=4)

    optionD = Label(option3, font=('arial', 14, 'bold'), text="D", bg="black", fg='white', bd=5, justify=LEFT)
    optionD.grid(row=2, column=2, pady=4, sticky=E)
    questions4 = Button(option3, font=('arial', 14, 'bold'), bg="blue", fg='white', bd=1, width=22, height=2,
                        justify=CENTER, textvariable=Answer4, command=lost)
    questions4.grid(row=2, column=3, pady=4)


"""............................................................."""
question1()
"""time.sleep(0.2)
question2()
time.sleep(0.1)
question3()
time.sleep(0.0)
question4()
time.sleep(0.0)
question5()
time.sleep(0.3)
question6()
time.sleep(0.0)
question7()
time.sleep(0.0)
question8()
time.sleep(0.3)
question9()
time.sleep(0.1)
question10()
time.sleep(0.2)
question11()"""
root.mainloop()
