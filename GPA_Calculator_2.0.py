def main():
    try:
        num_grades = int(input("Enter Number of Grades: "))
        total = 0
        student = student_name()

        for i in range(num_grades):
            while True:
                try:
                    score = float(input(f"Enter Test Score {i+1}: "))
                    total += score
                    break
                except ValueError:
                    print("Invalid Input. Please enter a number and try again.")

        average = total / num_grades
        print(f"The All-Around Grade for {student} is {average:.2f} ({letter_grade(average)})")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of grades.")

def student_name():
    first_name = input("Enter Student's First Name: ")
    last_name = input("Enter Student's Last Name: ")
    return f"{first_name} {last_name}"

def letter_grade(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "F"

main()
