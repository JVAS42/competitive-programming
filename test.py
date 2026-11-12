dia_1 = {"ana@email.com", "bruno@email.com", "carla@email.com"}
dia_2 = {"bruno@email.com", "daniel@email.com", "carla@email.com"}

questao1_letraA = dia_1 & dia_2 # Interção A e B
questao1_letraB = dia_1 - dia_2

print(questao1_letraA)
print(questao1_letraB)