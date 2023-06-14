# Display Longest Name GeeksforGeeks

names = ["Geek", "GeeksforGeeks", "Geeks", "Geeksfor",
         "GeeksforGeek"]
count = []
for i in names:
    num = 0
    for j in i:
        num += 1
    count.append(num)

nem = count.index(max(count))

print(names[nem])
