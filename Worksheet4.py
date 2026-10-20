
# ICT105 - WORKSHEET 4
# SESSIONS 7 AND 8
# Student: Sukhmanveer Singh
# Student ID: 12043370

import tkinter as tk
from tkinter import ttk
from datetime import datetime


# ========================================
# SESSION 7 - EXERCISE 1
# STUDENT REGISTRATION
# ========================================

print("\nSESSION 7 - EXERCISE 1")


def course_enrollment(student_id, first_name, last_name,
                      course_id, course_name, action="Echo"):

    print(f"\n{action}: Student Enrollment")
    print("Student ID:", student_id)
    print("Student Name:", first_name, last_name)
    print("Course ID:", course_id)
    print("Course Name:", course_name)


course_enrollment("12043370", "Sukhmanveer", "Singh",
                  "ICT105", "Introduction to Programming")

course_enrollment("12043370", "Sukhmanveer", "Singh",
                  "ICT105", "Introduction to Programming",
                  action="Add")

course_enrollment("12043370", "Sukhmanveer", "Singh",
                  "ICT105", "Introduction to Programming",
                  action="Amend")

course_enrollment("12043370", "Sukhmanveer", "Singh",
                  "ICT105", "Introduction to Programming",
                  action="Delete")


# ========================================
# SESSION 7 - EXERCISE 2
# STUDENT COURSE LIST
# ========================================

print("\nSESSION 7 - EXERCISE 2")


def collect_courses():
    courses = []

    for i in range(4):
        course_id = input(f"Enter Course ID {i + 1}: ")
        courses.append(course_id)

    return courses


def student_course_list(student_id, student_name):
    courses = collect_courses()

    semester = input("Enter Semester: ")
    year = input("Enter Year: ")

    print("\nStudent Enrollment Summary")
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Semester:", semester)
    print("Year:", year)
    print("Courses:", courses)

    return courses


def course_dictionary(**courses):
    return courses


student_id = "12043370"
student_name = "Sukhmanveer Singh"

enrolled_courses = student_course_list(
    student_id, student_name
)

course_details = {}

for course_id in enrolled_courses:
    course_name = input(f"Enter Course Name for {course_id}: ")
    course_details[course_id] = course_name

print("\nCourse Dictionary:")
print(course_details)

sample_courses = course_dictionary(
    ICT105="Introduction to Programming",
    ICT101="Computer Fundamentals",
    ICT102="Networking Basics",
    ICT103="Database Basics"
)

print("\nExample using keyword arguments:")
print(sample_courses)


# ========================================
# SESSION 7 - EXERCISE 3
# TKINTER CALCULATOR
# ========================================

print("\nSESSION 7 - EXERCISE 3")


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero")
                return

            result = num1 / num2

        result_label.config(text=f"Result: {result:g}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")


def open_calculator():
    root = tk.Tk()
    root.title("ICT105 Calculator")
    root.geometry("350x260")

    global entry1, entry2, result_label

    ttk.Label(root, text="First Number").pack(pady=5)
    entry1 = ttk.Entry(root)
    entry1.pack()

    ttk.Label(root, text="Second Number").pack(pady=5)
    entry2 = ttk.Entry(root)
    entry2.pack()

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=15)

    for i, operator in enumerate(["+", "-", "*", "/"]):
        ttk.Button(
            button_frame,
            text=operator,
            command=lambda op=operator: calculate(op)
        ).grid(row=0, column=i, padx=5)

    result_label = ttk.Label(root, text="Result:")
    result_label.pack(pady=10)

    root.mainloop()


# ========================================
# SESSION 8 - EXERCISE 1
# USER PROFILE CLASS
# ========================================

print("\nSESSION 8 - EXERCISE 1")


class User:

    def __init__(self, first_name, last_name, email,
                 username, date_of_birth, location):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser Details:")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Username:", self.username)
        print("Date of Birth:", self.date_of_birth)
        print("Location:", self.location)

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User(
    "Sukhmanveer", "Singh",
    "sukhmanveer@example.com",
    "sukhman", "2002-01-01", "Perth"
)

user2 = User(
    "Alex", "Lee",
    "alex@example.com",
    "alexlee", "2001-05-15", "Sydney"
)

user3 = User(
    "Sam", "Patel",
    "sam@example.com",
    "samp", "2003-09-20", "Melbourne"
)

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()


# ========================================
# SESSION 8 - EXERCISE 2
# LOGIN ATTEMPTS
# ========================================

print("\nSESSION 8 - EXERCISE 2")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login Attempts:", user1.login_attempts)

user1.reset_login_attempts()

print("After Reset:", user1.login_attempts)


# ========================================
# SESSION 8 - EXERCISE 3
# CLASSROOM CLASS
# ========================================

print("\nSESSION 8 - EXERCISE 3")


class Classroom:

    def __init__(self, classroom_name,
                 classroom_location, seats_in_class):

        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0
        self.audit_log = []

    def describe_classroom(self):
        print("\nClassroom:", self.classroom_name)
        print("Location:", self.classroom_location)
        print("Seats:", self.seats_in_class)

    def checksize_classroom(self, enrolled_students):
        if enrolled_students <= self.seats_in_class:
            print("Enough seats available")
        else:
            print("Not enough seats available")

    def record_change(self, old, new, reason):
        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.audit_log.append(
            f"{timestamp} - {reason}: {old} to {new}"
        )

    def set_number_enrolled(self, number):
        if number < 0 or number > self.seats_in_class:
            print("Invalid enrollment number")
            return

        old = self.students_enrolled
        self.students_enrolled = number

        self.record_change(old, number, "Set Enrollment")

    def update_number_enrolled(self, change):
        new_number = self.students_enrolled + change

        if new_number < 0 or new_number > self.seats_in_class:
            print("Invalid enrollment update")
            return

        old = self.students_enrolled
        self.students_enrolled = new_number

        self.record_change(old, new_number, "Update Enrollment")

    def show_audit_log(self):
        print("\nAudit Log:")

        for entry in self.audit_log:
            print(entry)


room1 = Classroom("Lab A", "Building 1", 30)
room2 = Classroom("Lab B", "Building 2", 20)
room3 = Classroom("Lab C", "Building 3", 40)

for room in [room1, room2, room3]:
    room.describe_classroom()

room1.checksize_classroom(25)


# ========================================
# SESSION 8 - EXERCISE 4
# CLASSROOM ENROLLMENT AND AUDIT LOG
# ========================================

print("\nSESSION 8 - EXERCISE 4")

print("Default Enrollment:", room1.students_enrolled)

old = room1.students_enrolled
room1.students_enrolled = 10
room1.record_change(old, 10, "Direct Change")

print("After Direct Change:", room1.students_enrolled)

room1.set_number_enrolled(15)
print("After Set:", room1.students_enrolled)

room1.update_number_enrolled(5)
print("After Update:", room1.students_enrolled)

room1.show_audit_log()


# ========================================
# SESSION 8 - EXERCISE 5
# CLASSROOM EQUIPMENT AND INHERITANCE
# ========================================

print("\nSESSION 8 - EXERCISE 5")


class Equipment(Classroom):

    def __init__(self, classroom_name,
                 classroom_location, seats_in_class, devices):

        super().__init__(
            classroom_name,
            classroom_location,
            seats_in_class
        )

        self.devices = devices

    def display_devices(self):
        print("\nEquipment Available:")

        for device in self.devices:
            print("-", device)


lab1 = Equipment(
    "Lab A",
    "Building 1",
    30,
    ["Computers", "Projector", "Printer", "Speakers"]
)

lab1.describe_classroom()
lab1.display_devices()


# ========================================
# OPEN CALCULATOR AT THE END
# ========================================

print("\nAll console exercises completed.")
print("Opening Tkinter Calculator...")

open_calculator()
