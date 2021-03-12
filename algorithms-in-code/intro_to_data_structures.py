##
# ARRAYS
## ------------------------------

new_list = [1, 2, 3, 4];
result = new_list[0];

# search for a value in the array/list
if 1 in new_list: print(True)

for n in new_list:
  if n == 1:
    print(True)

    break

# when creating an empty list python will allocate one element of space in memory
numbers = [];
# even though an element is reserved in memory the array's length will still come
# out to 0
len(numbers)
# now the size of the array and the memory allocation are the same
numbers.append(2);
# what if wee append another number?
# before it can add another item it has to reallocate memory

# it doesn't increase the memory allocation every time another item is added but
# only at specific points
numbers.append(200);
# 0, 4, 8, 16, 25, 35, 46...
# more memory is only allocated when the items in the array reach these different
# points so that memory doesn't have to be reallocated  over an over again

# adding one list to another
numbers_second = [];
numbers.extend([4, 5, 6])
print(numbers) # prints [4, 5, 6]