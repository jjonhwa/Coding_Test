n = int(input())
count = 1
num = 1

while True:
    if n <= num:
        break

    num += 6*count
    count += 1
print(count)