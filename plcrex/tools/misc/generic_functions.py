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

import time
import datetime
from lark import Tree, Lark
import os
import site
import typer
import logging

# ANSI escape sequences for terminal colors
class ColorCodes:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


# Custom formatter class
class CustomFormatter(logging.Formatter):
    format = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d\n%(message)s"

    FORMATS = {
        logging.DEBUG: ColorCodes.BLUE + format + ColorCodes.RESET,
        logging.INFO: ColorCodes.GREEN + format + ColorCodes.RESET,
        logging.WARNING: ColorCodes.YELLOW + format + ColorCodes.RESET,
        logging.ERROR: ColorCodes.RED + format + ColorCodes.RESET,
        logging.CRITICAL: ColorCodes.RED + format + ColorCodes.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

format_cli = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d\n%(message)s"
logging.basicConfig(format=format_cli)

# Configure logging
#logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger()
#handler = logger.handlers[0]
#handler.setFormatter(CustomFormatter())

def parse_src(grammar, source: str, debug_flag):
    src_parser = Lark(
        get_file(fr'plcrex\data\grammars\{grammar}.lark'),
        maybe_placeholders=True,
        keep_all_tokens=False,
        debug=False)
    src_ast = src_parser.parse(source)
    #print(src_ast) if debug_flag else None
    return src_ast


def find_1st_parent_tree(tree, target_node):
    if not isinstance(tree, Tree):
        return None

    for child in tree.children:
        if child == target_node:
            return tree
        parent = find_1st_parent_tree(child, target_node)
        if parent is not None:
            return parent
    return None


def find_all_parent_trees(tree, target_node, parent_list=None):
    if parent_list is None:
        parent_list = []

    if not isinstance(tree, Tree):
        return parent_list

    for child in tree.children:
        if child == target_node:
            parent_list.append(tree)
        else:
            find_all_parent_trees(child, target_node, parent_list)

    return parent_list


def get_file(rel_path: str):
    # initialize grammar
    f = ""

    # Get the list of all global site-packages directories
    site_packages_dirs = site.getsitepackages()

    # Iterate over all site-packages directories
    for dir in site_packages_dirs:
        # Create an absolute path to the file
        abs_file_path = os.path.join(dir, rel_path)

        # Check if the file exists at this path
        if os.path.isfile(abs_file_path):
            #print(abs_file_path)
            # If the file exists, open it
            with open(abs_file_path, 'rt') as file:
                f = file.read()
                #logging.warning(f"Ignoring data from local developer package! > {rel_path}")
                typer.echo(typer.style(f"WARNING: Ignoring data from local developer package! > {rel_path}",
                                       fg=typer.colors.YELLOW, bold=True))
                #file.close()
            return f
     
    # if plcrex is not installed via pip, use local dir
    if f == "":
        with open(rel_path, 'rt') as file:
            f = file.read()
            #logging.warning(f"Ignoring data from global site-package! > {rel_path}")
            typer.echo(
                typer.style(f"WARNING: Ignoring data from global site-package! > {rel_path}", fg=typer.colors.YELLOW,
                            bold=True))
            #file.close()
        return f


def print_header(script_name:str, version:str, author:str):

    global start_time
    start_time = time.time()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    typer.echo("--------------------------------------------------")
    typer.echo(f"Tool:\t\t{script_name}")
    typer.echo(f"Version:\t{version}")
    typer.echo(f"Author:\t\t{author}")
    typer.echo(f"Start:\t\t{current_time} {datetime.date.today()}")
    typer.echo("--------------------------------------------------")


def print_footer():
    typer.echo("--------------------------------------------------")
    typer.echo(f"Runtime: %s seconds" % format((time.time() - start_time), ".3f"))
