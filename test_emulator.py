import unittest
from shell_emulator.emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator("config.xml")

    # Тесты для команды ls
    def test_ls_root(self):
        result = self.emulator.ls()
        self.assertIn("file1.txt", result)
        self.assertIn("dir1", result)

    def test_ls_empty_directory(self):
        self.emulator.cd("dir2")
        result = self.emulator.ls()
        self.assertIn("file4.txt", result)

    # Тесты для команды cd
    def test_cd_valid_directory(self):
        self.emulator.cd("dir1")
        self.assertEqual(self.emulator.current_dir, "/dir1")

    def test_cd_invalid_directory(self):
        result = self.emulator.cd("nonexistent")
        self.assertEqual(result, "cd: no such file or directory: nonexistent")

    # Тесты для команды cat
    def test_cat_existing_file(self):
        result = self.emulator.cat("file1.txt")
        self.assertEqual(result, "Content of file1")

    def test_cat_nonexistent_file(self):
        result = self.emulator.cat("nonexistent.txt")
        self.assertIn("No such file or directory", result)

    # Тесты для команды date
    def test_date_format(self):
        result = self.emulator.date()
        self.assertRegex(result, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    def test_date_not_empty(self):
        result = self.emulator.date()
        self.assertTrue(len(result) > 0)

    # Тесты для команды clear
    def test_clear_output(self):
        result = self.emulator.clear()
        self.assertEqual(result, "CLEAR")

    def test_clear_no_side_effects(self):
        initial_dir = self.emulator.current_dir
        self.emulator.clear()
        self.assertEqual(self.emulator.current_dir, initial_dir)

    # Тесты для команды exit
    def test_exit_output(self):
        result = self.emulator.exit()
        self.assertEqual(result, "EXIT")

if __name__ == "__main__":
    unittest.main()

