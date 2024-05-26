from swap import swap_numbers
from extras.desc import print_descending

choice = input("Choose feature - swap (s) or descending (d): ")

if choice == 's':
    a = int(input("Enter the first number (0-3): "))
    b = int(input("Enter the second number (0-3): "))
    a_str, b_str = swap_numbers(a, b)
    print(f"a = {a_str}, b = {b_str}")

elif choice == 'd':
    n = int(input("Enter a number: "))
    print_descending(n)

else:
    print("Invalid choice. Choose 's' or 'd'.")


