def lengthOfLastWord(s):
    s = s.rstrip()
    last_space = 0
    words_count = 0
    for c in range(0, len(s)):
        if ' ' not in s:
            last_space = -1
            break
        else:
            if s[c] ==  " ":
                last_space = c

    for i in range(last_space + 1, len(s)): 
        words_count += 1

    return words_count

print(lengthOfLastWord(str(input("Sentence: "))))
