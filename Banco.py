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
    def __init__(self,agencia,conta,saldo,tipo_conta,cliente,limite=1000):
        self._agencia=agencia
        self._conta=conta
        self._saldo=saldo
        self._limite=limite
        self._tipo_conta=tipo_conta.title()
        self._cliente=cliente
    
    def extrato(self):
        print(f'``\nAgencia: {self._agencia}\nConta: {self._conta}\nSaldo: R${self._saldo}\n´´')
    
    def __str__(self):
        return f'´´\nAgencia: {self._agencia}\nConta: {self._conta}\n{self._cliente}\n``'
    
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel=(self._saldo+self._limite)
        return valor_a_sacar<=valor_disponivel
    
    def sacar(self,valor):
        if (self.__pode_sacar(valor)):
            self._saldo-=valor
            print('Saque Realizado com Sucesso!!!')
        else:
            print('Saldo Indisponivel para Saque!!!')
            
    def depositar(self,valor):
        self._saldo+=valor
        
    def tranfere(self, valor, destino):
        if(self.__pode_sacar(valor)):
            self.sacar(valor)
            destino.depositar(valor) 
            print(f'Transferencia de {valor} para {destino}')
        else:
            print('Saldo Insuficiente para a Transferencia!!!')
    
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
Vitor=Cliente('vitor vieira freire','15599007766','28/10/2003','Masculino')    
Nian=Cliente('nian freire','2112121212','10/02/2003','Masculino')

Conta0=Conta(1001,2212125,2330,'poupança',Nian)
Conta1=Conta(1001,1000235,20,'corrente',Vitor)

""" print(Conta0)
Conta0.extrato()
Conta0.depositar(100)
Conta0.extrato()
Conta0.limite=10000
print(Conta0.titular)
print(Conta0.limite)
Conta0.tranfere(1000000,Conta1) """

print(Conta1)
Conta1.extrato()
Conta1.sacar(6000)
Conta1.sacar(200)
Conta1.extrato()