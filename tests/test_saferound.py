import unittest
import iteround
from collections import OrderedDict

class TestSafeRoundMethods(unittest.TestCase):

    def setUp(self):
        self.in_list = [4.0001, 3.2345, 3.2321, 6.4523, 5.3453, 7.3422]
        self.in_dict = {'foo': 60.19012964572332,
                        'bar': 15.428802458406679,
                        'baz': 24.381067895870007}
        self.in_odict = OrderedDict(self.in_dict)
        self.in_tuple = (60.1901296, 15.42880, 24.38106789)

        self.neg_in_list = [x * -1. for x in self.in_list]
        self.huge_in_list = [x * 100000. for x in self.in_list]

    def test_basic_difference(self):
        out = [4.0, 3.24, 3.23, 6.45, 5.35, 7.34]
        self.assertListEqual(iteround.saferound(self.in_list, 2), out)

    def test_basic_largest(self):
        out = [4.0, 3.23, 3.23, 6.45, 5.35, 7.35]
        self.assertListEqual(iteround.saferound(self.in_list,
                                                2, iteround.LARGEST), out)

    def test_basic_smallest(self):
        out = [4.0, 3.24, 3.23, 6.45, 5.35, 7.34]
        self.assertListEqual(iteround.saferound(self.in_list,
                                                2, iteround.SMALLEST), out)

    def test_dict(self):
        out = {'foo': 60.0,
               'bar': 16.0,
               'baz': 24.0}
        self.assertDictEqual(iteround.saferound(self.in_dict, 0), out)

    def test_odict(self):
        out = OrderedDict({'foo': 60.0,
                           'bar': 16.0,
                           'baz': 24.0})
        self.assertDictEqual(iteround.saferound(self.in_odict, 0), out)

    def test_tuple(self):
        out = (60., 16., 24.)
        self.assertTupleEqual(iteround.saferound(self.in_tuple, 0), out)

    def test_error_bad_float(self):
        bad = ['a', 3.2345, 3.2321, 6.4523, 5.3453, 7.3422]
        with self.assertRaises(AssertionError):
            iteround.saferound(bad, 2)

    def test_error_bad_places(self):
        with self.assertRaises(AssertionError):
            iteround.saferound(self.in_list, 2.5)

    def test_error_bad_strategy(self):
        with self.assertRaises(AssertionError):
            iteround.saferound(self.in_list, 2, strategy='foo')

    def test_error_bad_rounder(self):
        with self.assertRaises(TypeError):
            iteround.saferound(self.in_list, 2, rounder=lambda x: x)

    def test_negative(self):
        out = [-4.0, -3.24, -3.23, -6.45, -5.35, -7.34]
        self.assertListEqual(iteround.saferound(self.neg_in_list, 2), out)

    def test_huge(self):
        out = [400000.0, 324000.0, 323000.0, 645000.0, 535000.0, 734000.0]
        self.assertListEqual(iteround.saferound(self.huge_in_list, -3), out)

    def test_overround(self):
        out = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertListEqual(iteround.saferound(self.in_list, -3), out)

    def test_over_with_sum(self):
        out = [0.0, 0.0, 0.0, 10.0, 10.0, 10.0]
        self.assertListEqual(iteround.saferound(self.in_list, -1), out)

    def test_topline(self):
        out = [4.0, 3.0, 3.0, 7.0, 5.0, 7.0]
        topline = 29
        actual_out = iteround.saferound(self.in_list, 0, topline=topline)
        actual_topline = sum(actual_out)
        self.assertListEqual(actual_out, out)
        self.assertEqual(topline, actual_topline)

    def test_topline_sum(self):
        self.assertEqual(sum(iteround.saferound(self.in_list, 0, topline=28)), 28)
        self.assertEqual(sum(iteround.saferound(self.in_list, 0, topline=29)), 29)
        self.assertEqual(sum(iteround.saferound(self.in_list, 0, topline=30)), 30)


if __name__ == '__main__':
    unittest.main()
