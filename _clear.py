import os
import shutil
from pathlib import Path

game = [str(file) for file in Path('game').rglob('*') if file.is_file()]
src = [str(file) for file in Path('src').rglob('*') if file.is_file()]