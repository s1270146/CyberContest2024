def logistic_map(index):
    x_n = 0.3
    for i in range(1, index):
        x_n = 3.99 * x_n * (1 - x_n)
    return x_n

print(logistic_map(10000))

