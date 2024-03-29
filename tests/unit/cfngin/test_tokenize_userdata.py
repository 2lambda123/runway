"""Tests for runway.cfngin.tokenize_userdata."""

# pyright: basic
import unittest

import yaml

from runway.cfngin.tokenize_userdata import cf_tokenize


class TestCfTokenize(unittest.TestCase):
    """Tests for runway.cfngin.tokenize_userdata."""

    def test_tokenize(self) -> None:
        """Test tokenize."""
        user_data = ["field0", 'Ref("SshKey")', "field1", 'Fn::GetAtt("Blah", "Woot")']
        user_data_dump = yaml.dump(user_data)
        parts = cf_tokenize(user_data_dump)
        self.assertIsInstance(parts[1], dict)
        self.assertIsInstance(parts[3], dict)
        self.assertEqual(parts[1]["Ref"], "SshKey")  # type: ignore
        self.assertEqual(parts[3]["Fn::GetAtt"], ["Blah", "Woot"])  # type: ignore
        self.assertEqual(len(parts), 5)
