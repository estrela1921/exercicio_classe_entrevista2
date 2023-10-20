class Entrevistado:
    def __init__(self, idade, cidade, estado, salario_atual, escolaridade):
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.salario_atual = salario_atual
        self.escolaridade = escolaridade

    def imprimirDados(self):
        dados = f"{self.idade},{self.cidade},{self.estado},{self.salario_atual},{self.escolaridade}"
        return dados

# Exemplo de uso da classe:
entrevistado = Entrevistado(30, "São Paulo", "SP", 5000, "Ensino Superior Completo")
dados_entrevistado = entrevistado.imprimirDados()
print(dados_entrevistado)

class Pesquisa:
    def __init__(self, nome):
        self.nome = nome
        self.listaEntrevistados = []

    def adicionarEntrevistado(self, entrevistado):
        self.listaEntrevistados.append(entrevistado)

    def imprimirEntrevistados(self):
        for entrevistado in self.listaEntrevistados:
            dados_entrevistado = entrevistado.imprimirDados()
            print(dados_entrevistado)

# Exemplo de uso das classes:
entrevistado1 = Entrevistado(30, "São Paulo", "SP", 5000, "Ensino Superior Completo")
entrevistado2 = Entrevistado(25, "Rio de Janeiro", "RJ", 4000, "Ensino Médio Completo")

pesquisa = Pesquisa("Pesquisa de Emprego")
pesquisa.adicionarEntrevistado(entrevistado1)
pesquisa.adicionarEntrevistado(entrevistado2)

print("Entrevistados na pesquisa:")
pesquisa.imprimirEntrevistados()

