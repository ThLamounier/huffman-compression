"""
Este trecho contem a organização do fluxo principal, consumindo funções
definidas no próprio diretório ``src``.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

from core import compress_text_block
from storage import DEFAULT_TEXTS, ensure_data_dir, parse_input_file, write_report
from reporting import generate_report


def load_texts(input_path: Path) -> List[str]:
    """
    Lê os textos do arquivo ou devolve os exemplos padrão, exibindo um aviso.
    """
    texts = parse_input_file(input_path)
    if texts:
        return texts

    print("Aviso: arquivo input.dat não encontrado. Utilizando textos de exemplo internos.\n")
    return DEFAULT_TEXTS


def process_blocks(texts: List[str]):
    """
    Aplica a compressão Huffman em cada trecho.
    """
    return [compress_text_block(text) for text in texts]


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"
    input_path = data_dir / "input.dat"
    output_path = data_dir / "output.dat"

    texts = load_texts(input_path)
    results = process_blocks(texts)
    report = generate_report(results)

    print(report)
    ensure_data_dir(data_dir)
    write_report(output_path, report)
    print(f"Relatório salvo em {output_path}")


if __name__ == "__main__":
    main()
