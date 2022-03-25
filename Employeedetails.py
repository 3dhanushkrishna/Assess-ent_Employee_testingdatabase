import sqlite3
from prettytable import PrettyTable

connection = sqlite3.connect("Employee.db")
tablelist = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='EMPLOYEEDETAILS'").fetchall()
if tablelist != []:
    print("table created already...")
else:
    connection.execute('''CREATE TABLE EMPLOYEEDETAILS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        EMPCODE INTEGER,
                        EMPNAME TEXT,
                        SALARY INTEGER,
                        DESIGNATION TEXT
                        );''')
    print("table created successfully")
while True:
    print("select an option from the menu ")
    print("1. Add the employees ")
    print("2. view all employees")
    print("3. EXIT")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        getempcode = input("Enter the empcode: ")
        getempname = input("Enter the empname: ")
        getsalary = input("Enter the salary: ")
        getdesignation = input("Enter the designation: ")
        connection.execute("INSERT INTO EMPLOYEEDETAILS(Empcode,EmpName,Salary,Designation) VALUES(" + getempcode + ",'" + getempname + "'," + getsalary + ",'" + getdesignation + "')")
        connection.commit()
        print("added successfully")
    elif choice == 2:
        result = connection.execute("SELECT * FROM EMPLOYEEDETAILS")
        table = PrettyTable(["ID", "EMPCODE", "EMPNAME","SALARY", "DESIGNATION"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4]])
        print(table)
    elif choice == 3:
        connection.close()
        break
    else:
        print("INVALID CHOICE")

