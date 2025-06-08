answer_catalog = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}

while True:
    c = int(input("How much questions are? "))
    count_answ = 0
    count_marks = 0
    count_255 = 0
    answer = ""

    if c == 0:
        break

    for n in range(0, c):
        answers = str(input("Question Input: ")).split()
        count_answ = 0
        count_marks = 0
        asnwer = ""

        for i in answers:
            i = int(i)
            
            if i <= 127:
                answer = answer_catalog[count_answ]
                count_marks += 1
            if i > 127:
                count_answ += 1

        if count_marks == 1:
            print(answer)
        else:
            print("*")