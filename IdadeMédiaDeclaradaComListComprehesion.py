qtde_familiares  = int(input('Insira a quantidade de familiares'))
nome_familiares  = [input(f'Insira o nome do {q + 1}º familiar.').title().strip() for q in range(qtde_familiares)]
idade_familiares = [int(input(f'Insira a idade de {nome_familiares[r]}')) for r in range(len(nome_familiares))]
dicio_familia    = dict(zip(nome_familiares, idade_familiares))

print(f'{"Detalhes da Família":^23}')
print('='*23)
for nome, idade in dicio_familia.items():
    print(f'|{nome:^10}|{idade:^6}anos|')

print('='*23)

idade_media_familiar = round(sum(idade_familiares) / len(idade_familiares))
print(f'Idade Média:{idade_media_familiar:^11}')
