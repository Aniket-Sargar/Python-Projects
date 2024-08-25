#Initial Bank Balance
balance = 10000.0

print("Welcome to the Basic Banking System")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
print("--------------------------------------")
choice = input("Enter your choice (1-4): ")


if choice == '1':
    print("Your current balance is:", balance, "rs")
    print("Thank you!")

elif choice == '2':
    amount = float(input("Enter the amount to deposit: Rs. "))
    if amount > 0:
        balance += amount
        print(amount, "rs deposited successfully.")
        print("Thank you!")
    else:
        print("Deposit amount must be greater than zero!")
    print("Your new balance is:", balance, "rs")
    print("Thank you!")


elif choice == '3':
    amount = float(input("Enter the amount to withdraw: Rs. "))
    if amount > balance:
        print("Insufficient funds!")
        print("Thank you!")
    elif amount <= 0:
        print("Withdrawal amount must be greater than zero!")
        print("Thank you!")
    else:
        balance -= amount
        print(amount, "withdrawn successfully.")
    print("Your new balance is:", balance, "rs")
    print("Thank you!")


elif choice == '4':
    print("Thank you for using the Basic Banking System. Goodbye!")


else:
    print("Invalid choice! Please select a valid option.")
    print("Thank you!")