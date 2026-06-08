# Assignment 2: Asymptotic Notation Foundations

## Question 1: Matching Notations to Real Life

1. Big-O (O) = Description B: Maximum Cost / Worst-Case.

Big-O represents the upper bound. This means the algorithm is guaranteed not to grow worse than this limit.

2. Big-Omega (Ω) = Description C: Minimum Cost / Best-Case.

Big-Omega represents the lower bound. This means the algorithm must take at least this much work.

3. Big-Theta (Θ) = Description A: Realistic Estimate / Tight Bound.

Big-Theta represents a tight bound. This means the algorithm grows within a predictable range, both from above and below.


## Question 2: Simplifying Sequential Tasks — The Max Rule

The primary bottleneck is Task 2, the heavy sorting routine, because it takes Quadratic Time, O(n²).

The total combined work is:

O(n + n²)

According to the Max Rule, when tasks happen one after another, we keep the term that grows the fastest. Since n² grows faster than n, the simplified Big-O runtime is:

O(n²)


## Question 3: Counting Code Loops — The Multiplication Rule

1. The outer loop runs N times.

2. Because the inner loop is nested inside the outer loop, we multiply their efficiencies together instead of adding them.

3. The final Big-O time complexity is:

O(n²)

This is because the outer loop runs N times, and for each outer loop, the inner loop also runs N times.

N × N = N²


## Question 4: Spotting the Fixed-Size Loop

The engineer is incorrect because the inner loop does not depend on the size of user_list.

Loop A runs once for each user, so it runs n times.

Loop B always runs exactly 3 times for each user. It does not grow when the user_list grows.

So the total work is:

n × 3 = 3n

According to the Drop Rule, we remove the constant 3.

Therefore, the true simplified Big-O complexity is:

O(n)

This is Linear Time, not Quadratic Time.


## Question 5: Arranging the Growth Hierarchy

From most efficient to least efficient:

1. Constant Time: O(1)
2. Linear Time: O(n)
3. Quadratic Time: O(n²)

One example of Constant O(1) time is accessing an item in a list by index, such as:

numbers[0]

This is O(1) because it takes the same amount of time no matter how large the list is.