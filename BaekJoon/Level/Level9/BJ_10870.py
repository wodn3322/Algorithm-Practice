def solution():
    num = int(input())

    def fibonaci(n):
        if n >= 2:
            return fibonaci(n - 1) + fibonaci(n - 2)
        else:
            return n
        return

    answer = fibonaci(num)
    print(answer)

    return

    
if __name__ == '__main__':
    solution()
