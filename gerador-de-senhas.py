import random, string

tamanho = int(input('Digite o tamanho da senha desejada: '))

# gera senhas maiúsculas e minúsculas com os tipos definidos abaixo
caracteres = string.ascii_letters + string.digits + '!@#$%&*()-+,.;?ç'

# gera números aleatórios fornecidos
rnd = random.SystemRandom()

# faz o print da senha
print(''.join(rnd.choice(caracteres) for i in range(tamanho)))

