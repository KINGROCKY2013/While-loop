# take input from user
num = int (input("Enter a number: "))

# intialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10       # 153%10 =3
    sum += digit ** 3
    temp //= 10            #153/10 =15

# display the reesult
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num," is not an Armstrong number")

    
