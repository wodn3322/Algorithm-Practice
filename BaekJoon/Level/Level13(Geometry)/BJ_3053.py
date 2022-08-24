import sys,math

def solution():
    r = int(sys.stdin.readline().strip())
    sys.stdout.write(str(round(r*r*math.pi,6))+'\n')
    sys.stdout.write(str(round(r*r*2)))
    return


if __name__ == '__main__':
    solution()
