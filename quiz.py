from tkinter import *
import tkinter.font as font
import random
import sqlite3
import time
import pygame
from tkinter import messagebox

pygame.mixer.init()


def soundopt():
    global soundbtn
    global nosoundimg

    def onsound():
        pygame.mixer.music.play(loops=-1)
        soundimg = PhotoImage(file='ssound.png')
        soundbtn.config(image=soundimg, command=soundopt)
        soundbtn.image = soundimg

    pygame.mixer.music.stop()
    nosoundimg = PhotoImage(file='nosound.png')
    soundbtn.config(image=nosoundimg, command=onsound)
    soundbtn.image = nosoundimg


def playerUname():
    root.destroy()
    global playersup
    global uname
    playersup = Tk()
    playersup.title('Quiz Game')

    uname = StringVar()

    psup_canvas = Canvas(playersup, width=800, height=440, bg="#df144c")
    psup_canvas.pack()

    psup_frame = Frame(psup_canvas, bg="#000e44")
    psup_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(psup_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.1, anchor=N)

    # playername
    ulabel = Label(psup_frame, text="Player's Name")
    ulabel.config(font=('rockwell 15'), fg='#ed01f4', bg='#000e44')
    ulabel.place(relx=0.5, rely=0.48, anchor=CENTER)
    user = Entry(psup_frame, bg='#221322', fg='#e1e6e6', textvariable=uname, highlightthickness=2)
    user.config(borderwidth=5, highlightbackground="#00d5e0", highlightcolor="#00d5e0", relief=FLAT, width=20,
                justify='center', font=('rockwell 15'))
    user.place(relx=0.5, rely=0.56, anchor=CENTER)

    def checkPname():
        if len(user.get()) == 0:
            messagebox.showinfo("Warning!", "Player's name can't be empty")
        else:
            homemenu()

    btnfont = font.Font(size=12)
    sp = Button(psup_frame, text='Enter', padx=5, pady=5, width=5, command=checkPname, bg="#df144c", fg="white")
    sp.configure(width=10, height=1, activebackground="#33B5E5", relief=FLAT)
    sp['font'] = btnfont
    sp.place(relx=0.5, rely=0.68, anchor=CENTER)

    playersup.mainloop()


def homemenu():
    playersup.destroy()
    global hmenu
    global render
    hmenu = Tk()
    hmenu.title('Quiz Game')

    hmenu_canvas = Canvas(hmenu, width=800, height=480, bg="#df144c")
    hmenu_canvas.pack()

    hmenu_frame = Frame(hmenu_canvas, bg="#000e44")
    hmenu_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(hmenu_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.1, anchor=N)

    # sounds
    global soundbtn

    pygame.mixer.music.load("bgsound.mp3")
    pygame.mixer.music.play(loops=-1)

    soundimg = PhotoImage(file='ssound.png')
    soundbtn = Button(hmenu_frame, image=soundimg, bg="#000e44", command=soundopt)
    soundbtn.image = soundimg
    soundbtn.place(relx=0.9, rely=0.1, anchor=N)

    wel = Label(hmenu_frame, text='Welcome ' + uname.get(), bg="#000e44", font="calibri 18", fg="#af57c7")
    wel.config(borderwidth=3)
    wel.place(relx=0.5, rely=0.45, anchor=CENTER)

    def openldboard():
        hmenu.withdraw()
        leaderboard()

    def closethis():
        hmenu.withdraw()
        menu()

    btnfont = font.Font(size=12)
    startq_btn = Button(hmenu_frame, text='Start', command=closethis, bg="#df144c", fg="white")
    startq_btn.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    startq_btn['font'] = btnfont
    startq_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
    rank_btn = Button(hmenu_frame, text='Leaderboard', command=openldboard, bg="#df144c", fg="white")
    rank_btn.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    rank_btn['font'] = btnfont
    rank_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
    exit_btn = Button(hmenu_frame, text='Exit', command=quit, bg="black", fg="white")
    exit_btn.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    exit_btn['font'] = btnfont
    exit_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    hmenu.mainloop()


def menu():
    global menus
    menus = Tk()
    menus.title('Quiz Game Menu')

    menus_canvas = Canvas(menus, width=800, height=480, bg="#df144c")
    menus_canvas.pack()

    menus_frame = Frame(menus_canvas, bg="#000e44")
    menus_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    def openlevel(choice):
        if choice == 1:
            hmenu.destroy()
            menus.destroy()
            easy()
        if choice == 2:
            hmenu.destroy()
            menus.destroy()
            medium()
        if choice == 3:
            hmenu.destroy()
            menus.destroy()
            difficult()

    var = StringVar()
    btnfont = font.Font(size=12)
    easyR = Button(menus_frame, text='Easy', command=lambda: openlevel(1), bg="#df144c", fg="white")
    easyR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    easyR['font'] = btnfont
    easyR.place(relx=0.5, rely=0.3, anchor=CENTER)

    mediumR = Button(menus_frame, text='Medium', command=lambda: openlevel(2), bg="#df144c", fg="white")
    mediumR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    mediumR['font'] = btnfont
    mediumR.place(relx=0.5, rely=0.4, anchor=CENTER)

    hardR = Button(menus_frame, text='Hard', command=lambda: openlevel(3), bg="#df144c", fg="white")
    hardR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    hardR['font'] = btnfont
    hardR.place(relx=0.5, rely=0.5, anchor=CENTER)

    def openhmenu():
        menus.withdraw()
        hmenu.deiconify()

    backtohmenu = Button(menus_frame, text='Back', command=openhmenu, bg='black', fg='white')
    backtohmenu.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    backtohmenu['font'] = btnfont
    backtohmenu.place(relx=0.5, rely=0.6, anchor=CENTER)

    menus.mainloop()


def leaderboard():
    global ld
    ld = Tk()
    ld.title('Quiz Game - Leaderboard')

    ld_canvas = Canvas(ld, width=800, height=650, bg="#df144c")
    ld_canvas.pack()

    ld_frame = Frame(ld_canvas, bg="#000e44")
    ld_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    def all_rank(type):
        ar_frame = Frame(ld_canvas, bg="#00d5e0")
        ar_frame.place(relwidth=0.55, relheight=0.95, relx=0.4, rely=0.03)

        if type == 'easy':
            top_title = Label(ar_frame, text='Highscores')
            top_title.config(font=('rockwell 20'), fg='black', bg='#00d5e0')
            top_title.place(relx=0.5, rely=0.1, anchor=CENTER)

            playername = uname.get()

            conn = sqlite3.connect('easyscore.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS easyscore(USERNAME text, SCORE int)')
            conn.commit()
            create.execute('SELECT * FROM easyscore')
            z = create.fetchall()
            #print(z)
            conn.close()

            z.sort(key=lambda x: x[1], reverse=True)
            top = z[:10]
            #print(top)

            print_records = ''
            for index, record in enumerate(top, 1):
                print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + "\n\n"

            rec_title = Label(ar_frame, text=' Rank\t           Name\t  Score')
            rec_title.config(font=('rockwell 15'), fg='black', bg='#00d5e0')
            rec_title.place(relx=0.5, rely=0.2, anchor=CENTER)
            rec = Label(ar_frame, text=print_records)
            rec.config(font=('rockwell 12'), fg='black', bg='#00d5e0')
            rec.place(relx=0.5, rely=0.55, anchor=CENTER)

            e_leadboard['state'] = DISABLED
            e_leadboard['background'] = '#33B5E5'
            m_leadboard['state'] = NORMAL
            m_leadboard['background'] = '#df144c'
            h_leadboard['state'] = NORMAL
            h_leadboard['background'] = '#df144c'

            def ereset():
                answer = messagebox.askyesno(title='Reset Score',
                                             message='Are you sure that you want to reset record?')
                if answer:
                    conn = sqlite3.connect('easyscore.db')
                    create = conn.cursor()
                    create.execute('CREATE TABLE IF NOT EXISTS easyscore(USERNAME text, SCORE int)')
                    create.execute('DELETE FROM easyscore;', )
                    conn.commit()
                    z = create.fetchall()
                    conn.close()

                    all_rank(ez)

            btnfont = font.Font(size=12)
            e_reset = Button(ar_frame, text='Reset', command=ereset, bg="#df144c", fg="white")
            e_reset.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
            e_reset['font'] = btnfont
            e_reset.place(relx=0.5, rely=0.95, anchor=S)

        if type == 'medium':
            top_title = Label(ar_frame, text='Highscores')
            top_title.config(font=('rockwell 20'), fg='black', bg='#00d5e0')
            top_title.place(relx=0.5, rely=0.1, anchor=CENTER)

            playername = uname.get()

            conn = sqlite3.connect('mediumscore.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS mediumscore(USERNAME text, SCORE int)')
            conn.commit()
            create.execute('SELECT * FROM mediumscore')
            z = create.fetchall()
            #print(z)
            conn.close()

            z.sort(key=lambda x: x[1], reverse=True)
            top = z[:10]
            #print(top)

            print_records = ''
            for index, record in enumerate(top, 1):
                print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + "\n\n"

            rec_title = Label(ar_frame, text=' Rank\t           Name\t  Score')
            rec_title.config(font=('rockwell 15'), fg='black', bg='#00d5e0')
            rec_title.place(relx=0.5, rely=0.2, anchor=CENTER)
            rec = Label(ar_frame, text=print_records)
            rec.config(font=('rockwell 12'), fg='black', bg='#00d5e0')
            rec.place(relx=0.5, rely=0.55, anchor=CENTER)

            e_leadboard["state"] = NORMAL
            e_leadboard['background'] = '#df144c'
            m_leadboard["state"] = DISABLED
            m_leadboard['background'] = '#33B5E5'
            h_leadboard["state"] = NORMAL
            h_leadboard['background'] = '#df144c'

            def mreset():
                answer = messagebox.askyesno(title='Reset Score',
                                             message='Are you sure that you want to reset record?')
                if answer:
                    conn = sqlite3.connect('mediumscore.db')
                    create = conn.cursor()
                    create.execute('CREATE TABLE IF NOT EXISTS mediumscore(USERNAME text, SCORE int)')
                    create.execute('DELETE FROM mediumscore;', )
                    conn.commit()
                    z = create.fetchall()
                    conn.close()

                    all_rank(med)

            btnfont = font.Font(size=12)
            m_reset = Button(ar_frame, text='Reset', command=mreset, bg="#df144c", fg="white")
            m_reset.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
            m_reset['font'] = btnfont
            m_reset.place(relx=0.5, rely=0.95, anchor=S)

        if type == 'hard':
            top_title = Label(ar_frame, text='Highscores')
            top_title.config(font=('rockwell 20'), fg='black', bg='#00d5e0')
            top_title.place(relx=0.5, rely=0.1, anchor=CENTER)

            playername = uname.get()

            conn = sqlite3.connect('hardscore.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS hardscore(USERNAME text, SCORE int)')
            conn.commit()
            create.execute('SELECT * FROM hardscore')
            z = create.fetchall()
            #print(z)
            conn.close()

            z.sort(key=lambda x: x[1], reverse=True)
            top = z[:10]
            #print(top)

            print_records = ''
            for index, record in enumerate(top, 1):
                print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + "\n\n"

            rec_title = Label(ar_frame, text=' Rank\t           Name\t  Score')
            rec_title.config(font=('rockwell 15'), fg='black', bg='#00d5e0')
            rec_title.place(relx=0.5, rely=0.2, anchor=CENTER)
            rec = Label(ar_frame, text=print_records)
            rec.config(font=('rockwell 12'), fg='black', bg='#00d5e0')
            rec.place(relx=0.5, rely=0.55, anchor=CENTER)

            e_leadboard["state"] = NORMAL
            e_leadboard['background'] = '#df144c'
            m_leadboard["state"] = NORMAL
            m_leadboard['background'] = '#df144c'
            h_leadboard["state"] = DISABLED
            h_leadboard['background'] = '#33B5E5'

            def hreset():
                answer = messagebox.askyesno(title='Reset Score',
                                             message='Are you sure that you want to reset record?')
                if answer:
                    conn = sqlite3.connect('hardscore.db')
                    create = conn.cursor()
                    create.execute('CREATE TABLE IF NOT EXISTS hardscore(USERNAME text, SCORE int)')
                    create.execute('DELETE FROM hardscore;', )
                    conn.commit()
                    z = create.fetchall()
                    conn.close()

                    all_rank(hr)

            btnfont = font.Font(size=12)
            h_reset = Button(ar_frame, text='Reset', command=hreset, bg="#df144c", fg="white")
            h_reset.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
            h_reset['font'] = btnfont
            h_reset.place(relx=0.5, rely=0.95, anchor=S)

    def backtohmenu():
        ld.withdraw()
        hmenu.deiconify()

    ez = 'easy'
    med = 'medium'
    hr = 'hard'

    btnfont = font.Font(size=12)
    e_leadboard = Button(ld_frame, text='Easy', command=lambda: all_rank(ez), bg="#df144c", fg="white")
    e_leadboard.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    e_leadboard['font'] = btnfont
    e_leadboard.place(relx=0.1, rely=0.15)
    m_leadboard = Button(ld_frame, text='Medium', command=lambda: all_rank(med), bg="#df144c", fg="white")
    m_leadboard.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    m_leadboard['font'] = btnfont
    m_leadboard.place(relx=0.1, rely=0.35)
    h_leadboard = Button(ld_frame, text='Hard', command=lambda: all_rank(hr), bg="#df144c", fg="white")
    h_leadboard.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    h_leadboard['font'] = btnfont
    h_leadboard.place(relx=0.1, rely=0.55)
    back_btn = Button(ld_frame, text='Back', command=backtohmenu, bg="black", fg="white")
    back_btn.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    back_btn['font'] = btnfont
    back_btn.place(relx=0.1, rely=0.75)

    all_rank(ez)

    ld.mainloop()


def easy():
    global e
    e = Tk()
    e.title('Quiz Game - Easy Level')

    easy_canvas = Canvas(e, width=800, height=480, bg="#df144c")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="#000e44")
    easy_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    def countDown():
        check = 0
        for k in range(15, 0, -1):

            if k == 1:
                check = -1

            timer.configure(text='Timer\n' + str(k), bg="#000e44", font="calibri 16", fg="#ed01f4")
            timer.place(relx=0.5, rely=0.1, anchor=CENTER)
            easy_frame.update()
            time.sleep(1)

        timer.configure(text="\nTimes up!", bg="#000e44", font="calibri 16", fg="#ed01f4")
        timer.place(relx=0.5, rely=0.1, anchor=CENTER)
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    global mistake
    global correctans
    score = 0
    mistake = 0
    correctans = 0

    from easy import easyQ, answer

    az = random.sample(easyQ, 5)
    #print(az)
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    lvltitle = Label(easy_frame, text='Easy', font="calibri 18", bg="#000e44", fg='#ed01f4')
    lvltitle.place(relx=0.5, rely=0.22, anchor=CENTER)
    ques = Label(easy_frame, text=az[x][0], font="calibri 18", bg="#000e44", fg='white')
    ques.place(relx=0.5, rely=0.4, anchor=CENTER)

    var = IntVar()

    a = Radiobutton(easy_frame, text='True', font="calibri 18", value=az[x][1], variable=var, bg="#000e44",
                    fg='#CFCFCF', selectcolor='black')
    a.place(relx=0.5, rely=0.5, anchor=CENTER)

    b = Radiobutton(easy_frame, text="False", font="calibri 18", value=az[x][2], variable=var, bg="#000e44",
                    fg='#CFCFCF', selectcolor='black')
    b.place(relx=0.5, rely=0.6, anchor=CENTER)

    my_score = Label(easy_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
    my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

    li.remove(x)

    timer = Label(e)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():
        global mistake
        if len(li) == 1:
            e.destroy()
            easyMark(score, mistake, correctans)
            #print(score)
        if len(li) == 2:
            # mistake += 1
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=az[x][0])

            a.configure(text="True", value=az[x][1], selectcolor='black')

            b.configure(text="False", value=az[x][2], selectcolor='black')

            my_score = Label(easy_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
            my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

            li.remove(x)
            y = countDown()
            if y == -1:
                mistake += 1
                display()

    def calc():
        global score
        global mistake
        global correctans

        if (var.get() in answer):
            score += 2
            correctans += 1

        else:
            mistake += 1

        #print('score: ' + str(score))
        display()

    btnfont = font.Font(size=12)
    submit = Button(easy_frame, command=calc, text="Submit", bg="#df144c", fg="white")
    submit.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    submit['font'] = btnfont
    submit.place(relx=0.5, rely=0.75, anchor=CENTER)

    def nextques():
        global mistake
        mistake += 1
        display()

    nextQuestion = Button(easy_frame, command=nextques, text="Next", fg="white", bg="black")
    nextQuestion.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    nextQuestion.place(relx=0.5, rely=0.85, anchor=CENTER)

    def xez():
        e.destroy()
        exiteasy()

    exitbtn = Button(easy_frame, text="X", command=xez, fg="#ed01f4", bg="black")
    exitbtn.configure(width=5, height=1, activebackground="#33B5E5", relief=FLAT)
    exitbtn.place(relx=0.1, rely=0.1, anchor=CENTER)

    y = countDown()
    if y == -1:
        mistake += 1
        display()

    e.mainloop()


def medium():
    global m
    m = Tk()
    m.title('Quiz Game - Medium Level')

    med_canvas = Canvas(m, width=800, height=490, bg="#df144c")
    med_canvas.pack()

    med_frame = Frame(med_canvas, bg="#000e44")
    med_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    def countDown():
        check = 0
        for k in range(25, 0, -1):

            if k == 1:
                check = -1
            timer.configure(text='Timer\n' + str(k), bg="#000e44", font="calibri 16", fg="#ed01f4")
            timer.place(relx=0.5, rely=0.1, anchor=CENTER)
            med_frame.update()
            time.sleep(1)

        timer.configure(text="\nTimes up!", bg="#000e44", font="calibri 16", fg="#ed01f4")
        timer.place(relx=0.5, rely=0.1, anchor=CENTER)
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    global mistake
    global correctans
    score = 0
    mistake = 0
    correctans = 0

    from medium import mediumQ, answer
    az = random.sample(mediumQ, 5)
    #print(az)
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    lvltitle = Label(med_frame, text='Medium', font="calibri 18", bg="#000e44", fg='#ed01f4')
    lvltitle.place(relx=0.5, rely=0.22, anchor=CENTER)
    ques = Label(med_frame, text=az[x][0], font="calibri 15", bg="#000e44", fg='white')
    ques.place(relx=0.5, rely=0.4, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(med_frame, text=az[x][1], font="calibri 14", value=az[x][1], tristatevalue='x', variable=var,
                    bg="#000e44", fg='#CFCFCF', selectcolor='black')
    a.place(relx=0.3, rely=0.55, anchor=CENTER)

    b = Radiobutton(med_frame, text=az[x][2], font="calibri 14", value=az[x][2], tristatevalue='x', variable=var,
                    bg="#000e44", fg='#CFCFCF', selectcolor='black')
    b.place(relx=0.3, rely=0.65, anchor=CENTER)

    c = Radiobutton(med_frame, text=az[x][3], font="calibri 14", value=az[x][3], tristatevalue='x', variable=var,
                    bg="#000e44", fg='#CFCFCF', selectcolor='black')
    c.place(relx=0.7, rely=0.55, anchor=CENTER)

    d = Radiobutton(med_frame, text=az[x][4], font="calibri 14", value=az[x][4], tristatevalue='x', variable=var,
                    bg="#000e44", fg='#CFCFCF', selectcolor='black')
    d.place(relx=0.7, rely=0.65, anchor=CENTER)

    my_score = Label(med_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
    my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

    #print(var.get())

    li.remove(x)

    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():
        global mistake

        if len(li) == 1:
            m.destroy()
            mediumMark(score, mistake, correctans)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=az[x][0])

            a.configure(text=az[x][1], tristatevalue='x', value=az[x][1], selectcolor='black')

            b.configure(text=az[x][2], tristatevalue='x', value=az[x][2], selectcolor='black')

            c.configure(text=az[x][3], tristatevalue='x', value=az[x][3], selectcolor='black')

            d.configure(text=az[x][4], tristatevalue='x', value=az[x][4], selectcolor='black')

            my_score = Label(med_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
            my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

            #print(var.get())

            li.remove(x)
            y = countDown()
            if y == -1:
                mistake += 1
                display()

    def calc():
        global score
        global mistake
        global correctans

        if (var.get() in answer):
            score += 5
            correctans += 1
        else:
            mistake += 1

        #print('score' + str(score))
        display()

    btnfont = font.Font(size=12)
    submit = Button(med_frame, command=calc, text="Submit", bg="#df144c", fg="white")
    submit.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    submit['font'] = btnfont
    submit.place(relx=0.5, rely=0.8, anchor=CENTER)

    def nextques():
        global mistake
        mistake += 1
        display()

    nextQuestion = Button(med_frame, command=nextques, text="Next", fg="white", bg="black")
    nextQuestion.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    nextQuestion.place(relx=0.5, rely=0.9, anchor=CENTER)

    def xmd():
        m.destroy()
        exitmed()

    exitbtn = Button(med_frame, text="X", command=xmd, fg="#ed01f4", bg="black")
    exitbtn.configure(width=5, height=1, activebackground="#33B5E5", relief=FLAT)
    exitbtn.place(relx=0.1, rely=0.1, anchor=CENTER)

    y = countDown()
    if y == -1:
        mistake += 1
        display()
    m.mainloop()


def difficult():
    global h
    h = Tk()
    h.title('Quiz Game - Hard Level')

    hard_canvas = Canvas(h, width=800, height=490, bg="#df144c")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas, bg="#000e44")
    hard_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    def countDown():
        check = 0
        for k in range(30, 0, -1):

            if k == 1:
                check = -1

            timer.configure(text='Timer\n' + str(k), bg="#000e44", font="calibri 16", fg="#ed01f4")
            timer.place(relx=0.5, rely=0.1, anchor=CENTER)
            hard_frame.update()
            time.sleep(1)

        timer.configure(text="\nTimes up!", bg="#000e44", font="calibri 16", fg="#ed01f4")
        timer.place(relx=0.5, rely=0.1, anchor=CENTER)
        if check == -1:
            return (-1)
        else:
            return 0

    global score
    global mistake
    global correctans
    score = 0
    mistake = 0
    correctans = 0

    from hard import hardq
    az = random.sample(hardq.items(), 5)
    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])
    #print(az)

    rand_q_answer = []
    for i in az:
        rand_q_answer.append(i[1])
    #print(rand_q_answer)
    la = (map(lambda x: x.lower(), rand_q_answer))
    ua = (map(lambda x: x.upper(), rand_q_answer))
    lower_ans = list(la)
    upper_ans = list(ua)
    #print(lower_ans)
    #print(upper_ans)

    lvltitle = Label(hard_frame, text='Hard', font="calibri 18", bg="#000e44", fg='#ed01f4')
    lvltitle.place(relx=0.5, rely=0.22, anchor=CENTER)
    ques = Label(hard_frame, text=az[x][0], font="calibri 16", bg="#000e44", fg='white')
    ques.place(relx=0.5, rely=0.4, anchor=CENTER)

    answer_entry = Entry(hard_frame, bg='#221322', fg='#e1e6e6', textvariable=uname, highlightthickness=2)
    answer_entry.config(borderwidth=5, highlightbackground="#00d5e0", highlightcolor="#00d5e0", relief=FLAT, width=20,
                        justify='center', font=('calibri 16'))
    answer_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

    my_score = Label(hard_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
    my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

    li.remove(x)

    timer = Label(h)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    def display():
        global mistake
        answer_entry.delete(0, 'end')
        if len(li) == 1:
            h.destroy()
            hardMark(score, mistake, correctans)
        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])
            ques.configure(text=az[x][0])
            answer_entry.configure()

            my_score = Label(hard_frame, text='Score\n' + str(score), fg='#ed01f4', bg="#000e44", font="calibri 16")
            my_score.place(relx=0.9, rely=0.1, anchor=CENTER)

            li.remove(x)
            y = countDown()
            if y == -1:
                mistake += 1
                answer_entry.delete(0, 'end')
                display()

    def calc():
        global score
        global mistake
        global correctans

        if answer_entry.get() in rand_q_answer or answer_entry.get() in lower_ans or answer_entry.get() in upper_ans:
            score += 10
            correctans += 1
        else:
            mistake += 1

        #print(answer_entry.get())
        #print(score)
        answer_entry.delete(0, 'end')
        display()

    btnfont = font.Font(size=12)
    submit = Button(hard_frame, command=calc, text="Submit", bg="#df144c", fg="white")
    submit.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    submit['font'] = btnfont
    submit.place(relx=0.5, rely=0.8, anchor=CENTER)


    def nextques():
        global mistake
        mistake += 1
        display()

    nextQuestion = Button(hard_frame, command=nextques, text="Next", fg="white", bg="black")
    nextQuestion.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    nextQuestion.place(relx=0.5, rely=0.9, anchor=CENTER)

    def xhd():
        h.destroy()
        exithard()

    exitbtn = Button(hard_frame, text="X", command=xhd, fg="#ed01f4", bg="black")
    exitbtn.configure(width=5, height=1, activebackground="#33B5E5", relief=FLAT)
    exitbtn.place(relx=0.1, rely=0.1, anchor=CENTER)

    y = countDown()
    if y == -1:
        mistake += 1
        display()
    h.mainloop()


def exiteasy():
    global ec
    ec = Tk()
    ec.title('Quiz Game')

    ec_canvas = Canvas(ec, width=430, height=400, bg="#df144c")
    ec_canvas.pack()

    ec_frame = Frame(ec_canvas, bg="#000e44")
    ec_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(ec_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    eclabel = Label(ec_frame, text='Try different level?')
    eclabel.config(font=('calibri 15'), fg='white', bg='#000e44', justify=LEFT)
    eclabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def choose(level):
        if level == 1:
            ec.destroy()
            medium()
        elif level == 2:
            ec.destroy()
            difficult()

    btnfont = font.Font(size=12)
    mediumR = Button(ec_frame, text='Medium', command=lambda: choose(1), bg="#df144c", fg="white")
    mediumR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    mediumR['font'] = btnfont
    mediumR.place(relx=0.5, rely=0.6, anchor=CENTER)

    hardR = Button(ec_frame, text='Hard', command=lambda: choose(2), bg="#df144c", fg="white")
    hardR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    hardR['font'] = btnfont
    hardR.place(relx=0.5, rely=0.7, anchor=CENTER)

    quitbtn = Button(ec_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.8, anchor=CENTER)

    ec.mainloop()


def exitmed():
    global xmed
    xmed = Tk()
    xmed.title('Quiz Game')

    xmed_canvas = Canvas(xmed, width=430, height=400, bg="#df144c")
    xmed_canvas.pack()

    xmed_frame = Frame(xmed_canvas, bg="#000e44")
    xmed_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(xmed_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    xmedlabel = Label(xmed_frame, text='Try different level?')
    xmedlabel.config(font=('calibri 15'), fg='white', bg='#000e44', justify=LEFT)
    xmedlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def choose(level):
        if level == 1:
            xmed.destroy()
            easy()
        elif level == 2:
            xmed.destroy()
            difficult()

    btnfont = font.Font(size=12)
    easyR = Button(xmed_frame, text='Easy', command=lambda: choose(1), bg="#df144c", fg="white")
    easyR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    easyR['font'] = btnfont
    easyR.place(relx=0.5, rely=0.6, anchor=CENTER)

    hardR = Button(xmed_frame, text='Hard', command=lambda: choose(2), bg="#df144c", fg="white")
    hardR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    hardR['font'] = btnfont
    hardR.place(relx=0.5, rely=0.7, anchor=CENTER)

    quitbtn = Button(xmed_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.8, anchor=CENTER)

    xmed.mainloop()


def exithard():
    global xhr
    xhr = Tk()
    xhr.title('Quiz Game')

    xhr_canvas = Canvas(xhr, width=430, height=400, bg="#df144c")
    xhr_canvas.pack()

    xhr_frame = Frame(xhr_canvas, bg="#000e44")
    xhr_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(xhr_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    xhrlabel = Label(xhr_frame, text='Try different level?')
    xhrlabel.config(font=('calibri 15'), fg='white', bg='#000e44', justify=LEFT)
    xhrlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

    def choose(level):
        if level == 1:
            xhr.destroy()
            easy()
        elif level == 2:
            xhr.destroy()
            medium()

    btnfont = font.Font(size=12)
    easyR = Button(xhr_frame, text='Easy', command=lambda: choose(1), bg="#df144c", fg="white")
    easyR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    easyR['font'] = btnfont
    easyR.place(relx=0.5, rely=0.6, anchor=CENTER)

    mediumR = Button(xhr_frame, text='Medium', command=lambda: choose(2), bg="#df144c", fg="white")
    mediumR.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    mediumR['font'] = btnfont
    mediumR.place(relx=0.5, rely=0.7, anchor=CENTER)

    quitbtn = Button(xhr_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.8, anchor=CENTER)

    xhr.mainloop()


def easyMark(mark, wrong, correct):
    global escore
    global sm
    global ez

    sm = Tk()
    sm.title('Quiz Game - Score')

    em_canvas = Canvas(sm, width=430, height=460, bg="#df144c")
    em_canvas.pack()

    em_frame = Frame(em_canvas, bg="#000e44")
    em_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(em_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    items = Label(em_frame, text='Items: 5')
    items.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    items.place(relx=0.5, rely=0.45, anchor=CENTER)
    check = Label(em_frame, text='Correct: ' + str(correct))
    check.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    check.place(relx=0.5, rely=0.55, anchor=CENTER)
    wlabel = Label(em_frame, text='Mistake: ' + str(wrong), fg="black", bg="white")
    wlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    wlabel.place(relx=0.5, rely=0.65, anchor=CENTER)
    mlabel = Label(em_frame, text='Score: ' + str(mark), fg="black", bg="white")
    mlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    mlabel.place(relx=0.5, rely=0.75, anchor=CENTER)
    escore = str(mark)

    def rankez():
        ez = 'easy'
        sm.destroy()
        rank(ez)

    btnfont = font.Font(size=10)
    savebtn = Button(em_frame, command=rankez, text="Save", bg="#df144c", fg="white")
    savebtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    savebtn['font'] = btnfont
    savebtn.place(relx=0.5, rely=0.88, anchor=CENTER)

    quitbtn = Button(em_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.95, anchor=CENTER)

    sm.mainloop()


def mediumMark(mark, wrong, correct):
    global sm
    global mscore
    global med

    sm = Tk()
    sm.title('Quiz Game - Score')

    mm_canvas = Canvas(sm, width=430, height=460, bg="#df144c")
    mm_canvas.pack()

    mm_frame = Frame(mm_canvas, bg="#000e44")
    mm_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(mm_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    items = Label(mm_frame, text='Items: 5')
    items.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    items.place(relx=0.5, rely=0.45, anchor=CENTER)
    check = Label(mm_frame, text='Correct: ' + str(correct))
    check.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    check.place(relx=0.5, rely=0.55, anchor=CENTER)
    wlabel = Label(mm_frame, text='Mistake: ' + str(wrong), fg="black", bg="white")
    wlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    wlabel.place(relx=0.5, rely=0.65, anchor=CENTER)
    mlabel = Label(mm_frame, text='Score: ' + str(mark), fg="black", bg="white")
    mlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    mlabel.place(relx=0.5, rely=0.75, anchor=CENTER)
    mscore = str(mark)

    def rankmed():
        med = 'medium'
        sm.destroy()
        rank(med)

    btnfont = font.Font(size=10)
    savebtn = Button(mm_frame, command=rankmed, text="Save", bg="#df144c", fg="white")
    savebtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    savebtn['font'] = btnfont
    savebtn.place(relx=0.5, rely=0.88, anchor=CENTER)

    quitbtn = Button(mm_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.95, anchor=CENTER)

    sm.mainloop()


def hardMark(mark, wrong, correct):
    global sm
    global hscore
    global hr

    sm = Tk()
    sm.title('Quiz Game - Score')

    hm_canvas = Canvas(sm, width=430, height=460, bg="#df144c")
    hm_canvas.pack()

    hm_frame = Frame(hm_canvas, bg="#000e44")
    hm_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(hm_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=N)

    items = Label(hm_frame, text='Items: 5')
    items.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    items.place(relx=0.5, rely=0.45, anchor=CENTER)
    check = Label(hm_frame, text='Correct: ' + str(correct))
    check.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    check.place(relx=0.5, rely=0.55, anchor=CENTER)
    wlabel = Label(hm_frame, text='Mistake: ' + str(wrong), fg="black", bg="white")
    wlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    wlabel.place(relx=0.5, rely=0.65, anchor=CENTER)
    mlabel = Label(hm_frame, text='Score: ' + str(mark), fg="black", bg="white")
    mlabel.config(font=('rockwell 13'), fg='white', bg='#000e44', justify=LEFT)
    mlabel.place(relx=0.5, rely=0.75, anchor=CENTER)
    hscore = str(mark)

    def rankhard():
        hr = 'hard'
        sm.destroy()
        rank(hr)

    btnfont = font.Font(size=10)
    savebtn = Button(hm_frame, command=rankhard, text="Save", bg="#df144c", fg="white")
    savebtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    savebtn['font'] = btnfont
    savebtn.place(relx=0.5, rely=0.88, anchor=CENTER)

    quitbtn = Button(hm_frame, command=quit, text="Quit", fg="white", bg="black")
    quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
    quitbtn.place(relx=0.5, rely=0.95, anchor=CENTER)

    sm.mainloop()


def rank(type):
    # sm.destroy()
    global rnk
    rnk = Tk()
    rnk.title('Quiz Game - Leaderboard')

    rank_canvas = Canvas(rnk, width=800, height=700, bg="#df144c")
    rank_canvas.pack()

    rank_frame = Frame(rank_canvas, bg="#000e44")
    rank_frame.place(relwidth=0.95, relheight=1, relx=0.5, rely=0.5, anchor=CENTER)

    render = PhotoImage(file='logo.png')
    img = Label(rank_frame, image=render, bg="#000e44")
    img.image = render
    img.place(relx=0.5, rely=0.09, anchor=CENTER)

    if type == 'easy':
        playername = uname.get()

        conn = sqlite3.connect('easyscore.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS easyscore(USERNAME text, SCORE int)')
        create.execute("INSERT INTO easyscore VALUES (?,?)", (playername, escore))
        conn.commit()
        create.execute('SELECT * FROM easyscore')
        z = create.fetchall()
        #print(z)
        conn.close()

        z.sort(key=lambda x: x[1], reverse=True)
        top = z[:20]
        #print(top)

        print_records = ''
        for index, record in enumerate(top, 1):
            print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + " \n"

        rec_title = Label(rank_frame, text=' Rank\t           Name\t  Score')
        rec_title.config(font=('rockwell 15'), fg='white', bg='#000e44')
        rec_title.place(relx=0.5, rely=0.22, anchor=CENTER)
        rec = Label(rank_frame, text=print_records)
        rec.config(font=('rockwell 13'), fg='white', bg='#000e44')
        rec.place(relx=0.5, rely=0.55, anchor=CENTER)

        def diflvl():
            rnk.destroy()
            exiteasy()

        quitbtn = Button(rank_frame, command=diflvl, text="Next", fg="white", bg="black")
        quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
        quitbtn.place(relx=0.5, rely=0.93, anchor=CENTER)

    if type == 'medium':

        playername = uname.get()

        conn = sqlite3.connect('mediumscore.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS mediumscore(USERNAME text, SCORE int)')
        create.execute("INSERT INTO mediumscore VALUES (?,?)", (playername, mscore))
        conn.commit()
        create.execute('SELECT * FROM mediumscore')
        z = create.fetchall()
        #print(z)
        conn.close()

        z.sort(key=lambda x: x[1], reverse=True)
        top = z[:20]
        #print(top)

        print_records = ''
        for index, record in enumerate(top, 1):
            print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + " \n"

        rec_title = Label(rank_frame, text=' Rank\t           Name\t  Score')
        rec_title.config(font=('rockwell 15'), fg='white', bg='#000e44')
        rec_title.place(relx=0.5, rely=0.22, anchor=CENTER)
        rec = Label(rank_frame, text=print_records)
        rec.config(font=('rockwell 13'), fg='white', bg='#000e44')
        rec.place(relx=0.5, rely=0.55, anchor=CENTER)

        def diflvl():
            rnk.destroy()
            exitmed()

        quitbtn = Button(rank_frame, command=diflvl, text="Next", fg="white", bg="black")
        quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
        quitbtn.place(relx=0.5, rely=0.93, anchor=CENTER)

    if type == 'hard':

        playername = uname.get()

        conn = sqlite3.connect('hardscore.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS hardscore(USERNAME text, SCORE int)')
        create.execute("INSERT INTO hardscore VALUES (?,?)", (playername, hscore))
        conn.commit()
        create.execute('SELECT * FROM hardscore')
        z = create.fetchall()
        #print(z)
        conn.close()

        z.sort(key=lambda x: x[1], reverse=True)
        top = z[:20]
        #print(top)

        print_records = ''
        for index, record in enumerate(top, 1):
            print_records += str(index) + "\t\t" + str(record[0]) + "\t\t" + str(record[1]) + " \n"

        rec_title = Label(rank_frame, text=' Rank\t           Name\t  Score')
        rec_title.config(font=('rockwell 15'), fg='white', bg='#000e44')
        rec_title.place(relx=0.5, rely=0.22, anchor=CENTER)
        rec = Label(rank_frame, text=print_records)
        rec.config(font=('rockwell 13'), fg='white', bg='#000e44')
        rec.place(relx=0.5, rely=0.55, anchor=CENTER)

        def diflvl():
            rnk.destroy()
            exithard()

        quitbtn = Button(rank_frame, command=diflvl, text="Next", fg="white", bg="black")
        quitbtn.configure(width=13, height=1, activebackground="#33B5E5", relief=FLAT)
        quitbtn.place(relx=0.5, rely=0.93, anchor=CENTER)

    rnk.mainloop()


def start():
    global root
    root = Tk()
    root.title('Welcome To Quiz Game')
    canvas = Canvas(root, width=782, height=440, bg='#000e44')
    canvas.grid(column=0, row=0)
    img = PhotoImage(file="QUIZ GAME gENERAL MATHEMATICS.png")
    canvas.create_image(25, 10, image=img, anchor=NW)

    btnfont = font.Font(size=15)
    button = Button(root, text='Start', command=playerUname, bg="#221626", fg="#ff00ff")
    button.configure(width=20, height=1, activebackground="#33B5E5", relief=RAISED)
    button['font'] = btnfont
    button.place(relx=0.5, rely=0.8, anchor=S)

    root.mainloop()


if __name__ == '__main__':
    start()