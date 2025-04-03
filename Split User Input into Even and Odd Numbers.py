a = input("Enter numbers: ")
b = a.split()  

even = []
odd = []

for item in b:
    num = int(item) 
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
