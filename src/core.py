from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class Node:
    """
    Nó da árvore de Huffman.
    """

    frequency: int
    word: Optional[str] = field(compare=False, default=None)
    left: Optional["Node"] = field(compare=False, default=None)
    right: Optional["Node"] = field(compare=False, default=None)

    def __lt__(self, other: "Node") -> bool:
        return self.frequency < other.frequency


@dataclass
class CompressionResult:
    text: str
    frequencies: List[Tuple[str, int]]
    codes: Dict[str, str]
    tree_lines: List[str]
    binary_final: str


def build_huffman_tree(frequency_dict: Dict[str, int]) -> Optional[Node]:
    """
    Constrói a árvore de Huffman usando uma fila de prioridade.
    """
    priority_queue: List[Node] = []
    for word, freq in frequency_dict.items():
        heapq.heappush(priority_queue, Node(freq, word=word))

    if len(priority_queue) == 1:
        node = heapq.heappop(priority_queue)
        priority_queue.append(Node(node.frequency, left=node))

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged = Node(left_child.frequency + right_child.frequency, left=left_child, right=right_child)
        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None


def build_tree_lines(root: Optional[Node]) -> List[str]:
    """
    Constroi representação horizontal com conectores alinhados.
    """

    if root is None:
        return []

    def _render(node: Optional[Node]):
        if node is None:
            return [], 0, 0, 0

        label = f'"{node.word}"' if node.word else f"[{node.frequency}]"
        left_lines, left_w, left_h, left_mid = _render(node.left)
        right_lines, right_w, right_h, right_mid = _render(node.right)

        if left_w == 0 and right_w == 0:
            width = len(label)
            return [label], width, 1, width // 2

        gap = 2
        total_width = left_w + right_w + gap
        start = left_mid + 1
        end = left_w + gap + right_mid
        connector_len = end - start
        connector = (
            " " * start
            + "/"
            + "-" * (connector_len - 1)
            + "\\"
            + " " * (total_width - end - 1)
        )

        parent_mid = (start + end) // 2
        label_len = len(label)
        label_offset = parent_mid - (label_len // 2)
        extra_pad = 0
        if label_offset < 0:
            extra_pad = -label_offset
            label_offset = 0

        first_line = " " * label_offset + label
        second_line = " " * extra_pad + connector
        block_width = max(len(first_line), len(second_line), total_width + extra_pad)

        first_line = first_line.ljust(block_width)
        second_line = second_line.ljust(block_width)
        lines = [first_line, second_line]

        for idx in range(max(left_h, right_h)):
            l_line = left_lines[idx] if idx < left_h else " " * left_w
            r_line = right_lines[idx] if idx < right_h else " " * right_w
            lines.append((" " * extra_pad + l_line + " " * gap + r_line).ljust(block_width))

        return lines, block_width, len(lines), parent_mid + extra_pad

    rendered, _, _, _ = _render(root)
    return rendered


def generate_codes(node: Optional[Node], prefix: str = "", code_map: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    if code_map is None:
        code_map = {}

    if node is not None:
        if node.word is not None:
            code_map[node.word] = prefix or "0"
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)

    return code_map


def compress_text_block(text: str) -> CompressionResult:
    """
    Processa um texto e devolve as informações necessárias para o relatório legado.
    """
    normalized = text.replace("\n", " ").strip()
    words = normalized.split()

    freq_dict: Dict[str, int] = {}
    first_occurrence: Dict[str, int] = {}
    for idx, word in enumerate(words):
        freq_dict[word] = freq_dict.get(word, 0) + 1
        if word not in first_occurrence:
            first_occurrence[word] = idx

    root = build_huffman_tree(freq_dict)
    codes = generate_codes(root)
    binary_final = "".join(codes[word] for word in words) if words else ""

    ordered_freq = sorted(
        freq_dict.items(),
        key=lambda item: (-item[1], first_occurrence[item[0]]),
    )

    tree_lines = build_tree_lines(root)

    return CompressionResult(
        text=normalized,
        frequencies=ordered_freq,
        codes=codes,
        tree_lines=tree_lines,
        binary_final=binary_final,
    )
