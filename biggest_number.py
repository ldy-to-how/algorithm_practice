answer = ''
number = "4177252841"
k = 4
t_max = 0

for idx in range(len(number)):
    if k > 0:
        if idx == len(number) - 1:
            break
        else:
            current = int(number[idx])
            next = int(number[idx+1])

            if current > t_max:
                t_max = current
                if len(answer) > k:
                    answer = answer[:-k]
                    k = 0
                elif len(answer) == k:
                    answer = ''
                    k = 0
                    pass
                else:
                    k -= len(answer)
                    answer = ''
                    

            if current >= next:
                answer += str(current)
            else:
                k -= 1
    else:
        answer += number[idx:]
        break

print(answer)