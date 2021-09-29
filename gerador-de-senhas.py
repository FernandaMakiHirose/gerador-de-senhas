import random, string

password_length = int(input('Digite o tamanho da senha desejada: '))

# gera senhas maiúsculas e minúsculas com os tipos definidos abaixo
characters = string.ascii_letters + string.digits + '!@#$%&*()-+,.;?ç'

# gera números aleatórios fornecidos
rnd = random.SystemRandom()

# faz o print da senha
print(''.join(rnd.choice(characters) for i in range(password_length)))

