"""Takes a list of numbers and removes any duplicates from the right."""


def solve(arr):
    used = []
    output = []
    arr.reverse()
    for i in arr:
        if i not in used:
            used.append(i)
            output.append(i)
        else:
            continue
    output.reverse()
    return output


print(solve([1, 2, 3, 4, 5, 5, 1, 2, 1]))
