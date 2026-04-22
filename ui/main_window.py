from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QListWidget,
    QTextEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QMessageBox,
    QListWidgetItem,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QBrush

from problems.problem_bank import PROBLEMS
from utils.runner import execute_user_code, run_problem_tests
from utils.progress import mark_completed, is_completed_today, get_streak


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("datastructure-master")
        self.resize(1350, 800)

        self.current_problem = None

        self.setup_ui()
        self.apply_styles()
        self.load_problem_list()
        self.update_streak_label()

        if PROBLEMS:
            self.problem_list.setCurrentRow(0)

    def setup_ui(self):
        self.sidebar_title = QLabel("Problems")
        self.sidebar_title.setObjectName("sidebarTitle")

        self.problem_count_label = QLabel(f"{len(PROBLEMS)} total problems")
        self.problem_count_label.setObjectName("sidebarSubtext")

        self.streak_label = QLabel("Daily Streak: 0 days")
        self.streak_label.setObjectName("streakLabel")

        self.problem_list = QListWidget()
        self.problem_list.setMinimumWidth(320)
        self.problem_list.currentRowChanged.connect(self.load_problem)

        self.header_title = QLabel("datastructure-master")
        self.header_title.setObjectName("headerTitle")

        self.header_subtitle = QLabel("Practice interview-style Python problems with instant feedback.")
        self.header_subtitle.setObjectName("headerSubtitle")

        self.problem_title_label = QLabel("Select a problem")
        self.problem_title_label.setObjectName("problemTitle")

        self.problem_category_label = QLabel("")
        self.problem_category_label.setObjectName("problemCategory")

        self.prompt_label = QLabel("Choose a problem from the list to begin.")
        self.prompt_label.setWordWrap(True)
        self.prompt_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.prompt_label.setObjectName("promptBox")

        self.editor_label = QLabel("Code Editor")
        self.editor_label.setObjectName("sectionLabel")

        self.editor = QTextEdit()
        self.editor.setFont(QFont("Consolas", 11))
        self.editor.setPlaceholderText("Your starter code will appear here...")

        self.run_button = QPushButton("Run Tests")
        self.run_button.clicked.connect(self.run_tests)

        self.reset_button = QPushButton("Reset Code")
        self.reset_button.clicked.connect(self.reset_code)

        self.output_label = QLabel("Output")
        self.output_label.setObjectName("sectionLabel")

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setFont(QFont("Consolas", 10))

        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.sidebar_title)
        sidebar_layout.addWidget(self.problem_count_label)
        sidebar_layout.addWidget(self.streak_label)
        sidebar_layout.addWidget(self.problem_list)

        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)

        header_layout = QVBoxLayout()
        header_layout.addWidget(self.header_title)
        header_layout.addWidget(self.header_subtitle)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addSpacing(8)
        main_layout.addWidget(self.problem_title_label)
        main_layout.addWidget(self.problem_category_label)
        main_layout.addWidget(self.prompt_label)
        main_layout.addWidget(self.editor_label)
        main_layout.addWidget(self.editor, stretch=3)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_label)
        main_layout.addWidget(self.output_box, stretch=2)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        splitter = QSplitter()
        splitter.addWidget(sidebar_widget)
        splitter.addWidget(main_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 4)
        splitter.setSizes([340, 1010])

        container = QWidget()
        container_layout = QHBoxLayout()
        container_layout.setContentsMargins(12, 12, 12, 12)
        container_layout.addWidget(splitter)
        container.setLayout(container_layout)

        self.setCentralWidget(container)

    def load_problem_list(self):
        self.problem_list.clear()

        for problem in PROBLEMS:
            item = QListWidgetItem(f"{problem.category} • {problem.title}")
            self.problem_list.addItem(item)

        self.update_problem_colors()

    def update_problem_colors(self):
        current_row = self.problem_list.currentRow()

        for i, problem in enumerate(PROBLEMS):
            item = self.problem_list.item(i)

            if item is None:
                continue

            completed_today = is_completed_today(problem.title)
            is_selected = i == current_row

            if completed_today and is_selected:
                bg = QColor("#22c55e")   # bright green
                fg = QColor("#04130a")
            elif completed_today:
                bg = QColor("#166534")   # dark green
                fg = QColor("#dcfce7")
            elif is_selected:
                bg = QColor("#16a34a")   # selected but incomplete
                fg = QColor("#f0fdf4")
            else:
                bg = QColor("#08100a")   # default
                fg = QColor("#bbf7d0")

            item.setBackground(QBrush(bg))
            item.setForeground(QBrush(fg))

        self.problem_list.viewport().update()

    def update_streak_label(self):
        streak = get_streak()
        if streak == 1:
            self.streak_label.setText("Daily Streak: 1 day")
        else:
            self.streak_label.setText(f"Daily Streak: {streak} days")

    def load_problem(self, index: int):
        if index < 0 or index >= len(PROBLEMS):
            return

        self.current_problem = PROBLEMS[index]
        self.problem_title_label.setText(self.current_problem.title)
        self.problem_category_label.setText(f"Category: {self.current_problem.category}")
        self.prompt_label.setText(self.current_problem.prompt)
        self.editor.setPlainText(self.current_problem.starter_code)
        self.output_box.clear()
        self.update_problem_colors()

    def reset_code(self):
        if not self.current_problem:
            return

        self.editor.setPlainText(self.current_problem.starter_code)
        self.output_box.setPlainText("Code reset to starter template.")

    def run_tests(self):
        if not self.current_problem:
            QMessageBox.warning(self, "No Problem", "Please select a problem first.")
            return

        user_code = self.editor.toPlainText()
        execution_result = execute_user_code(user_code)

        if not execution_result["success"]:
            error_text = "Your code has a syntax/runtime error before tests could run.\n\n"
            if execution_result["stdout"]:
                error_text += f"Console Output:\n{execution_result['stdout']}\n\n"
            error_text += execution_result["error"]
            self.output_box.setPlainText(error_text)
            return

        final_result = run_problem_tests(self.current_problem, execution_result["namespace"])

        output_parts = []
        if execution_result["stdout"]:
            output_parts.append("Console Output:")
            output_parts.append(execution_result["stdout"])
            output_parts.append("")

        output_parts.append(final_result["output"])
        self.output_box.setPlainText("\n".join(output_parts))

        total = len(self.current_problem.tests)
        if final_result["success"] and f"{total}/{total}" in final_result["output"]:
            mark_completed(self.current_problem.title)
            self.update_problem_colors()
            self.update_streak_label()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #050807;
            }

            QWidget {
                background-color: #050807;
                color: #ecfdf5;
                font-size: 14px;
            }

            QLabel#headerTitle {
                font-size: 30px;
                font-weight: bold;
                color: #bbf7d0;
                padding-bottom: 2px;
            }

            QLabel#headerSubtitle {
                font-size: 14px;
                color: #86efac;
                padding-bottom: 10px;
            }

            QLabel#sidebarTitle {
                font-size: 22px;
                font-weight: bold;
                color: #dcfce7;
                padding-bottom: 2px;
            }

            QLabel#sidebarSubtext {
                font-size: 13px;
                color: #86efac;
                padding-bottom: 4px;
            }

            QLabel#streakLabel {
                font-size: 14px;
                font-weight: bold;
                color: #dcfce7;
                background-color: #0f2e1b;
                border: 1px solid #22c55e;
                border-radius: 10px;
                padding: 8px;
                margin-bottom: 8px;
            }

            QLabel#problemTitle {
                font-size: 28px;
                font-weight: bold;
                color: #dcfce7;
                padding-top: 6px;
            }

            QLabel#problemCategory {
                font-size: 13px;
                color: #4ade80;
                padding-bottom: 8px;
            }

            QLabel#sectionLabel {
                font-size: 15px;
                font-weight: bold;
                color: #bbf7d0;
                padding-top: 8px;
                padding-bottom: 4px;
            }

            QLabel#promptBox {
                background-color: #0b120d;
                border: 1px solid #166534;
                border-radius: 12px;
                padding: 14px;
                color: #ecfdf5;
                margin-bottom: 8px;
            }

            QListWidget {
                background-color: #08100a;
                border: 1px solid #14532d;
                border-radius: 12px;
                padding: 8px;
                outline: none;
            }

            QListWidget::item {
                border: none;
                padding: 10px;
                margin-bottom: 4px;
            }

            QTextEdit {
                background-color: #08100a;
                border: 1px solid #14532d;
                border-radius: 12px;
                padding: 10px;
                color: #ecfdf5;
                selection-background-color: #166534;
                selection-color: #f0fdf4;
            }

            QPushButton {
                background-color: #16a34a;
                color: #f0fdf4;
                border: none;
                border-radius: 10px;
                padding: 10px 16px;
                font-weight: bold;
                min-width: 120px;
            }

            QPushButton:hover {
                background-color: #15803d;
            }

            QPushButton:pressed {
                background-color: #166534;
            }

            QSplitter::handle {
                background-color: #14532d;
                width: 2px;
            }
        """)