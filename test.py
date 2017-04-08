def hi(age):
    print(age)
    if int(age) < 20:
        print("hey")
    elif int(age) > 20 and int(age) < 40:
        print('hi')
    else:
        print("hello")

print('please enter your age')
myage = input()
hi(myage)
