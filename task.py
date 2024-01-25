import unittest


def process_list(input_list):
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError(
            "Error: The length of the list must be a multiple of 10.")

    # Remove items at positions which are a multiple of 2 or 3
    result_list = [item for index, item in enumerate(
        input_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]

    # Return the processed list
    return result_list


class TestProcessList(unittest.TestCase):
    def test_valid_list(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        expected_result = [1, 5, 7, 11, 13, 17, 19]
        self.assertEqual(process_list(input_list), expected_result)

    def test_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                      10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            process_list(input_list)


if __name__ == '__main__':
    unittest.main()
