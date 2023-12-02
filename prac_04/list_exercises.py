
# 1
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print('The first number is', numbers[0])
print('The last number is', numbers[-1])
print('The samllest number is', min(numbers))
print('The largest number is', max(numbers))
print('The average of the numbers is', sum(numbers) / len(numbers))

# 2

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Enter the username: ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")
