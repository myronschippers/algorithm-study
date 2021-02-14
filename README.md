# Algorithm Study

- [ ] Introduction to Algorithms

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

## Evaluate Algorithms

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
