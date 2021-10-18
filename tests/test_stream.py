import pytest

from stream import Stream


class TestStream:
    def test_map(self):
        a = [1, 2, 3]
        b = Stream(a).map(lambda x: x * 2).to_list()
        assert b == [2, 4, 6]


if __name__ == '__main__':
    pytest.main()
