from pathlib import Path
from subprocess import call


def execution(src: Path, option: str = '--quiet'):
    call([r'.\bin\iec_checker_Windows_x86_64_v0.4.exe', src, option])
    return