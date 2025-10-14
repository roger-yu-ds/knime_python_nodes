# Ensure repository root is on sys.path so `import src` works regardless of pytest's cwd/import mode
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
