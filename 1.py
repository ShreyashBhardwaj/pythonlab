def students_scores():
    n = int(input("Enter the No of Students"))
    for i in range(n):
        student=input(f"Enter the name of Student {i}")
        marks=int(input("Enter their marks"))
        students.append(student)
        scores.append(marks)

def max_marks():
    return max(scores)

def min_marks():
    return min(scores)

def avg_marks():
    return sum(scores)/len(scores)


students=[]
scores=[]

def main():

    students_scores()
    print(f"Max Marks: {max_marks()}")
    print(f"Min Marks: {min_marks()}")
    x=avg_marks()
    print(f"Avg Marks: {x}")

    print("Students who got more than avg marks")

    for i in range(len(students)):
        if scores[i]>x:
            print(students[i])

if __name__ == "__main__":
    main()