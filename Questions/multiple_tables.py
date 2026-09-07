
start = int(input("Enter starting table: "))
end = int(input("Enter ending table: "))

for num in range(start, end + 1):
    print("\nTable of", num)

    for i in range(1, 11):
          print(num, "x", i, "=", num * i)
