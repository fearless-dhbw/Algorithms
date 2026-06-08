# Assignment 3: Recursion

## Q1. The Factorial Countdown

The code for this question is in `recursive_factorial.py`.

The function uses recursion to calculate the factorial of a number. It has a base case to stop the recursion and a recursive call to continue solving a smaller version of the problem.


## Q2. Building the Fibonacci Sequence

The code for this question is in `loop_fibonacci.py`.

The function uses a loop to build a list of the first n Fibonacci numbers. It starts with `[0, 1]` and then repeatedly appends the sum of the previous two numbers.


## Q3. Spot the Bug!

The missing part is a base case.

Without a base case, the function keeps calling itself forever:

```python
def countdown(n):
    print(n)
    countdown(n - 1)

#The corrected version is

def countdown(n):
    # Base case: stop when n is less than 1
    if n < 1:
        return

    print(n)

    # Recursive call
    countdown(n - 1)

```   

## Q4. The Memory Trade-Off
An iteration loop is more memory efficient that a naive recursive funtion because it uses the same block of memory again and again.
A recursive function keeps calling itself but each unfinished function call is stored in the Call Stack. If there are too many recursive calls, the Call Stack grows and uses more memory. If it grows too much, the program can crash with a Recursion Error. 

## Q5. The Stacking Box Dilemma
The recursive action is opening the next smaller box again and again.
The base case is when I reach the smallest box and find the golden key, so there are no more boxes to open.

## Q6. The 29th Day Puzzle
The jar was half full at minute 29.
This requires backward thinking because we start from the final result, 100% full at minute 30, and work back to the smaller previous state. Since the bacteria doubles each minute, one minute before full it must have been half full.

## Q7. The Echo in the Canyon
The recursive call is the echo repeating again and again.
Nature’s base case is when the echo becomes too weak or quiet to continue, so it fades away and stops.
