# Projeto Trilha Python DIO

from datetime import datetime, time, date

def deposito(saldo: float):
    valor_deposito = float(input('Digite o valor a ser depositado: R$ '))
    while True:
        if valor_deposito < 0:
            valor_deposito = float(input('Valor invalido! Digite o valor a ser depositado: R$ '))
        else:
            return valor_deposito
            break


def saque(saldo: float):
    limite = 500
    valor_saque = float(input('Digite o valor a ser sacado: R$ '))
    while True:
        if valor_saque > limite:
            valor_saque = float(input('Valor acima do limite! Digite o valor a ser sacado: R$ '))
        elif valor_saque > saldo:
            valor_saque = float(input('Valor acima do saldo disponível! Digite o valor a ser sacado: R$ '))
        else:
            return valor_saque
            break


def extrato(operacoes: list, valores: list, data_hora: list, saldo: float):
    for i in range(len(operacoes)):
        print(f'{data_hora[i]} - Operacao: {operacoes[i]} - valor: R$ {valores[i]:.2f}')
    print(f'Total depositos: R$ {total_depositos:.2f} - Total saques: R$ {total_saques:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}\n')

def check_novo_dia():
    global ultimo_dia
    dia_atual = date.today()
    return dia_atual > ultimo_dia


if __name__ == '__main__':
    saldo = 0
    numero_transacoes = 0
    limite_transacoes = 3
    ultimo_dia = date.today()
    operacoes = []
    valores = []
    data_hora = []
    total_depositos = total_saques = 0
    while True:
        op = input('Digite a opção desejada: \n'
                   '(d) Deposito\n'
                   '(s) Saque\n'
                   '(e) Extrato\n'
                   '(q) Sair\n').strip().lower()
        if check_novo_dia():
            numero_transacoes = 0
            ultimo_dia = date.today()
        match op:
            case 'd':
                numero_transacoes += 1
                if numero_transacoes > limite_transacoes:
                    print('Voce excedeu o numero de transacoes diarias!')
                    break
                operacoes.append('deposito')
                valor_operacao = deposito(saldo)
                valores.append(valor_operacao)
                data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                total_depositos += valor_operacao
                saldo += valor_operacao
            case 's':
                numero_transacoes += 1
                if numero_transacoes > limite_transacoes:
                    print('Voce excedeu o numero de transacoes diarias!')
                    break
                operacoes.append('saque')
                valor_operacao = saque(saldo)
                valores.append(valor_operacao)
                data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                total_saques += valor_operacao
                saldo -= valor_operacao
            case 'e':
                extrato(operacoes, valores, data_hora, saldo)
            case 'q':
                break
            case _:
                print('Opcao invalida ! Digite uma das opcoes disponiveis.')

