#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2023 Marcel Werner.
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

from plcrex.tools.ds2ts.tag.ds2ts_R2_1_2 import *
from pathlib import Path
from plcrex.add import *
import os

def cli(formula:str, constr:str, full:bool, export:Path, filename:str):
    print_header(os.path.basename(__file__)[1:-3], get_version())
    dir_path = Path(fr'{export}\PLCreX_outputs')
    # Ensure the directory exists
    os.makedirs(dir_path, exist_ok=True)
    dest = Path(fr'{dir_path}\{filename}.log')
    create(formula, constr, full, dest, "default")
    print_runtime()
    return
