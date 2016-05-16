# Uses python3
import sys

def gcd(a, b):
    current_gcd = 1
    if a == 0:
        current_gcd = b
        return current_gcd
    if b == 0:
        current_gcd = a
        return current_gcd
    if a == 1 or b == 1:
        return current_gcd
    if a % b == 0:
        current_gcd = min(a,b)
        return current_gcd
    else:
        if b < a:
            r = a % b
            min_int = b
        else:
            r = b % a
            min_int = a
        if r == 1:
            return current_gcd
        return gcd(min_int,r)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
