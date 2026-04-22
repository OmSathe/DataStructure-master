import io
import traceback
import contextlib


def execute_user_code(user_code: str):
    namespace = {}
    execution_output = io.StringIO()

    try:
        with contextlib.redirect_stdout(execution_output):
            exec(user_code, namespace)
        return {
            "success": True,
            "namespace": namespace,
            "stdout": execution_output.getvalue().strip(),
            "error": None,
        }
    except Exception:
        return {
            "success": False,
            "namespace": None,
            "stdout": execution_output.getvalue().strip(),
            "error": traceback.format_exc(),
        }


def run_problem_tests(problem, namespace):
    func = namespace.get(problem.function_name)

    if not callable(func):
        return {
            "success": False,
            "output": f"Could not find a callable function named '{problem.function_name}'."
        }

    lines = []
    passed_count = 0

    for i, test in enumerate(problem.tests, start=1):
        try:
            raw_input = test["input"]

            if isinstance(raw_input, tuple):
                result = func(*raw_input)
            else:
                result = func(raw_input)

            expected = test["expected"]

            if result == expected:
                passed_count += 1
                lines.append(f"Test {i}: Passed")
            else:
                lines.append(f"Test {i}: Failed")
                lines.append(f"  Input: {raw_input}")
                lines.append(f"  Expected: {expected}")
                lines.append(f"  Got: {result}")

        except Exception:
            lines.append(f"Test {i}: Error")
            lines.append(traceback.format_exc())

    lines.append("")
    lines.append(f"Result: {passed_count}/{len(problem.tests)} tests passed.")

    return {
        "success": True,
        "output": "\n".join(lines)
    }