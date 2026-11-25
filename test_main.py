"""Tests for main.py: the roast must pass the competition's gate, and the
program must write the same bytes on every run.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import MAX_CHARS, OUTPUT_PATH, ROAST, main, validate, write_entry


class TestRoastLine(unittest.TestCase):
    def test_roast_is_a_single_line(self):
        self.assertNotIn("\n", ROAST)
        self.assertNotIn("\r", ROAST)

    def test_roast_passes_the_gate(self):
        # 1 to 200 characters, not only whitespace, valid UTF-8.
        validate(ROAST)
        self.assertGreaterEqual(len(ROAST), 1)
        self.assertLessEqual(len(ROAST), MAX_CHARS)
        self.assertTrue(ROAST.strip())
        ROAST.encode("utf-8")

    def test_roast_is_about_a_fridge(self):
        self.assertIn("fridge", ROAST.lower())

    def test_roast_has_no_leading_or_trailing_whitespace(self):
        self.assertEqual(ROAST, ROAST.strip())

    def test_roast_is_plain_ascii(self):
        # Keeps the byte count equal to the character count, so the gate's
        # character limit and the leaderboard's Size column can never drift.
        ROAST.encode("ascii")


class TestValidate(unittest.TestCase):
    def test_rejects_empty_and_whitespace_only(self):
        for bad in ("", "   ", "\t\n"):
            with self.assertRaises(ValueError, msg=repr(bad)):
                validate(bad)

    def test_rejects_over_200_characters(self):
        with self.assertRaises(ValueError):
            validate("x" * (MAX_CHARS + 1))

    def test_rejects_multiple_lines(self):
        with self.assertRaises(ValueError):
            validate("one line\ntwo lines")

    def test_rejects_surrounding_whitespace(self):
        with self.assertRaises(ValueError):
            validate(" padded line ")


class TestWriteEntry(unittest.TestCase):
    def test_writes_the_line_and_nothing_else(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            text = write_entry(ROAST, path)
            with open(path, "r", encoding="utf-8") as handle:
                self.assertEqual(handle.read(), text)
            self.assertEqual(text.rstrip("\n"), ROAST)
            self.assertEqual(len(text.rstrip("\n")), len(ROAST))

    def test_two_runs_are_byte_identical(self):
        # The grader runs the program twice; the output must not vary.
        with tempfile.TemporaryDirectory() as tmp:
            first = os.path.join(tmp, "first.txt")
            second = os.path.join(tmp, "second.txt")
            write_entry(ROAST, first)
            write_entry(ROAST, second)
            with open(first, "rb") as handle:
                first_bytes = handle.read()
            with open(second, "rb") as handle:
                second_bytes = handle.read()
            self.assertEqual(first_bytes, second_bytes)

    def test_main_returns_zero_and_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            self.assertEqual(main([path]), 0)
            with open(path, encoding="utf-8") as handle:
                self.assertEqual(handle.read().rstrip("\n"), ROAST)

    def test_default_output_path(self):
        self.assertEqual(OUTPUT_PATH, "/output/entry.txt")


if __name__ == "__main__":
    unittest.main()
