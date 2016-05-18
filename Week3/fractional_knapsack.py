# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    if len(weights) > 1:
        value_per_unit = []
        for i in range(len(weights)):
            value_per_unit.append(values[i]/weights[i])
        while len(weights) > 1 and capacity > 0:
            max_index = value_per_unit.index(max(value_per_unit))
            if weights[max_index] <= capacity:
                value = value + values[max_index]
                capacity = capacity - weights[max_index]
                del value_per_unit[max_index]
                del weights[max_index]
                del values[max_index]
            else:
                partial_value = capacity/weights[max_index]
                value = value + values[max_value]*partial_value
                capacity = 0
        if len(weights) == 1 and capacity > 0:
            if weights[0] <= capacity:
                value = value + values[0]
            else:
                partial_value = capacity/weights[0]
                value = value + values[0]*partial_value
    else:
        if weights[0] <= capacity:
            value = value + values[0]
        else:
            partial_value = capacity/weights[0]
            value = value + values[0]*partial_value
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
