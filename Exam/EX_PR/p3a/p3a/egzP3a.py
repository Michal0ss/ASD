from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    #tutaj proszę wpisać własną implementację
    return 0

runtests(wybory, all_tests = True)