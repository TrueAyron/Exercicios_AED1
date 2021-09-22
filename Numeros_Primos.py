#Variaveis e listas que vão ser usadas no codigo
n = int(input())
x = False
num = []
loop = 0

#Aqui estamos pegando a variavel n (que leu o numero que sera utilizado como maximo) e fazendo uma lista de numeros igual a (1, 2, 3,..., n) 
#Tambem observamos se o numero esta entre 0 e 300, como requisitado no exercicio
if n < 300 and n > 0:
    while loop <= n:
        for i in range(n):
            num.append(int(loop))
            loop += 1
        break
#Aqui é utilizado uma formula matematica para ver se um numero é primo e sempre que for primo ele vai printar
    for i in num:
        #esse if foi feito pois esses 3 numeros acabam por serem muito pequenos e não se aplicam na formula
        if i == 2 or i == 3 or i == 5:
            print(i)
        else:
            ehprimo = False
            for z in range(2, int(i / 2)):
                if (i % z) == 0:
                    ehprimo = False
                    break
                else:
                    ehprimo = True
            if ehprimo:
                print(i)
else:
    print("O numero deve ser maior que 0 e menor que 300")
