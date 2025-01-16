import sys
import os
import unittest
from dotenv import load_dotenv

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# .env ファイルを読み込む
load_dotenv(os.path.join(os.path.dirname(__file__), '../../..', '.env'))

from policy_tools import lookup_policy

class TestPolicyTools(unittest.TestCase):
    def test_lookup_policy(self):
        print("Testing lookup_policy...")
        query = "How to cancel a Home Depot order?"
        result = lookup_policy(query)
        print(result)
        self.assertIn("How to Cancel a Home Depot Order", result)

if __name__ == "__main__":
    unittest.main()