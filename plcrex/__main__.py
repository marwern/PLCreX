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

from plcrex import cli
from plcrex import __app_name__
import tomllib

#with open("pyproject.toml", "rb") as f:
#    _META = tomllib.load(f)

#NAME = _META["project"]["name"]

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()