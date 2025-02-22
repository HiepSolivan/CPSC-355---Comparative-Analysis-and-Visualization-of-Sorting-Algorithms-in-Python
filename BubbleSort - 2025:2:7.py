import time

# Bubble Sort Algorithm

def BubbleSort(students):
    n = len(students)

    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:
                students[j], students[j + 1] = students[j+1], students[j]

# Take user input
num_students = int(input("Enter number of students: "))
students = []

for _ in range(num_students):
    name = input("Enter student name: ")
    score = int(input(f"Enter {name}'s score: "))
    students.append((name, score))

#BubbleSort(students)

# Measure execution time
start_time = time.time()
BubbleSort(students)
end_time = time.time()

print("Storted students by score:", students)
print(f"Execution time: {end_time - start_time:.6f} seconds")

# The time complexity for this algorithm will be O(n^2)
