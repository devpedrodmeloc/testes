import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile, ZIP_DEFLATED
from urllib.parse import urljoin


url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'


arquivos_desejados = [
    "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]


def obter_links_pdf(url, arquivos_desejados):
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    links_pdf = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        for nome_arquivo in arquivos_desejados:
            if nome_arquivo in href:  
                full_url = urljoin(url, href)
                links_pdf.append(full_url)

    return links_pdf


def download_pdf(url, nome_arquivo):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        with open(nome_arquivo, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo {nome_arquivo} baixado com sucesso!")
        return True
    except requests.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return False


def compactar_em_zip(nome_arquivos, nome_zip):
    with ZipFile(nome_zip, 'w', compression=ZIP_DEFLATED) as zipf:
        for arquivo in nome_arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
            os.remove(arquivo)  
    print(f"Arquivos compactados em {nome_zip}")


def main():
    print("Buscando links para os PDFs Anexo I e II...")
    links_pdf = obter_links_pdf(url, arquivos_desejados)

    if not links_pdf:
        print("Nenhum link de PDF correspondente encontrado.")
        return

    arquivos_baixados = []
    for link in links_pdf:
        nome_arquivo = os.path.basename(link)  
        if download_pdf(link, nome_arquivo):
            arquivos_baixados.append(nome_arquivo)
    
    if arquivos_baixados:
        compactar_em_zip(arquivos_baixados, "anexos_rol.zip")
    else:
        print("Nenhum arquivo foi baixado com sucesso.")

if __name__ == '__main__':
    main()
