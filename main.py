from threading import Thread, Lock
from time import sleep

memoFisica =  [2, 4, 5, 6, 10, 15, 7, 22]

threadUmOp = ["1", "3", "0", "R"]

threadDoisOp = ["7", "R", "8", "1"]

syncronized = Lock()

class Memoria:
  def lerMemo(self, posicao):
    print(f'Valor {memoFisica[posicao]} na {posicao+1}º posicao da memoria fisica')
    print ("------>>>>", memoFisica)
  
  def escreverMemo(self, posicao, novoValor):
    novoValor = int(novoValor)
    print(f' O Valor  {memoFisica[posicao]} na {posicao+1}º posicao da memoria fisica será substituído por {novoValor}')
    memoFisica[posicao] = novoValor
    novoValorT = int(novoValor)
    print ("------|||||", memoFisica)

memoria = Memoria()

class thread(Thread):
  
  def __init__(self, nomeThread, memoria,  memoVirtualPosi, threadOp):
    Thread.__init__(self)
    self.nome = nomeThread
    self.memoria = memoria
    self.memoVirtualPosi = memoVirtualPosi
    self.threadOp = threadOp

  def run(self):
    syncronized.acquire()
    if self.threadOp == "R":
        print('Comando recebido de leitura')
        self.memoria.lerMemo(self.memoVirtualPosi)
        
    else:
        print('Comando recebido de escrita')
        self.memoria.escreverMemo(self.memoVirtualPosi, self.threadOp)
        if self.nome == "Thread1":
            threadUmOp[self.memoVirtualPosi]= self.threadOp
        else:
            threadDoisOp[self.memoVirtualPosi]= self.threadOp
    syncronized.release()

if __name__ == "__main__":
  print(memoFisica)
  for index in range(len(threadUmOp)):
    # mudar nome da thread
    thread("Thread1", memoria, index, threadUmOp[index]).start()
    # sleep(3)
    thread("Thread2", memoria, index, threadDoisOp[index]).start()
