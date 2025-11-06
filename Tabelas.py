import matplotlib.pyplot as plt

#1 Tendência de Estoque Diário
dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.figure(figsize=(8, 5))
plt.plot(dias, estoque)
plt.title('Tendência de Estoque Diário')
plt.xlabel('Dia')
plt.ylabel('Quantidade em Estoque')
plt.grid(True)
plt.show()

#2 Comparação de Produtos
produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

plt.figure(figsize=(8, 5))
plt.bar(produtos, quantidades)
plt.title('Comparação de Produtos em Estoque')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()

#3 Proporção de Categorias
categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]

plt.figure(figsize=(8, 5))
plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Proporção de Valor por Categoria')
plt.show()

#4 Preço vs. Quantidade
precos = [50, 120, 300, 80, 20]
estoque_produtos = [80, 25, 10, 70, 150]

plt.figure(figsize=(8, 5))
plt.scatter(precos, estoque_produtos)
plt.title('Preço vs. Quantidade em Estoque')
plt.xlabel('Preço Unitário (R$)')
plt.ylabel('Quantidade em Estoque')
plt.grid(True)
plt.show()
