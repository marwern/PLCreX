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

from plcrex.tools.fbdia.pyd.io_analysis import *
from plcrex.tools.fbd2st import call_fbd2st_compiler
from pathlib import Path
from plcrex.tools.misc.generic_functions import *
import os

def cli(source: Path, export: Path, filename: str):
    print_header(
        IOAnalysis.__tool__,
        IOAnalysis.__version__,
        IOAnalysis.__author__
    )
    if source.is_file() and source.suffix == '.xml':
        dir_path  = Path(fr'{export}\PLCreX_outputs')
        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        # 1. FBD-to-ST, backward + no-formal
        call_fbd2st_compiler.cli(source, export, filename, True, False)

        # 2. ST-to-I/O Dependency
        IOAnalysis(Path(fr'{dir_path}\{filename}.st'), dir_path, filename).data_flow_analysis_st()
    else:
        raise RuntimeError("no xml file found")
    print_footer()
