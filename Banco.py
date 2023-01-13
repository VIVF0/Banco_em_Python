class Cliente:
    def __init__(self,nome,cpf,ano_nascimento,sexo):
        self._nome=nome.title()
        self._cpf=cpf
        self.ano_nascimento=ano_nascimento
        self.sexo=sexo
    
    def __str__(self):
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nAno de Nascimento: {self.ano_nascimento}\nSexo: {self.sexo}'
    
class Conta(Cliente):
    def __init__(self,agencia,conta,saldo,tipo_conta,cliente,limite=1000):
        self._agencia=agencia
        self._conta=conta
        self._saldo=saldo
        self._limite=limite
        self._tipo_conta=tipo_conta.title()
        self._cliente=cliente
    
    def extrato(self):
        print(f'Saldo: {self._saldo}')
    
    def __str__(self):
        return f'Agencia: {self._agencia}\nConta: {self._conta}\n{self._cliente}'
    
Vitor=Cliente('vitor','15599007766','28/10/2003','Masculino')    
    
Conta1=Conta(1001,1000235,20,'corrente',Vitor)

print(Conta1)