import Banco

print("####Banco Python####")
print("Faça seu Registro")
nome=input("Insira seu nome: ")
cpf=int(input("Insira seu CPF: "))
nascimento=input("Data de Nascimento: ")
sexo=input("Masculino(M), Feminino(F) ou Outro(O):")
if sexo.upper()=='M':
    sexo='Masculino'
elif sexo.upper()=='F':
    sexo='Feminino'
else:
    sexo='Outro'

cliente=Banco.Cliente(nome,cpf,nascimento,sexo)
conta=Banco.Conta(1001,2212125,2330,'poupança',cliente,'senha123')

while True:
    print("Faça sua escolha:\n1-Extrato\n2-Saque\n3-Deposito\n4-Transferencia\n5-Sair")
    resposta=int(input(">>"))
    if resposta==1:
        Banco.Conta.extrato(conta)
    elif resposta==2:
        senha=input("Insira sua senha: ")
        valor=int(input("Insira o valor para o saque: "))
        Banco.Conta.sacar(conta,valor,senha)
    elif resposta==3:
        valor=int(input("Insira o valor para ser depositado: "))
        Banco.Conta.depositar(conta,valor)
    elif resposta==4:
        valor=int(input("Insira o valor para ser transferido: "))
        senha=input("Insira a sua senha: ")
        agencia_destino=int(input("Insira a agencia do destinatario: "))
        conta_destino=int(input("Insira a conta do destinatario: "))
        destino=Banco.Conta
        Banco.Conta.tranfere(conta,valor,destino)
    else:
        break