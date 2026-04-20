import sys

numbers = [int(x) for x in sys.argv[1:]]
evens = [x for x in numbers if x % 2 == 0]

print(evens)