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

from pathlib import Path
from plcrex.tools.misc.generic_functions import *
import xmlschema


class XMLValidation:
    __version__ = "2.0.0"
    __author__ = "Marcel C. Werner"
    __tool__ = "XML-Validator"

    def __init__(self,
                 xml_file: Path,
                 validation_file: str
    ):
        self.xml_file = xml_file
        self.validation_file = validation_file
        #logging.debug(
        #    f"Module: {self.__tool__}, Version: {self.__version__}, Author: {self.__author__}")



    def validate(self):
        xsd_file = get_file(fr'plcrex\data\tc6\{self.validation_file}')

        # create validation scheme
        scheme = xmlschema.XMLSchema(xsd_file)

        # validate PLCopen xml file
        scheme.validate(self.xml_file)
