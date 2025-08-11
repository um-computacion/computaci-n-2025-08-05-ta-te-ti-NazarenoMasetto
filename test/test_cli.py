import unittest
import types
import cli

class TestCli(unittest.TestCase):
    def test_main_existe(self):
        self.assertTrue(hasattr(cli, "main"))
        self.assertTrue(isinstance(cli.main, types.FunctionType))

if __name__ == "__main__":
    unittest.main()
