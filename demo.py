# 1. Use a for loop with range() to print numbers from 1 to 10.
# 2. Then, write another loop that counts down from 10 to 1.
# 3. Print a message before and after the loop (for example: "Counting up..." and "Counting down...").
#for i in range(5):
 #   print("Hello")

#for i in range(1,11):
#    print("Counting up:", i)

#for i in range(11,-1,-1):
#    print("Counting down:", i)

#num = int(input("Choose the number of times you want to repeat message "))
#for i in range(num):
#    print("Mesage number: ", i +1)

#word = input("Please enter a word ")
#for letter in word:
#    print(letter)

number = int(input("Choose a number "))
for i in range(0,number,2):
    print(i)
