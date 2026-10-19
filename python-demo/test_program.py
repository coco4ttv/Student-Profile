#test_program.py
import unittest
from MyProgram import say_hello

class TestMyProgram(unittest.TestCase):
    def test_hello_output(self):
        self.assertEqual(say_hello(), "Hello from GitHub Actions!")

if __name__ == '__main__':
    unittest.main()
