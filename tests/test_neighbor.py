import unittest

import json


class TestAnnotation(unittest.TestCase):

    def test_find_neighbors_0(self):
        self.assertEqual([1, 2], [1, 2])


if __name__ == '__main__':
    unittest.main()
