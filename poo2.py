from poo import criar_conta,deposito

conta = criar_conta(1285154,"tonine",1560,5000)
deposito(conta,15)
print(conta['saldo'])