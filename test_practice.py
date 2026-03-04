import unittest
from io import StringIO
import sys
import practice   # <-- change this to your filename


class TestLoopFunctions(unittest.TestCase):

    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue().strip().split("\n")

    # 1️⃣ countup_odd(n)
    def test_countup_odd(self):
        output = self.capture_output(practice.countup_odd, 7)
        self.assertEqual(output, ["1", "3", "5", "7"])

    # 2️⃣ countdown_multiples_of_five(n)
    def test_countdown_multiples_of_five(self):
        output = self.capture_output(practice.countdown_multiples_of_five, 12)
        self.assertEqual(output, ["10", "5", "0"])

    # 3️⃣ count_range(start, end)
    def test_count_range(self):
        output = self.capture_output(practice.count_range, 6, 3)
        self.assertEqual(output, ["6", "5", "4", "3"])


class TestPasswordFunctions(unittest.TestCase):

    # 4️⃣ check_access_code
    def test_check_access_code(self):
        self.assertEqual(practice.check_access_code(""), "Invalid")
        self.assertEqual(practice.check_access_code("abc"), "Weak")
        self.assertEqual(practice.check_access_code("abc123"), "Medium")
        self.assertEqual(practice.check_access_code("abc123!"), "Strong")

    # 5️⃣ evaluate_key
    def test_evaluate_key(self):
        self.assertEqual(practice.evaluate_key(""), "Invalid")
        self.assertEqual(practice.evaluate_key("1234"), "Numeric Only")
        self.assertEqual(practice.evaluate_key("abcd"), "Alphabet Only")
        self.assertEqual(practice.evaluate_key("abc123"), "Alphanumeric")
        self.assertEqual(practice.evaluate_key("abc123*"), "Secure Key")

    # 6️⃣ check_user_password
    def test_check_user_password(self):
        self.assertEqual(practice.check_user_password(""), "Invalid")
        self.assertEqual(practice.check_user_password("short"), "Too Short")
        self.assertEqual(practice.check_user_password("abcdefgh"), "Basic")
        self.assertEqual(practice.check_user_password("abcd1234"), "Standard")
        self.assertEqual(practice.check_user_password("abcd1234%"), "Advanced")


class TestReverseFunctions(unittest.TestCase):

    # 7️⃣ reverse_sentence
    def test_reverse_sentence(self):
        self.assertEqual(
            practice.reverse_sentence("Python makes life easier"),
            "easier life makes Python"
        )

    # 8️⃣ reverse_if_long
    def test_reverse_if_long(self):
        self.assertEqual(
            practice.reverse_if_long("This is a simple test"),
            "test simple a is This"
        )
        self.assertEqual(
            practice.reverse_if_long("Hello world"),
            "Hello world"
        )

    # 9️⃣ reverse_and_uppercase
    def test_reverse_and_uppercase(self):
        self.assertEqual(
            practice.reverse_and_uppercase("Python is fun"),
            "FUN IS PYTHON"
        )


if __name__ == "__main__":
    unittest.main()