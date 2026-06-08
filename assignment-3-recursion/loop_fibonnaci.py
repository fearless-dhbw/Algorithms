def loop_fibonacci(n):
    if n <= 0:
        return []
    
    if n == 1:
        return [1]
    
    series = [0, 1]

    for i in range(2, n):
        next_number = series[-1] + series [-2]
        series.append(next_number)

    return series
    
print(loop_fibonacci(8))