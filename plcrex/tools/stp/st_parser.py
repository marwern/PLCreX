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
from plcrex.tools.misc.generic_functions import *

class STParser:
    __version__ = "2.0.0"
    __author__ = "Marcel C. Werner"
    __tool__ = "ST-Parser"

    def __init__(
            self,
            src: Path,
            dir_path: Path,
            filename: str,
            txt: bool = False,
            dot: bool = False,
            beckhoff: bool = False
    ):
        self.src = src
        self.dir_path = dir_path
        self.filename = filename
        self.txt = txt
        self.dot = dot
        self.beckhoff = beckhoff

    def read_src(self, src_dir: Path):
        f = open(src_dir, 'rt')
        src_txt = f.read()
        f.close()
        return src_txt

    def translate(self):

        if self.beckhoff:
            grammar = get_file(r'plcrex\data\grammars\STgrammar_Beckhoff.lark')
        else:
            grammar = get_file(r'plcrex\data\grammars\STgrammar.lark')

        parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)
        source = self.read_src(self.src)

        # write (pretty) tree as .txt
        if self.txt:
            txt_export = open(fr'{self.dir_path}\{self.filename}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))
            txt_export.close()

        # write tree as .dot file
        if self.dot:
            tree.pydot__tree_to_dot(parser.parse(source), fr'{self.dir_path}\{self.filename}.dot')
