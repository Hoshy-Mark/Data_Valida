print("digite as seguintes informações: ")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

mes31 = (1, 3, 5, 7, 8, 10, 12)
mes30 = (4, 6, 9, 11)

if(ano <= 2022):
    if(mes <= 12):
            if(mes == 2):
                if(dia <= 28):
                    float(dia)
                    float(mes)
                    float(ano)
                    data = print("{:02.0f}/{:02.0f}/{:04.0f}".format(dia, mes, ano))
                else:
                    print("Dia inválido")
            elif(mes in mes31):
                if(dia  <= 31):
                    float(dia)
                    float(mes)
                    float(ano)
                    data = print("{:02.0f}/{:02.0f}/{:04.0f}".format(dia, mes, ano))
                else:
                    print("Dia inválido")
            elif(mes in mes30):
                if(dia  <= 30):
                    float(dia)
                    float(mes)
                    float(ano)
                    data = print("{:02.0f}/{:02.0f}/{:04.0f}".format(dia, mes, ano))
                else:
                    print("Dia inválido")
            else:
                print("Mês inválido")
else:
    print("Ano inválido")
                    
