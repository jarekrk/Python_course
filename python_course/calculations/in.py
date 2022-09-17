import calculations.calclulations

def ask(message):
    input_val=input(message)
    return int(input_val)

start1 = ask("kwotanastart")
procent1 = ask("najakiprocent")
okres1 = ask("jakiokreslat")

koniec=calculations.calclulations.final(start1, procent1, okres1)
print(f" final wynik to to {koniec:.2f} zl")
