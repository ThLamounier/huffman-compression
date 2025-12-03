"""
Pacote com os componentes reutilizáveis do projeto de compressão de Huffman.
"""

from .core import CompressionResult, Node, build_huffman_tree, compress_text_block
from .io import DEFAULT_TEXTS, ensure_data_dir, parse_input_file, write_report
from .reporting import generate_report

__all__ = [
    "CompressionResult",
    "Node",
    "build_huffman_tree",
    "compress_text_block",
    "DEFAULT_TEXTS",
    "ensure_data_dir",
    "parse_input_file",
    "write_report",
    "generate_report",
]
