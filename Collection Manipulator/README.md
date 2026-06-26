# 🎓 Student Data Organizer

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-CRUD%20Application-orange?style=for-the-badge)

</p>

A **menu-driven Python application** that demonstrates how to manage student records using Python's built-in collection data types. This project performs complete **CRUD (Create, Read, Update, Delete)** operations while showcasing the practical use of **Lists, Dictionaries, Sets, Loops, Conditional Statements, and User Input Handling**.

Designed specifically for beginners who want to strengthen their understanding of Python collections and data manipulation.

---

# 📖 Table of Contents

- Project Overview
- Features
- Screenshots
- Project Structure
- Technologies Used
- Data Structure
- Workflow
- Installation
- Usage
- Sample Output
- Python Concepts Covered
- Future Enhancements
- Learning Outcomes
- Author
- License

---

# 🚀 Project Overview

Managing student information is one of the most common beginner-level programming exercises.

This project allows users to:

- Add new students
- View all student records
- Update existing records
- Delete student records
- Display all unique subjects

The project stores student information using **Python Lists of Dictionaries**, making it a great example of working with structured data without using databases.

---

# ✨ Features

### ✅ Add Student

- Add new student records
- Prevent duplicate Student IDs
- Store multiple student details

---

### 📋 Display Students

View all available student records in a clean format.

---

### ✏️ Update Student

Modify student information using Student ID.

---

### ❌ Delete Student

Delete existing student records safely.

---

### 📚 Display Subjects

Displays all unique subjects offered by students using Python Sets.

---

### 🚪 Exit Program

Gracefully exits the application.

---

# 📂 Project Structure

```
Student-Data-Organizer/
│
├── Collection Manipulator.py
├── README.md
└── LICENSE
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 3 | Programming Language |
| List | Store Student Records |
| Dictionary | Store Individual Student Data |
| Set | Remove Duplicate Subjects |
| Loops | Iterate Records |
| Conditional Statements | Menu Navigation |
| String Methods | Process Subjects |

---

# 📊 Data Structure

Each student record is stored as a Python Dictionary.

```python
{
    "id":101,
    "name":"Rahul",
    "age":18,
    "grade":"A",
    "dob":"12-05-2007",
    "subjects":"Python,SQL,Excel"
}
```

All dictionaries are stored inside a Python List.

```python
students = [
    {...},
    {...},
    {...}
]
```

---

# 🔄 Project Workflow

```text
                Start
                  │
                  ▼
        Display Main Menu
                  │
                  ▼
        User Selects Option
                  │
 ┌─────────────────────────────────┐
 │                                 │
 ▼                                 ▼
Add Student                  Display Students
 │                                 │
 ▼                                 ▼
Update Student              Delete Student
 │                                 │
 ▼                                 ▼
Display Subjects             Exit Program
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Student-Data-Organizer.git
```

---

## Navigate

```bash
cd Student-Data-Organizer
```

---

## Run

```bash
python "Collection Manipulator.py"
```

---

# 💻 Usage

After running the program, the following menu appears:

```text
Welcome to the Student Data Organizer!

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

Simply enter the corresponding number to perform the desired operation.

---

# 📸 Sample Output

### Add Student

```text
Enter Student ID : 101
Enter Student Name : Rahul
Enter Student Age : 18
Enter Student Grade : A
Enter Student DOB : 12-05-2007
Subjects : Python, SQL, Excel

Student Added Successfully!
```

---

### Display Students

```text
Student ID : 101
Name : Rahul
Age : 18
Grade : A
Subjects : Python, SQL, Excel
```

---

### Display Subjects

```text
{
'Python',
'SQL',
'Excel'
}
```

---

# 📚 Python Concepts Demonstrated

✔ Lists

✔ Dictionaries

✔ Sets

✔ CRUD Operations

✔ User Input

✔ Loops

✔ Conditional Statements

✔ String Manipulation

✔ Data Validation

✔ Menu Driven Programming

---

# 📈 Time Complexity

| Operation | Complexity |
|------------|-----------|
| Add Student | O(n) |
| Display Students | O(n) |
| Update Student | O(n) |
| Delete Student | O(n) |
| Display Subjects | O(n × m) |

*n = Number of Students*

*m = Number of Subjects*

---

# 🎯 Learning Outcomes

This project helps understand:

- Real-world CRUD implementation
- Python collection framework
- Menu-driven applications
- Data organization techniques
- Duplicate checking
- Searching algorithms
- Record manipulation
- Set operations
- Beginner-level software design

---

# 🚀 Future Enhancements

- ✅ File Handling (CSV)
- ✅ SQLite Database
- ✅ MySQL Integration
- ✅ Search Student
- ✅ Sort Students
- ✅ Login Authentication
- ✅ Password Protection
- ✅ Exception Handling
- ✅ Object-Oriented Programming
- ✅ GUI using Tkinter
- ✅ Export Student Records
- ✅ Student Report Generation

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 👨‍💻 Author

## Indrajeet Maheshwari

**Aspiring Data Analyst | Python Developer | SQL | Excel | Power BI**

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

---

<p align="center">

### ⭐ If you like this project, don't forget to star the repository! ⭐

Made with ❤️ using Python

</p>
