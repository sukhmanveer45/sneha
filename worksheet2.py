# ============================================
# ICT105 - Lists, Loops & Tuples
# ============================================


# --------------------------------------------
# PART 1: LISTS
# --------------------------------------------

courses = [
    "Physics I",
    "Calculus II",
    "Biology I",
    "Introduction to Programming",
    "History I",
    "Chemistry I",
    "Microeconomics",
    "Linear Algebra",
    "Psychology I",
    "Data Structures and Algorithms"
]

# Print the original list
print("Original list:")
print(courses)


# Alphabetical order using sorted()
print("\nAlphabetical order:")
print(sorted(courses))


# Reverse alphabetical order using sorted()
print("\nReverse alphabetical order:")
print(sorted(courses, reverse=True))


# --------------------------------------------
# PART 2: reverse()
# --------------------------------------------

courses.reverse()

print("\nList after reverse():")
print(courses)


# --------------------------------------------
# PART 3: sort()
# --------------------------------------------

courses.sort()

print("\nList after sort():")
print(courses)


# Reverse alphabetical order using sort()
courses.sort(reverse=True)

print("\nList after sort(reverse=True):")
print(courses)


# --------------------------------------------
# PART 4: insert() and append()
# --------------------------------------------

# Add a course at the beginning
courses.insert(0, "Introduction to Philosophy")

# Add a course in the middle
courses.insert(5, "English Composition I")

# Add a course at the end
courses.append("Discrete Mathematics")

print("\nList after adding courses:")
print(courses)


# --------------------------------------------
# PART 5: pop()
# --------------------------------------------

removed1 = courses.pop()
removed2 = courses.pop()
removed3 = courses.pop()
removed4 = courses.pop()

print("\nWithdrawn courses:")
print(removed1)
print(removed2)
print(removed3)
print(removed4)

print("\nAvailable courses:")
print(courses)


# --------------------------------------------
# PART 6: TUPLES AND LOOPS
# --------------------------------------------

course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I")
]

# Empty list
course_names = []

# Loop through the tuples
for course_id, course_name in course_tuples:
    course_names.append(course_name)

print("\nCourse names from tuples:")
print(course_names)


# --------------------------------------------
# PART 7: COURSE DEPARTMENT SEARCH
# --------------------------------------------

departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

while True:

    user_input = input(
        "\nEnter Course ID (1-15), 0 to exit, or quit: "
    )

    # Exit using quit
    if user_input.lower() == "quit":
        print("Program ended.")
        break

    # Exit using 0
    elif user_input == "0":
        print("Program ended.")
        break

    # Check if input is a number
    elif user_input.isdigit():

        course_id = int(user_input)

        # Check range
        if 1 <= course_id <= 15:

            found = False

            # Search through departments
            for course in departments:

                if course[0] == course_id:

                    print(
                        "Course ID",
                        course[0],
                        "is in the",
                        course[1],
                        "department."
                    )

                    found = True
                    break

            if found == False:
                print("Course ID was not found.")

        else:
            print(
                "Invalid input. Please enter a number "
                "from 1 to 15, 0, or quit."
            )

    else:
        print(
            "Invalid input. Please enter a number "
            "from 1 to 15, 0, or quit."
        )


# --------------------------------------------
# PART 8: COURSE INFORMATION RETRIEVAL SYSTEM
# --------------------------------------------

course_information = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Calculus II", "Mathematics", "Calculus I"],
    [4, "Physics I", "Physics", "None"],
    [5, "Data Structures and Algorithms",
     "Computer Science", "Introduction to Programming"]
]

while True:

    user_input = input(
        "\nEnter Course ID (0 to exit or quit): "
    )

    # Exit the program
    if user_input.lower() == "quit" or user_input == "0":
        print("Program ended.")
        break

    # Check if input is a number
    elif user_input.isdigit():

        course_id = int(user_input)

        found = False

        # Search through course information
        for course in course_information:

            if course[0] == course_id:

                print("\nCourse Information")
                print("-------------------")
                print("Course ID:", course[0])
                print("Course Name:", course[1])
                print("Department:", course[2])
                print("Prerequisites:", course[3])

                found = True
                break

        # If course doesn't exist
        if found == False:
            print("Course ID was not found.")

    else:
        print(
            "Invalid input. Please enter a Course ID, "
            "0, or quit."
        )