
# ============================================================
# ICT105 - WORKSHEET 5
# SESSION 9 AND SESSION 10
# COMPLETE PYTHON PROGRAM
# ============================================================

import csv
import json
import logging
from pathlib import Path

BASE = Path(__file__).resolve().parent


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ============================================================
# SESSION 9 - EXERCISE 1
# File handling, reading a file and error handling using OOP
# ============================================================

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_all(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")

    def read_lines(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            for line in lines:
                print(line.strip())

        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: Permission denied.")


def s9_ex1():
    filename = BASE / "learning_python.txt"

    content = (
        "I have learned Python basics.\n"
        "Python uses variables and loops.\n"
        "Functions help organise programs.\n"
        "Error handling prevents programs from crashing.\n"
    )

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        reader = FileReader(filename)

        print("\nReading entire file:")
        reader.read_all()

        print("\nReading line by line:")
        reader.read_lines()

    except OSError as error:
        print("File error:", error)


# ============================================================
# SESSION 9 - EXERCISE 2
# Replace learner with student in a text file
# ============================================================

def s9_ex2():
    filename = BASE / "learning_students.txt"

    content = (
        "Every learner must complete their assignments on time.\n"
        "A good learner always seeks to learn more.\n"
        "Learners are the future leaders.\n"
    )

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                modified_line = line.replace("learner", "student")
                modified_line = modified_line.replace("Learners", "Students")
                print(modified_line.strip())

    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as error:
        print("File error:", error)


# ============================================================
# SESSION 9 - EXERCISE 3
# Add two numbers and handle ValueError
# ============================================================

def s9_ex3():
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        total = number1 + number2

        print("The sum is:", total)

    except ValueError:
        print("Error: Please enter numbers only.")


# ============================================================
# SESSION 9 - EXERCISE 4
# Repeatable calculator with error handling
# ============================================================

def s9_ex4():
    while True:
        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2

            elif choice == "2":
                result = num1 - num2

            elif choice == "3":
                result = num1 * num2

            elif choice == "4":
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2

            print("Result:", result)

        except ValueError:
            print("Error: Enter numeric values only.")


# ============================================================
# SESSION 9 - EXERCISE 5
# CSV file handling, splitting files and error logging
# ============================================================

def create_students_csv():
    filename = BASE / "students.csv"

    students = [
        ["StudentID", "FirstName", "LastName", "Email"],
        ["1001", "Alice", "Smith", "alice@example.com"],
        ["1002", "Bob", "Johnson", "bob@example.com"],
        ["1003", "Charlie", "Brown", "charlie@example.com"],
        ["1004", "David", "Lee", "david@example.com"],
        ["1005", "Emily", "Davis", "emily@example.com"],
        ["1006", "Frank", "Wilson", "frank@example.com"]
    ]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("students.csv created successfully.")


def split_students_csv():
    source = BASE / "students.csv"

    with open(source, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0]
    students = rows[1:]

    midpoint = (len(students) + 1) // 2

    file1 = BASE / "students_c1.txt"
    file2 = BASE / "students_c2.txt"

    with open(file1, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students[:midpoint])

    with open(file2, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(students[midpoint:])

    print("Student data split into two files.")


def read_student_parts(silent=False):
    files = [
        BASE / "students_c1.txt",
        BASE / "students_c2.txt"
    ]

    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            print("\nContents of", filename.name)
            print(content)

        except FileNotFoundError:
            if silent:
                logging.basicConfig(
                    filename=str(BASE / "error.log"),
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    force=True
                )
                logging.error("File not found: %s", filename.name)
            else:
                print("Error: File not found:", filename.name)


def s9_ex5():
    try:
        create_students_csv()
        split_students_csv()
        read_student_parts()

        print("\nTo test missing file handling:")
        print("Move students_c1.txt to another folder.")
        print("Then select menu option 14 or 15.")

    except (FileNotFoundError, PermissionError, OSError) as error:
        print("File error:", error)


# ============================================================
# SESSION 9 - EXERCISE 6
# Store favourite number using JSON.dumps()
# ============================================================

def s9_ex6():
    filename = BASE / "favourite_number.json"

    try:
        number = int(input("Enter your favourite number: "))

        with open(filename, "w", encoding="utf-8") as file:
            file.write(json.dumps(number))

        print("Favourite number saved.")

        with open(filename, "r", encoding="utf-8") as file:
            saved_number = json.loads(file.read())

        print(f"I know your favourite number! It is {saved_number}.")

    except ValueError:
        print("Please enter a valid whole number.")
    except OSError as error:
        print("File error:", error)


# ============================================================
# SESSION 9 - EXERCISE 7
# Remember favourite number between runs
# ============================================================

def s9_ex7():
    filename = BASE / "remember_number.json"

    try:
        if filename.exists():
            with open(filename, "r", encoding="utf-8") as file:
                number = json.load(file)

            print(f"Your favourite number is {number}!")

        else:
            number = int(input("Enter your favourite number: "))

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(number, file)

            print("Your favourite number has been saved.")

    except ValueError:
        print("Please enter a valid number.")
    except (OSError, json.JSONDecodeError) as error:
        print("Error:", error)


# ============================================================
# SESSION 9 - EXERCISE 8
# User profile, dictionaries and JSON
# ============================================================

def s9_ex8():
    filename = BASE / "user_profile.txt"

    profiles = {}

    try:
        count = int(input("How many students? "))

        if count <= 0:
            print("Please enter a positive number.")
            return

        # Part A: Collect student IDs
        for i in range(count):
            student_id = input(f"Enter student ID {i + 1}: ").strip()

            if student_id in profiles:
                print("This student ID already exists.")
                continue

            profiles[student_id] = {}

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(profiles, file, indent=4)

        print("Student IDs saved.")

        # Part B: Load JSON data into a dictionary
        with open(filename, "r", encoding="utf-8") as file:
            profiles = json.load(file)

        # Part C: Add DOB and email
        for student_id in profiles:
            print("\nStudent ID:", student_id)

            dob = input("Enter date of birth: ")
            email = input("Enter email address: ")

            profiles[student_id]["DOB"] = dob
            profiles[student_id]["Email"] = email

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(profiles, file, indent=4)

        # Part D: Summary report
        with open(filename, "r", encoding="utf-8") as file:
            saved_profiles = json.load(file)

        print("\nSTUDENT PROFILE SUMMARY")

        for student_id, details in saved_profiles.items():
            print("\nStudent ID:", student_id)
            print("DOB:", details.get("DOB"))
            print("Email:", details.get("Email"))

    except ValueError:
        print("Please enter a valid number.")
    except (OSError, json.JSONDecodeError) as error:
        print("Error:", error)


# ============================================================
# SESSION 9 - EXERCISE 9
# Remember username and verify previous user
# ============================================================

def s9_ex9():
    filename = BASE / "remember_me.json"

    previous_name = None

    try:
        if filename.exists():
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            previous_name = data.get("username")

        if previous_name:
            print("Previous username:", previous_name)

            answer = input("Are you this user? (yes/no): ").lower().strip()

            if answer == "yes":
                username = previous_name
            else:
                username = input("Enter new username: ").strip()

                if username == previous_name:
                    print("Duplicate username is not allowed.")
                    return

        else:
            username = input("Enter your username: ").strip()

        if not username:
            print("Username cannot be empty.")
            return

        data = {"username": username}

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Username '{username}' saved or updated successfully.")

    except (OSError, json.JSONDecodeError) as error:
        print("Error:", error)


# ============================================================
# SESSION 10 - EXERCISE 1
# Understanding APIs and making GitHub API requests
#
# API = Application Programming Interface
#
# GitHub API URL:
# https://api.github.com/search/repositories?q=language:python+sort:stars
#
# https = secure web protocol
# api.github.com = GitHub API server
# search/repositories = repository search endpoint
# q = search query parameter
# language:python = search Python repositories
# sort:stars = request sorting by stars
#
# Install requests:
# python -m pip install requests
# ============================================================

def fetch_github():
    try:
        import requests

    except ImportError:
        print("Requests library not installed.")
        print("Run: python -m pip install requests")
        return None

    url = "https://api.github.com/search/repositories"

    params = {
        "q": "language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        print("HTTP Status Code:", response.status_code)

        remaining = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")

        print("Rate Limit Remaining:", remaining)
        print("Rate Limit Reset:", reset)

        response.raise_for_status()

        data = response.json()

        return data

    except (requests.RequestException, ValueError) as error:
        print("Could not get API data:", error)
        return None


def s10_ex1():
    data = fetch_github()

    if data is not None:
        print("\nTop five Python GitHub repositories by stars:")

        repositories = data.get("items", [])[:5]

        for index, repo in enumerate(repositories, start=1):
            print(f"{index}. {repo['full_name']}")


# ============================================================
# SESSION 10 - EXERCISE 2
# Managing virtual environments
# ============================================================

def s10_ex2():
    print("\nCreate a virtual environment:")
    print("python -m venv .venv")

    print("\nActivate on Windows PowerShell:")
    print(r".\.venv\Scripts\Activate.ps1")

    print("\nActivate on macOS/Linux:")
    print("source .venv/bin/activate")

    print("\nExport installed packages:")
    print("python -m pip freeze > requirements.txt")

    print("\nInstall packages from requirements.txt:")
    print("python -m pip install -r requirements.txt")


# ============================================================
# SESSION 10 - EXERCISE 3
# API responses, dictionaries and HTTP status checking
# ============================================================

def s10_ex3():
    data = fetch_github()

    if data is not None:
        total_count = data.get("total_count", 0)

        print("\nTotal Python repositories found:", total_count)

        print("\nResponse converted into a Python dictionary.")
        print("Data type:", type(data))


# ============================================================
# SESSION 10 - EXERCISE 4
# Plotly bar chart and GitHub API rate limits
#
# remaining = API calls left in the current time window
# reset = Unix timestamp when the limit resets
#
# If rate limited:
# Wait until the reset time.
# Reduce requests or use GitHub authentication.
# ============================================================

def s10_ex4():
    data = fetch_github()

    if data is None:
        return

    try:
        import plotly.express as px

    except ImportError:
        print("Plotly is not installed.")
        print("Run: python -m pip install plotly")
        return

    items = data.get("items", [])

    if not items:
        print("No repository data available.")
        return

    repo_names = [
        item["full_name"] for item in items
    ]

    stars = [
        item["stargazers_count"] for item in items
    ]

    fig = px.bar(
        x=repo_names,
        y=stars,
        title="Top Python GitHub Repositories",
        labels={
            "x": "Repository Names",
            "y": "Number of Stars"
        }
    )

    fig.update_layout(
        xaxis_tickangle=-25
    )

    output = BASE / "github_stars.html"

    fig.write_html(str(output))

    print("Bar chart saved successfully.")
    print("File location:", output)
    print("Open the HTML file in your browser.")


# ============================================================
# MAIN MENU
# Run all exercises from one Python file
# ============================================================

EXERCISES = {
    "1": ("Session 9 - Exercise 1: File Reading", s9_ex1),
    "2": ("Session 9 - Exercise 2: Replace Words", s9_ex2),
    "3": ("Session 9 - Exercise 3: ValueError", s9_ex3),
    "4": ("Session 9 - Exercise 4: Calculator", s9_ex4),
    "5": ("Session 9 - Exercise 5: CSV File Handling", s9_ex5),
    "6": ("Session 9 - Exercise 6: Favourite Number", s9_ex6),
    "7": ("Session 9 - Exercise 7: Remember Number", s9_ex7),
    "8": ("Session 9 - Exercise 8: Student Profile", s9_ex8),
    "9": ("Session 9 - Exercise 9: Remember Username", s9_ex9),
    "10": ("Session 10 - Exercise 1: GitHub API", s10_ex1),
    "11": ("Session 10 - Exercise 2: Virtual Environment", s10_ex2),
    "12": ("Session 10 - Exercise 3: API Dictionary", s10_ex3),
    "13": ("Session 10 - Exercise 4: Plotly Bar Chart", s10_ex4),
    "14": ("Session 9 - Exercise 5: Test Missing Files",
           lambda: read_student_parts(silent=False)),
    "15": ("Session 9 - Exercise 5: Silent Error Logging",
           lambda: read_student_parts(silent=True))
}


def main():
    while True:
        heading("ICT105 WORKSHEET 5 - SESSIONS 9 & 10")

        for key, (description, function) in EXERCISES.items():
            print(f"{key}. {description}")

        print("0. Exit")

        selection = input("\nChoose an exercise (0-15): ").strip()

        if selection == "0":
            print("Goodbye!")
            break

        elif selection in EXERCISES:
            description, function = EXERCISES[selection]

            heading(description)

            try:
                function()

            except (KeyboardInterrupt, EOFError):
                print("\nExercise cancelled.")

            except OSError as error:
                print("File or system error:", error)

        else:
            print("Invalid choice. Enter a number from 0 to 15.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
