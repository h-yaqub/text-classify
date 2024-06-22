import unittest

from core.utils import Utils


class TestDataProcessing(unittest.TestCase):
    def test_read_data(self):
        data = Utils().read_data("data/classes/dev.txt")
        self.assertIsInstance(data, list)

    def test_create_dict(self):
        data = Utils().read_data("data/classes/dev.txt")
        word_to_index = {"<unk>": 0}
        tag_to_index = {}
        Utils().create_dict(data, word_to_index, tag_to_index)
        self.assertGreater(len(word_to_index), 1)
        self.assertGreater(len(tag_to_index), 0)

    def test_create_tensor(self):
        data = Utils().read_data("data/classes/dev.txt")
        word_to_index = {"<unk>": 0}
        tag_to_index = {}
        Utils().create_dict(data, word_to_index, tag_to_index)
        tensors = list(Utils().create_tensor(data, word_to_index, tag_to_index))
        self.assertIsInstance(tensors[0], tuple)


if __name__ == "__main__":
    unittest.main()
