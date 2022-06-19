contador_total = 1

empresa = str(input('Escreva o nome da empresa: '))
num_funcionarios = int(input('Informe o número de funcionários da empresa: '))
contador_isentos = 0.0

while contador_total <= num_funcionarios:
    nome_fun = str(input('Informe o nome do(a) funcionário(a)'))
    horas_trab = int(input('Informe o número de horas trabalhadas: '))
    categoria = int(input('Informe a categoria do(a) funcionário(a) (1,2 ou 3): '))

    if horas_trab > 160:
        horas_extra = horas_trab - 160
    else:
        horas_extra = 0
    
    if categoria == 1:
        valor_hora = 15.00
    elif categoria == 2:
        valor_hora = 30.00
    else:
        valor_hora = 50.00
    
    #cálculo do salário bruto e das horas extra, caso existam.
    salario_bruto = (horas_trab - horas_extra) * valor_hora + horas_extra * (valor_hora + valor_hora * 0.5)

    #cálculo para o total de salários brutos da empresa
    total_brutos = 0.0
    total_brutos = total_brutos + salario_bruto

    #cálculo para média de salários brutos
    media_brutos = total_brutos / contador_total

    #cálculo de desconto do INSS
    salario_inss = salario_bruto - (salario_bruto * 0.08)
    inss = salario_bruto - salario_inss
    print("----------------------------------------")
    
    #cálculo do imposto de renda e contador de isentos
    

    if salario_inss <= 2500:
        desconto_ir = 0.0
        contador_isentos += 1
    
    elif salario_inss > 2500 and salario_inss <=5000:
        desconto_ir = salario_inss * 0.1
    
    elif salario_inss > 5000 and salario_inss <=8000:
        desconto_ir = salario_inss * 0.2
    
    else:
        desconto_ir = salario_inss * 0.3

    #cálculo do salário líquido
    salario_liquido = salario_inss - desconto_ir

    #cálculo do menor salário líquido 
    if contador_total == 1:
        menor_liquido = salario_liquido
        nome_menor = nome_fun
        categoria_menor = categoria
    
    elif menor_liquido > salario_liquido:
        menor_liquido = salario_liquido
        nome_menor = nome_fun
        categoria_menor = categoria
    
    #cálculo do maior salário líquido
    maior_liquido = 0.0 

    while maior_liquido < salario_liquido:
        maior_liquido = salario_liquido
        nome_maior = nome_fun
        categoria_maior = categoria

    #código para ficha do funcionário
    print(f"\nNome: ", nome_fun," categoria: ", categoria,"\nSalário Bruto: R$", salario_bruto,"\nDesconto do INSS: R$", inss, "\nDesconto do Imposto de Renda: R$", desconto_ir, "\nSalário Líquido: R$", salario_liquido,"\n----------------------------------------\n")

    contador_total += 1

    #cálculo do percentual de isentos
    percentual_isentos = contador_isentos / num_funcionarios * 100

    #Tabela Final com dados gerais da empresa
    print(f"\nEmpresa: ", empresa,
        "\nTotal de salários brutos: R$", total_brutos, 
        "\nMédia dos salários brutos: R$",media_brutos, 
        "\nPercentual de funcionários isentos: ", percentual_isentos,"%", 
        "\n----------------------------------------",
        "\nMenor salário líquido: ",menor_liquido, "\nNome: ",nome_menor,"\nCategoria: ", categoria_menor,
        "\n----------------------------------------",
        "\nMaior salário líquido: ", maior_liquido, "\nNome: ", nome_maior, "\nCategoria ", categoria_maior,
        "\n----------------------------------------")

    #resposta = print("\nDeseja executar para outra empresa S/N?","\n")
    print("\n----------------------------------------\n")