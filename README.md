<div>
<h1>Validador de CPF em Python</h1>
</div>

### O que é:
Este é um simples validador de CPF em Python. Ele permite que você verifique se um número de CPF é válido ou não.
##

### <h1>Como funciona:</h1>

 Exemplo: Cálculo dos Dígitos Verificadores de um CPF

 CPF: 108.016.490-13

Para calcular os dígitos verificadores do CPF fornecido, siga os passos abaixo:

### Cálculo do Primeiro Dígito Verificador

1. **Multiplicação e Soma:**
   - Multiplique cada um dos 9 primeiros dígitos do CPF pelos valores correspondentes de uma contagem regressiva começando de 10.
   - Exemplo:
     ```
     10 9 8 7 6 5 4 3 2 
      1 0 8 0 1 6 4 9 0 
     10 0 64 0 6 30 16 27 0 
     ```
   - Some todos os resultados: 10 + 0 + 64 + 0 + 6 + 30 + 16 + 27 + 0 = 153
   
2. **Cálculo do Resto:**
   - Multiplique o resultado anterior por 10: 153 * 10 = 1530
   - Obtenha o resto da divisão da conta anterior por 11: 1530 % 11 = 1
   
3. **Verificação do Primeiro Dígito:**
   - Se o resto for maior que 9, o primeiro dígito é 0. Caso contrário, é o próprio valor do resto.
   - Neste exemplo, o primeiro dígito do CPF é 1.

### Cálculo do Segundo Dígito Verificador

1. **Multiplicação e Soma:**
   - Multiplique os 10 primeiros dígitos do CPF pelos valores correspondentes de uma contagem regressiva começando de 11.
   
2. **Cálculo do Resto:**
   - Some todos os resultados e multiplique por 10.
   - Obtenha o resto da divisão da conta anterior por 11.
   
3. **Verificação do Segundo Dígito:**
   - Se o resto for maior que 9, o segundo dígito é 0. Caso contrário, é o próprio valor do resto.
   - Neste exemplo, o segundo dígito do CPF é 3.

Este é um exemplo de como calcular os dígitos verificadores de um CPF. Os passos descritos podem ser aplicados para qualquer CPF.

##

### Contribuição:
Se você gostaria de contribuir com melhorias para este validador de CPF, sinta-se à vontade para abrir uma issue ou enviar uma solicitação de pull request. Todas as contribuições são bem-vindas!
##

### Contato:
GitHub: Alexandre-Cunha <br>
Email: alexandrebarreto853@gmail.com
