# Contact Book (Python Console App)

A simple command-line contact book built while practicing core Python fundamentals: variables, data types, lists, tuples, dictionaries, loops, and functions.

## Features

- **Add Contact** – store a new contact with name, phone, and email (warns if the name already exists)
- **View Contacts** – list all saved contacts and show how many are stored
- **Search Contact** – look up a contact by name
- **Update Contact** – edit an existing contact's phone/email
- **Delete Contact** – remove a contact

## How to Run

1. Make sure you have Python 3 installed.
2. Download `contact_book.py`.
3. Open a terminal in that folder and run:

```bash
python contact_book.py
```

4. Follow the on-screen menu to add, view, search, update, or delete contacts.

## What I Learned Building This

- Using **dictionaries** to store structured data (a dictionary of dictionaries)
- Using **loops** to keep a menu running until the user exits
- Writing **functions** to organize each feature separately
- Using **f-strings** for clean, readable output
- Basic input validation (checking if a name already exists before adding)

## Possible Next Steps

- Save contacts to a file so they persist after closing the program
- Add input validation for phone numbers/emails
- Convert to a simple GUI using `tkinter`

---
*This project was built as part of my journey learning Python fundamentals.*