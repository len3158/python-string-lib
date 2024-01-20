from src.simple_string_lib import compare_versions


def test_string():
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
    print("All test cases passed")
