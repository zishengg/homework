def user_input():
    print("Do you want to continue? '0' to Continue '-1' to Terminate:")
    choice = int(input("Continue or terminate?"))
    if choice == 0:
        option = int(input("Your Options are:\n\t1. Add new student detail.\n\t2. View all student details.\n\t3. Search Specific student detail."))
        if option == 1:
            student = []
            name = input("Enter Student Name: ")
            tpnumber = input(f"Enter {name}'s TP Number: ")
            subcount = int(input("How many subjects in Semester: "))

            marks = []
            for i in range(subcount):
                subject_marks = int(input("Enter " + str(i+1) + " subject Marks: "))
                marks.append(subject_marks)

            student.append(name)
            student.append(tpnumber)
            student.append(subcount)
    elif option == 2:
        print("Not specified yet")
    elif option == 3:
        print("Not specified yet")
    else:
        print("Error")

def display():
    display_name = student[0]
    display_tp = student[1]
    display_total = mark
    display_percentage = average
    display_grade = grade
    print("Name: ", display_name)
    print("TP Number: ",display_tp)
    print("Total: ",display_total)
    print("Percentage: ",display_percentage ,"%")
    print("Grade: ", display_grade)
    return 


def mark(marks):
    return sum(marks)

def average():
    average = mark / subcount
    return average

def grade(average):
    if average >= 80:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 65:
        return "B"
    elif average >= 60:
        return "C+"
    elif average >= 55:
        return "C"
    elif average >= 50:
        return "C-"
    else:
        return "D/Fail"