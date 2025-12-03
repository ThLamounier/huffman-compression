from __future__ import annotations

from typing import Iterable, List

from core import CompressionResult


def _format_frequency(result: CompressionResult) -> List[str]:
    lines = ["[Frequência das Palavras]"]
    for word, freq in result.frequencies:
        lines.append(f"  {word}: {freq}")
    return lines


def _format_codes(result: CompressionResult) -> List[str]:
    lines = ["[Tabela de Códigos]:"]
    for word, code in sorted(result.codes.items(), key=lambda item: (len(item[1]), item[0])):
        lines.append(f"  {word}: {code}")
    return lines


def _format_tree(result: CompressionResult) -> List[str]:
    lines = ["[Estrutura Visual da Árvore de Huffman]:", "(Raiz no Topo | 0 = Esquerda | 1 = Direita)\n"]
    lines.extend(result.tree_lines)
    return lines


def _format_block(index: int, result: CompressionResult) -> str:
    section: List[str] = [f"--- TEXTO {index} ---", f"Original: {result.text}", ""]
    section.extend(_format_frequency(result))
    section.append("")
    section.extend(_format_codes(result))
    section.append("")
    section.extend(_format_tree(result))
    section.append("")
    section.append("[Texto Comprimido]:")
    section.append(result.binary_final if result.binary_final else "")
    section.append("-" * 40)
    return "\n".join(section)


def generate_report(results: Iterable[CompressionResult]) -> str:
    blocks = [_format_block(idx, result) for idx, result in enumerate(results, start=1)]
    return "\n\n".join(blocks)
