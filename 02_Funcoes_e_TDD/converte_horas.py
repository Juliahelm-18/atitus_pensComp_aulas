def hora_para_minuto(valor):
    pass
    return valor * 60

def minuto_para_segundo(valor):
    pass
    return valor * 60

def hora_para_segundo(valor):
    pass
    return valor * 60 * 60

def dias_para_segundos(valor):
    pass
    return valor * 24 * 60 * 60 

assert hora_para_minuto(0) == 0
assert hora_para_minuto(1) == 60
assert hora_para_minuto(2) == 120

assert minuto_para_segundo(0) == 0
assert minuto_para_segundo(1) == 60
assert minuto_para_segundo(2) == 120

assert hora_para_segundo(0) == 0
assert hora_para_segundo(1) == 3600  # 1 * 60 * 60
assert hora_para_segundo(2) == 7200  # 2 * 60 * 60

assert dia_para_segundo(0) == 0
assert dia_para_segundo(1) == 86.400
assert dia_para_segundo(2) == 172.800

print("Terminou com sucesso!")
