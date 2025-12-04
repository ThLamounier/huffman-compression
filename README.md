# Huffman Compression Report

Ferramenta em Python que analisa textos em português, calcula sua codificação pelo algoritmo de Huffman e gera um relatório completo (no console e no arquivo `data/output.dat`) contendo frequências de palavras, tabela de códigos, visualização da árvore e texto comprimido.

---

## Sumário

1. [Requisitos](#requisitos)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Fluxo Geral de Execução](#fluxo-geral-de-execução)
4. [Preparando as Entradas](#preparando-as-entradas)
5. [Como Executar](#como-executar)
6. [Arquivos e Funções Principais](#arquivos-e-funções-principais)
7. [Saída Gerada](#saída-gerada)
8. [Personalizações](#personalizações)

---

## Requisitos

- **Python** 3.10 ou superior.
- Opcional, mas recomendado: ambiente virtual (`python3 -m venv .venv` e `source .venv/bin/activate` no Linux/macOS ou `.venv\Scripts\activate` no Windows PowerShell).
- Nenhuma dependência externa além da biblioteca padrão.

---

## Estrutura do Projeto

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

## Fluxo Geral de Execução

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

## Preparando as Entradas

1. Crie o diretório `data/` na raiz do projeto (se ainda não existir).
2. Edite `data/input.dat` com os textos desejados. Utilize uma linha em branco (`\n\n`) para separar cada trecho.

Exemplo de `input.dat`:

```
Texto 1 linha 1.
Texto 1 linha 2.

Outro bloco qualquer.
```

Se você deixar o arquivo vazio, os textos padrão serão utilizados automaticamente.

---

## Como Executar

Dentro da raiz do projeto:

```bash
python3 src/huffman_compression.py
```

Saída esperada no terminal (resumida):

```
--- TEXTO 1 ---
Original: O computador executa instruções ...
...
[Texto Comprimido]:
1100...
----------------------------------------

Relatório salvo em /caminho/do/projeto/data/output.dat
```

O arquivo `data/output.dat` conterá o mesmo conteúdo mostrado no console, podendo ser compartilhado ou inspecionado depois.

---

## Arquivos e Funções Principais

### `src/huffman_compression.py`
- `load_texts(input_path)`: tenta carregar `input.dat`; em caso de ausência, usa `DEFAULT_TEXTS`.
- `process_blocks(texts)`: aplica `compress_text_block` para cada bloco de texto.
- `main()`: organiza o fluxo completo (leitura, processamento, geração do relatório e escrita em disco).

### `src/core.py`
- `Node`: representa um nó da árvore de Huffman (folha com palavra ou nó interno com frequência acumulada).
- `build_huffman_tree(frequency_dict)`: cria a árvore a partir de um dicionário de frequências usando `heapq`.
- `generate_codes(node)`: percorre a árvore recursivamente e mapeia cada palavra para seu código binário.
- `build_tree_lines(root)`: gera a representação textual da árvore conforme o layout clássico.
- `compress_text_block(text)`: ponto central do módulo; normaliza o texto, calcula frequências e primeira ocorrência, monta a árvore, gera códigos e retorna um `CompressionResult` contendo tudo o que o relatório precisa.

### `src/reporting.py`
- `_format_frequency`, `_format_codes`, `_format_tree`: helpers que formatam cada seção do relatório.
- `_format_block(index, result)`: produz a estrutura completa de um texto (cabeçalho, frequências, códigos, árvore e binário).
- `generate_report(results)`: concatena todos os blocos com uma linha separadora.

### `src/storage.py`
- `DEFAULT_TEXTS`: lista de seis textos padrão usados caso `input.dat` não esteja disponível.
- `parse_input_file(input_path)`: faz a leitura do arquivo de entrada e retorna uma lista de blocos.
- `ensure_data_dir(data_dir)`: cria o diretório `data/` caso não exista.
- `write_report(output_path, content)`: escreve o relatório em `output.dat`.

---

## Saída Gerada

Cada bloco tem o seguinte formato:

```
--- TEXTO N ---
Original: <texto normalizado>

[Frequência das Palavras]
  palavra: contagem
  ...

[Tabela de Códigos]:
  palavra: código
  ...

[Estrutura Visual da Árvore de Huffman]:
(Raiz no Topo | 0 = Esquerda | 1 = Direita)
<desenho ASCII>

[Texto Comprimido]:
<sequência binária>
----------------------------------------
```

Ao final do relatório completo, o script imprime `Relatório salvo em output.dat` indicando o caminho completo do arquivo.

---

## Personalizações

- **Textos padrão**: altere a lista `DEFAULT_TEXTS` em `src/storage.py` para definir novos exemplos.
- **Formatação do relatório**: edite as funções em `src/reporting.py` para incluir novas métricas ou alterar o layout (por exemplo, adicionar estatísticas de compressão ou remover o desenho da árvore).
- **Divisão de tokens**: atualmente o algoritmo usa `str.split()` (palavras separadas por espaço). Para tratar pontuação de outra forma, adapte a lógica em `core.compress_text_block`.
- **Integração com outros sistemas**: o módulo `core` devolve objetos `CompressionResult`, permitindo que você use os dados em outras interfaces (GUI, APIs etc.) sem depender do formato textual.

---

Com isso, o projeto está pronto para ser executado, adaptado e estudado. Se quiser ampliar o sistema, considere adicionar testes automatizados, exportação do relatório em outros formatos (JSON/HTML) ou uma etapa de decomposição para validar a reversibilidade da compressão. Divirta-se explorando Huffman!
