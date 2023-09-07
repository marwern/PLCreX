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

from plcrex.tools.fbd2st import _fbd2st
from plcrex.tools.st2x.tag.st2x_R2_2_0 import *
from plcrex.add import *
from pathlib import Path
import os


def cli(source: Path, export: Path, filename: str, exe: Path, edge_opt: bool, var_opt: bool, op_opt: bool):
    print_header(os.path.basename(__file__)[1:-3], get_version())
    if source.is_file() and source.suffix == '.xml':
        dir_path = Path(fr'{export}\PLCreX_outputs')
        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        # 1. FBD-to-ST Translation (backward + formal)
        _fbd2st.cli(source, export, filename, True, True)

        # 2. ST-to-X Translation
        translation(Path(fr'{dir_path}\{filename}.st'),
                    dir_path, filename, exe,
                    edge_opt, var_opt, op_opt, True)

    else:
        raise RuntimeError("no xml file found")
    print_runtime()
    return
