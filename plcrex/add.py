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

import os
import site
import typer
import time
import datetime

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
            # If the file exists, open it
            with open(abs_file_path, 'rt') as file:
                f = file.read()
                typer.echo(typer.style(f"WARNING: Ignoring data from local developer package! > {rel_path}",
                                       fg=typer.colors.YELLOW, bold=True))
                file.close()
            return f

    # if plcrex is not installed via pip, use local dir
    if f == "":
        with open(rel_path, 'rt') as file:
            f = file.read()
            typer.echo(
                typer.style(f"WARNING: Ignoring data from global site-package! > {rel_path}", fg=typer.colors.YELLOW,
                            bold=True))
            file.close()
        return f

def print_header(script_name:str, version:str):

    global start_time
    start_time = time.time()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    print("--------------------------------------------------")
    print(f"Script:\t\t{script_name}")
    print(f"Version:\t{version}")
    print("Author:\t\tMarcel C. Werner")
    print(f"Start:\t\t{current_time} {datetime.date.today()}")
    print("--------------------------------------------------")

def print_runtime():
    print("--------------------------------------------------")
    print(f"Runtime: %s seconds" % format((time.time() - start_time), ".3f"))

# decorator to print name header before every output
#def print_plcrex_header():
#    print(typer.style("""
# ██████╗  ██╗       ██████╗  █████╗   █████╗  ██╗  ██╗
# ██╔══██╗ ██║      ██╔════╝ ██╔══██╗ ██╔══██╗ ╚██╗██╔╝
# ██████╔╝ ██║      ██║      ██║  ╚═╝ ██████╔╝  ╚███╔╝
# ██╔═══╝  ██║      ██║      ██║      ██╔═══╝   ██╔██╗
# ██║      ███████╗ ╚██████╗ ██║      ╚█████╗  ██╔╝ ██╗
# ╚═╝      ╚══════╝  ╚═════╝ ╚═╝       ╚════╝  ╚═╝  ╚═╝
# """, fg=typer.colors.BRIGHT_YELLOW, bold=True))
#v    return