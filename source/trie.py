class TrieNode:
    """
    Trie node class for the Trie data structure.
    """

    def __init__(self):
        # Using the dictionary data structure to store the children of the node
        self.children = {}
        # Initialize the node as not the end of a word
        self.is_end_of_word = False
        # Initialize the price as infinity
        self.price = float("inf")


class Trie:
    """
    Trie data structure class for storing
    phone number prefixes and prices.
    """

    def __init__(self):
        # Create the root node of the Trie
        self.root = TrieNode()

    def insert(self, prefix, price):
        """
        Insert a phone number prefix and price into the Trie.
        """
        # Start at the root node
        current_node = self.root
        # Insert each character of the prefix into the Trie
        for char in prefix:
            # If the prefix character is not in the Trie, add it
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            # Move to the next node
            current_node = current_node.children[char]
        # Mark the end of the prefix and set the price
        current_node.is_end_of_word = True
        current_node.price = price

    def search(self, phone_number):
        """
        Search for the longest prefix match and cheapest price
        """
        # Start at the root node
        current_node = self.root
        cheapest_price = float("inf")
        # Search for the longest prefix match
        for char in phone_number:
            # If the prefix character is not in the Trie, break
            if char not in current_node.children:
                break
            # Move to the next node
            current_node = current_node.children[char]
            # Update the cheapest price if the current node is the end of a word
            if current_node.is_end_of_word:
                cheapest_price = current_node.price
        # If the price is not set, return None
        return cheapest_price if cheapest_price != float("inf") else None
