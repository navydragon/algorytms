class BloomFilter:
    def __init__(self, size=32):
        self.size = size
        self.bit_array = 0

    def _hash1(self, string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 17 + ord(char)) % self.size
        return hash_value

    def _hash2(self, string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 223 + ord(char)) % self.size
        return hash_value

    def add(self, string):
        hash1 = self._hash1(string)
        hash2 = self._hash2(string)
        self.bit_array |= (1 << hash1)
        self.bit_array |= (1 << hash2)

    def contains(self, string):
        hash1 = self._hash1(string)
        hash2 = self._hash2(string)
        return (self.bit_array & (1 << hash1)) and (self.bit_array & (1 << hash2))


# Тестирование

import unittest

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bloom = BloomFilter()

    def test_add_and_contains(self):
        test_strings = [
            "0123456789", "1234567890", "2345678901",
            "3456789012", "4567890123", "5678901234",
            "6789012345", "7890123456", "8901234567",
            "9012345678"
        ]

        for string in test_strings:
            self.bloom.add(string)
            self.assertTrue(self.bloom.contains(string))

        # Проверка ложноположительных срабатываний
        false_strings = ["abcdefghij", "klmnopqrst"]
        for string in false_strings:
            self.assertFalse(self.bloom.contains(string))


if __name__ == '__main__':
    unittest.main()
