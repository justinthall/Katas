"""Failed. Was able to set up a sieve of erathamos algorithm, but was quick enough. Did not have enough time on my 1
hour timer to complete a segmented sieve """


def is_prime(nums):
    if nums <= 1:
        return False
    y = [True for i in range(nums + 1)]
    start = 2
    while start * start <= nums:
        if y[start] == True:
            for i in range(start * start, nums + 1, start):
                y[i] = False
        start += 1
    return y[nums]
