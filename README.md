# Algorithm Study

- [x] Introduction to Algorithms
- [ ] Efficiency of an Algorithm

## Introduction to Algorithms

**Linear Search**

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target: 50

initial value compared to target value (initial value starting value)
if value === target the algorithm is done
if value !== target then move on sequentially
comparison repeats as you make your way through the list

Algorithm follows a certain set of guidelines. All in order to solve a problem. In most basic it is a set of steps that solve a problem. An algorithm must contain a certain set of instructions in a particular order. Each step needs to be a distinct step. They should produce a result.

**What an Algorithm is...**

1. clearly defined problem statement with an input and output
1. steps need to be in a specific order
1. steps should be distinct
1. should produce a result
1. should complete in a finite amount of time

### Evaluate Algorithms

Correctness & Efficiency

**Correctness**

- start by defining the problem
- clearly defined input and output for the problem
- for any possible input the algorithm should terminate / end (output)
- usually proved by mathematical induction

Algorithms are used in the sequencing of DNA

**Efficiency**

- measured in time and space
- time complexity (how long it takes to run)
- space complexity (amount of memory taken up on the computer)
- how well it does in best case
- how well it does in average case
- how well it does in worst case
- using worst case is good for measurement because it will never be worst than that

**Binary Search**

- List must be sorted
- split and reduce
- split and reduce
- input: a sorted list of values
- output: the position of the matched item
- step1: determine the middle position of a sorted list
- step2: compare element in middle position to the target element
- step3: if the elements match return the position of the matched item and end
- step4: if they don't match check if item is smaller than target if it is return the position of the item if not return to step 2 with a new list that has the paired down list of valid sorted items
- step5: if the item is less than the target element then take the lower half of the list and pass it back returning to step 2

## Efficiency of an Algorithm

when measuring efficiency we always use the worst case scenarios as a bench mark. We use the worst case scenario because it can never perform worse than the worst case scenario.

### Plotting efficiency on a graph

- y-axis: `tries`, the number of tries before coming to a match/success (runtime)
- x-axis: `n`, maximum number of values in the series

**Binary Search**

- **@:** `n` = 10, `tries` = 4
- **@:** `n` = 100, `tries` = 7

**Linear Search**

- **@:** `n` = 10, `tries` = 10
- **@:** `n` = 100, `tries` = 100

How do they perform as `n` gets larger and larger? At values that a computer might have trouble processing the value of `n`.

Growth rate of the algorithm is referred to as the **Order of Growth**. This brings us to the concept of **Big O**.

**Big O**:

- Theoretical definition of the complexity of an algorithm as a function of the size.
- a notation that describes complexity
- _example_, `O(n)`
- `O`, comes from _Order of magnitude of complexity_
- complexity is relative
- Big O can solve the time and space comparison but only against algorithms that are solving the same problem
- last bit in **Big O** is a function of the size, measures complexity as the size grows
- **Big O** is sometimes referred to as the upper bounds of the algorithm
- Linear Search, `O(n)`
- Binary Search, `O(log n)`

**Constant Time**

- Runtime per Operations with n as the x-axis stays the same referred to as **Constant Time**
- in **Big O** notation it is `O(1)`
- `O(1)`, read as "Constant Time"

**Binary Search**

- Logarithm of n, every time n is doubled number of times increases by 1
- Exponents
  - `2 * 1 = 2 || 2 ^ 1 = 2`
  - `2 * 2 = 4 || 2 ^ 2 = 2`
  - `2 * 2 * 2 = 8 || 2 ^ 3 = 8`
  - `log2 8 = 3` - log to the base of 2 on 8 = 3
  - `log2 of n + 1`
- the runtime is referred to as **Logarithmic time**
- **Logarithmic** type of **Big O** represented as `O(log n)` or sometimes `O(ln n)`
- algorithms with **logarithmic time** are referred to as **Sub-linear**

**Linear Search**

- `O(n)` most commonly referred to as **Linear Time**
- reading every item in a list means linear run time
- quadratic

**Sorting Algorithms???**

- have verying difficulties

**Big O of n squared**

- `O(n^2)`
- `n = 4`
- 4 x 4 Grid
- `n^2 = 16`
- Quadratic Runtime
- Cubic Runtime - `n^3`
- can be referred to as expensive computationally

**Quasilinear Runtime**

- `O(n log n)`
- visual graphed, upward curve above linear runtime
- graphed it falls between Linear Runtime and Quadratic Runtime (on the upper bounds)
- see an example of this when dealing with sorting algorithms

_example:_
Merge Sort

`O(n log n)`

1. start with
   - `[8, 4, 5, 1, 3, 2, 6, 7]`
1. split the list into 2 lists down the middle
   - `[8, 4, 5, 1]` `[3, 2, 6, 7]`
1. take each sublist and split in half
   - `[8, 4]` `[5, 1]` `[3, 2]` `[6, 7]`
1. take each sublist and split in half again until left with each list having only a single number
   - `[8]` `[4]` `[5]` `[1]` `[3]` `[2]` `[6]` `[7]`
   - **Merge Operations**, `n = 0`

- need to carry out comparison operations (n number of comparisons on the single item arrays)

**Quadratic Runtime**

- `O(n^2)`
- visual graphed, mirror over linear of Binary Runtime (`O(log n)`)

**Polynomial Runtime**

- An algorithm is considered to be a Polynomial Runtime if `O(n^k)` (`k` power meaning some value...???)
- `k` = 2, for a **Quadratic Runtime**
- `k` = 3, for a **Cubic Runtime**
- anything that falls under the `O(n^k)` graph is considered a **Polynomial Runtime**

### Exponential Runtimes

- `O(x^n)`

**Example:**

- 2 sets of 10 possible digits on a lock could be noted as `10^2`
- trying every combination on the lock until it opens is referred to as **Brute Force**
- **Brute Force** algorithms have exponential run times
- for the lock we have 2 digits so we can say `n = 2` and say that the possibilities ar `10^n` with `n` representing the number of dials
- the reason this is so inefficient is because with just one more dial added to the lock `n` is now 3 and the number of possibilities goes up significantly (number of combinations in the worst case scenario increase dramatically)

**The Traveling Salesman (Exponential Algorithms)**

- given a list of cities and the distance between each pair of cities, what is the shortest route that visits each city and then returns to the origin city
- with cities A, B, & C we have to find all the possible combinations for the city routes
- factorial represented by `n!`
- `3!` is `3 x 2 x 1 = 6`
- `4!` is `4 x 3 x 2 x 1 = 24`
- Factorial / Combinatorial Runtime
- `O(n!)`

### How do we determine what the worst case complexity of an Algorithm is?

