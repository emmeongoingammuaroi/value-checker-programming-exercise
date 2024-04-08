import unittest
from source.main import find_cheapest_operator


class TestFindCheapestOperator(unittest.TestCase):
    def setUp(self):
        # Create a dictionary of operator price lists for testing
        self.operator_price_list = {
            "Operator A": [
                ["1", 0.9],
                ["268", 5.1],
                ["46", 0.17],
                ["4620", 0.0],
                ["468", 0.15],
                ["4631", 0.15],
                ["4673", 0.9],
                ["46732", 1.1],
            ],
            "Operator B": [
                ["1", 0.92],
                ["44", 0.5],
                ["46", 0.2],
                ["467", 1.0],
                ["48", 1.2],
            ],
        }

    def test_find_cheapest_operator(self):
        """
        Test with some regular test cases.
        """
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "4673212345"),
            ("Operator B", 1.0),
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "4673"),
            ("Operator A", 0.9),
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "1"), ("Operator A", 0.9)
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "44"), ("Operator B", 0.5)
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "48"), ("Operator B", 1.2)
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "4620"),
            ("Operator A", 0.0),
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "4631"),
            ("Operator A", 0.15),
        )
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "46732"),
            ("Operator B", 1.0),
        )

    def test_find_cheapest_operator_with_same_price(self):
        """
        Test when two operators have the same price for the same prefix.
        """
        self.operator_price_list["Operator C"] = [["46", 0.2]]
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "4673"),
            ("Operator C", 0.2),
        )

    def test_find_cheapest_operator_with_no_prefixes(self):
        """
        Test when the phone number has no matching prefixes.
        """
        self.assertEqual(
            find_cheapest_operator(self.operator_price_list, "999"),
            (None, float("inf")),
        )

    def test_find_cheapest_operator_with_no_operators(self):
        """
        Test when there are no operator price lists.
        """
        self.assertEqual(
            find_cheapest_operator({}, "4673212345"),
            (None, float("inf")),
        )


if __name__ == "__main__":
    unittest.main()
