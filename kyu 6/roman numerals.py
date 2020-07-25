'''This is code to convert a integer up to 4000 into roman numerals. It's not the best way, but it is the first way I
found. the code essentially takes the integer, checks to see if its more than a power of 10, and then subtracts that power.
then it figures out what symbol that integer needs.'''


def solution(n):
    reponse = []
    if n >= 1000:
        number = int(n / 1000)
        mcount = 'M' * number
        n = n - (1000 * number)
        reponse.append(mcount)
    if n >= 100:
        hundreths = int(n / 100)
        if hundreths <= 3:
            ccount = 'C' * hundreths
        elif hundreths == 4:
            ccount = 'CD'
        elif hundreths == 5:
            ccount = 'D'
        elif 6 <= hundreths < 9:
            ccount = 'D' + 'C' * (hundreths - 5)
        else:
            ccount = 'CM'
        n = n - (100 * hundreths)
        reponse.append(ccount)
    if n >= 10:
        tens = int(n / 10)
        if tens <= 3:
            xcount = 'X' * tens
        elif tens == 4:
            xcount = 'XL'
        elif tens == 5:
            xcount = 'L'
        elif 6 <= tens < 9:
            xcount = 'L' + 'X' * (tens - 5)
        else:
            xcount = 'XC'
        n = n - (10 * tens)
        reponse.append(xcount)
    if n <= 3:
        icount = 'I' * n
        reponse.append(icount)
    elif n == 4:
        icount = 'IV'
        reponse.append(icount)
    elif n == 5:
        icount = 'V'
        reponse.append(icount)
    elif 6 <= n < 9:
        icount = 'V' + 'I' * (n - 5)
        reponse.append(icount)
    else:
        icount = 'IX'
        reponse.append(icount)
    return ''.join(reponse)


print(solution(1005))
