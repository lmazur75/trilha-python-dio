# Projeto Trilha Python DIO

from datetime import datetime, time, date

def deposito(saldo: float):
    global operacoes
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    valor_deposito = float(input('Digite o valor a ser depositado: R$ '))
    while True:
        if valor_deposito < 0:
            valor_deposito = float(input('Valor invalido! Digite o valor a ser depositado: R$ '))
        else:
            transacao = {'operacao': 'deposito', 'valor': valor_deposito, 'data_hora': data_hora}
            operacoes.append(transacao)
            return valor_deposito
            break


def saque(saldo: float):
    global operacoes, numero_transacoes, limite_transacoes
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    limite = 500
    valor_saque = float(input('Digite o valor a ser sacado: R$ '))
    while True:
        if numero_transacoes >= limite_transacoes:
            print('Voce excedeu o numero de transacoes diarias!')
            return 0
            break
        elif valor_saque > limite:
            valor_saque = float(input('Valor acima do limite! Digite o valor a ser sacado: R$ '))
        elif valor_saque > saldo:
            valor_saque = float(input('Valor acima do saldo disponível! Digite o valor a ser sacado: R$ '))
        else:
            numero_transacoes += 1
            transacao = {'operacao': 'deposito', 'valor': valor_saque, 'data_hora': data_hora}
            operacoes.append(transacao)
            return valor_saque
            break


def extrato(operacoes: list, saldo: float):
    for key, value in enumerate(operacoes):
        print(f'{value['data_hora']} - Operacao: {value['operacao']} - valor: R$ {value['valor']:.2f}')
    print(f'\nSaldo atual: R$ {saldo:.2f}\n')

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
                valor_operacao = deposito(saldo)
                saldo += valor_operacao
            case 's':
                valor_operacao = saque(saldo)
                saldo -= valor_operacao
            case 'e':
                extrato(operacoes, saldo)
            case 'q':
                break
            case _:
                print('Opcao invalida ! Digite uma das opcoes disponiveis.')