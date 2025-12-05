from __future__ import annotations

from pathlib import Path
from typing import List

DEFAULT_TEXTS: List[str] = [
    "O gato pulou sobre a mesa procurando um pedaço de queijo invisível.",
    "Nuvens roxas dançavam no céu enquanto o vento assobiava feliz.",
    "Robôs antigos colecionavam sonhos quebrados em uma caixa de metal.",
    "A biblioteca secreta só aparecia quando alguém esquecia o próprio nome.",
    "Relógios derretidos marcavam horas que nunca haviam existido.",
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
