# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    f_list = [0, 1]
    for i in range(2, n + 1):
        f_list.append((f_list[i-2] + f_list[i-1]) % 10)
    return f_list[n]
if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
