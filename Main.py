from Threads import *

class Memoria:
  def __init__(self):
    self.memoriaFisi = [None, None, None, None]
    self.memoriaVirtu = [None, None, None, None, None, None, None, None]

memoria = Memoria()

listaUmPosicao =  [2,   4,   5,   6]
listaUmOp = ["1", "3", "0", "R"]

listaDoisPosicao = [9,   0,   3,   4]
listaDoisOp = ["7", "R", "8", "1"]

if __name__ == "__main__":
  for i in range(len(listaDoisPosicao)):
    thread1 = willcareca("Thread1", memoria, listaUmPosicao[i], listaUmOp[i])
    thread1.start()
