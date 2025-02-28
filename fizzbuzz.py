# print numbers 1 to 50 DONE
# print out 'fizz' if a number is divisible by 5
# print out 'buzz' if a number is divisible by 3
# print out 'fizzbuzz' if a number is divisible by both
my_nums = [1, 3, 5, 7, 9, 11, 13, 15]
# for each number in the my_nums list, print it out
for num in my_nums:
    if(num % 5 == 0 and num % 3 == 0):
        print("fizzbuzz")
    elif(num % 5 == 0):
        print("fizz")
    elif(num % 3 == 0):
        print("buzz")
    else:
        print(num)