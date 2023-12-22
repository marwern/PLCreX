#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2023 Marcel C. Werner.
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

from plcrex.tools.ds2ts.tag.ds2ts_R3_1_0 import *
from pathlib import Path
from plcrex.add import *
import os


def cli(formula:str, sc:bool, dc:bool, mcdc:bool, mcc:bool):
    print_header(os.path.basename(__file__)[1:-3], get_version())
    create(formula, sc, dc, mcdc, mcc)
    print_runtime()
    return
