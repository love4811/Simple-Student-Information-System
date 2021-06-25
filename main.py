import csv
import datetime
now = datetime.datetime.now()
print("\t Current date : "+now.strftime("%Y-%m-%d"))
print("*************************************")

listformat = ['Name', 'ID Number', 'Year Level', 'Gender', 'Course']

def menu():
    print("Welcome to Student Information System")
    print("*************************************")
    print("Select the option you want to do: ")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Information")
    print("5. Delete Student")
    print("6. Close")
    print("*************************************")
    
def add():
    print("*************************************")
    print("Add Student")
    global listformat
    data = []
    for field in listformat:
        user_input = input("Enter " + field + ": ")
        data.append(user_input)      
    with open('student.csv', "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([data])
    print("Information Added Successfully")
    print("*************************************")
    input("Press Any Key to Continue")
    return

def view():
    global listformat
    print("*************************************")
    print("Student Information")
    with open('student.csv', "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in listformat:
            print(x, end='\t \t |')
        print("\n")
        for row in reader:
            for item in row:
                print(item, end="\t \t |")
            print("\n")
            print("*************************************")
    input("Press Any Key to Continue")

def search():
    print("*************************************")
    print("Search Student")
    Number = input("Enter ID Number to search: ")
    with open('student.csv', "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if Number == row[1]:
                    print("Found Student with ID number: " + Number)
                    print("Name: ", row[0])
                    print("ID Number: ", row[1])
                    print("Year Level: ", row[2])
                    print("Gender: ", row[3])
                    print("Course: ", row[4])
                    break
        else:
            print("ID Number " + Number + " not found in our list")
            print("*************************************")
    input("Press Any Key to Continue")

def update():
    global listformat 
    global listofstudents
    print("*************************************")
    print("Searh Student")
    Number = input("Enter ID Number of student you want to edit:\n ")
    index = None
    edited = []
    with open('student.csv', "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if Number == row[1]:
                    index = counter
                    print("Student Found: at index ", index)
                    student = []
                    for field in listformat :
                        value = input("Enter " + field + ":\n ")
                        student.append(value)
                    edited.append(student)
                else:
                    edited.append(row)
                counter += 1
    if index is not None:
        with open('student.csv', "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(edited)
    else:
        print("ID Number not found on the list\n")
    print("Successfully edited!\n")
    print("*************************************")
    input("Press Any Key to Continue:\n")

def delete():
    global listformat
    print("*************************************")
    print("Delete Student")
    Number = input("Enter ID Number to delete: ")
    student_found = False
    updated_data = []
    with open('student.csv', "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if Number != row[1]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
    if student_found is True:
        with open('student.csv', "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID Number", Number, "deleted successfully")
    else:
        print("ID Number not found in our database")
    print("*************************************")
    input("Press any key to continue")

while True:
    menu()
    choice = input("Enter Your Option: ")
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        search()
    elif choice == '4':
        update()
    elif choice == '5':
        delete()
    else:
        break
print(" Thank You for Using the System")