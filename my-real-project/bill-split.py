# 1. Taking inputs
bill = float(input("Enter the total bill amount in ETB: "))
people = int(input("Enter the number of friends splitting the bill: "))

# 2. Ask for tip (press Enter for 10%)
tip_input = input("Enter tip percentage (press Enter for 10%): ")
if tip_input == "":
    tip_rate = 0.1
else:
    tip_rate = float(tip_input) / 100

# 3. Function (same as your hardcoded version)
def split_bill(bill, people, tip_rate=0.1):
    total = bill + (bill * tip_rate)
    per_person = total / people
    return per_person

# 4. Call the function
price = split_bill(bill, people, tip_rate)

# 5. Get names
names = []
print("\nEnter the names of your friends:")
for i in range(people):
    name = input(f"Friend {i+1}: ")
    names.append(name)

# 6. Print results (same style as your hardcoded version)
print("\n--- Final Split ---")
for person in names:
    print(person, "pays", round(price, 2), "ETB")