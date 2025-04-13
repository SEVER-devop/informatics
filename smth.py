
for i in range(int(input()[1:])):
    text = input()
    for i in range(len(text)):
        if text[i] == "#":
            for j in range(i-1, 0, -1):
                print(j, i)
                if text[j] != ' ':
                    i = j
                    break
            text = text[:i+1]
            break
    p = 0
    for i in range(len(text)-1, -1, -1):
        if text[i] == " ":
            p = i
        else:
            if p == 0:
                p = len(text)
            break
    print(text[:p])
        
    