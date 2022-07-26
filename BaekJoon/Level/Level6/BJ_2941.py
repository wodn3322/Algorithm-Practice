def solution():
    inputString = input()

    crotiaAlphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    alphabetCount = 0
    for i in crotiaAlphabet:
        if inputString.count(i) != 0:
            alphabetCount += inputString.count(i)
            inputString = inputString.replace(i, '_')
    alphabetCount += len(list(inputString.replace('_', '')))
    print(alphabetCount)
    return


if __name__ == '__main__':
    solution()
