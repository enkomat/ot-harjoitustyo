import unittest
import spaghetti

class TestSpaghetti(unittest.TestCase):
    def setUp(self):
        print("Set up.")

    def test_player_move_down(self):
        print('Test.')

if __name__ == '__main__':
    unittest.main()