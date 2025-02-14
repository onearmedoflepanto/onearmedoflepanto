s = input()

sum_total = 0

i=0

while i < len(s):
    if s[i] == '[':
        j = s.find(']',i)

        num = int(s[i+1:j])
        sum_total += num

        i = j +1

    elif s[i] == '{':
        j = s.find('}', i)
        
        num = int(s[i+1:j])
        sum_total *= num
        
        i = j +1

    else:
        i += 1

print(sum_total)