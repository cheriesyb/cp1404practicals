
# 1

output_file = open("name.txt", 'w')
user_name = input("What is your name?")
print(user_name, file=output_file)
output_file.close()

# 2

input_file = open("name.txt", 'r')
user_name = input_file.read().strip()
print("Your name is", user_name)
input_file.close()
