foods = ["mango", "apple", "orange", "banana", "burger"]
for food in foods:
    print(food)

colors = ["red", "green", "blue", "yellow", "orange"]
for color in colors:
    print(color)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

message = "Please update"
for msg in message:
    print(msg)

for number in range(40):
    print(number)

for number in range(4, 10):
    print(number)

numbers = [1, 5, 3, 9]
total = 0
for number in numbers:
    total += number

print(f"The total sum of the numbers is: {total}")


shopping_list = ["perfume", "socks", "shoes", "mirror", "soap"]
item_found = False
while not item_found:
    item = input("Search for an item in your list (or 'q' to quit): ").lower()
    if item == 'q':
        break
    if item in shopping_list:
        item_found = True
        print(f"{item} is in your list!")
    else:
        print(f"{item} is not in your list.")

for i in range(1, 13):
    # Outer loop iterates through rows (multiplication factors)
    for j in range(1, 13):
        # Inner loop iterates through columns (other factors)
        product = i * j
        print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
    print()  # Move to a new line after each row

rows = 5

for i in range(1, rows + 1):
    # Outer loop controls the number of rows
    for j in range(1, i + 1):
        # Inner loop prints asterisks for each row
        print("*", end="")
    print()  # Move to a new line after each row of asterisks