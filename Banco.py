class Cliente:
    def __init__(self,nome,cpf,ano_nascimento,sexo):
        self._nome=nome.title()
        self._cpf=cpf
        self.ano_nascimento=ano_nascimento
        self.sexo=sexo
    
    def __str__(self):
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nAno de Nascimento: {self.ano_nascimento}\nSexo: {self.sexo}'
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
class Conta(Cliente):
    def __init__(self,agencia,conta,saldo,tipo_conta,cliente,senha,limite=1000):
        self._agencia=agencia
        self._conta=conta
        self._saldo=saldo
        self._limite=limite
        self._tipo_conta=tipo_conta.title()
        self.__senha=senha
        self._cliente=cliente
    
    def extrato(self):
        print(f'``\nAgencia: {self._agencia}\nConta: {self._conta}\nSaldo: R${self._saldo}\n´´')
    
    def __str__(self):
        return f'´´\nAgencia: {self._agencia}\nConta: {self._conta}\n{self._cliente}\n``'
    
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel=(self._saldo+self._limite)
        return valor_a_sacar<=valor_disponivel
    
    def verifica_senha(self,senha):
        return self.__senha==senha
    
    def sacar(self,valor,senha):
        if(self.verifica_senha(senha)):
            if (self.__pode_sacar(valor)):
                self._saldo-=valor
                print('Saque Realizado com Sucesso!!!')
            else:
                print('Saldo Indisponivel para Saque!!!')
        else:
            print('##SENHA ERRADA!!! SAQUE NÃO REALIZADO##')
            
    def depositar(self,valor):
        self._saldo+=valor
        print("Deposito Realizado com Sucesso!!!")
        
    def tranfere(self, valor, destino,senha):
        if(self.verifica_senha(senha)):
            if(self.__pode_sacar(valor)):
                self.sacar(valor,senha)
                destino.depositar(valor) 
                print(f'Transferencia de R$ {valor} para {destino}')
            else:
                print('Saldo Insuficiente para a Transferencia!!!')
        else:
            print('##SENHA ERRADA!!! TRANFERENCIA NÃO REALIZADA!##')

    @property    
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._cliente.nome
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self,limite_atual):
        self._limite=limite_atual


#ZONA DE EXECUÇÃO:   
"""Vitor=Cliente('JOAO PINTO','1559905669','20/10/2011','Masculino')    
Nian=Cliente('PEDRO paulo','2112121212','18/02/2098','Masculino')

Conta0=Conta(1001,2212125,2330,'poupança',Nian,'senha123')
Conta1=Conta(1001,1000235,20,'corrente',Vitor,'senha123')

 print(Conta0)
Conta0.extrato()
Conta0.depositar(100)
Conta0.extrato()
Conta0.limite=10000
print(Conta0.titular)
print(Conta0.limite)
 

print(Conta1)
Conta1.extrato()
Conta1.sacar(6000,'senha123')
Conta1.sacar(200,'errada123')
Conta1.extrato()
Conta1.tranfere(1,Conta0,'errado')"""