"Example calling Swi-Prolog N-Queens program from Python"

from swiplserver import PrologMQI
from pprint import pprint

with PrologMQI() as mqi:
  with mqi.create_thread() as prolog_thread:
    prolog_thread.query("use_module(library(clpfd)).")
    prolog_thread.query("[n_queens].")
    result = prolog_thread.query("n_queens(8, Qs), label(Qs).")
    pprint(result)
    print(len(result))

