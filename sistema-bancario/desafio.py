# Projeto Trilha Python DIO

def deposito(saldo: float):
    valor_deposito = float(input('Digite o valor a ser depositado: R$ '))
    while True:
        if valor_deposito < 0:
            valor_deposito = float(input('Valor invalido! Digite o valor a ser depositado: R$ '))
        else:
            return valor_deposito
            break


def saque(saldo: float, numero_saques: int):
    limite = 500
    limite_saques = 3
    valor_saque = float(input('Digite o valor a ser sacado: R$ '))
    while True:
        if valor_saque > limite:
            valor_saque = float(input('Valor acima do limite! Digite o valor a ser sacado: R$ '))
        if numero_saques >= limite_saques:
            print('Quantidade máxima de saques atingida! Volte amanhã !')
            break
        if valor_saque > saldo:
            valor_saque = float(input('Valor acima do saldo disponível! Digite o valor a ser sacado: R$ '))
        else:
            numero_saques += 1
            return (valor_saque, numero_saques)
            break


def extrato(operacoes: list, valores: list, saldo: float):
    for i in range(len(operacoes)):
        print(f'Operacao: {operacoes[i]} - valor: R$ {valores[i]:.2f}')
    print(f'Total depositos: R$ {total_depositos:.2f} - Total saques: R$ {total_saques:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}\n')


if __name__ == '__main__':
    saldo = 0
    numero_saques = 0
    operacoes = []
    valores = []
    total_depositos = total_saques = 0
    while True:
        op = input('Digite a opção desejada: \n'
                   '(d) Deposito\n'
                   '(s) Saque\n'
                   '(e) Extrato\n'
                   '(q) Sair\n').strip().lower()
        match op:
            case 'd':
                operacoes.append('deposito')
                valor_operacao = deposito(saldo)
                valores.append(valor_operacao)
                total_depositos += valor_operacao
                saldo += valor_operacao
            case 's':
                operacoes.append('saque')
                (valor_operacao, numero_saques) = saque(saldo, numero_saques)
                valores.append(valor_operacao)
                total_saques += valor_operacao
                saldo -= valor_operacao
            case 'e':
                extrato(operacoes, valores, saldo)
            case 'q':
                break
            case _:
                print('Opcao invalida ! Digite uma das opcoes disponiveis.')

