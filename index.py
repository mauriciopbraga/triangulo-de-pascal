def coeficienteBinominal(n, k): 
    resolucao = 1
    if (k > n - k): 
        k = n - k 
    for i in range(0, k): 
        resolucao = resolucao * (n - i) 
        resolucao = resolucao // (i + 1) 
      
    return resolucao 

def exibirPascal(n): 
    for linha in range(0, n): 
        for i in range(0, linha + 1): 
            print(coeficienteBinominal(linha, i), " ", end = "") 
        print() 

numeroLinhas = int(input("Digite o número de linhas: "))
exibirPascal(numeroLinhas) 