#Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que aceita cartões de crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior conforme a quantidade de parcelas que o cliente desejar

print("Pedro Ryan Magalhães's Store")

#valor do pedido em float por poder ter virgula
valorDoPedido = float(input("Qual valor do pedido? R$  "))
quantidadeDeParcelas = int(input("Qual quantidade de parcelas?  "))

if quantidadeDeParcelas < 4:
    print (f"Valor total de R${valorDoPedido} e Sem Juros")

#somando o valor do pedido com o valor do juros se tem o valor novo que sera parcelado

elif 4 <= quantidadeDeParcelas < 6:
    valorComJuros = (valorDoPedido + (valorDoPedido * 4/100))
    valorDaParcela = (valorComJuros / quantidadeDeParcelas)
    print (f"Valor com juros é de R${valorComJuros} e as parcelas ficam R${valorDaParcela}")
elif 6 >= quantidadeDeParcelas < 9:
    valorComJuros = (valorDoPedido + (valorDoPedido * 8/100))
    valorDaParcela = (valorComJuros / quantidadeDeParcelas)
    print (f"Valor com juros é de R${valorComJuros} e as parcelas ficam R${valorDaParcela}")
elif 9 >= quantidadeDeParcelas < 13:
    valorComJuros = (valorDoPedido + (valorDoPedido * 16/100))
    valorDaParcela = (valorComJuros / quantidadeDeParcelas)
    print (f"Valor com juros é de R${valorComJuros} e as parcelas ficam R${valorDaParcela}")
else:
    valorComJuros = (valorDoPedido + (valorDoPedido * 32/100))
    valorDaParcela = (valorComJuros / quantidadeDeParcelas)
    print (f"Valor com juros é de {valorComJuros} e as parcelas ficam {valorDaParcela}")
##