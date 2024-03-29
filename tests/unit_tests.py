import unittest
from src.simple_string_lib import compare_versions


class Testing(unittest.TestCase):
    def test_string(self):
        assert compare_versions("1.2", "1.1") == 1
        assert compare_versions("1.1", "1.2") == -1
        assert compare_versions("1.2", "1.2") == 0
        assert compare_versions("1.2.0", "1.2") == 0
        assert compare_versions("1.2.1", "1.2") == 1
        assert compare_versions("1.2", "1.2.1") == -1
        assert compare_versions("1.2.9", "1.3.0") == -1
        assert compare_versions("2.0", "1.9999.9999") == 1
        assert compare_versions("1.0.0.0", "1") == 0
        assert compare_versions("0.9", "1.0") == -1
        # Test cases for invalid inputs
        try:
            compare_versions("1.2a", "1.2")
            assert False, "Expected ValueError"
        except ValueError:
            pass

        try:
            compare_versions(1.2, "1.2")
            assert False, "Expected TypeError"
        except TypeError:
            pass

        try:
            compare_versions("1..2", "1.2")
            assert False, "Expected ValueError"
        except ValueError:
            pass

        try:
            compare_versions("1.2", None)
            assert False, "Expected TypeError"
        except TypeError:
            pass
        print("All test cases passed")


if __name__ == '__main__':
    unittest.main()
