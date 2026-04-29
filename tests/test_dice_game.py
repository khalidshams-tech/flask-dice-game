import sys
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1] / "project"
sys.path.insert(0, str(PROJECT_DIR))

from games.dice_game import DiceGameState, new_game, play_turn, validate_roll


class DiceGameTests(unittest.TestCase):
    def test_new_game_starts_unfinished(self):
        state = new_game()

        self.assertEqual(state.turn, 1)
        self.assertIsNone(state.point)
        self.assertFalse(state.finished)

    def test_validate_roll_rejects_out_of_range_values(self):
        with self.assertRaises(ValueError):
            validate_roll(1)

        with self.assertRaises(ValueError):
            validate_roll(13)

    def test_first_turn_win_and_loss_rules(self):
        self.assertTrue(play_turn(DiceGameState(), 7).finished)
        self.assertIn("WIN", play_turn(DiceGameState(), 11).result)
        self.assertIn("LOSE", play_turn(DiceGameState(), 2).result)

    def test_point_rule_after_first_turn(self):
        state = play_turn(DiceGameState(), 5)

        self.assertEqual(state.point, 5)
        self.assertEqual(state.turn, 2)

        state = play_turn(state, 5)

        self.assertTrue(state.finished)
        self.assertIn("WIN", state.result)


if __name__ == "__main__":
    unittest.main()
