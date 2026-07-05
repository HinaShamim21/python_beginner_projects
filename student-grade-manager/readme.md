# Student Grade Manager (Python Console App)

A simple command-line student grade manager built while practicing core Python fundamentals: variables, data types, dictionaries, loops, and functions.

## Features

- **Add Student** – register a new student with a unique student ID and name
- **Add Grade** – add a grade to an existing student's record
- **View Student** – look up a student by ID and see their name and grades
- **Calculate Average** – calculate the average grade for a student
- **Find Highest/Lowest Grade** – find the highest and lowest grade for a student
- **View All Students** – list every student with their ID, name, and grades

## How to Run

1. Make sure you have Python 3 installed.
2. Download `main.py`.
3. Open a terminal in that folder and run:

python main.py

4. Follow the on-screen menu to add students, add grades, and view stats.

## Note

Data is stored only in memory while the program runs — closing the program clears all students and grades. Add a few students and grades each time you test it. File-based saving (so data persists between runs) is a planned next step.

## What I Learned Building This

- Using **nested dictionaries** to store structured data (student ID → name + list of grades)
- Handling **edge cases** (e.g. calculating average/highest/lowest when a student has no grades yet)
- Using **list operations** like `sum()`, `max()`, `min()`, and `len()`
- Writing **functions** to organize each feature separately
- Using a **loop-based menu** to keep the program running until the user exits

## Possible Next Steps

- Save student data to a file (JSON) so it persists between runs
- Allow entering multiple grades at once (comma-separated input)
- Add input validation (e.g. reject non-numeric grades, restrict grade ranges)

*This project was built as part of my journey learning Python fundamentals.*