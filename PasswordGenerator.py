import random 
pass_len = int(input("Enter the length of the password::"))
pass_data = "abcdefghijklmnop1234567890[];',./#$"
password = "".join(random.sample(pass_data,pass_len))
print(password)