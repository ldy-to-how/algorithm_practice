answer = ''
number = "4177252841"
k = 4

while k != 0:
    if k == 1:
        if int(number[0]) < int(number[1]):
            answer += number[1:]
        else:
            answer += (number[0] + number[2:])
        k = 0
    else:
        max = 0
        temp = 0
        for i in range(k):
            if int(number[i]) > max:
                max = int(number[i])
                temp = i
        number = number[temp+1:]
        answer += str(max)
        k -= temp

print(answer)