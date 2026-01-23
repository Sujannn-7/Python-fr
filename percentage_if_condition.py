marks1 = int(input("Enter your marks in Physics "))
marks2 = int(input("Enter your marks in Computer Science "))
marks3 = int(input("Enter your marks in Chemistry "))

total = marks1+marks2+marks3
print(total)

percentage = (total/300)*100
print(f"{percentage}%")

if (marks1<33 or marks2<33 or marks3<33):
    if (percentage < 40):
        print("You failed the exam.")
else:
    print("You passed the exam. ")