count = 1
sum = 0
while (count <= 10):
    if ( count % 2 == 0):  # 双数时跳过输出
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
    print(sum)
print(sum)
