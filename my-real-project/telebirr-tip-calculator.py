
# 1. Taking inputs
bill_total = float(input("Enter the total bill amount in ETB: "))
people = int(input("Enter the number of friends splitting the bill: "))

# 2. Ask for tip (press Enter for 10%)
tip_input = input("Enter tip percentage (press Enter for 10%): ")
if tip_input == "":
    tip_rate = 0.10
else:
    tip_rate = float(tip_input) / 100

# 3. Get names
names = []
print("\nEnter the names of your friends:")
for i in range(people):
    name = input(f"Friend {i+1}: ")
    names.append(name)

# 4. Function
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

# 5. Calculate each person's share
share = split_bill(bill_total, people, tip_rate)

# 6. Print result
print("\n" + "=" * 30)
print("   TeleBirr Tip Calculator")
print("=" * 30)
print(f"Bill Total: {bill_total:.2f} ETB")
print(f"Tip: {tip_rate * 100:.0f}%")
print(f"Each person pays: {share:.2f} ETB")
print("=" * 30)

# 7. Loop through names
for name in names:
    print(f"{name} pays {share:.2f} ETB")