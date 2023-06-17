def main():
    import tkinter as tk
    #from tkinter import *
    from tkinter import messagebox as ms
    import sqlite3
    from PIL import Image, ImageTk
    import re


    window = tk.Tk()
    window.geometry("700x700")
    window.title("Lecture Details FORM")
   #window.configure(background="grey")
    
    

    staff_name = tk.StringVar()
    lecture_subject = tk.StringVar()
    lecture_date = tk.StringVar()
    start_time = tk.StringVar()
    end_time = tk.StringVar()



    db = sqlite3.connect(r'C:\Users\hrish\OneDrive\Desktop\100%-lecture_evaluation_Shital Code\100%-lecture_evaluation_Shital Code\evaluation.db')
    cursor = db.cursor()

    cursor.execute("DROP TABLE lecture_details;")

    cursor.execute("CREATE TABLE IF NOT EXISTS lecture_details"
                   "(staff_name TEXT,lecture_subject TEXT,lecture_date TEXT,start_time TEXT, end_time TEXT)")
    db.commit()


    def submit():
        name= staff_name.get()
        lecture_subject1 = lecture_subject.get()
        date = lecture_date.get()
        time1 = start_time.get()
        time2 = end_time.get()

        with sqlite3.connect(r'C:\Users\hrish\OneDrive\Desktop\100%-lecture_evaluation_Shital Code\100%-lecture_evaluation_Shital Code\evaluation.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        #find_user = ('SELECT * FROM lecture_details WHERE staff_name = ?')
        #c.execute(find_user, [(staff_name.get())])

        #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        ####if (re.search(regex, lecture_date)):
           ### a = True
        #####else:
          ####  a = False

        if (name.isdigit() or (name == "")):
                ms.showinfo("Message", "please enter valid name")

        elif (lecture_subject1 == ""):
                ms.showinfo("Message", "Please Enter valid lecture_subject")

        elif (date == ""):
                ms.showinfo("Message", "Please Enter valid date")

        elif (time1 == ""):
                ms.showinfo("Message", "Please Enter valid start_time")
        elif (time2 == ""):
                ms.showinfo("Message", "Please Enter valid start_time")

        else:
            conn = sqlite3.connect(r'C:\Users\hrish\OneDrive\Desktop\100%-lecture_evaluation_Shital Code\100%-lecture_evaluation_Shital Code\evaluation.db')
            with conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        'INSERT INTO lecture_details(staff_name,lecture_subject,lecture_date, start_time, end_time) VALUES(?,?,?,?,?)',
                        (name,lecture_subject1,date,time1,time2))

                    conn.commit()
                    db.close()
                    ms.showinfo('Success!', 'Details Submitted Successfully !')
                    # window.destroy()
                    window.destroy()
                    from subprocess import call
                    call (['python',r'C:\Users\hrish\OneDrive\Desktop\100%-lecture_evaluation_Shital Code\100%-lecture_evaluation_Shital Code\Lecture_GUImaster.py'])


    image2 = Image.open(r'C:\Users\hrish\OneDrive\Desktop\100%-lecture_evaluation_Shital Code\100%-lecture_evaluation_Shital Code\bookimg2.jpg')
    image2 = image2.resize((700, 700),Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)

    background_label = tk.Label(window, image=background_image)

    background_label.image = background_image

    background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

    l1 = tk.Label(window, text="Lecture Details", font=("Times new roman", 30, "bold"), bg="cyan", fg="black")
    l1.place(x=220, y=50)


    l2 = tk.Label(window, text="Staff Name :", width=12, font=("Times new roman", 18, "bold"), bg="cyan")
    l2.place(x=130, y=150)
    t1 = tk.Entry(window, textvar=staff_name, width=20, font=('', 18))
    t1.place(x=330, y=150)

    l7 = tk.Label(window, text="Subject :", width=12, font=("Times new roman", 18, "bold"), bg="cyan")
    l7.place(x=130, y=230)
    t6 = tk.Entry(window, textvar=lecture_subject, width=20, font=('', 18))
    t6.place(x=330, y=230)

    l3 = tk.Label(window, text="Date :", width=12, font=("Times new roman", 18, "bold"), bg="cyan")
    l3.place(x=130, y=310)
    t2 = tk.Entry(window, textvar=lecture_date, width=20, font=('', 18))
    t2.place(x=330, y=310)

    l5 = tk.Label(window, text="Start Time :", width=12, font=("Times new roman", 18, "bold"), bg="cyan")
    l5.place(x=130, y=390)
    t4 = tk.Entry(window, textvar=start_time, width=20, font=('', 18))
    t4.place(x=330, y=390)

    l6 = tk.Label(window, text="End Time :", width=12, font=("Times new roman", 18, "bold"), bg="cyan")
    l6.place(x=130, y=470)
    t5 = tk.Entry(window, textvar=end_time, width=20, font=('', 18))
    t5.place(x=330, y=470)

    btn = tk.Button(window, text="Submit",font=("Times new roman",20,"bold"), bg="cyan", fg="black", width=10, height=1, command=submit)
    btn.place(x=250, y=600)

    window.mainloop()
main()