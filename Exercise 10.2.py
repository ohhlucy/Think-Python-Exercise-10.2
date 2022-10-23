#Exercise 10.2. Write a function called cumsum that takes a list of numbers.

list = [20, 40, 60, 80, 100]
new_list = []
j = 0
for i in range(0, len(list)):
    j += list[i]
    new_list.append(j)

print(new_list)
