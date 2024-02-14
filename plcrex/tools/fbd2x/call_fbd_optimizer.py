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

from plcrex.tools.fbd2x.pyd.fbd_optimizer import *
from plcrex.tools.fbd2st.pyd.fbd2st_compiler import *
from plcrex.tools.misc.generic_functions import *
from pathlib import Path
import os


def cli(
        source: Path,
        export: Path,
        filename: str,
        exe: Path,
        edge_opt: bool,
        var_opt: bool,
        op_opt: bool,
        target_format: str
):
    print_header(
        FBDOptimizer.__tool__,
        FBDOptimizer.__version__,
        FBDOptimizer.__author__
    )
    if source.is_file() and source.suffix == '.xml':
        dir_path = Path(fr'{export}\PLCreX_outputs')
        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        # 1. FBD-to-ST Translation (backward + formal)
        FBD2ST(source, dir_path, filename, True, True).translate()

        # 2. ST-to-X Translation
        FBDOptimizer(Path(fr'{dir_path}\{filename}.st'),
                  dir_path, filename, exe,
                  edge_opt, var_opt, op_opt, edge_opt or var_opt or op_opt, target_format).translate()

    else:
        raise RuntimeError("no xml file found")
    print_footer()
