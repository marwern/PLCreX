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

from plcrex.tools.st2scl.pyd.st2scl_compiler import *
from plcrex.tools.misc.generic_functions import *


def cli(
        source: Path,
        export: Path,
        kicodia: Path,
        mode: str
):
    print_header(
        ST2SCL.__tool__,
        ST2SCL.__version__,
        ST2SCL.__author__
    )
    ST2SCL().run(source, export, kicodia, mode)
    print_footer()
