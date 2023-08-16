import Imagem as img

nome = "naturezaMorta.jpg"
dados = img.getMatrizImagemColorida(nome)

matrizR = dados[0]
matrizG = dados[1]
matrizB = dados[2]

lin = len(matrizR)
col = len(matrizR[0])
print(lin, "x", col)

for i in range(lin):
    for j in range(col):


