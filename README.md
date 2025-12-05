<h1 align="center">
  <br>
  🗜️ Huffman Algorithm
  <br>
</h1>

<h4 align="center">Implementação de compressão de dados com base em árvores binárias e filas prioritárias.</h4>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/status-Completed-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/course-Algorithms-orange?style=for-the-badge">
</p>

<p align="center">
  <a href="#-introdução">Introdução</a> •
  <a href="#-requisitos">Requisitos</a> •
  <a href="#-estrutura">Estrutura</a> •
  <a href="#-fluxo-Geral">Fluxo Geral</a> •
  <a href="#-entradas">Entradas</a> •
  <a href="#-como-Executar">Como Executar</a> •
  <a href="#-funções">Funções</a> •
  <a href="#-tecnologias">Tecnologias</a> • 
  <a href="#-autor">Autor</a> 
</p>

## 📖Introdução

- O Algoritmo de Huffman é um método clássico de compressão sem perdas baseado na construção de códigos binários de tamanho variável. A ideia central dete trabalho é atribuir códigos mais curtos aos símbolos(neste trabalho, palavras) mais frequentes e códigos mais longos aos menos frequentes, reduzindo o tamanho total da representação do texto.

- A construção deste programa nao se baseia somente na demonstração dos codigos gerados, mas tambem na visualização da estrutura(Huffman Tree), permitindo melhor avaliação e entendimento.
---

## 📑Requisitos

- **Python** 3.10 ou superior.
- **Opcional**, mas recomendado: ambiente virtual (copie e cola no terminal): (`python3 -m venv .venv` e `source .venv/bin/activate` no Linux/macOS ou `.venv\Scripts\activate` no Windows PowerShell).
- Nenhuma dependência externa além da biblioteca padrão.

---

## 🗂Estrutura

```
.
├── data/
│   ├── input.dat      # Textos a serem comprimidos (separados por linha em branco)
│   └── output.dat     # Relatório gerado após a execução
└── src/
    ├── core.py        # Algoritmo de Huffman e compactação de cada bloco
    ├── reporting.py   # Formatação textual do relatório
    ├── storage.py     # Entrada padrão, leitura/escrita de arquivos
    └── huffman_compression.py  # Script principal (CLI)
```

`data/input.dat` e `data/output.dat` são criados automaticamente se o diretório `data/` existir; caso `input.dat` esteja vazio ou ausente, o programa usa textos padrão definidos em `storage.py`.

---

## 🔁Fluxo Geral

1. **Leitura** (`storage.parse_input_file`):
   - O script procura `data/input.dat`.
   - Cada bloco é delimitado por uma linha em branco.
   - Se o arquivo não existir ou estiver vazio, os seis parágrafos padrão são utilizados.

2. **Processamento** (`core.compress_text_block`):
   - Normaliza o texto (remove quebras de linha internas).
   - Calcula frequências e ordem de ocorrência das palavras.
   - Constrói a árvore de Huffman (`core.build_huffman_tree`) e os códigos binários (`core.generate_codes`).
   - Gera a representação ASCII da árvore (`core.build_tree_lines`).
   - Monta o binário comprimido concatenando os códigos de cada palavra.

3. **Relatório** (`reporting.generate_report`):
   - Para cada bloco, imprime:
     - Texto original normalizado.
     - Lista completa de frequências (`[Frequência das Palavras]`).
     - Tabela de códigos ordenada pelo tamanho do código.
     - Diagrama da árvore com conectores `/` e `\`.
     - Binário final.
   - O report é exibido no console e salvo em `data/output.dat`.

---

## 📥Entradas

1. Crie o diretório `data/` na raiz do projeto (se ainda não existir).
2. Edite `data/input.dat` com os textos desejados. Utilize uma linha em branco (`\n\n`) para separar cada trecho.

Exemplo de `input.dat`:

```
A chuva cai, cai, cai forte no telhado da casa.

O gato corre rápido, mas o cachorro corre ainda mais rápido.

Sim, eu posso, porque posso tentar, posso aprender e posso melhorar.

Hoje o vento sopra leve, leve, leve, mas o frio continua forte.

Eles falaram muito, muito, muito, mas realmente não disseram nada importante.

```

Se você deixar o arquivo vazio, os textos padrão serão utilizados automaticamente.

---

## 📝Como Executar
No terminal:
```
 git clone https://github.com/ThLamounier/huffman-compression.git
 cd huffman-compression
```

Dentro da raiz do projeto:

```bash
python src/huffman_compression.py
```

Saída esperada no terminal:

```
-- TEXTO 1 ---
Original: O computador executa instruções em alta velocidade e processa dados com precisão.

[Frequência das Palavras]
  O: 1
  computador: 1
  executa: 1
  instruções: 1
  em: 1
  alta: 1
  velocidade: 1
  e: 1
  processa: 1
  dados: 1
  com: 1
  precisão.: 1

[Tabela de Códigos]:
  alta: 011
  com: 010
  dados: 000
  processa: 001
  O: 1100
  computador: 1010
  e: 1000
  em: 1011
  executa: 1101
  instruções: 1001
  precisão.: 1111
  velocidade: 1110

[Estrutura Visual da Árvore de Huffman]:
(Raiz no Topo | 0 = Esquerda | 1 = Direita)

                                            [12]                                                                    
                   /-----------------------------------------------------\                                          
                 [4]                                                    [8]                                         
          /----------------\                           /------------------------------------\                       
        [2]               [2]                        [4]                                   [4]                      
    /---------\         /------\           /----------------------\              /----------------------\           
"dados"  "processa"  "com"  "alta"       [2]                     [2]           [2]                     [2]          
                                      /--------\              /--------\     /------\             /-----------\     
                                    "e"  "instruções"  "computador"  "em"  "O"  "executa"  "velocidade"  "precisão."

[Texto Comprimido]:
11001010110110011011011111010000010000101111
----------------------------------------
Relatório salvo em /caminho/do/projeto/data/output.dat
```

O arquivo `data/output.dat` tem o mesmo conteúdo mostrado, podendo ser compartilhado ou visto depois.

---

## 📋Funções

### `src/huffman_compression.py`
- `load_texts(input_path)`: tenta carregar `input.dat`; em caso de ausência, usa `DEFAULT_TEXTS`.
- `process_blocks(texts)`: aplica `compress_text_block` para cada bloco de texto.
- `main()`: organiza o fluxo completo (leitura, processamento, geração do relatório e escrita).

### `src/core.py`
- `Node`: representa um nó da árvore de Huffman.
- `build_huffman_tree(frequency_dict)`: cria a árvore a partir de um dicionário de frequências usando `heapq`.
- `generate_codes(node)`: percorre a árvore recursivamente e mapeia cada palavra para seu código binário.
- `build_tree_lines(root)`: gera a representação textual da árvore conforme o layout clássico.
- `compress_text_block(text)`: ponto central do módulo; normaliza o texto, calcula frequências e primeira ocorrência, monta a árvore, gera códigos e retorna um `CompressionResult` contendo tudo o que o relatório precisa.

### `src/reporting.py`
- `_format_frequency`, `_format_codes`, `_format_tree`: helpers que formatam cada seção do relatório.
- `_format_block(index, result)`: produz a estrutura completa de um texto.
- `generate_report(results)`: concatena todos os blocos com uma linha separadora.

### `src/storage.py`
- `DEFAULT_TEXTS`: lista de seis textos padrão usados caso `input.dat` não esteja disponível.
- `parse_input_file(input_path)`: faz a leitura do arquivo de entrada e retorna uma lista de blocos.
- `ensure_data_dir(data_dir)`: cria o diretório `data/` caso não exista.
- `write_report(output_path, content)`: escreve o relatório em `output.dat`.

---

## 👨‍💻 Autor

<div align="center">
  <a href="https:https://github.com/ThLamounier">
   <img style="border-radius: 50%;" src="h" width="100px;" alt=""/>
   <br />
   <sub><b>ThLamounier</b></sub>
  </a>
  <br />
  <a href="https://github.com/ThLamounier" title="Rocketseat">🚀</a>
  <p>Feito por <b>Thallys</b>. Entre em contato!</p>
  
  <a href="https:www.linkedin.com/in/thallys-lamounier-aa522932b" target="_blank">
    <img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank">
  </a> 
  <a href="mailto:thallyslamounier6x1@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/-Gmail-%23D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank">
  </a>
</div>
