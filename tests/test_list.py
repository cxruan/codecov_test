import unittest


class TestListMethods(unittest.TestCase):
    def setUp(self):
        self.list = []

    def test_append(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list, ['a', 'b'])

    def test_pop(self):
        self.list.append('a')
        self.list.append('b')
        self.list.pop()
        self.assertEqual(self.list, ['a'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestListMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
