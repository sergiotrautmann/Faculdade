#criando classe no python
class Televisao:
    #definição de caracteristicas(atributos) da classe
    canal = 0
    ligada = False

    #metodo construtor
    def __init__(self, canal, ligada):
        self.canal = canal
        self.ligada = ligada
    #metodo para mudar de canal
    def mudar_canal(self, canal):
        #procedimento para mudar de canal
        #verificar se a tv esta ligada
        if self.ligada:
            self.canal = canal
    #metodo para ligar a tv
    def ligar_tv(self):
        self.ligada = True
    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1
    def diminuir_canal(self):
        if self.ligada & self.canal > 0:
            self.canal -= 1

#criar(instanciar) objetos com base na classe Televisao
tv_sala = Televisao(5, True)
print(tv_sala.ligada)
tv_quarto = Televisao(2, True)
print(tv_quarto.ligada)
tv_sala.ligar_tv()
tv_sala.mudar_canal(10)
tv_sala.aumentar_canal()
print(tv_sala.canal)
tv_sala.diminuir_canal()
print(tv_sala.canal)