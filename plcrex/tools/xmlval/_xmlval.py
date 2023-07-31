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

from pathlib import Path
import xmlschema
import os
import site

def validate(xml_file: Path, validation_file: str):

    # initialize xsd_file
    xsd_file = ""

    # Get the list of all global site-packages directories
    site_packages_dirs = site.getsitepackages()

    # Define the relative path to your file from the site-packages directory
    rel_path = fr"plcrex\data\tc6\{validation_file}"

    # Iterate over all site-packages directories
    for dir in site_packages_dirs:
        # Create an absolute path to the file
        abs_file_path = os.path.join(dir, rel_path)

        # Check if the file exists at this path
        if os.path.isfile(abs_file_path):
            # If the file exists
            xsd_file = abs_file_path
            break

    # if plcrex is not installed via pip, use local dir
    if xsd_file =="":
        with open(rel_path, 'rt') as file:
            print("Developer path: ", rel_path)
            xsd_file = file.read()
            file.close()

    # create validation scheme
    scheme = xmlschema.XMLSchema(xsd_file)

    # validate PLCopen xml file
    scheme.validate(xml_file)
    return
