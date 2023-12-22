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

from plcrex.tools.xmlval.tag.xml_val_R1_2_1 import *
from pathlib import Path
from plcrex.add import *


def cli(source: Path, v201: bool):
    print_header(os.path.basename(__file__)[1:-3], get_version())
    if source.is_file() and source.suffix == '.xml':
        if v201:
            # tc6_xml_v201.xsd (https: // plcopen.org / downloads / plcopen-xml-version-201-xsd-file-0)
            validate(source, "tc6_xml_v201.xsd")
        else:
            # tc6_xml_v10.xsd (Beremiz v1.2)
            validate(source, "tc6_xml_v10.xsd")

    else:
        raise RuntimeError("no xml file found")
    print_runtime()
    return
