def binary_search(list, target):
  first = 0
  last = len(list) - 1

  # use a while loop to iterate
  while first <= last:
    # // floor division number rounds down divided value
    midpoint = (first + last)//2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

# binary search has to be passed a list that has been sorted or it will NOT work
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)