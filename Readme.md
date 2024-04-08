# Cheapest Operator Finder

This Python application helps find the cheapest operator for a given phone number. It efficiently handles any number of price lists (operators) and calculates the most economical option.

## How It Works

The application employs a Trie data structure to organize and search through operator prefixes and their associated prices. Upon receiving a phone number, it traverses the Trie to locate the longest matching prefix and determines the operator with the lowest price.

The time complexity of the algorithm is O(n + m), where n is the total number of entries across all operator price lists and m is the length of the phone number.

## Usage

To use the application, start by organizing your operator price lists in the specified format:

```python
operator_price_lists = {
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

```

Next, utilize the `find_cheapest_operator` function with your operator price lists and the desired phone number:

```python
from source.main import find_cheapest_operator

phone_number = "4673212345"
operator, price = find_cheapest_operator(operator_price_lists, phone_number)
print(f"The cheapest operator for {phone_number} is {operator} with price {price}")
```

This will display the most cost-effective operator and its corresponding price for the provided phone number.

## Testing

To run the tests, execute the following command:

```bash
python -m unittest source/tests.py
```

This command will execute all the defined test cases in `source/tests.py`.