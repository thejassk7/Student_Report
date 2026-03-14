import math
def main():
    name=input("Enter your name: ")
    no_subject=int(input("Enter the number of Subjects: "))
    subject=[]
    marks=[]
    max_marks=[]
    for i in range(no_subject): 
        subject_name=input("Enter number of Subject: ")
        student_marks=int(input("Enter the marks of each subject: "))
        maximum_marks=int(input("Enter Maximum Marks: "))
        subject.append(subject_name)
        marks.append(student_marks)
        max_marks.append(maximum_marks)
        i=i+1
    operation=input("Performance Parameter: ")
    if operation.upper()=="TOTAL MARKS":
        total_marks()
    elif operation.upper()=="PERCENTAGE":
        percentage()
    elif operation.upper()=="AVERAGE":
        average()
    elif operation.upper()=="MEDIAN":
        median()
    else:
        print("Invalid Entry!!!")
    return no_subject,subject,marks,max_marks
def total_marks(no_subject,subject,marks,max_marks):
    student_marks=0
    for i in range(no_subject):
        student_marks=student_marks+marks[i]
        i=i+1
    for i in range(no_subject):
        maximum=maximum+max_marks[i]
        i=i+1
    print("Student scored",student_marks,"out of",maximum)
def percentage(no_subject,subject,marks,max_marks):
    for i in range(no_subject):
        student_subject=subject[i]
        student_marks=marks[i]
        maximum=max_marks[i]
        subject_percentage=student_marks/max_marks
        print("Subject: ",student_subject,"Percentage: ",student_marks)
        i=i+1
    student_marks=0
    maximum=0
    for i in range(no_subject):
        student_marks=student_marks+marks[i]
        maximum=maximum+max_marks[i]
        i=i+1
    total_percentage=student_marks/maximum
def average(no_subject,subject,marks,max_marks):
    student_marks=0
    for i in range(no_subject):
        student_marks=student_marks+[i]
        i=i+1
    average=student_marks/no_subject
    print("Average: ",average)
def median(no_subject,subject,marks,max_marks):
    subject_marks={}
    for i in range(no_subject):
        subject_marks[subject[i]]=marks[i]
        i=i+1
    marks.sort()
    if no_subject%2==0:
        n=no_subject/2
        med=marks[n]
    else:
        n=(no_subject/2)+0.5
        med=marks[n]
    for key,value in subject_marks.items():
        if med==value:
            print("The median value is: ",med,"scored in ",key)
main()
