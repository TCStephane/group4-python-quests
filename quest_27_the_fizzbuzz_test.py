# Quest 27:  The FizzBuzz Test
# Author : @gunnogere
# 25th February 2026

print("=== The FizzBuzz Test - Group 4 ===")

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for number in range(1, 101): #Rnage from 1 to 100. with a default increment of +1

    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} - FizzBuzz")
        fizzbuzz_count += 1

    elif number % 3 == 0:
        print(f"{number} - Fizz")
        fizz_count += 1

    elif number % 5 == 0:
        print(f"{number} - Buzz")
        buzz_count += 1

    else:
        print(number)

# Print totals
print("\n=== Summary ===")
print(f"Total Fizz: {fizz_count}")
print(f"Total Buzz: {buzz_count}")
print(f"Total FizzBuzz: {fizzbuzz_count}")