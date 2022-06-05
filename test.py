def solution(n, k, cmd):
    answer = ''
    z = []
    delete_list = []
    n_ = list(range(n))
    for c in cmd:
        c = c.split()
        if c[0] == 'D':
            k+=int(c[1])
        elif c[0] == 'U':
            k-=int(c[1])
        elif c[0] == 'C':
            delete_list.append(k)
            n_.remove(k)
            if k != n:
                k += 1
            else:
                k -= 1
                
        elif c[0] == 'Z':
            if k < delete_list[-1]:
                n_.append(delete_list[-1])
            else:
                n_.append(delete_list[-1])
                n_ = sorted(n_)
                k += 1
                
            del delete_list[-1]
            
    for i in range(n):
        if i not in n_:
            answer += 'X'
        else:
            answer += 'O'
            
    return answer

a = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(a)