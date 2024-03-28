fibonacci = [0, 1]
numero = input("insira o numero a ser verificado")

while fibonacci[-1] < int(numero):
    length = len(fibonacci)
    new_number = fibonacci[length - 1] + fibonacci[length - 2]
    fibonacci.append(new_number)
    
if int(numero) in fibonacci:
    print("o numero esta na sequencia de fibonacci")
else:
    print("o numero não pertence a sequencia de fibonacci")
    
