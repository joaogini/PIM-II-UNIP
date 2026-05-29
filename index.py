### Bioimpedância - Cálculo de Água Corporal, Massa Magra e Percentual de Gordura
### Este programa solicita ao usuário seus dados pessoais, como nome, idade, peso, altura e resistência, e utiliza esses dados para calcular a quantidade de água corporal, massa magra e percentual de gordura. O programa continua a solicitar novos dados até que o usuário decida encerrar.

### Variável de controle para o loop
continuar = bool(True)

### Solicitação de dados do usuário
def solicitar_dados_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso (kg): "))  
    altura = float(input("Digite sua altura (cm): "))
    resistencia = float(input("Digite sua resistência (mV): "))
    
    return {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "resistencia": resistencia
    }

### Cálcular de água corporal
def calcular_agua_corporal(altura, resistencia):
     return 0.372 * ((altura ** 2) / resistencia) + 3.05

### Cálcular de massa magra
def calcular_massa_magra(agua_corporal):
    return agua_corporal / 0.73

### Cálcular de percentual de gordura
def calcular_percentual_de_gordura(peso, massa_magra):
    return ((peso - massa_magra) / peso) * 100

### Loop principal do programa
while continuar:

    ### Solicitar dados do usuário
    dados = solicitar_dados_usuario()

    ### Realizar cálculos
    ### Cálcular da água corporal
    agua_corporal = calcular_agua_corporal(dados["altura"], dados["resistencia"])
    
    ### Cálcular da massa magra
    massa_magra = calcular_massa_magra(agua_corporal)
    
    ### Cálcular do percentual de gordura
    percentual_de_gordura = calcular_percentual_de_gordura(dados["peso"], massa_magra)

    ### Exibir resultados
    print(f"Água Corporal: {agua_corporal:.2f} L")
    print(f"Massa Magra: {massa_magra:.2f} kg")
    print(f"Percentual de Gordura: {percentual_de_gordura:.2f}%")

    ### Perguntar ao usuário se deseja continuar
    print("Deseja continuar? (s/n)")
    resposta = input().lower()
    
    ### Verificar resposta do usuário
    if resposta == "n":
        continuar = False 

