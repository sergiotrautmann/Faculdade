from datetime import date, timedelta

class Livro:
    def __init__(self, titulo, autor, editora, edicao, ano_publicacao, isbn):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn
        self.disponivel = True
        self.data_devolucao = None

    def consultar_data_devolucao(self):
        return date_devolucao

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_editora(self):
        return self.editora

    def get_edicao(self):
        return self.edicao

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def get_isbn(self):
        return self.isbn

    def disponibilidade(self):
        return self.disponivel

    def calcular_data_devolucao(self, data_emprestimo, qtd_dias):
        data_devolucao = data_emprestimo
        contador = 0
        while contador != qtd_dias:
            if data_devolucao.weekday() not in [5, 6]:
                contador += 1
            data_devolucao += timedelta(days=1)

        if data_devolucao.weekday() == 5:
            data_devolucao += timedelta(days=2)
        elif data_devolucao.weekday() == 6:
            data_devolucao += timedelta(days=1)
            self.data_devolucao = data_devolucao
        return self.data_devolucao

    def registrar_empretimo(self):
        if self.disponibilidade():
            self.disponivel = False
            data = date.today() + timedelta(days=7)
            if data.weekday() == 5:
                data -= timedelta(days=1)
            elif data.weekday() == 6:
                data -= timedelta(days=2)
            self.data_devolucao = data
            return True
        else:
            return False


    def registrar_devolucao(self):
        multa = 0
        if self.disponibilidade() is False:
            self.disponivel = True
            if date.today() > self.data_devolucao:
                dias_de_atraso = date.today() - self.data_devolucao
                multa = dias_de_atraso * 5

        self.data_devolucao = None
        return multa

livro1 = Livro('titulo', 'autor', 'editora', 2, 2018, 111)
# print(livro1.disponibilidade())
# livro1.registrar_empretimo()
# print(livro1.disponibilidade())
# livro1.registrar_devolucao()
# print(livro1.disponibilidade())
print(livro1.registrar_empretimo())
print(livro1.calcular_data_devolucao(date.today(), 6))
print(livro1.data_devolucao)
