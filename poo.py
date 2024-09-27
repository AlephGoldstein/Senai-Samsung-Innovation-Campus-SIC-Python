numero_conta = ""
titular = ''
saldo = 1111
limite = 3500

conta = {'numero_conta': '11515158', 'titular':'João', 'saldo' : 1111}
def criar_conta(numero_conta,titular,saldo,limite):
    conta = {"numero":numero_conta,'titular':titular,"saldo":saldo,"limite":limite}
    return conta
conta1 = criar_conta(125154,"jorge",1500,5000)
conta2 = criar_conta(125154,"jorge",1500,5000)
def extrato(conta):
    print("numero: {}\n saldo: {}".format(conta['numero'],conta['saldo']))
    return conta['saldo']
def deposito(conta,valor):
    ValorConta = extrato(conta)
    ValorConta += valor
    print("seu valor agora é ",ValorConta)
    conta['saldo'] = ValorConta


