# Gradebook Analyzer
# Name = Gurveen Kaur
# Course = Btech(cse)(datascience) 1st semester
# Rollno = 250114262
print("Welcome to Gradebook Analyzer!")
print("This programme helps you to analyze student marks easily.")
# Task 1 : Menu for data input

def menu():
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. Exit")


# Task 2: Data entry or CSV import
def manual_entry():
    marks = {}
    n = int(input("enter number of student"))
    for i in range(n):
        name = (input(f"enter name of student {i+1}:"))
        marks = float(input(f"Enter marks of {name}:"))
        marks[name] = marks
    return marks

def csv_import():
    marks = {}
    filename = input("enter csv filename (with .csv extension):")
    try
        with open(filename,newline='') as file:
            reader = csv.DictReader(file)
            for row in reaader:
                # Assuming CSV has columns: Name , Marks
                name = row['name']
                mark = float(row['mark'])
            mark[name] = mark 
print("file not found . please check the filename and try again")
except  keyerror:
print("CSV file must contain 'name' and 'mark' columns.")
except  Exception as e:
print("error reading file:,e")
return:  marks 
def main():
    print ("choose data entry method:")
    print("a) manually entry")
    print("b) load from CSV file")
    choice = input("enter choice (a/b):").lower()
    if choice == 'a':
        marks = manual_entry()
    elif choice == 'b':
        marks = csv_import()
    else:
        print("invalid choice.")
        return
    print("\ndata successfully stored in memory:")
    print(marks)
if __name__ == "__main__":main()

#Task 3: statistical functions
def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    if n%2 == 0:
        return (scores[n//2 - 1]+ scores[n//2]) / 2
    else:
        return scores[n//2]

def find_max_scores(marks):
    return max(mark.values())
def find_min_score(marks):
    return min(marks.values())

#Task 4: Grade assignment
def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if scores >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
            return grades

#Task 5: Pass / Fail
def pass_fail(marks):
    passed = [n for n, s in marks.items() if s >= 40]
    failed = [n for n, s in marks.items() if s < 40]
    print(f"\nPassed students({len(passed)}): {passed}")
    print(f"Failed Students ({len(failed)}): {failed}")

#Task 6: Display results table
def display_table(mark, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")

#Main Program Loop

while True:
    menu()
    choice = input("enter your choice:")
    if choice == '1':
        marks = manual_input()
    elif choice == '2':
        marks = csv_input()
    elif choice == '3':
        print("Exiting programe. THANK YOU!")
        break
    else:
        print("Invalid choice! Try again.")
    continue
if len(marks)== 0:
    print("No data found.")
continue:
grades = assign_grades(marks)
display_table(marks, grades)

print("\n---Summary ---")
print(f"Average Marks:{calculate_average(marks):.2f}")
print(f"Median Marks:{calculate_median(marks):.2f}")
print(f"Highest Marks:{find_max_score(marks)}")
print(f"Lowest Marks: {find_min_score(marks)}")

pass_fail(markas)

again = input("\n Do you want to analyze again? (yes/no): ").lower()
if again != 'yes':
    print("Thank you for using GradeBook Analyzer!")


    

            