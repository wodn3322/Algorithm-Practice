def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            answer = False
            return answer
    return answer


if __name__ == '__main__':
    book = ["119", "97674223", "1195524421"]
    solution(book)
