def recursive_binary_search(list, target):
  # what happens if an empty list is passed in
  if len(list) == 0:
    # base case for stopping condition
    return False
  else:
    midpoint = (len(list))//2

    if list[midpoint] == target:
      # base case for stopping condition
      return True
    else:
      if list[midpoint] < target:
        # base case for stopping condition
        # creates a sub list from one index to another
        # list[startIndex:endIndex]
        return recursive_binary_search(list[midpoint+1:], target)
      else:
        # base case for stopping condition
        return recursive_binary_search(list[:midpoint], target)

def verify(result):
  print("Target found:", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)