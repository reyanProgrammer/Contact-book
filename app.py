import sqlite3

db = sqlite3.connect("contacts-db-sql.db")
cursor = db.cursor()
while True:

    cmd = input("> ")

    if cmd == "ADD CONTACT":
        contact_name = input("Enter contact name: ")
        contact_phonenumber = int(input("Enter contact phone number: "))
        cursor.execute("INSERT INTO Contacts(full_name, phno) VALUES(?, ?)",
                       (contact_name, contact_phonenumber))
        db.commit()

    elif cmd == "VIEW CONTACTS":
        cursor.execute("SELECT * FROM Contacts")
        items = cursor.fetchall()
        for index, item in enumerate(items):
            print("Contact no. {rowid} Info ".format(rowid=index+1))
            print(f"Name {item[1]}")
            print(f"Phone no. {item[2]}")
            print()

    elif cmd == "UPDATE CONTACT":
        method = input("Do you want to update contact by number or name? ")
        if method == "number":
            phno = input("Enter phone Number ")
            updatephno = input("Enter updated phone Number ")

            cursor.execute(
                """UPDATE Contacts SET phno=? WHERE phno=?""", (updatephno, phno))
            db.commit()
        elif method == "name":
            name = input("Enter Name ")
            updatename = input("Enter Updated Name ")

            cursor.execute(
                """UPDATE Contacts SET full_name=? WHERE full_name=?""", (updatename, name))
            db.commit()

    elif cmd == "DELETE CONTACT":
        method = input("Do you want to Delete contact by number or name? ")
        if method == "number":
            phno = input("Enter phone Number ")

            cursor.execute(
                """DELETE FROM Contacts WHERE phno=?""", (phno, ))
            db.commit()
        elif method == "name":
            name = input("Enter Name ")

            cursor.execute(
                """DELETE FROM Contacts WHERE full_name=?""", (name, ))
            db.commit()
