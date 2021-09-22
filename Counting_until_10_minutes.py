minuto = 0
segundo = 0

for i in range(601):
    print(minuto,":",segundo)

    if segundo == 59 and minuto < 10:
        segundo = 0
        minuto += 1
    else:
        segundo += 1
