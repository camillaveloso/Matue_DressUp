import pickle

#Função para salvar os dados do jogo
def salvar_progresso(indice_blusa, indice_calca, indice_tenis):
    dados = {
        "indice_blusa": indice_blusa,
        "indice_calca": indice_calca,
        "indice_tenis": indice_tenis
    }
    with open("progresso_jogo.pkl", "wb") as arquivo:
        pickle.dump(dados, arquivo)

#Função para carregar os dados do jogo
def carregar_progresso():
    try:
        with open("progresso_jogo.pkl", "rb") as arquivo:
            dados = pickle.load(arquivo)
            indice_blusa = dados["indice_blusa"]
            indice_calca = dados["indice_calca"]
            indice_tenis = dados["indice_tenis"]
    except FileNotFoundError:
        #Se o arquivo não existir, retorna os índices padrão
        indice_blusa = 0
        indice_calca = 0
        indice_tenis = 0
    return indice_blusa, indice_calca, indice_tenis
