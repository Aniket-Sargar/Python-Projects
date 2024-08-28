# Taking input from the user
number = list(map(float, input("Enter the numbers separated by spaces: ").split()))
print(number)

# Sort the list of numbers
number.sort()
print("Sorting List: ", number)

#if the numbers of dataset is Even
if len(number)%2 == 0:
    print("Dataset length is Even")
    # Calculate the average of the two middle values
    middle1 = number[len(number) // 2 - 1]
    middle2 = number[len(number) // 2]
    median = (middle1 + middle2) / 2
    print("Median: ",median)

#if the numbers of dataset is Odd
else:
    print("Dataset is Odd")
    # Return the middle value
    print("Median: ", number[len(number) // 2])