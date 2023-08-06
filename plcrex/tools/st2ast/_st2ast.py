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

from lark import Lark, tree
from pathlib import Path
import os
import site
import typer

def translation(
        src: Path,
        dir_path: Path,
        filename: str,
        txt: bool = False,
        dot: bool = False,
        beckhoff: bool = False):

    # initialize grammar
    grammar = ""

    # Get the list of all global site-packages directories
    site_packages_dirs = site.getsitepackages()

    # Define the relative path to your file from the site-packages directory
    if beckhoff:
        rel_path = "plcrex\data\grammars\STgrammar_Beckhoff.lark"
    else:
        rel_path = "plcrex\data\grammars\STgrammar.lark"

    # Iterate over all site-packages directories
    for dir in site_packages_dirs:
        # Create an absolute path to the file
        abs_file_path = os.path.join(dir, rel_path)

        # Check if the file exists at this path
        if os.path.isfile(abs_file_path):
            # If the file exists, open it
            with open(abs_file_path, 'rt') as file:
                grammar = file.read()
                file.close()
            break

    # if plcrex is not installed via pip, use local dir
    if grammar == "":
        typer.echo(typer.style("* * Developer Mode * *", fg=typer.colors.YELLOW, bold=True))
        with open(rel_path, 'rt') as file:
            #print("Developer Lark grammar: ", rel_path)
            grammar = file.read()
            file.close()

    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    with open(src, 'rt') as file:
        source = file.read()

        # write (pretty) tree as .txt
        if txt:
            #txt_export = open(fr'{dir_path}\{Path(src).name}.txt', "w")
            txt_export = open(fr'{dir_path}\{filename}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))

        # write tree as .dot file
        if dot:
            #tree.pydot__tree_to_dot(parser.parse(source), fr'{dir_path}\{Path(src).name}.dot')
            tree.pydot__tree_to_dot(parser.parse(source), fr'{dir_path}\{filename}.dot')
        return