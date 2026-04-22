import sys
from PyQt6.QtWidgets import QApplication
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Problem:
    title: str
    category: str
    prompt: str
    starter_code: str
    function_name: str
    tests: List[Dict[str, Any]]

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()