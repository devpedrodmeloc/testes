# 📄 Download e Compactação de PDFs do site da ANS

Este projeto tem como objetivo baixar especificamente os anexos I e II em formato PDF da página da ANS (Agência Nacional de Saúde Suplementar) e compactá-los em um arquivo ZIP automaticamente.

## 🛠 Requisitos Técnicos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos atendidos:

- Python 3.7 ou superior instalado
- Pip (gerenciador de pacotes do Python) atualizado
- Dependências do projeto instaladas

## 📥 Instalação das Dependências

Antes de rodar o script, instale as bibliotecas necessárias executando o seguinte comando no terminal:

```sh
pip install requests beautifulsoup4
```

## 🚀 Como Executar o Script

1. Clone ou baixe este repositório para seu computador:

```sh
git clone https://github.com/devpedrodmeloc/testes
```

2. Navegue até a pasta do projeto:

```sh
cd testes/teste_scraping
```

3. Execute o script Python:

```sh
python main.py
```

## 📦 O que o Script Faz?

1. Acessa a página da ANS.
2. Filtra os links dos PDFs desejados (Anexo I e Anexo II).
3. Faz o download dos arquivos.
4. Compacta os PDFs baixados em um arquivo ZIP chamado `anexos_rol.zip`.

## 📂 Estrutura dos Arquivos

```
/
├── main.py  # Código principal do projeto
├── README.md  # Instruções de uso
```
