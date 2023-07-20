def generate_fibonacci(n):
    fibonacci = [0, 1] 
    for i in range(2, n):
        next_num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(next_num)
    return fibonacci
n = int(input("Enter the number of Fibonacci numbers to print: "))
fibonacci_sequence = generate_fibonacci(n)
print("Fibonacci sequence:", fibonacci_sequence)
