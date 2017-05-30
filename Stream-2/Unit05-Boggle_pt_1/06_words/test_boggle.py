import unittest
from string import ascii_uppercase
import boggle


class TestBoggle(unittest.TestCase):
    """
    Our test case for boggle solver
    """

    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty boggle
        grid
        """
        grid = boggle.make_grid(0, 0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_is_width_times_height(self):
        """
        Test to ensure that the total size of the grid is
        equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates
        inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertTrue((0, 0) in grid)
        self.assertTrue((0, 1) in grid)
        self.assertTrue((1, 0) in grid)
        self.assertTrue((1, 1) in grid)
        self.assertTrue((2, 2) not in grid)

    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid contains
        letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertTrue(letter in ascii_uppercase)

    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertTrue((0, 1) in neighbours)
        self.assertTrue((0, 2) in neighbours)
        self.assertTrue((0, 3) in neighbours)
        self.assertTrue((1, 1) in neighbours)
        self.assertTrue((1, 3) in neighbours)
        self.assertTrue((2, 1) in neighbours)
        self.assertTrue((2, 2) in neighbours)
        self.assertTrue((2, 3) in neighbours)

    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid)  # creates a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
    
    def test_converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])

    def test_search_grid_for_words(self):
        """
        Ensure that certain patterns can be found in a path
        """
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = "AB"
        threeLetterWord = "ABC"
        notThereWord = "EEE"
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]

        foundWords = boggle.search(grid, dictionary)

        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)

    def test_load_dictionary(self):
        """
        Test that the `get_dictionary` function returns a dictionary
        that has a length greater than 0
        """
        dictionary = boggle.get_dictionary('/usr/share/dict/words')
        self.assertGreater(len(dictionary), 0)


if __name__ == '__main__':
    unittest.main()