import time

# Merge Sort
def MergeSort(flights):

    if len(flights) > 1:
        mid = len(flights) // 2 #Find the middle index (floor division)
        left_half = flights[:mid] # Divide list into halves
        right_half = flights [mid:]

        MergeSort(left_half) #Recursively split
        MergeSort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                flights[k] = left_half[i]
                i += 1
            else:
                flights[k] = right_half[j]
                j += 1
            k+=1

        while i < len(left_half):
            flights[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            flights[k] = right_half[j]
            j += 1
            k += 1

# Take User Input
num_flights = int(input("Enter number of flights "))
flights = []
for _ in range(num_flights):
    flight_num = input("Enter the flight number: ")
    depart_time = int(input(f"Enter the departure time for {flight_num}: "))
    flights.append((flight_num, depart_time))

start_time = time.time()
MergeSort(flights)
end_time = time.time()

print("Sorted flights:", flights)
print(f"Execution time: {end_time - start_time:.6f} seconds")
