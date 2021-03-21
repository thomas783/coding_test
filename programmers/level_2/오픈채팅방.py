# Programmers_level_2_오픈채팅방

def solution(record) :
    r = [i.split(' ') for i in record]
    chat = []
    result = []
    finalname = dict()
    for i in range(len(r)) : 
        if r[i][0] == 'Enter' : 
            finalname[r[i][1]] = r[i][2]
            chat.append([r[i][1],'님이 들어왔습니다.'])
        elif r[i][0] == 'Leave' : 
            chat.append([r[i][1],'님이 나갔습니다.'])
        elif r[i][0] == 'Change' : 
            finalname[r[i][1]] = r[i][2]
    for c in chat : 
        result.append(finalname[c[0]]+c[1])
    return result