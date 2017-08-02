# Python program to display all the prime numbers inside an interval specified by the user

# uncomment the following lines to take input from the user
bot = int(input("Enter bottom of range: "))
top = int(input("Enter top of range: "))

print("Prime numbers between the values",bot,"and",top,"are as listed:")

for number in range(bot,top + 1):
   if number > 1:
       for test in range(2,num):
           #test if each number in the range is divisible by the test digit
           if (number % test) == 0:
               break
               #breaks once it finds a number divisible by any digit between 2 and the number being tested
       else:
         #prints the number if it is prime
           print(number)
