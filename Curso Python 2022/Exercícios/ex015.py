#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A
#QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O
#CARRO CUSTA R$60 POR DUA E R$0,15 POR KM RODADO.
dia = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
pago = (dia * 60) + (km + 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))  