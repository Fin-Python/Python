from itertools import product
from unittest.mock import patch
import runpy
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

script = Path(__file__).with_name("at_if_then.py")

testCases = product(range(1, 5), range(1, 3))

for message, method in testCases:
    inputs = iter([str(message), str(method)])
    output = StringIO()

    with patch("builtins.input", side_effect=inputs):
        with redirect_stdout(output):
            runpy.run_path(str(script))

    result = output.getvalue()

    expected = f"Message {message}"
    passed = expected in result

    print(f"Input: {(message, method)} | Expected: {expected} | Result: {passed}")
