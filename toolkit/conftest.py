"""Make the src/ layout importable in tests without requiring an install.

This lets `python -m pytest` work from the toolkit/ directory in environments
(like PEP 668 externally-managed Python) where `pip install -e` is blocked.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
