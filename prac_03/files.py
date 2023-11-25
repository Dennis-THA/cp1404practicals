# 1

out_file = open("name.txt", "w")
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

# 2

in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Your name is {name}.")
in_file.close()


# 3

in_file = open("numbers.txt", "r")
first_line = int(in_file.readline())
second_line = int(in_file.readline())
in_file.close()
print(first_line + second_line)


# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

