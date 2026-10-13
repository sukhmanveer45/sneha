
# ICT105 - WORKSHEET 3
# SESSION 5 AND SESSION 6
# Complete Python Lab Exercises


# ==========================================
# SESSION 5 - WORKING WITH DICTIONARIES
# ==========================================

print("\nSESSION 5 - WORKING WITH DICTIONARIES")


# QUESTION 1 - STUDENT COURSE ENROLLMENT

print("\nQUESTION 1 - STUDENT COURSE ENROLLMENT")

# Store student IDs and enrolled courses
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
    1006: ["BIO102", "ENGL101"],
    1007: ["ECON101", "PSY101"],
    1008: ["ECON102", "SOC101"],
    1009: ["PSY102", "SOC102"],
    1010: ["CS101", "MATH101"]
}

# Display each student's courses
for student_id, courses in course_enrollments.items():
    print("Student ID:", student_id)
    print("Enrolled Courses:", ", ".join(courses))
    print()


# QUESTION 2 - CLASS SCHEDULE

print("\nQUESTION 2 - CLASS SCHEDULE")

# Store departments and course information
departments = {
    "Computer Science": [
        ("Computer Science", "CS101", "Introduction to Computer Science"),
        ("Computer Science", "CS202", "Data Structures and Algorithms")
    ],
    "Mathematics": [
        ("Mathematics", "MATH101", "Calculus I"),
        ("Mathematics", "MATH102", "Calculus II")
    ],
    "Physics": [
        ("Physics", "PHY101", "General Physics I"),
        ("Physics", "PHY102", "General Physics II")
    ],
    "Chemistry": [
        ("Chemistry", "CHEM101", "General Chemistry I"),
        ("Chemistry", "CHEM102", "General Chemistry II")
    ],
    "Biology": [
        ("Biology", "BIO101", "Biology I"),
        ("Biology", "BIO102", "Biology II")
    ],
    "History": [
        ("History", "HIST101", "American History I"),
        ("History", "HIST102", "American History II")
    ],
    "English": [
        ("English", "ENGL101", "English Composition I"),
        ("English", "ENGL102", "English Composition II")
    ],
    "Economics": [
        ("Economics", "ECON101", "Principles of Economics"),
        ("Economics", "ECON102", "Intermediate Microeconomics")
    ],
    "Psychology": [
        ("Psychology", "PSY101", "Introduction to Psychology"),
        ("Psychology", "PSY102", "Developmental Psychology")
    ],
    "Sociology": [
        ("Sociology", "SOC101", "Introduction to Sociology"),
        ("Sociology", "SOC102", "Social Problems")
    ]
}

# Display courses by department
for department, courses in departments.items():
    print("\nDepartment:", department)

    for course in courses:
        print("Course ID:", course[1])
        print("Course Name:", course[2])


# QUESTION 3 - LECTURER ASSIGNMENTS

print("\nQUESTION 3 - LECTURER ASSIGNMENTS")

# Store lecturers and their courses
lecturer_assignments = {
    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
    "Prof. David Lee": ["PHY101"],
    "Miss. Sophia Carter": ["CHEM102", "BIO101", "BIO102"],
    "Dr. Oliver Hernandez": ["HIST101", "HIST102", "ENGL101"],
    "Prof. Isabella Garcia": ["ENGL102", "SOC101"],
    "Prof. Evelyn Russell": ["ECON101", "ECON102"],
    "Dr. Lucas Sanchez": ["PSY101", "PSY102"],
    "Asst. Prof. Liam Lopez": ["SOC102"]
}

# Display lecturers and assigned courses
for lecturer, courses in lecturer_assignments.items():
    print("Lecturer:", lecturer)
    print("Assigned Courses:", ", ".join(courses))
    print()


# ==========================================
# SESSION 6 - USER INPUTS AND WHILE LOOPS
# ==========================================

print("\nSESSION 6 - USER INPUTS AND WHILE LOOPS")


# QUESTION 1 - USER INPUT LOOP

print("\nQUESTION 1 - USER INPUT LOOP")

students = []

# Ask for student names
while True:
    name = input("Enter student name (or quit): ")

    if name.lower() == "quit":
        break

    students.append(name)
    print(name, "has been added to the class.")

# Display the class list
print("\nClass List:")

for student in students:
    print(student)

print("Total Students:", len(students))


# QUESTION 2 - FIND SUITABLE ROOMS

print("\nQUESTION 2 - FIND SUITABLE ROOMS")

# Store room information from worksheet
rooms = [
    (101, 15, "Ground Floor", "Building A"),
    (102, 15, "Ground Floor", "Building A"),
    (103, 20, "Ground Floor", "Building A"),
    (104, 20, "Ground Floor", "Building A"),
    (105, 25, "Ground Floor", "Building A"),
    (106, 25, "Ground Floor", "Building A"),
    (107, 30, "Ground Floor", "Building A"),
    (108, 30, "Ground Floor", "Building A"),
    (109, 30, "Ground Floor", "Building A"),
    (110, 10, "Ground Floor", "Building A"),
    (201, 10, "1st Floor", "Building A"),
    (202, 10, "1st Floor", "Building A"),
    (203, 25, "1st Floor", "Building A"),
    (204, 25, "1st Floor", "Building A"),
    (205, 30, "1st Floor", "Building A"),
    (206, 40, "1st Floor", "Building A"),
    (207, 40, "1st Floor", "Building A"),
    (208, 40, "1st Floor", "Building A")
]

# Ask for the required number of seats
required = int(input("Enter number of students: "))

if required <= 0:
    print("Please enter a positive number.")
else:
    suitable_rooms = []

    # Find rooms big enough for the class
    for room in rooms:
        if room[1] >= required:
            suitable_rooms.append(room)

    selected = []

    if suitable_rooms:
        # Choose the smallest suitable room
        smallest_room = min(
            suitable_rooms,
            key=lambda room: room[1]
        )
        selected.append(smallest_room)

    else:
        # Choose the largest rooms first
        sorted_rooms = sorted(
            rooms,
            key=lambda room: room[1],
            reverse=True
        )

        total_capacity = 0

        for room in sorted_rooms:
            selected.append(room)
            total_capacity += room[1]

            if total_capacity >= required:
                break

    total_capacity = sum(room[1] for room in selected)

    if total_capacity < required:
        print("Not enough room capacity available.")
    else:
        print("Minimum Rooms Needed:", len(selected))
        print("Total Capacity:", total_capacity)

        for room in selected:
            print("Room Number:", room[0])
            print("Capacity:", room[1])
            print("Floor:", room[2])
            print("Location:", room[3])
            print()


# QUESTION 3A - EXIT WITH QUIT, EXIT OR 0

print("\nQUESTION 3A - EXIT COMMANDS")

students = []

while True:
    name = input("Enter student name (quit/exit/0 to stop): ")

    if name.lower() in ["quit", "exit", "0"]:
        exit_parameter = name
        break

    students.append(name)
    print(name, "added successfully.")

print("\nStudent List:")

for student in students:
    print(student)

print("Total Students:", len(students))
print("Exit Parameter:", exit_parameter)


# QUESTION 3B - ACTIVE VARIABLE

print("\nQUESTION 3B - ACTIVE VARIABLE")

students = []
active = True

while active:
    name = input("Enter student name (or quit): ")

    if name.lower() == "quit":
        active = False
    else:
        students.append(name)
        print(name, "added successfully.")

print("\nStudent List:")

for student in students:
    print(student)

print("Total Students:", len(students))


# QUESTION 3C - MAXIMUM ROOM CAPACITY

print("\nQUESTION 3C - MAXIMUM ROOM CAPACITY")

# Room 101 has 15 seats
max_cap = 15
students = []

while True:
    name = input("Enter student name: ")

    students.append(name)
    print(name, "has been added.")

    if len(students) >= max_cap:
        print("Room capacity reached.")
        break

print("\nStudent List:")

for student in students:
    print(student)

print("Total Students:", len(students))
print("Maximum Capacity:", max_cap)


# QUESTION 4 - INFINITE LOOP

print("\nQUESTION 4 - INFINITE LOOP")
print("Press CTRL+C to stop entering text.")

total_lines = 0
lines = []

try:
    while True:
        text = input("Enter text: ")

        lines.append(text)
        total_lines += 1

        print("You entered:", text)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

# Display all entered lines
print("\nAll Entered Lines:")

for line in lines:
    print(line)

print("Total Number of Lines:", total_lines)

print("\nICT105 WORKSHEET 3 COMPLETED")
