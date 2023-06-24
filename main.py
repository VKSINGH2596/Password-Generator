# Password Generator Project
import generator as g

print("******************** Password Generator *********************\n")
print("Welcome to the Ghost Password Generator!")
nr_letters = int(input("\nHow many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

status = "Y"  # This is for keep the loop going
created_password = ""
while status.upper() == "Y":
    g.generate_password(total_letters=nr_letters, total_symbols=nr_symbols, total_numbers=nr_numbers)
    status = input("\nGenerate new (Y/N): ").upper()
    if status not in ["y", "Y", "n", "N"]:
        print("\nWrong parameter! Try again.")

print("\n**** Thanks for using the application ****")
