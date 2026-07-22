 # TeleBirr Transaction Log Reader

# Step 1: Try to read the file (handle missing file gracefully)
try:
    file = open("transactions.txt", "r")
except FileNotFoundError:
    print("Error: transactions.txt not found!")
    exit()

# Step 2: Build dictionary (customer -> total spend)
totals = {}

for line in file:
    line = line.strip()
    if line == "":
        continue

    parts = line.split(",")
    name = parts[0].strip()
    amount = float(parts[1].strip())

    if name in totals:
        totals[name] += amount
    else:
        totals[name] = amount

file.close()

# Step 3: Sort by total (highest first)
sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)

# Step 4: Print to screen
print("=" * 35)
print("   TeleBirr Transaction Report")
print("=" * 35)
for name, total in sorted_totals:
    print(f"{name:<15} {total:>10.2f} ETB")

# Step 5: Write summary to report.txt
report = open("report.txt", "w")
report.write("TeleBirr Transaction Report\n")
report.write("=" * 35 + "\n")
for name, total in sorted_totals:
    report.write(f"{name}: {total:.2f} ETB\n")
report.close()

print("\nReport saved to report.txt")