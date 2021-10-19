from stream import Stream


class TestStream:
    def test_init(self):
        assert len(Stream().to_list()) == 0

    def test_map(self):
        a = [1, 2, 3]
        b = Stream(a).map(lambda x: x * 2).to_list()
        assert b == [2, 4, 6]

    def test_filter(self):
        a = [1, 2, 3]
        b = Stream(a).filter(lambda x: x > 1).to_list()
        assert b == [2, 3]

    def test_for_each(self):
        a = [1, 2, 3]
        Stream(a).for_each(lambda x: x)

    def test_sorted(self):
        a = [2, 1, 3]
        b = Stream(a).sorted().to_list()
        assert b == [1, 2, 3]

    def test_count(self):
        a = [1, 2, 3]
        b = Stream(a).count()
        assert b == 3

    def test_limit(self):
        a = [1, 2, 3]
        b = Stream(a).limit(2).to_list()
        assert b == [1, 2]

    def test_skip(self):
        a = [1, 2, 3]
        b = Stream(a).skip(1).to_list()
        assert b == [2, 3]

    def test_list(self):
        a = [1, 2, 3]
        b = Stream(a).count()
        assert b == 3

    def test_set(self):
        a = [1, 2, 3, 3]
        b = Stream(a).to_set()
        assert len(b) == 3

    def test_to_map(self):
        a = [1, 2]
        b = Stream(a).to_map(lambda x: str(x), lambda y: y)
        assert b == {
            '1': 1,
            '2': 2
        }
