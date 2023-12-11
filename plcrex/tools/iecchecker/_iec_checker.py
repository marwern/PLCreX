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

from plcrex.add import *
from plcrex.tools.iecchecker.tag.iec_checker_R1_2_0 import *
from pathlib import Path
import os


def cli(source: Path, exe: Path, verbose: bool, export: Path, filename: str, help_: bool):
    print_header(os.path.basename(__file__)[1:-3], get_version())
    if source.is_file():
        if exe.is_file():
            dir_path = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)
            dest = Path(fr'{dir_path}\{filename}.log')
            if source.is_file() and (source.suffix == '.st' or source.suffix == '.xml'):
                # call iec-checker with ONE supported OPTIONS (only a subset is covered)
                if help_:
                    execution(source, exe, '--help', dest)
                elif not verbose:
                    execution(source, exe, '--quiet', dest)
                elif verbose:
                    execution(source, exe, '--verbose', dest)
                with open(dest, 'rt') as file:
                    print(file.read())
                file.close()
            else:
                raise RuntimeError("no ST/xml file found")
        else:
            raise RuntimeError(rf"no .exe found at {exe}")
    print_runtime()
    return
