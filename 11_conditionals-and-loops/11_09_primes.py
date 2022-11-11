# Print out every prime number between 1 and 1000.

for p in range(2, 1001):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print(p)
