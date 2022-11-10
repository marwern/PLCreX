# PLCreX - a modular IEC 61131-3 PLC analysis CLI application

[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

PLCreX is a modular CLI application for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)), designed to support on topics such '**re**view', '**re**design', '**re**use', '**re**liability', and more.

This project is motivated by our research and will be extended by further features step by step. Together with integrated external tools, PLCreX represents a collection of numerous analysis and reuse features for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))), implemented in IEC 61131-3 Function Block Diagrams (FBDs) and Structured Text (ST).


## Quick links

* [PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) [![Documentation Status](https://readthedocs.org/projects/plcrex/badge/?version=latest)](https://plcrex.readthedocs.io/en/latest/?badge=latest)
* [Install PLCreX](#install-plcrex)
* [Test PLCreX](#test-plcrex) [![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)

* [Features](#features)
* [Issues and Contributing Guidelines](#issues-and-contributing-guidelines)
* [Licenses](#licenses) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
---

## Install PLCreX
See [PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) for further details.

1. Download or clone repository
2. Download IEC-Checker (.exe) from last [PLCreX Release](https://github.com/marwern/PLCreX/tags) or official [IEC Checker repository](https://github.com/jubnzv/iec-checker) and change `IEC_Checker_exe` path in `./config.ini` according to your local path
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

   
## Test PLCreX
See [PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) for further details.
Run the following command for some local tests and coverage report: 
>`(venv) C:\Python\plcrex_project>coverage run -m pytest ./tests/`

>`(venv) C:\Python\plcrex_project>coverage report -m`

# Features
The current version of PLCreX includes the features shown below, of which external tools are referenced accordingly.
Due to the architecture of PLCreX it is quite easy to integrate external tools and updates.
This means, topics related to external tools, like feature requests, bugs, discussions, etc. should be raised in the respective project and not in PLCreX. 
See [PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) for further details.

![Overview](https://user-images.githubusercontent.com/92115516/200553270-435c4607-2786-484a-8917-fe2819fc1595.svg)


## Quick links to PLCreX’s documentation
* [Print PLCreX Help](https://plcrex.readthedocs.io/en/latest/features.html#plcrex-help)
* [Print PLCreX Version](https://plcrex.readthedocs.io/en/latest/features.html#plcrex-version)
* [Static Analysis (IEC Checker)](https://plcrex.readthedocs.io/en/latest/iec_checker.html)
* [XML Validator (PLCopen XML Exchange Validator)](https://plcrex.readthedocs.io/en/latest/xml_checker.html)
* [FBD-to-ST Transpiler](https://plcrex.readthedocs.io/en/latest/fbd2st.html)
* [ST Parser](https://plcrex.readthedocs.io/en/latest/st2tree.html)


# Issues and Contributing Guidelines
Contributors are welcome. Please use GitHub Issues and use appropriate labels to prioritize tasks and track implementation progress. 

Pull requests should link to a specific issue in the comment. I think this keeps the repository well structured. Thanks a lot!


# Licenses
- PLCreX [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- IEC Checker v0.4  [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
- STgrammar_Beckhoff.lark ([Blark](https://github.com/klauer/blark) v0.5.0) [![License: GPL v2](https://img.shields.io/badge/License-GPLv2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0)
