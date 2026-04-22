# 📘 DS Practice Tool (Python)

A desktop-based coding practice IDE designed to help prepare for technical interviews by focusing on core data structures and algorithms.

This tool provides a structured environment where users implement fundamental concepts such as linked lists, sorting algorithms, stacks, queues, and more — all in Python.

---

## 🚀 Features

- 🧠 **Interview-Focused Problems**
  - Practice common topics like:
    - Linked Lists
    - Sorting Algorithms (Bubble Sort, etc.)
    - Binary Search
    - Stacks & Queues

- 💻 **Built-in Code Editor**
  - Write and test Python code directly inside the app

- ✅ **Automated Test Runner**
  - Run your code against predefined test cases
  - Get instant feedback (pass/fail, expected vs actual output)

- 🔁 **Reset Functionality**
  - Quickly reset to starter code for each problem

- 🧪 **Realistic Practice Flow**
  - Mimics interview-style coding questions with constraints and structure

---

## 🛠️ Tech Stack

- **Language:** Python  
- **GUI Framework:** PyQt  
- **Execution Engine:** Python `exec()` for dynamic code evaluation  
- **Architecture:** Modular problem + test engine system  

---

## 📂 Project Structure


.
├── main.py # Entry point (GUI + logic)
├── problems/ # Problem definitions (future expansion)
├── engine/ # Test runner logic (future expansion)
└── README.md


---

## ⚙️ Installation & Setup

1. Clone the repository:

git clone https://github.com/your-username/ds-practice-tool.git

cd ds-practice-tool


2. Install dependencies:

pip install PyQt6


3. Run the app:

python main.py


---

## 🧠 Example Problem

### Bubble Sort

```python
def bubble_sort(arr):
    arr = arr[:]
    # Your code here
    return arr
Sample Output
Test 1: Passed
Test 2: Failed
Expected: [1,2,3]
Got: [2,1,3]
Result: 1/2 tests passed.
```

🙌 Author

Om Sathe
Computer Science Student @ Ontario Tech University
GitHub: https://github.com/OmSathe
