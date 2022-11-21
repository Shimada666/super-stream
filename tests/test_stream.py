from src.superstream.stream import Stream


class TestStream:
    def test_init(self):
        assert len(Stream([]).to_list()) == 0

    def test_map(self):
        a = [1, 2, 3]
        b = Stream(a).map(lambda x: x * 2).to_list()
        assert b == [2, 4, 6]

    def test_star_map(self):
        a = [(2,5), (3,2), (10,3)]
        b = Stream(a).star_map(pow).to_list()
        assert b == [32, 9, 1000]

    def test_flat_map(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = Stream(a).flat_map(lambda x: Stream(x)).to_list()
        assert b == [1, 2, 3, 4, 5, 6]

    def test_filter(self):
        a = [1, 2, 3]
        b = Stream(a).filter(lambda x: x > 1).to_list()
        assert b == [2, 3]

    def test_for_each(self):
        a = [1, 2, 3]
        Stream(a).for_each(lambda x: x)

    def test_distinct(self):
        a = [1, 2, 5, 3, 5, 4]
        b = Stream(a).distinct().to_list()
        assert b == [1, 2, 5, 3, 4]

    def test_sorted(self):
        a = [2, 1, 3]
        b = Stream(a).sorted().to_list()
        assert b == [1, 2, 3]

    def test_count(self):
        a = [1, 2, 3]
        b = Stream(a).count()
        assert b == 3

    def test_sum(self):
        a = [1, 2, 3]
        b = Stream(a).sum()
        assert b == 6

        a = [[1], [2, 3], [4]]
        b = Stream(a).sum(start = [0])
        assert b == [0, 1, 2, 3, 4]

    def test_group_by(self):
        a = [{'p': '1', 'name': 'foo'}, {'p': '2', 'name': 'bar'}, {'p': '2', 'name': 'bar'}]
        b = Stream(a).group_by(lambda x: x['p'])
        assert len(b['2']) == 2

    def test_reduce(self):
        a = [1, 2, 3]
        b = Stream(a).reduce(lambda x, y: x + y)
        assert b == 6
        c = Stream(a).reduce(lambda x, y: x + y, 10)
        assert c == 16

        a = []
        d = Stream(a).reduce(lambda x, y: x + y)
        assert d is None

        e = Stream(a).reduce(lambda x, y: x + y, 0)
        assert e == 0

    def test_limit(self):
        a = [1, 2, 3]
        b = Stream(a).limit(2).to_list()
        assert b == [1, 2]

    def test_skip(self):
        a = [1, 2, 3]
        b = Stream(a).skip(1).to_list()
        assert b == [2, 3]

    def test_take_while(self):
        a = [1, 4, 6, 4, 1]
        b = Stream(a).take_while(lambda x: x < 5).to_list()
        assert b == [1, 4]

    def test_drop_while(self):
        a = [1, 4, 6, 4, 1]
        b = Stream(a).drop_while(lambda x: x < 5).to_list()
        assert b == [6, 4, 1]

    def test_min(self):
        a = [{'a': 1}, {'a': 2}]
        b = Stream(a).min(key=lambda x: x['a'])
        assert b == {'a': 1}
        assert Stream([1, 2]).min() == 1

    def test_max(self):
        a = [{'a': 1}, {'a': 2}]
        b = Stream(a).max(key=lambda x: x['a'])
        assert b == {'a': 2}
        assert Stream([1, 2]).max() == 2

    def test_find_first(self):
        a = [1, 2, 3]
        b = Stream(a).find_first()
        assert b == 1

        a = []
        b = Stream(a).find_first()
        assert b is None

    def test_any_match(self):
        a = [1, 2, 3]
        b = Stream(a).any_match(lambda x: x < 2)
        assert b is True

    def test_all_match(self):
        a = [1, 2, 3]
        b = Stream(a).all_match(lambda x: x < 4)
        assert b is True

    def test_none_match(self):
        a = [1, 2, 3]
        b = Stream(a).none_match(lambda x: x < 0)
        assert b is True

    def test_to_list(self):
        a = [1, 2, 3]
        b = len(Stream(a).to_list())
        assert b == 3

    def test_set(self):
        a = [1, 2, 3, 3]
        b = Stream(a).to_set()
        assert len(b) == 3

    def test_to_dict(self):
        a = [1, 2]
        b = Stream(a).to_dict(lambda x: str(x), lambda y: y)
        assert b == {
            '1': 1,
            '2': 2
        }

    def test_to_map(self):
        a = [1, 2]
        b = Stream(a).to_map(lambda x: str(x), lambda y: y)
        assert b == {
            '1': 1,
            '2': 2
        }

    def test_of(self):
        assert Stream.of(1, 2, 3).to_list() == [1, 2, 3]

    def test_collect(self):
        a = [1, 2, 3]
        b = Stream(a).collect(set)
        assert b == {1, 2, 3}

    def test_collects(self):
        a = [1, 2, 3]
        b = Stream(a).collects(enumerate).filter(lambda x: x[1] % 2 != 0).map(lambda x: x[0]).to_list()
        assert b == [0, 2]
