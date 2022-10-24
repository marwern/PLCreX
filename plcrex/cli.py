from typing import Optional
from plcrex import __app_name__, __version__, _st2tree, _iec_checker, _xml_checker
from pathlib import Path
import typer
import colorama
import sys

app = typer.Typer()


@app.command("iec-checker")
def iec_checker(
        src: Path,
        verbo: bool = typer.Option(False, "-v", help="call iec-checker with '--verbose' OPTION"),
        qui: bool = typer.Option(False, "-q", help="call iec-checker with '--quiet' OPTION"),
        help_: bool = typer.Option(False, "--help_iec_checker", help="call iec-checker help")):
    if src.is_file():
        if src.suffix == '.st' or src.suffix == '.xml':
            # call iec-checker with ONE supported OPTIONS (only a subset is covered)
            if help_ and not (qui or verbo):
                _iec_checker.execution(src, '--help')
            elif qui and not (help_ or verbo):
                _iec_checker.execution(src, '--quiet')
            elif verbo and not (qui or help_):
                _iec_checker.execution(src, '--verbose')
            else:
                # default: verbose
                _iec_checker.execution(src, '--verbose')
            typer.echo("\n"+typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST/xml file found")
    raise typer.Exit()


@app.command("st2tree")
def st2tree(
        src: Path,
        txt: bool = typer.Option(False, "-txt", help="Enable *.txt export"),
        dot: bool = typer.Option(False, "-dot", help="Enable *.dot export")):
    if src.is_file():
        if src.suffix == '.st':
            _st2tree.translation(src, txt, dot)
            typer.echo("\n"+typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST file found")
    raise typer.Exit()


@app.command("xml-checker")
def xml_checker(
        src: Path,
        v201: bool = typer.Option(False, "-v201", help="use tc6_xml_v201.xsd"),
        v10: bool = typer.Option(False, "-v10", help="use tc6_xml_v10.xsd")):
    if src.is_file():
        if src.suffix == '.xml':
            if v201 and not v10:
                # tc6_xml_v201.xsd (https: // plcopen.org / downloads / plcopen-xml-version-201-xsd-file-0)
                _xml_checker.validate(src, "tc6_xml_v201.xsd")
                typer.echo("\n"+typer.style("Success!", fg=typer.colors.GREEN, bold=True))
            elif v10 and not v201:
                # tc6_xml_v10.xsd (Beremiz v1.2)
                _xml_checker.validate(src, "tc6_xml_v10.xsd")
                typer.echo("\n"+typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError()
    raise typer.Exit()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(None,"--version", "-v",callback=version_callback,is_eager=True)):
    return