# programmers 해시 - 전화번호 목록

def solution(phone_book):
    phone_book = sorted(phone_book, key = lambda x : len(x),reverse = True)
    answer = True
    while answer == True : 
        if len(phone_book) == 1 : 
            break
        for i in phone_book[:-1] : 
            if phone_book[-1] == i[:len(phone_book[-1])] : 
                answer = False
                break
        phone_book.pop()
        print(phone_book)
    return answer