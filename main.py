import sys

cpf_validar = input('Digite um CPF: ').replace('.', '') \
    .replace('-', '') \
    .replace(' ', '')  

entrada_sequencial = cpf_validar == cpf_validar[0] * len(cpf_validar)

if entrada_sequencial:
    print('CPF inválido')
    print('Você digitou dados sequenciais')
    sys.exit()

nove_digitos = cpf_validar[:9]
multiplicador_regressivo1 = 10

resultado_digito1 = 0
for digito in nove_digitos:
    resultado_digito1 += int(digito) * multiplicador_regressivo1
    multiplicador_regressivo1 -= 1

digito_1 = (resultado_digito1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'O primeiro digito do CPF é {digito_1}')

dez_digitos = cpf_validar[:10]
multiplicador_regressivo2 = 11

resultado_digito2 = 0
for digito in dez_digitos:
    resultado_digito2 += int(digito) * multiplicador_regressivo2
    multiplicador_regressivo2 -= 1

digito_2 = (resultado_digito2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O segundo digito do CPF é {digito_2}')

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_validar == cpf_gerado_pelo_calculo:
    print(f'O CPF {cpf_validar} é Válido')
else:
    print(f'O CPF {cpf_validar} é Inválido')