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

from pathlib import Path
from plcrex.add import *
import xmlschema
import os


def get_version():
    return os.path.basename(__file__)#[-9:-3]


def validate(xml_file: Path, validation_file: str):
    xsd_file = get_file(fr'plcrex\data\tc6\{validation_file}')

    # create validation scheme
    scheme = xmlschema.XMLSchema(xsd_file)

    # validate PLCopen xml file
    scheme.validate(xml_file)

    return
