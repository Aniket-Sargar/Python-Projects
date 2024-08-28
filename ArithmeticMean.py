# Taking input from the user
number=list(map(float, input("Enter the Packages of students: ").split()))


if len(number) > 0:
    #Summing up all the numbers in the list
    print("Sum of Number: ", sum(number))

    print("Length of Number:", len(number))

    #Dividing the sum by the number of elements to find the mean
    print("Mean or Average: ", sum(number)/len(number))

else:
    print("The list is empty, so the mean cannot be calculated.")