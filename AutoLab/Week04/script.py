import time

def fast(x):
    result = x + 2
    return result

@profile
def slow(x):
    # Job security
    time.sleep(3)
    result = x * x
    return result


print(fast(10))
print(slow(10))