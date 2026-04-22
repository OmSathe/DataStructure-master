from models.problem import Problem


PROBLEMS = [
    # ---------------- SORTING ----------------
    Problem(
        title="Bubble Sort",
        category="Sorting",
        prompt=(
            "Implement bubble_sort(arr). Return a new sorted list in ascending order.\n"
            "Do not use Python's built-in sort methods."
        ),
        starter_code="""def bubble_sort(arr):
    arr = arr[:]
    # Write your code here
    return arr
""",
        function_name="bubble_sort",
        tests=[
            {"input": [3, 2, 1], "expected": [1, 2, 3]},
            {"input": [5, 1, 4, 2], "expected": [1, 2, 4, 5]},
            {"input": [], "expected": []},
            {"input": [7], "expected": [7]},
        ],
    ),
    Problem(
        title="Selection Sort",
        category="Sorting",
        prompt=(
            "Implement selection_sort(arr). Return a new sorted list in ascending order.\n"
            "Do not use Python's built-in sort methods."
        ),
        starter_code="""def selection_sort(arr):
    arr = arr[:]
    # Write your code here
    return arr
""",
        function_name="selection_sort",
        tests=[
            {"input": [64, 25, 12, 22, 11], "expected": [11, 12, 22, 25, 64]},
            {"input": [3, 1, 2], "expected": [1, 2, 3]},
            {"input": [1], "expected": [1]},
        ],
    ),
    Problem(
        title="Insertion Sort",
        category="Sorting",
        prompt=(
            "Implement insertion_sort(arr). Return a new sorted list in ascending order.\n"
            "Do not use Python's built-in sort methods."
        ),
        starter_code="""def insertion_sort(arr):
    arr = arr[:]
    # Write your code here
    return arr
""",
        function_name="insertion_sort",
        tests=[
            {"input": [5, 2, 4, 6, 1, 3], "expected": [1, 2, 3, 4, 5, 6]},
            {"input": [3, 2, 1], "expected": [1, 2, 3]},
            {"input": [], "expected": []},
        ],
    ),

    # ---------------- SEARCHING ----------------
    Problem(
        title="Binary Search",
        category="Searching",
        prompt=(
            "Implement binary_search(arr, target).\n"
            "Return the index of target if found, otherwise -1.\n"
            "Assume arr is sorted in ascending order."
        ),
        starter_code="""def binary_search(arr, target):
    # Write your code here
    return -1
""",
        function_name="binary_search",
        tests=[
            {"input": ([1, 3, 5, 7, 9], 7), "expected": 3},
            {"input": ([2, 4, 6, 8], 5), "expected": -1},
            {"input": ([], 1), "expected": -1},
            {"input": ([10], 10), "expected": 0},
        ],
    ),

    # ---------------- ARRAYS ----------------
    Problem(
        title="Maximum Value in Array",
        category="Arrays",
        prompt=(
            "Implement find_max(arr). Return the maximum value in the array.\n"
            "Assume the array is non-empty."
        ),
        starter_code="""def find_max(arr):
    # Write your code here
    return None
""",
        function_name="find_max",
        tests=[
            {"input": [3, 7, 2, 9, 4], "expected": 9},
            {"input": [-5, -2, -10], "expected": -2},
            {"input": [1], "expected": 1},
        ],
    ),
    Problem(
        title="Remove Duplicates",
        category="Arrays",
        prompt=(
            "Implement remove_duplicates(arr). Return a new list with duplicates removed\n"
            "while preserving original order."
        ),
        starter_code="""def remove_duplicates(arr):
    # Write your code here
    return []
""",
        function_name="remove_duplicates",
        tests=[
            {"input": [1, 2, 2, 3, 1, 4], "expected": [1, 2, 3, 4]},
            {"input": [5, 5, 5], "expected": [5]},
            {"input": [], "expected": []},
        ],
    ),
    Problem(
        title="Rotate Array Right",
        category="Arrays",
        prompt=(
            "Implement rotate_right(arr, k). Return the array rotated to the right by k steps."
        ),
        starter_code="""def rotate_right(arr, k):
    # Write your code here
    return arr
""",
        function_name="rotate_right",
        tests=[
            {"input": ([1, 2, 3, 4, 5], 2), "expected": [4, 5, 1, 2, 3]},
            {"input": ([1, 2, 3], 1), "expected": [3, 1, 2]},
            {"input": ([1], 10), "expected": [1]},
        ],
    ),

    # ---------------- STRINGS ----------------
    Problem(
        title="Reverse String",
        category="Strings",
        prompt="Implement reverse_string(s). Return the reversed string.",
        starter_code="""def reverse_string(s):
    # Write your code here
    return s
""",
        function_name="reverse_string",
        tests=[
            {"input": "hello", "expected": "olleh"},
            {"input": "a", "expected": "a"},
            {"input": "", "expected": ""},
        ],
    ),
    Problem(
        title="Palindrome Check",
        category="Strings",
        prompt=(
            "Implement is_palindrome(s). Return True if s is a palindrome, otherwise False.\n"
            "Assume case-sensitive comparison."
        ),
        starter_code="""def is_palindrome(s):
    # Write your code here
    return False
""",
        function_name="is_palindrome",
        tests=[
            {"input": "racecar", "expected": True},
            {"input": "level", "expected": True},
            {"input": "hello", "expected": False},
        ],
    ),
    Problem(
        title="Count Vowels",
        category="Strings",
        prompt="Implement count_vowels(s). Return the number of vowels in the string.",
        starter_code="""def count_vowels(s):
    # Write your code here
    return 0
""",
        function_name="count_vowels",
        tests=[
            {"input": "hello", "expected": 2},
            {"input": "AEIOU", "expected": 5},
            {"input": "xyz", "expected": 0},
        ],
    ),
    Problem(
        title="Longest Substring Without Repeating",
        category="Strings",
        prompt="Return the length of the longest substring without repeating characters.",
        starter_code="""def longest_substring(s):
    # Write your code here
    return 0
""",
        function_name="longest_substring",
        tests=[
            {"input": "abcabcbb", "expected": 3},
            {"input": "bbbbb", "expected": 1},
            {"input": "pwwkew", "expected": 3},
            {"input": "", "expected": 0},
        ],
    ),

    # ---------------- STACK ----------------
    Problem(
        title="Valid Parentheses",
        category="Stack",
        prompt=(
            "Given a string s containing only (), {}, and [], determine if it is valid.\n"
            "Use a stack."
        ),
        starter_code="""def is_valid(s):
    # Write your code here
    return True
""",
        function_name="is_valid",
        tests=[
            {"input": "()", "expected": True},
            {"input": "()[]{}", "expected": True},
            {"input": "(]", "expected": False},
            {"input": "([)]", "expected": False},
            {"input": "{[]}", "expected": True},
        ],
    ),
    Problem(
        title="Min Stack Simulation",
        category="Stack",
        prompt=(
            "Implement process_stack(operations).\n"
            "Each operation is a tuple like ('push', 3), ('pop', None), ('top', None), ('get_min', None).\n"
            "Return a list of outputs for top/get_min/pop operations."
        ),
        starter_code="""def process_stack(operations):
    # Write your code here
    return []
""",
        function_name="process_stack",
        tests=[
            {
                "input": [("push", 3), ("push", 1), ("get_min", None), ("pop", None), ("top", None)],
                "expected": [1, 1, 3]
            }
        ],
    ),

    # ---------------- QUEUE ----------------
    Problem(
        title="Implement Queue Using List",
        category="Queue",
        prompt=(
            "Implement process_queue(operations).\n"
            "Each operation is a tuple like ('enqueue', 1) or ('dequeue', None).\n"
            "Return a list of outputs from dequeue operations."
        ),
        starter_code="""def process_queue(operations):
    # Write your code here
    return []
""",
        function_name="process_queue",
        tests=[
            {
                "input": [("enqueue", 1), ("enqueue", 2), ("dequeue", None)],
                "expected": [1]
            },
            {
                "input": [("enqueue", 10), ("dequeue", None), ("enqueue", 20), ("dequeue", None)],
                "expected": [10, 20]
            },
        ],
    ),

    # ---------------- LINKED LIST STYLE ----------------
    Problem(
        title="Reverse List",
        category="Linked Lists",
        prompt=(
            "Implement reverse_list(arr). Return a new list in reverse order.\n"
            "Do not use Python's built-in reverse methods."
        ),
        starter_code="""def reverse_list(arr):
    # Write your code here
    return arr
""",
        function_name="reverse_list",
        tests=[
            {"input": [1, 2, 3], "expected": [3, 2, 1]},
            {"input": [5], "expected": [5]},
            {"input": [], "expected": []},
        ],
    ),
    Problem(
        title="Find Middle Element",
        category="Linked Lists",
        prompt="Implement find_middle(arr). Return the middle element of the list.",
        starter_code="""def find_middle(arr):
    # Write your code here
    return None
""",
        function_name="find_middle",
        tests=[
            {"input": [1, 2, 3], "expected": 2},
            {"input": [1, 2, 3, 4, 5], "expected": 3},
            {"input": [10], "expected": 10},
        ],
    ),
    Problem(
        title="Remove Value",
        category="Linked Lists",
        prompt=(
            "Implement remove_value(arr, target). Return a new list with all occurrences of target removed."
        ),
        starter_code="""def remove_value(arr, target):
    # Write your code here
    return arr
""",
        function_name="remove_value",
        tests=[
            {"input": ([1, 2, 3, 2, 4], 2), "expected": [1, 3, 4]},
            {"input": ([5, 5, 5], 5), "expected": []},
            {"input": ([1, 2, 3], 7), "expected": [1, 2, 3]},
        ],
    ),

    # ---------------- HASH MAP ----------------
    Problem(
        title="Two Sum",
        category="Hash Map",
        prompt=(
            "Given nums and target, return the indices of the two numbers that add up to target.\n"
            "Assume exactly one solution exists."
        ),
        starter_code="""def two_sum(nums, target):
    # Write your code here
    return []
""",
        function_name="two_sum",
        tests=[
            {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
            {"input": ([3, 2, 4], 6), "expected": [1, 2]},
            {"input": ([3, 3], 6), "expected": [0, 1]},
        ],
    ),
    Problem(
        title="Character Frequency",
        category="Hash Map",
        prompt="Implement char_frequency(s). Return a dictionary with character counts.",
        starter_code="""def char_frequency(s):
    # Write your code here
    return {}
""",
        function_name="char_frequency",
        tests=[
            {"input": "aab", "expected": {"a": 2, "b": 1}},
            {"input": "hello", "expected": {"h": 1, "e": 1, "l": 2, "o": 1}},
            {"input": "", "expected": {}},
        ],
    ),
    Problem(
        title="First Unique Character",
        category="Hash Map",
        prompt=(
            "Implement first_unique_char(s). Return the index of the first non-repeating character,\n"
            "or -1 if none exists."
        ),
        starter_code="""def first_unique_char(s):
    # Write your code here
    return -1
""",
        function_name="first_unique_char",
        tests=[
            {"input": "leetcode", "expected": 0},
            {"input": "loveleetcode", "expected": 2},
            {"input": "aabb", "expected": -1},
        ],
    ),

    # ---------------- RECURSION ----------------
    Problem(
        title="Factorial",
        category="Recursion",
        prompt="Implement factorial(n) recursively.",
        starter_code="""def factorial(n):
    # Write your code here
    return 1
""",
        function_name="factorial",
        tests=[
            {"input": 0, "expected": 1},
            {"input": 1, "expected": 1},
            {"input": 5, "expected": 120},
        ],
    ),
    Problem(
        title="Fibonacci",
        category="Recursion",
        prompt="Implement fibonacci(n). Return the nth Fibonacci number.",
        starter_code="""def fibonacci(n):
    # Write your code here
    return 0
""",
        function_name="fibonacci",
        tests=[
            {"input": 0, "expected": 0},
            {"input": 1, "expected": 1},
            {"input": 6, "expected": 8},
        ],
    ),

    # ---------------- TREES ----------------
    Problem(
        title="Max Depth of Binary Tree (List Form)",
        category="Trees",
        prompt=(
            "A binary tree is represented as a list in level-order, using None for missing nodes.\n"
            "Implement max_depth(tree) and return the maximum depth."
        ),
        starter_code="""def max_depth(tree):
    # Write your code here
    return 0
""",
        function_name="max_depth",
        tests=[
            {"input": [3, 9, 20, None, None, 15, 7], "expected": 3},
            {"input": [1, None, 2], "expected": 2},
            {"input": [], "expected": 0},
        ],
    ),
    Problem(
        title="Count Leaf Nodes (List Form)",
        category="Trees",
        prompt=(
            "A binary tree is represented as a level-order list with None values.\n"
            "Implement count_leaves(tree) and return the number of leaf nodes."
        ),
        starter_code="""def count_leaves(tree):
    # Write your code here
    return 0
""",
        function_name="count_leaves",
        tests=[
            {"input": [3, 9, 20, None, None, 15, 7], "expected": 3},
            {"input": [1], "expected": 1},
            {"input": [], "expected": 0},
        ],
    ),
]