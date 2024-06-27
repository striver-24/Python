# conditions -> < (greater than),>(less than),==(equal to),!= (not equal to)

print(5!=7)

#if/else/elif

# if condition == True:
#     do this

age = input("Input your age : ")
if int(age) == 16:
    print("You are 16")
elif int(age) >= 16:
    print("You are over 16")
else:
    print("You are minor")