first_num = int(input("Enter First number = "))
second_num = int(input("Enter second number = "))

print("Operations Available : \n1: Plus(+)\n2: Minus(-)\n3: Division( /)\n4: Mode(%) \n")
input = int(input("Enter your operation : "))
if input == 1:
    sum = first_num + second_num
    print(f"{first_num} + {second_num} = ", sum)


elif input == 2:
    sub = first_num - second_num
    print(f"{first_num} - {second_num} = ", sub)

elif input == 3:
    div = first_num / second_num
    print(f"{first_num} / {second_num} = ", div)

elif input == 4:
    mod = first_num % second_num
    print(f"{first_num} % {second_num} = ", mod)
    
else:
    print("Invalid Choice !")
