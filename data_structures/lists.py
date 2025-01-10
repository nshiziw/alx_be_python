my_list = [1, 2, 6, 34, 65, 4, 3]
# indexing
print (my_list[3]) # outputs 34
print (my_list[6]) #outputs 3

# slicing
print(my_list[3:6]) # outputs 34, 65, 4
print(my_list[1:5:2]) # outputs 2,34
print(my_list[::-1]) # outputs 4, 65, 34, 6, 2, 1

# appending
my_list.append(89)

# removing

my_list.remove(1)

print(my_list)
print(my_list[3]) # outputs 65