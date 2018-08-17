disciplinas = [
    [{"nome": "LTP1"},
     {"João": 2.5, "Maria": 8.9, "José": 6.7}],
    [{"nome": "Compiladores"},
     {"João": 6.2, "Maria": 10, "José": 2.1, "Mario": 6.9}],
    [{"nome": "Tópicos Especiais"},
     {"Maria": 9.2, "José": 9.1, "Mario": 5.5}]
]

a = input("Qual o nome do aluno?")
for notas in disciplinas:
    aluno = a
    disciplina = notas[0]
    nome_aluno = notas[1]
    if aluno in nome_aluno.keys():
        nome_disciplina = notas[0]["nome"]
        nota = notas[1][a]
        print('Disciplina:', nome_disciplina)
        def calcular_mencao(nota):
            if nota >= 9:
                mencao = ' SS'
            elif nota >= 7:
                mencao = 'MS'
            elif nota >= 5:
                mencao = 'MM'
            elif nota >= 3:
                mencao = 'MI'
            elif nota > 0:
                mencao = 'II'
            else:
                mencao = 'SR'
            return  mencao
        print("Menção:", calcular_mencao(nota))

