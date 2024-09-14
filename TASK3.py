print("-------MINI CALCULATOR-------")
num_1 = int(input("Enter the First number: "))
num_2 = int(input("Enter the second number: "))

print("Choose 1 for Addition\nChoose 2 for Subtraction\nChoose 3 for Multiplication\nChoose 4 for Division")

choice = int(input("Enter your choice from 1-4:"))

if choice == 1:
     print(num_1+num_2)
elif choice ==2:
     print(num_1-num_2)
elif choice == 3:
     print(num_1*num_2)  
elif choice == 4:
     print(num_1/num_2) 

else:
     print("Invalid choice")            
    
