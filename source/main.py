from source.trie import Trie


def find_cheapest_operator(operator_price_lists, phone_number):
    """
    Find the cheapest operator for a given phone number based on the operator price lists.
    """
    results = {}
    # Create a Trie for each operator's price list
    for operator, price_list in operator_price_lists.items():
        trie = Trie()
        # Insert each prefix and price into the Trie
        for prefix, price in price_list:
            trie.insert(prefix, price)
        # Search for the cheapest price for the phone number
        price = trie.search(phone_number)
        # Add the operator and price to the results if a price is found
        if price is not None:
            results[operator] = price

    # Return None and infinity if no results are found
    if not results:
        return None, float("inf")

    # Return the cheapest operator and price
    cheapest_operator = min(results, key=results.get)
    cheapest_price = results[cheapest_operator]

    return cheapest_operator, cheapest_price


if __name__ == "__main__":
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

    phone_number = "4673212345"
    cheapest_operator, cheapest_price = find_cheapest_operator(
        operator_price_lists, phone_number
    )
    if cheapest_operator:
        print(
            f"The cheapest operator for phone number {phone_number} is {cheapest_operator}"
        )
    else:
        print(f"No operator found for phone number {phone_number}")
