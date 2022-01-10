from threading import Thread
from time import sleep
import Main

class willcareca(Thread):
  def __init__(self, nomeThread, memoria, memoVirtualPosi, valorOp):
    Thread.__init__(self)
    self.nome = nomeThread
    self.memoria = memoria
    self.memoVirtualPosi = memoVirtualPosi
    self.valorOp = valorOp

  def run(self):

    # print('iniciou a thread')