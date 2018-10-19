from pessoa import Pessoa
from Funcionario import Funcionario
from Professor import Professor
from estudante import Estudante
p1 = Pessoa('João', '123', 20)
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
print(p1)
f1 = Funcionario('José', '456', 40, '0099', 2526.45, 'Biblioteca')
print(f1)
t1 = Professor('Bila', '789', 50, '0100', 3000, 'Gastronomia', 'Degustação')
e1 = Estudante('Rafael', '017', 22, '1717', 'Ciência da Computação', 'Quarto semestre')
print(t1)

print(e1)