def display(total, average):
    print(f"Total of all Subjects: {total}\nAverage of Semester: {average}")
    print("Grade of Semester: ", grade(average))

def mark(marks:list):
    return sum(marks)

def avg(total:int, num:int):
    return total/num

def grade(average):
    g=""
    if average >=80:
        g="A+"
    elif average>=75:
        g="A"
    elif average>=70:
        g="B+"
    elif average>=65:
        g="B"
    elif average>=60:
        g="C+"
    elif average>=55:
        g="C"
    elif average>=50:
        g="C-"
    else:
        g="D/Fail"
    return g


data_ls=[]
while True:
    tmp=[]    
    opt=input("Do you want to continue '0' to Continue '-1' to Terminate :")
    choice=name=tp=num_subject=""

    if opt=="-1":
        break
    elif opt=="0":
        print("Your options are:")
        print("1. Add new student detail.\n2. View all student details\n3. Search Specific Student Detail.\n")
        choice=input("Select your choice: ")
        match (choice):
            case "1":
                name=input("Enter Student Name: ")
                tp=input(f"Enter {name}'s TP Number: ")
                num_subject=int(input("How many subjects in Semester: "))
                tmp=[name, tp]
                for i in range(num_subject):
                    tmp.append(int(input(f"Enter {i+1} subject Marks: ")))
                total=mark(tmp[3:])
                average=avg(total, num_subject)
                display(total, average)
                data_ls.append(tmp)
                
    else:
        print("Invalid option")