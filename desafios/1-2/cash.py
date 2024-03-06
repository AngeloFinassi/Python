cont_20 = cont_10 = cont_5 = cont_1 = 0
print("=-" * 30)
credit = int(input("Troco: "))
while credit > 0:
    if credit >= 20:
        credit -= 20
        cont_20 += 1
    else:
        if credit >= 10:
            credit -= 10
            cont_10 += 1
        else:
            if credit >= 5:
                credit -= 5
                cont_5 += 1
            else:
                if credit >= 1:
                    credit -= 1
                    cont_1 += 1
print("=-" * 30)
print(f"Credit: 20:{cont_20}, 10:{cont_10}, 5:{cont_5}, 1:{cont_1}")
print(f"Total: {cont_20 +  cont_10 + cont_5 + cont_1} papers")
