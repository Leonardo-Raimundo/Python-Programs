def e_primo(num):
    divisor = num - 1
    while divisor > 2:
        if num % divisor == 0:
            return False
        divisor = divisor -1
    return True

num = int(input('Informe um número: '))

#excluindo todos os nums pares que não são 2, pois são divisíveis por ele. 2 é primo, só dividido por ele e por 1.
if num % 2 == 0 and num > 2 or num == 1:
    print(f'{num} não é primo.')

elif num == 2:
    print(f'{num} é primo.')
    
else:
    if e_primo(num) == True:
        print('É primo')
    else:
        print('Não é primo')
    
    