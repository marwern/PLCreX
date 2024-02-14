#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2024 Marcel C. Werner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from plcrex.tools.stp.st_parser import *
from pathlib import Path
import os


def cli(source: Path, export: Path, filename: str, txt: bool, dot: bool, beckhoff: bool):
    print_header(
        STParser.__tool__,
        STParser.__version__,
        STParser.__author__
    )
    if source.is_file() and source.suffix == '.st':
        dir_path = Path(fr'{export}\PLCreX_outputs')
        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)
        STParser(source, dir_path, filename, txt, dot, beckhoff).translate()
    else:
        raise RuntimeError("no ST file found")
    print_footer()
