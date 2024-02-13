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

from plcrex.tools.misc.generic_functions import *
from pathlib import Path
from subprocess import run


class IECChecker:
    __version__ = "2.0.0"
    __author__ = "Marcel C. Werner"
    __tool__ = "IEC-Checker"

    def __init__(
            self,
            src: Path,
            exe: Path,
            option: str,
            dest: Path
    ):
        self.src = src
        self.exe = exe
        self.option = option
        self.dest = dest

    def run_checker(self):
        run([rf'{self.exe}', self.src, self.option], stdout=open(self.dest, 'w'))
        return
