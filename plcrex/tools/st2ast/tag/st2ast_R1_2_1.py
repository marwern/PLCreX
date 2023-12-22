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

from lark import Lark, tree
from pathlib import Path
from plcrex.add import *
import os

def get_version():
    return os.path.basename(__file__)#[-9:-3]

def translation(
        src: Path,
        dir_path: Path,
        filename: str,
        txt: bool = False,
        dot: bool = False,
        beckhoff: bool = False):

    if beckhoff:
        grammar = get_file(r'plcrex\data\grammars\STgrammar_Beckhoff.lark')
    else:
        grammar = get_file(r'plcrex\data\grammars\STgrammar.lark')

    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    with open(src, 'rt') as file:
        source = file.read()

        # write (pretty) tree as .txt
        if txt:
            txt_export = open(fr'{dir_path}\{filename}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))
            txt_export.close()

        # write tree as .dot file
        if dot:
            tree.pydot__tree_to_dot(parser.parse(source), fr'{dir_path}\{filename}.dot')

        return
