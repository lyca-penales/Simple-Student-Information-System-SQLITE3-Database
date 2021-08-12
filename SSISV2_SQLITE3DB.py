from tkinter import*
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

SSIS = Tk()
SSIS.geometry("1250x640+8+0")
SSIS.title("MSU-IIT SSIS")

#***************************************************GLOBAL VARIABLES***************************************************#
field_names = ["ID Number", "Name", "Gender", "Year Level", "Course Code", "Course"]
Cfield_names = ["Course Code", "Course"]
idnumber_entry = ""
name_entry = "" 
gender_entry = ""
yearlvl_entry = ""
courseCode_entry = ""
course_entry = ""
courseCode_Centry = ""
course_Centry = ""
greetings1 = ""
Search_Student_id = ""
idnumber_entryU = ""
name_entryU = ""
gender_entryU = ""
yearlvl_entryU = ""
courseCode_entryU = ""
TreeView = ttk.Treeview(SSIS)
CtreeView = ttk.Treeview(SSIS)

student_id = StringVar()
name = StringVar()
gender = StringVar()
year_lvl = StringVar()
course_code = StringVar()
course = StringVar()
ssis_db = sqlite3.connect("student_info.db")
cur = ssis_db.cursor()

#***************************************************DATABASE***************************************************#
def student_info_db():
    #initiate database
    con = sqlite3.connect("student_info.db")
    cur = con.cursor()
    #create table
    cur.execute("""CREATE TABLE IF NOT EXISTS courses(
                   Course_Code TEXT PRIMARY KEY,
                   Course_Name TEXT NOT NULL);
                   """)
    cur.execute("""CREATE TABLE IF NOT EXISTS student_info(
                   Student_Id TEXT PRIMARY KEY,
                   Name TEXT NOT NULL,
                   Gender TEXT NOT NULL,
                   Year_Level TEXT NOT NULL,
                   Course_Code TEXT,
                   FOREIGN KEY (Course_Code)REFERENCES courses(Course_Code));
                   """)
    #insert values
    #cur.execute("""INSERT INTO courses (Course_Code, Course_Name) VALUES ("BSCS", "Bachelor of Science in Computer Science");""")
    #cur.execute("""INSERT INTO courses (Course_Code, Course_Name) VALUES ("BSCA", "Bachelor of Science in Computer Application");""")
    #cur.execute("""INSERT INTO courses (Course_Code, Course_Name) VALUES ("BSIT", "Bachelor of Science in Information Technology");""")
    #cur.execute("""INSERT INTO courses (Course_Code, Course_Name) VALUES ("BSIS", "Bachelor of Science in Information Systems");""")
    #cur.execute("""INSERT INTO student_info (Student_Id, Name, Gender, Year_Level) VALUES ("2019-0001", "Angel D. Vera", "Female", "2nd Year");""")
    #cur.execute("""INSERT INTO student_info (Student_Id, Name, Gender, Year_Level) VALUES ("2019-0002", "Do Kyungsoo", "Male", "2nd Year");""")
    #cur.execute("""INSERT INTO student_info (Student_Id, Name, Gender, Year_Level) VALUES ("2019-0003", "Diane J. Suarez", "Female", "2nd Year");""")
    #cur.execute("""INSERT INTO student_info (Student_Id, Name, Gender, Year_Level) VALUES ("2019-0004", "Leah G. Austero", "Female", "2nd Year");""")
                   
    con.commit()
    con.close()

#***************************************************TREEVIEW***************************************************#
#student data treeview
def my_treeview():
    global fieldnames
    global Treeview

    #Style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background = "goldenrod", foreground = "goldenrod", fieldbackground = "goldenrod")
    style.map("Treeview", background=[("selected", "maroon")])

    #Columns
    TreeView["columns"] = field_names

    #Columns Format
    TreeView.column("#0", stretch = NO, width=0)
    TreeView.column("ID Number", anchor = W, width = 90)
    TreeView.column("Name", anchor = W, width = 160)
    TreeView.column("Gender", anchor = W, width = 80)
    TreeView.column("Year Level", anchor = W, width = 80)
    TreeView.column("Course Code", anchor = W, width = 80)
    TreeView.column("Course", anchor = W, width = 290)

    #Headings
    TreeView.heading("#0", anchor = W)
    TreeView.heading("ID Number", text = "ID Number", anchor = W)
    TreeView.heading("Name", text = "Name", anchor = W)
    TreeView.heading("Gender", text = "Gender", anchor = W)
    TreeView.heading("Year Level", text = "Year Level", anchor = W)
    TreeView.heading("Course Code", text = "Course Code", anchor = W)
    TreeView.heading("Course", text = "Course", anchor = W)

    TreeView.place(x = 34, y = 300)

#course data treview
def course_treeview():
    global Cfield_names
    global CtreeView

    #Style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background = "goldenrod", foreground = "goldenrod", fieldbackground = "goldenrod")
    style.map("Treeview", background=[("selected", "maroon")])

    #Columns
    CtreeView["columns"] = Cfield_names

    #Columns Format
    CtreeView.column("#0", stretch = NO, width=0)
    CtreeView.column("Course Code", anchor = W, width = 80)
    CtreeView.column("Course", anchor = W, width = 290)

    #Headings
    CtreeView.heading("#0", anchor = W)
    CtreeView.heading("Course Code", text = "Course Code", anchor = W)
    CtreeView.heading("Course", text = "Course", anchor = W)
  
    CtreeView.place(x = 840, y = 300)

#***************************************************Functions***************************************************#
#displaying student data on the treeview
def display_data(searchResult=None):
    global greetings1
    greetings1.destroy()
    my_treeview()

    StudentList = Label(SSIS, text = "STUDENT LIST",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 20,
                height = 1
                )
    StudentList.place(x = 34, y = 270)

    TreeView.delete(*TreeView.get_children())

    if searchResult:
        for student in searchResult:
            TreeView.insert('', 0, values=[student[0], student[1], student[2], student[3], student[4], student[5]])
    else:
        cur.execute("""
                    SELECT s.Student_Id, s.Name, s.Gender, s.Year_Level, s.Course_Code, c.Course_Name
                    FROM student_info s
                    JOIN courses c ON s.Course_Code = c.Course_Code
                    """)
        fetch = cur.fetchall()
        fetch = [list(i) for i in fetch]
        for info in fetch:
            TreeView.insert('', 0, values=[info[0], info[1], info[2], info[3], info[4], info[5]])

    
#displaying course data on the treeview
def display_course():
    global greetings1
    course_treeview()
     
    StudentList = Label(SSIS, text = "COURSE LIST",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 20,
                height = 1
                )
    StudentList.place(x = 840, y = 270)

    CtreeView.delete(*CtreeView.get_children())
    cur.execute("SELECT * FROM courses")
    fetch = cur.fetchall()
    fetch = [list(i) for i in fetch]
    for info in fetch:
        CtreeView.insert('', 0, values=[info[0], info[1]])

    greetings1.destroy()

#adding data to the database and on the treeview
def add_student():
    global ssis_db
    global idnumber_entry, name_entry, gender_entry, yearlvl_entry, courseCode_entry 
    global course_nameW

    cur.execute("SELECT * FROM courses")
    fetch = cur.fetchall()
    fetch = [list(i)[0] for i in fetch]
    
    if courseCode_entry.get() not in fetch:
        course_code_window()
    else:
        cur.execute('''
                    SELECT s.Student_Id, s.Name, s.Gender, s.Year_Level, s.Course_Code, c.Course_Name
                    FROM student_info s
                    JOIN courses c ON s.Course_Code = c.Course_Code
                        ''')
        cur.execute("INSERT INTO student_info VALUES (:Student_Id, :Name, :Gender, :Year_Level, :Course_Code)",
                   {
                        "Student_Id": idnumber_entry.get(),
                        "Name": name_entry.get(),
                        "Gender": gender_entry.get(),
                        "Year_Level": yearlvl_entry.get(),
                        "Course_Code": courseCode_entry.get()
                    })
        Add_Success()
        ssis_db.commit()
        add_studentW.destroy()
        display_data()
        
#adding new course data to the database and on the treeview in add student function
def add_Scourse():
    global courseCode_Centry, course_Centry
    
    cur.execute("INSERT INTO courses VALUES (:Course_Code, :Course_Name)",
                {
                    "Course_Code": courseCode_Centry.get(),
                    "Course_Name": course_Centry.get()
                })
    ssis_db.commit()
    course_nameW.destroy()
    Addcourse_Success()
    display_course()
    add_student()

#adding new course data to the database and on the treeview
def add_course():
    global courseCode_Centry, course_Centry
    
    cur.execute("INSERT INTO courses VALUES (:Course_Code, :Course_Name)",
                {
                    "Course_Code": courseCode_Centry.get(),
                    "Course_Name": course_Centry.get()
                })
    ssis_db.commit()
    course_nameW.destroy()
    Addcourse_Success()
    display_course()

#updating student data on the database and on the treeview
def update_student():
    global ssis_db
    global idnumber_entryU, name_entryU, gender_entryU, yearlvl_entryU, courseCode_entryU

    cur.execute('''
                SELECT s.Student_Id, s.Name, s.Gender, s.Year_Level, s.Course_Code, c.Course_Name
                FROM student_info s
                JOIN courses c ON s.Course_Code = c.Course_Code
                ''')
    cur.execute("""UPDATE student_info SET
                Name = :name,
                Gender = :gender,
                Year_Level = :yearlvl,
                Course_Code = :courseCode

                WHERE Student_Id = :idnumber""",
                {
                    "name": name_entryU.get(),
                    "gender": gender_entryU.get(),
                    "yearlvl": yearlvl_entryU.get(),
                    "courseCode": courseCode_entryU.get(),
                    "idnumber": idnumber_entryU.get()
                })
    
    ssis_db.commit()
    update_studentW.destroy()
    Update_Success()
    display_data()
    
#updating course data on the database and on the treeview
def update_course():
    global ssis_db
    global courseCode_Centry, course_Centry

    cur.execute('''
                SELECT Course_Code, Course_Name
                FROM courses
                ''')
    cur.execute("""UPDATE courses SET
                Course_Name = :courseName

                WHERE Course_Code = :courseCode""",
                {
                    "courseName": course_Centry.get(),
                    "courseCode": courseCode_Centry.get()
                })

    ssis_db.commit()
    update_courseW.destroy()
    CUpdate_Success()
    display_course()

#deleting student data on the database and on the treeview
def delete_Sdata():
    global ssis_db

    confirmation = messagebox.askokcancel("Delete Warning!",
                                          "Student information will be deleted on the list. \nDo you wish to continue?")
    if confirmation == YES:
        selected = TreeView.item(TreeView.selection())
        selectedID = selected['values'][0]
        cur.execute("DELETE FROM student_info WHERE Student_Id = ?", (selectedID,))

        ssis_db.commit()
        display_data()

#deleting course data on the database and on the treeview
def delete_Cdata():
    global ssis_db

    confirmation = messagebox.askokcancel("Delete Warning!",
                                          "Course information will be deleted on the list. \nDo you wish to continue?")
    if confirmation == YES:
        selected = CtreeView.item(CtreeView.selection())
        selectedID = selected['values'][0]

    if enrollee_checker(selectedID):
        cur.execute("DELETE FROM Courses WHERE Course_Code = ?", (selectedID,))
        ssis_db.commit()
        display_course()
    else:
        messagebox.showinfo("Delete Cancelled.", "Cannot delete an unempty course.")

#checking if there were student enrolled in the course before deleting
def enrollee_checker(selected=None):
    global ssis_db

    cur.execute('''
        SELECT s.Course_Code, c.Course_Name, COUNT(*) AS enrolled 
        FROM student_info s
        JOIN Courses c
        ON c.Course_Code = s.Course_Code
        GROUP BY s.Course_Code
    ''')

    result = cur.fetchall()

    for course in result:
        code, _, num = course
        if code == selected and num != 0:
            return False

    return True

#searching student data on the database and on the treeview
def search_student_data(Student_Id = "", Name = "", Gender = "", Year_Level = "", Course_Code = "", Course_Name = ""):
    global TreeView
    global Search_Student_id
    global greetings1
    
    my_treeview()
    
    TreeView.delete(*TreeView.get_children())

    search1 = (Search_Student_id.get()).lower()
    cur.execute("""
                        SELECT s.Student_Id, s.Name, s.Gender, s.Year_Level, s.Course_Code, c.Course_Name
                        FROM student_info s
                        JOIN courses c ON s.Course_Code = c.Course_Code
                        """)
    result = cur.fetchall()
    result = [list(i) for i in result]
    search_result = []
    for student in result:
        if search1 in [info.lower() for info in student]:
            search_result.append(student)

    if len(search_result) != 0:
        display_data(search_result)
    else:
        Search_Error()
        display_data()

    ssis_db.commit()
    greetings1.destroy()

def delete_all():
    my_treeview()
    for data in TreeView.get_children():
        TreeView.delete(data)

def select_CrecordU():
    global CtreeView
    global courseCode_Centry, course_Centry
    
    #Clear Entry Boxes 
    courseCode_Centry.delete(0, END)
    course_Centry.delete(0, END)

    selected =  CtreeView.focus()
    values = CtreeView.item(selected, 'values')

    #Input New Data
    courseCode_Centry.insert(0, values[0])
    course_Centry.insert(0, values[1])

    #disable courscode entry
    courseCode_Centry['state'] = 'disabled'
    return

#selecting student record for update
def select_SrecordU():
    global TreeView
    global idnumber_entryU, name_entryU, gender_entryU, yearlvl_entryU, courseCode_entryU
    #update_student_window()
    
    #Clear Entry Boxes 
    idnumber_entryU.delete(0, END)
    name_entryU.delete(0, END)
    gender_entryU.delete(0, END)
    yearlvl_entryU.delete(0, END)
    courseCode_entryU.delete(0, END)

    selected =  TreeView.focus()
    values = TreeView.item(selected, 'values')

    #Input New Data
    idnumber_entryU.insert(0, values[0])
    name_entryU.insert(0, values[1])
    gender_entryU.insert(0, values[2])
    yearlvl_entryU.insert(0, values[3])
    courseCode_entryU.insert(0, values[4])

    #disable courscode entry
    idnumber_entryU['state'] = 'disabled'
    return
    return

#***************************************************MESSAGEBOXES***************************************************#
def Search_Error():
    messagebox.showerror("Search Error!", "Sorry, the student information cannot be found. \nCheck the information you provided or try again for another search.")

def Add_Success():
    messagebox.showinfo("Added Successfully!", "Student information was successfully added on the list!")

def Addcourse_Success():
    messagebox.showinfo("Added Successfully!", "Course information was successfully added on the list!")

def Add_Duplication():
    messagebox.showwarning("Add Duplication!", "Student was already on the list and cannot be added again to avoid duplication.")
    
def Update_Success():
    messagebox.showinfo("Updated Successfully!", "Student information was successfully updated!")

def CUpdate_Success():
    messagebox.showinfo("Updated Successfully!", "Course information was successfully updated!")

def Delete_Success():
    messagebox.showinfo("Deleted Successfully!", "Student information was successfully deleted on the list!")
    
def Exit():
    response = messagebox.askyesno("Exit?", "Do you really want to exit and close the program?")
    #Label(SSIS, text = response).place(x=900,y=500)
    if response == True:
        SSIS.destroy()
    else:
        None

#***************************************************POPOP WINDOWS***************************************************#
#Add Student Popop Window    
def add_student_window():
    global idnumber_entry, name_entry, gender_entry, yearlvl_entry, courseCode_entry
    global greetings1
    global add_studentW
    add_studentW = Toplevel(SSIS)
    add_studentW.title("Add Student")
    add_studentW.geometry("363x255+610+237")
    add_studentW.config(bg = "maroon")
   
    #labels
    id_number = Label(add_studentW, text = "ID Number:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    name = Label(add_studentW, text = "Full Name:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    gender = Label(add_studentW, text = "Gender:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    year_lvl = Label(add_studentW, text = "Year Level:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    course_code = Label(add_studentW, text = "Course Code:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )

    #entry
    idnumber_entry = Entry(add_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    name_entry = Entry(add_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    gender_entry = Entry(add_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    yearlvl_entry = Entry(add_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    courseCode_entry = Entry(add_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )

    #buttons
    ConfirmAdd = Button(add_studentW, text = "Confirm",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     command = add_student
                     )
    
    #positions
    id_number.place(x = 26, y = 25)
    name.place(x = 26, y = 53)
    gender.place(x = 26, y = 81)
    year_lvl.place(x = 26, y = 109)
    course_code.place(x = 26, y = 137)
    idnumber_entry.place(x = 177, y = 25)
    name_entry.place(x = 177, y = 53)
    gender_entry.place(x = 177, y = 81)
    yearlvl_entry.place(x = 177, y = 109)
    courseCode_entry.place(x = 177, y = 137)
    ConfirmAdd.place(x = 220, y = 200)

    greetings1.destroy()

#adding new course to db
def course_name_window():
    global courseCode_Centry, course_Centry
    global course_nameW
    course_nameW = Toplevel(SSIS)
    course_nameW.title("Add Course")
    course_nameW.geometry("363x255+610+273")
    course_nameW.config(bg = "maroon")
   
    #labels
    guide = Label(course_nameW, text = "If course is not yet registered in the database. \nPlease fill in the needed information \nto add course to the database",
                        font = ("Arial Rounded MT Bold", 10),
                        fg = "white",
                        bg = "black",
                        width = 40,
                        height = 4
                        )
    course_code = Label(course_nameW, text = "Course Code:",
                        font = ("Arial Rounded MT Bold", 13),
                        fg = "white",
                        bg = "black",
                        width = 13,
                        height = 1
                        )
    course = Label(course_nameW, text = "Course:",
                   font = ("Arial Rounded MT Bold", 13),
                   fg = "white",
                   bg = "black",
                   width = 13,
                   height = 1
                   )

    #entry
    courseCode_Centry = Entry(course_nameW,
                             bg = "ghost white",
                             fg = "black",
                             bd = 4,
                             width = 25,
                             font = ("Times New Roman", 10)
                             )

    course_Centry = Entry(course_nameW,
                         bg = "ghost white",
                         fg = "black",
                         bd = 4,
                         width = 25,
                         font = ("Times New Roman", 10)
                         )
   
    #buttons
    ConfirmAdd = Button(course_nameW, text = "Confirm",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        command = add_course
                        )
    
    #positions
    guide.place(x = 20, y = 40)
    course_code.place(x = 26, y = 137)
    course.place(x = 26, y = 165)
    courseCode_Centry.place(x = 177, y = 137)
    course_Centry.place(x = 177, y = 165)
    ConfirmAdd.place(x = 220, y = 200)
    
#to add course if course code not in db window
def course_code_window():
    global courseCode_Centry, course_Centry
    global course_nameW
    course_nameW = Toplevel(SSIS)
    course_nameW.title("Add Course")
    course_nameW.geometry("363x255+610+273")
    course_nameW.config(bg = "maroon")
   
    #labels
    guide = Label(course_nameW, text = "If course is not yet registered in the database. \nPlease fill in the needed information \nto add course to the database",
                        font = ("Arial Rounded MT Bold", 10),
                        fg = "white",
                        bg = "black",
                        width = 40,
                        height = 4
                        )
    course_code = Label(course_nameW, text = "Course Code:",
                        font = ("Arial Rounded MT Bold", 13),
                        fg = "white",
                        bg = "black",
                        width = 13,
                        height = 1
                        )
    course = Label(course_nameW, text = "Course:",
                   font = ("Arial Rounded MT Bold", 13),
                   fg = "white",
                   bg = "black",
                   width = 13,
                   height = 1
                   )

    #entry
    courseCode_Centry = Entry(course_nameW,
                             bg = "ghost white",
                             fg = "black",
                             bd = 4,
                             width = 25,
                             font = ("Times New Roman", 10)
                             )

    course_Centry = Entry(course_nameW,
                         bg = "ghost white",
                         fg = "black",
                         bd = 4,
                         width = 25,
                         font = ("Times New Roman", 10)
                         )
   
    #buttons
    ConfirmAdd = Button(course_nameW, text = "Confirm",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        command = add_Scourse
                        )
    
    #positions
    guide.place(x = 20, y = 40)
    course_code.place(x = 26, y = 137)
    course.place(x = 26, y = 165)
    courseCode_Centry.place(x = 177, y = 137)
    course_Centry.place(x = 177, y = 165)
    ConfirmAdd.place(x = 220, y = 200)

#Update Student Popop Window
def update_student_window():
    global idnumber_entryU, name_entryU, gender_entryU, yearlvl_entryU, courseCode_entryU
    global update_studentW
    update_studentW = Toplevel(SSIS)
    update_studentW.title("Update Student")
    update_studentW.geometry("363x255+813+237")
    update_studentW.config(bg = "maroon")
   
    #labels
    id_number = Label(update_studentW, text = "ID Number:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    name = Label(update_studentW, text = "Full Name:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    gender = Label(update_studentW, text = "Gender:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    year_lvl = Label(update_studentW, text = "Year Level:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )
    course_code = Label(update_studentW, text = "Course Code:",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 13,
                height = 1
                )

    #entry
    idnumber_entryU = Entry(update_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    name_entryU = Entry(update_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    gender_entryU = Entry(update_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    yearlvl_entryU = Entry(update_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )
    courseCode_entryU = Entry(update_studentW,
                           bg = "ghost white",
                           fg = "black",
                           bd = 4,
                           width = 25,
                           font = ("Times New Roman", 10)
                           )

    #buttons
    ConfirmUpdate = Button(update_studentW, text = "Confirm",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     command = update_student
                     )
    
    #positions
    id_number.place(x = 26, y = 25)
    name.place(x = 26, y = 53)
    gender.place(x = 26, y = 81)
    year_lvl.place(x = 26, y = 109)
    course_code.place(x = 26, y = 137)
    idnumber_entryU.place(x = 177, y = 25)
    name_entryU.place(x = 177, y = 53)
    gender_entryU.place(x = 177, y = 81)
    yearlvl_entryU.place(x = 177, y = 109)
    courseCode_entryU.place(x = 177, y = 137)
    ConfirmUpdate.place(x = 220, y = 200)

    select_SrecordU()

#Update Course Popop Window
def update_course_window():
    global courseCode_Centry, course_Centry
    global update_courseW
    update_courseW = Toplevel(SSIS)
    update_courseW.title("Update Course")
    update_courseW.geometry("363x255+813+273")
    update_courseW.config(bg = "maroon")

    course_code = Label(update_courseW, text = "Course Code:",
                        font = ("Arial Rounded MT Bold", 13),
                        fg = "white",
                        bg = "black",
                        width = 13,
                        height = 1
                        )
    course = Label(update_courseW, text = "Course:",
                   font = ("Arial Rounded MT Bold", 13),
                   fg = "white",
                   bg = "black",
                   width = 13,
                   height = 1
                   )

    #entry
    courseCode_Centry = Entry(update_courseW,
                             bg = "ghost white",
                             fg = "black",
                             bd = 4,
                             width = 25,
                             font = ("Times New Roman", 10)
                             )

    course_Centry = Entry(update_courseW,
                         bg = "ghost white",
                         fg = "black",
                         bd = 4,
                         width = 25,
                         font = ("Times New Roman", 10)
                         )
   
    #buttons
    ConfirmUpdate = Button(update_courseW, text = "Confirm",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     command = update_course
                     )
    
    #positions
    course_code.place(x = 26, y = 77)
    course.place(x = 26, y = 105)
    courseCode_Centry.place(x = 177, y = 77)
    course_Centry.place(x = 177, y = 105)
    ConfirmUpdate.place(x = 220, y = 180)

    select_CrecordU()
    
#***************************************************MAIN WINDOW***************************************************#
#Labels
yellow_bg = Label(SSIS, text = "",
               bg = "yellow3",
               width = 185,
               height = 2
               )
maroon_bg = Label(SSIS, text = "",
               bg = "maroon",
               width = 185,
               height = 4
               )
black_bg = Label(SSIS, text = "",
               bg = "black",
               width = 185,
               height = 3
               )
school = Label(SSIS, text = "Mindanao State University \n ILIGAN INSTITUTE OF TECHNOLOGY",
                font = ("Times New Roman", 15),
                fg = "white",
                bg = "maroon",
                width = 32,
                height = 2
                )
program = Label(SSIS, text = "Simple Student Information System (SSIS)",
                font = ("Arial Rounded MT Bold", 13),
                fg = "white",
                bg = "black",
                width = 32,
                height = 2
                )
greetings1 = Label(SSIS, text = "WELCOME!",
                font = ("Arial Rounded MT Bold", 90),
                fg = "yellow3",
                bg = "maroon",
                width = 12,
                height = 2
                )

#Buttons
Search = Button(SSIS, text = "Search",
                font = ("Arial Rounded MT Bold", 12),
                fg = "black",
                bg = "goldenrod",
                bd = 4,
                width = 19,
                height = 1,              
                command = search_student_data
                )
Display_List = Button(SSIS, text = "Display Students List",
                      font = ("Arial Rounded MT Bold", 12),
                      fg = "black",
                      bg = "goldenrod",
                      bd = 4,
                      width = 19,
                      height = 1,
                      command = display_data
                      )
Display_Course = Button(SSIS, text = "Display Course List",
                      font = ("Arial Rounded MT Bold", 12),
                      fg = "black",
                      bg = "goldenrod",
                      bd = 4,
                      width = 19,
                      height = 1,
                      command = display_course
                      )
Add_Student = Button(SSIS, text = "Add Student",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     width = 19,
                     height = 1,
                     command = add_student_window
                     )
Add_Course = Button(SSIS, text = "Add Course",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     width = 19,
                     height = 1,
                     command = course_name_window
                     )
Update_Student = Button(SSIS, text = "Update Student",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        width = 19,
                        height = 1,
                        command = update_student_window
                                )
Update_Course = Button(SSIS, text = "Update Course",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        width = 19,
                        height = 1,
                        command = update_course_window
                                )
Delete_Student = Button(SSIS, text = "Delete Student",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        width = 19,
                        height = 1,
                        command = delete_Sdata
                        )
Delete_Course = Button(SSIS, text = "Delete Course",
                        font = ("Arial Rounded MT Bold", 12),
                        fg = "black",
                        bg = "goldenrod",
                        bd = 4,
                        width = 19,
                        height = 1,
                        command = delete_Cdata
                        )
Exit = Button(SSIS, text = "EXIT",
                     font = ("Arial Rounded MT Bold", 12),
                     fg = "black",
                     bg = "goldenrod",
                     bd = 4,
                     width = 10,
                     command = Exit
                     )

#Entry
Search_Student_id = Entry(SSIS,
                          bg = "ghost white",
                          fg = "black",
                          bd = 4,
                          width = 25,
                          font = ("Times New Roman", 10)
                          )

#Positions
yellow_bg.grid(row = 0, column = 0)
maroon_bg.grid(row = 1, column = 0)
black_bg.grid(row = 2, column = 0)
school.grid(row = 1, column = 0)
program.grid(row = 2, column = 0)
greetings1.place(x = 250, y = 265)

Search_Student_id.place(x = 34, y = 178)
Search.place(x = 194, y = 170)
Display_List.place(x = 398, y = 170)
Display_Course.place(x = 398, y = 206)
Add_Student.place(x = 602, y = 170)
Add_Course.place(x = 602, y = 206)
Update_Student.place(x = 806, y = 170)
Update_Course.place(x = 806, y = 206)
Delete_Student.place(x = 1010, y = 170)
Delete_Course.place(x = 1010, y = 206)
Exit.place(x = 1100, y = 580)

student_info_db()
SSIS.mainloop()
