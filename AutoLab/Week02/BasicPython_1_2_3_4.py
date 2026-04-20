def listsum(numbers):
    return sum(numbers)


def deduplicate(items):
    return list(set(items))


def sorttuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])


def squarecubes(numbers):
    squares = [x**2 for x in numbers]
    cubes = [x**3 for x in numbers]
    return squares, cubes