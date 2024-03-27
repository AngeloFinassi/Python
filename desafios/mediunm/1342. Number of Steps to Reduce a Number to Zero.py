num = 14
cont_step = 0

while num != 0:
    if num % 2 == 0:
        num = num / 2
    else:
        num = num - 1
    cont_step += 1

#botar o cont_step fora dos ifs aumentou 4 vezes o tempo do processamento???
#desde quando diminuir linha de cosdigo e fz a msm coisa resulta em demorar mais wtfffff????
print(cont_step)
