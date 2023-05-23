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

from lark import Lark, tree
from pathlib import Path


def translation(
        src: Path,
        txt: bool = False,
        dot: bool = False,
        beckhoff: bool = False):
    if beckhoff:
        with open(r'.\data\lark\STgrammar_Beckhoff.lark', 'rt') as file:
            grammar = file.read()
    else:
        with open(r'.\data\lark\STgrammar.lark', 'rt') as file:
            grammar = file.read()
    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    with open(src, 'rt') as file:
        source = file.read()

        # write (pretty) tree as .txt
        if txt:
            txt_export = open(fr'.\exports\tree\txt\{Path(src).name}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))

        # write tree as .dot file
        if dot:
            tree.pydot__tree_to_dot(parser.parse(source), fr'.\exports\tree\dot\{Path(src).name}.dot')
        return
