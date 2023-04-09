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
import sys
import os

# Get the absolute path of the directory containing D.pyd
module_path = os.path.abspath(os.path.dirname(__file__))

# Add the directory to sys.path
if module_path not in sys.path:
    sys.path.append(module_path)

import _test_case_gen

def create(formula: str):
    _test_case_gen.create(formula)
    #A | (B & (C | (D==E)))
    #(A & B) | (C == (D & E))
#create("A&B")