import random
from datetime import datetime

"""
Gera uma lista de números aleatórios, calcula a paridade de cada um, introduz
erros aleatórios nos valores, grava todos os ficheiros resultantes e identifica
as linhas onde a paridade mudou.
"""

def bit_paridade(n):
    return bin(n).count("1") % 2


random.seed(datetime.now().timestamp())

k = random.randint(51, 64)  

nums = []
for _ in range(k):
    nums.append(random.randint(0, 127))


pars = []
for n in nums:
    pars.append(bit_paridade(n))



with open("numeros.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")

with open("paridade.txt", "w") as f:
    for p in pars:
        f.write(str(p) + "\n")



nums_err = nums.copy()

for i in range(len(nums_err)):
    if random.random() < 0.3:  
        b = random.randint(0, 7)  
        nums_err[i] ^= (1 << b)  



with open("numeros_erro.txt", "w") as f:
    for n in nums_err:
        f.write(str(n) + "\n")



pars_err = []
for n in nums_err:
    pars_err.append(bit_paridade(n))

with open("paridade_erro.txt", "w") as f:
    for p in pars_err:
        f.write(str(p) + "\n")


print("erros:")

for i in range(k):
    if pars[i] != pars_err[i]:
        print(f"linha {i+1} -> {nums[i]} virou {nums_err[i]}")