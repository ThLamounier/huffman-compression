from __future__ import annotations

from pathlib import Path
from typing import List

DEFAULT_TEXTS: List[str] = [
    "O computador executa instruções em alta velocidade e processa dados com precisão.",
    "A memória armazena informações que são acessadas rapidamente pela CPU.",
    "Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador.",
    "O dado é um dado bruto. O processador processa o dado e gera informação. A informação é um dado processado. O dado processado é útil.",
    "A memória rápida é cara. A memória lenta é barata. A CPU usa a memória rápida. O disco é memória lenta. A memória rápida ajuda a CPU.",
    "O sistema controla o processo. O processo usa o recurso. O sistema libera o recurso para o processo. O sistema é o controlador do processo.",
]


def parse_input_file(input_path: Path) -> List[str]:
    """
    Lê o arquivo de entrada e devolve os blocos separados por linhas em branco.
    """
    if not input_path.exists():
        return []

    texts: List[str] = []
    current_lines: List[str] = []

    for line in input_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "" and current_lines:
            texts.append(" ".join(current_lines))
            current_lines = []
        elif stripped:
            current_lines.append(stripped)

    if current_lines:
        texts.append(" ".join(current_lines))

    return texts


def ensure_data_dir(data_dir: Path) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)


def write_report(output_path: Path, content: str) -> None:
    output_path.write_text(content, encoding="utf-8")
