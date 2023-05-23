# PLCreX - a modular IEC 61131-3 PLC analysis CLI application

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

PLCreX is a modular command-line interface (CLI) application for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)), designed to support on topics such '**re**view', '**re**design', '**re**use', '**re**liability', and more.

This project is motivated by our research and new features will be added incrementally. Together with external tools, PLCreX represents a collection of numerous analysis and reuse features for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))), implemented in Function Block Diagrams (FBDs) and Structured Text (ST). The current version comes with features shown below. The modular architecture of PLCreX allows easy integration of external tools and updates. This means, topics related to external tools, like feature requests, bugs, discussions, etc. should be raised in the respective project and not in PLCreX. See [PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) for further details.

![PLCreX_overview](https://github.com/marwern/PLCreX/assets/92115516/31957c5f-8db9-4a45-8ee3-4333a47df43e)

## Quick links

* [📄 PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) [![Documentation Status](https://readthedocs.org/projects/plcrex/badge/?version=latest)](https://plcrex.readthedocs.io/en/latest/?badge=latest)
  * [PLCreX Help](https://plcrex.readthedocs.io/en/latest/features.html#plcrex-help)
  * [FBD-to-ST Compiler](https://plcrex.readthedocs.io/en/latest/fbd2st.html)
  * [Impact Analysis](xxx)
  * [XML Validator](https://plcrex.readthedocs.io/en/latest/xml_checker.html)
  * [Static Analysis](https://plcrex.readthedocs.io/en/latest/iec_checker.html)
  * [ST Parser](https://plcrex.readthedocs.io/en/latest/st2tree.html)
  * [Test Case Generator](https://plcrex.readthedocs.io/en/latest/test_case_gen.html)
* [🛠 Installation](#-installation)
* [🔎 Test](#-test) [![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)
* [💻 Commands](#-commands)
* [ℹ️ Issues and Contributing Guidelines](#-issues-and-contributing-guidelines)
* [ℹ️ Licenses](#-licenses) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
---

## 🛠 Installation
1. Download or clone PLCreX repository
2. Install [Python](https://www.python.org/downloads/) (version 3.10 needed)
3. Download IEC-Checker (.exe) from last [PLCreX Release](https://github.com/marwern/PLCreX/tags) or official [IEC Checker repository](https://github.com/jubnzv/iec-checker) and change `IEC_Checker_exe` path in `./config.ini` according to your local path
    ```console
    [IEC-Checker]
    IEC_Checker_exe = .\bin\iec_checker_Windows_x86_64_v0.4.exe
    ```
3. Create a virtual environment in the project root directory: 
    >`C:\Python\plcrex_project>python -m venv venv`
4. Activate virtual environment:
   >`C:\Python\plcrex_project>venv\Scripts\activate.bat`
5. Install the dependencies (`requirements.txt`):
   >`(venv) C:\Python\plcrex_project>python -m pip install -r requirements.txt`

| ℹ️ Run ``install.bat`` to automatically create a virtual environment and install the dependencies |
|---------------------------------------------------------------------------------------------------|
  
## 🔎 Test
Run the following command for some local tests and coverage report: 
>`(venv) C:\Python\plcrex_project>coverage run -m pytest ./tests/`

>`(venv) C:\Python\plcrex_project>coverage report -m`

Results: [![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)

    Name                           Stmts   Miss  Cover   Missing
    ------------------------------------------------------------
    docs\source\__init__.py            0      0   100%
    docs\source\conf.py               22      0   100%
    plcrex\__init__.py                 0      0   100%
    plcrex\_fbd2st.py                278      0   100%
    plcrex\_fbd_io_checker.py        177      0   100%
    plcrex\_iec_checker.py            11      1    91%   33
    plcrex\_spec2test.py               5      1    80%   24
    plcrex\_st2tree.py                17      0   100%
    plcrex\_xml_checker.py             7      0   100%
    plcrex\cli.py                     57      3    95%   29-30, 99
    tests\__init__.py                  0      0   100%
    tests\test_fbd2st.py              93      0   100%
    tests\test_fbd_io_checker.py       7      0   100%
    tests\test_help.py                 6      0   100%
    tests\test_iec_checker.py         29      0   100%
    tests\test_st2tree.py             25      0   100%
    tests\test_version.py             12      0   100%
    tests\test_xml_checker.py         19      0   100%
    ------------------------------------------------------------
    TOTAL                            765      5    99%

# 💻 Commands
Run ``python -m plcrex [OPTIONS] COMMAND``

* PLCreX Help

        Usage: plcrex [OPTIONS] COMMAND [ARGS]...

        Options:
          -v, --version
          --install-completion [bash|zsh|fish|powershell|pwsh]
                                          Install completion for the specified shell.
          --show-completion [bash|zsh|fish|powershell|pwsh]
                                          Show completion for the specified shell, to
                                          copy it or customize the installation.
        
          --help                          Show this message and exit.
        
        Commands:
          fbd2st
          iec-checker
          st2tree
          test-case-gen
          xml-checker

* FBD-to-ST Compiler & Impact Analysis

        Usage: plcrex fbd2st [OPTIONS] SRC

        Arguments:
          SRC  [required]
        
        Options:
          --iec-check / --no-iec-check    run IEC Checker  [default: False]
          --formal / --no-formal          formal parameter list  [default: False]
          --backward / --no-backward      use backward translation  [default: False]
          --st-parser / --no-st-parser    run ST parser with exports  [default: False]
          --impact-analysis / --no-impact-analysis
                                          check I/O impact analysis  [default: False]
          --help                          Show this message and exit.

* Static Analysis

        Usage: plcrex iec-checker [OPTIONS] SRC
        
        Arguments:
          SRC  [required]
        
        Options:
          --verbose / --no-verbose  print full log  [default: False]
          --help_iec_checker        call iec-checker help  [default: False]
          --help                    Show this message and exit.

* ST Parser

      Usage: plcrex st2tree [OPTIONS] SRC
    
      Arguments:
        SRC  [required]
    
      Options:
        --txt / --no-txt            tree export as *.txt  [default: True]
        --dot / --no-dot            tree export as *.dot  [default: True]
        --beckhoff / --no-beckhoff  use Beckhoff TwinCAT ST grammar  [default:
                                    False]
    
        --help                      Show this message and exit.

* Test Case Generator

        Usage: plcrex test-case-gen [OPTIONS] FORMULA
        
          Arguments:
            FORMULA  [required]
        
          Options:
            --help  Show this message and exit.
      

* XML Validator

        Usage: plcrex xml-checker [OPTIONS] SRC

        Arguments:
          SRC  [required]
        
        Options:
          --v201 / --no-v201  use tc6_xml_v201.xsd  [default: False]
          --help              Show this message and exit.


# ℹ️ Issues and Contributing Guidelines
Contributors are welcome. Please use GitHub Issues and use appropriate labels to prioritize tasks and track implementation progress. 

Pull requests should link to a specific issue in the comment. We think this keeps the repository well-structured. Thanks a lot!


# ℹ️ Licenses
- PLCreX [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- IEC Checker v0.4  [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
- STgrammar_Beckhoff.lark ([Blark](https://github.com/klauer/blark) v0.5.0) [![License: GPL v2](https://img.shields.io/badge/License-GPLv2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0)
