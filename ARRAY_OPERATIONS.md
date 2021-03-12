# Operations on Arrays

## Python

### Accessing Elements

Use the index operator on a list to access values using an index. Note that index values start at 0.

```python
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> numbers[2]
3
```

Using an index that is out of bounds of the current range of values results in a runtime error.

```python
>>> numbers[12]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

### List Length

To determine the number of items in a list, use the len function.

```python
>>> len(numbers)
6
```

len is often used to determine the range of valid index values in a list. To avoid runtime errors it is good practice to iterate over a list with a range defined by the result of calling len instead of a hard coded constant.

```python
>>> for i in range(len(numbers)):
...     print(numbers[i])
...
1
2
3
4
5
6
```

### List Operations

To add to a list, use the append(x) method

```python
>>> numbers.append(7)
```

To add (or concatenate) one list to another, use extend(iterable)

```python
>>> numbers.extend([8, 9, 10])
```

To insert an item into a list at a given position. Here the value 11 is inserted at index position 10.

```python
>>> numbers.insert(10, 11)
```

Use the remove(x) method to remove an item from a list. remove() takes a value as an argument and removes the first element in the list that matches the argument.

```python
>>> numbers.remove(11)
```

Searching for the position of an element in a list is possible using the index(x)

```python
>>> numbers.index(4)
3
```

### List Membership

Use the in and not in operators to test for membership in a list.

```python
>>> if 5 in numbers: print(True)
True
>>> if 30 not in numbers: print(True)
True
```

Python lists are mutable which means any element can be updated using the index operator along with an index position.

```python
>>> numbers[0] = 22 # Updates first element in list to 22
```

**Additional Resources:**

- [Lists](http://openbookproject.net/thinkcs/python/english3e/lists.html)
- [List Operations](https://docs.python.org/3/tutorial/datastructures.html)

<br>

## Swift

### Accessing Elements

Accessing elements individually is generally done using subscript notation with index values starting at 0.

```swift
let numbers: [Int] = [1, 2, 3, 4, 5]
let firstValue = numbers[0]
```

You can subscript an array with any integer starting from 0 up to, but not including, the count of the array. Unlike languages like Python you cannot use a negative number or an index equal to or greater than count. This triggers a runtime error.

In addition to subscripting, there are several methods defined on the type that offer a degree of safety when accessing values. Use the first and last properties to get the first and last elements of an array.

Both these properties return optional values so you can guard against them instead of hitting a runtime error.

```swift
if let firstElement = numbers.first, let lastElement = numbers.last {
    print(firstElement, lastElement, separator: ", ")
}
```

To iterate over a the entire array use a `for-in` loop.

```swift
for number in numbers {
    print(number)
}
```

You can also call `enumerated()` on an array to return a sequence of pairs (n, x) where n representes the index value and x represents the element.

```swift
for (index, element) in numbers.enumerated() {
    print("Element \(element) is at index position \(index)")
}
```

### Adding and Removing Elements

Arrays can only be modified if they are assigned to a variable and not a constant.

```swift
let numbers = [1, 2, 3]
numbers.append(4) // Cannot use mutating member on immutable value: 'numbers' is a 'let' constant
```

Use the `append(_:)` method to add values to the end of a variable array

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(6)
```

When appending more than one value, you have several options. You can concatenate one array to another provided they are of the same type.

```swift
let numbers = [1, 2, 3, 4, 5]
numbers + [6, 7, 8]
```

Notice that the concatenation operation is carried out an array assigned to a constant. This is because the concatenation operation does not mutate the original array and returns a new array containing values from both.

To mutate the array and add multiple elements at the same time by passing another array or a sequence use the `append(contentsOf:)` method.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(contentsOf: [6, 7 ,8])
```

All of these operations add elements to the end of an array. To insert an element in the middle of an array use the insert`(_:at:)` method for single elements or the `insert(contentsOf:at:)` method for multiple elements.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(10, at: 2)
numbers.insert(contentsOf: [18, 22, 35], at: 4)
```

To remove elements from an array there are three options. To remove a single element at an index, use the `remove(at:)` method.

```swift
numbers.remove(at: 2)
```

To remove multiple elements use the `removeSubrange(_:)` method along with a range, either the half-open range operator `(..<)` or the closed range operator `(...)`.

```swift
numbers.removeSubrange(3...6)
numbers.removeSubrange(3..<7)
```

Finally, you can use the convenience methods `removeFirst()` and `removeLast()` to remove the first and last elements in the array.

```swift
numbers.removeFirst() // 1
numbers.removeLast()
```

### Querying An Array

To determine the number of elements in the array use the count property

```swift
let numbers = [1, 2, 3]
numbers.count // 3
```

To determine whether an array is empty use the isEmpty property

```swift
if numbers.isEmpty {
    // do something
}
```

### Array Membership
To check whether an element exists in an array, use the `contains(_:)` method.

```swift
numbers.contains(2)
```

You can also use contains(where:) to search for an element that satisfies a predicate.

```swift
numbers.contains(where: { $0 % 2 == 0 })
```

To find the first instance of an element and return its index position use `firstIndex(of:)`.

```swift
numbers.firstIndex(of: 10)
```

Similarly use `lastIndex(of:)` to return the last index where the specified value appears in the array.

### Creating Array Slices

Often times you will want to extract or query only a portion of an array and you can do this using array slices. Array slices are created when a range is used with a subscript.

```swift
let someNumbers = numbers[2...6]
```

There are couple interesting points to array slices you should be aware of if you're coming from another language:

- Slicing an array returns a different type - ArraySlice. someNumber in the code snippet above is of type ArraySlice<Int>.
- ArraySlice, like Array is a generic type that infers the type of Element from the array it was dervied from. It cannot be used where the type Array is expected.
- In addition, array slices maintain index values of the parent array.

```swift
let numbers = [1, 2, 10, 3, 18, 22, 35, 4, 5]
let someNumbers = numbers[2...6] // [10, 3, 18, 22, 35]
someNumbers.firstIndex(of: 18)
```

In the code snippet above while it seems like `firstIndex(of:) `should return the value 2, the value returned is actually 4. This is becase someNumbers maintains the indices of its parent array. This is because array slices are acttually just views into an array.