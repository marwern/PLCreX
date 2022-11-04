#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022 Marcel Werner.
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

from pathlib import Path
from subprocess import call
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

iec_checker_path = Path(cfg['IEC-Checker']['IEC_Checker_exe'])

def execution(src: Path, option: str = '--quiet'):
    if iec_checker_path.is_file():
        call([rf'{iec_checker_path}', src, option])
    else:
        raise RuntimeError(rf"no .exe found at {iec_checker_path}")
    return