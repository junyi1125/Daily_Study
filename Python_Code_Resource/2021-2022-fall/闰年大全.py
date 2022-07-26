count = 0
for y in range(1900,2022):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(y,end=' ')
        count += 1
        if count % 5 == 0:
            print('\n')