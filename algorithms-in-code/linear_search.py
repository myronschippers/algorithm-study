def linear_search(list, target):
  """
  Returns the index position of the target if found, else returns None
  """

  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None

# Linear search can be cleaned up a bit with the enumerate function 

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)