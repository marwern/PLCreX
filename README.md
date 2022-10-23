# PLCreX - a modular IEC 61131-3 PLC analysis CLI application

PLCreX is a modular CLI application for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)), designed to support on topics such '**re**view', '**re**design', '**re**use', '**re**liability', and more.

This project is motivated by our research and will be extended by further features step by step. Together with integrated external tools, PLCreX represents a collection of numerous analysis and reuse features for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))), implemented in IEC 61131-3 Function Block Diagrams (FBDs) and Structured Text (ST).

---
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg) 
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

### Quick links
* [Setup PLCreX](#setup-plcrex)
* [Test PLCreX](#test-plcrex)
* [Features](#features)
  * [Print PLCreX Help](#print-plcrex-help)
  * [Print PLCreX Version](#print-plcrex-version)
  * [IEC Checker](#iec-checker)
  * [PLCopen XML Exchange Validator](#plcopen-xml-exchange-validator)
  * [ST Parser](#st-parser)
* [Licenses](#licenses)

---

## Setup PLCreX
1. Download or clone repository
2. Create a virtual environment in the project root directory: 
    >`C:\Python\plcrex_project>python -m venv venv`
3. Activate virtual environment:
   >`C:\Python\plcrex_project>venv\Scripts\activate.bat`
4. Install the dependencies (`requirements.txt`):
   >`(venv) C:\Python\plcrex_project>python -m pip install -r requirements.txt`

---

## Test PLCreX
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)


Run the following command for some local tests: 
>`(venv) C:\Python\plcrex_project>python -m pytest tests/`

###### Coverage report
>`(venv) C:\Python\plcrex_project>coverage run -m pytest tests/`

>`(venv) C:\Python\plcrex_project>coverage report -m`
```
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
plcrex\__init__.py              2      0   100%
plcrex\_iec_checker.py          5      0   100%
plcrex\_st2tree.py             14      0   100%
plcrex\_xml_checker.py          7      0   100%
plcrex\cli.py                  48      1    98%   63
tests\__init__.py               0      0   100%
tests\test_help.py              6      0   100%
tests\test_iec_checker.py      33      0   100%
tests\test_st2tree.py          21      0   100%
tests\test_version.py          11      0   100%
tests\test_xml_checker.py      19      0   100%
---------------------------------------------------------
TOTAL                         166      1    99%
```

---

## Features
The current version of PLCreX includes the features below, of which external tools are referenced accordingly. Due to the architecture of PLCreX it is quite easy to integrate external tools and updates. This means, topics related to external tools, like feature requests, bugs, discussions, etc. should be raised in the respective project and not in PLCreX.

---

### Print PLCreX Help
<!--- Print PLCreX `--help` by command:--->

>`(venv) C:\Python\plcrex_project>python -m plcrex --help`
```
Usage: PLCreX [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version
  --help                          Show this message and exit.

Commands:
  iec-checker
  st2tree
  xml-checker
```

---

### Print PLCreX Version
<!--- Print PLCreXs' *version* by command: --->

>`(venv) C:\Python\plcrex_project>python -m plcrex --version`

```
PLCreX v0.0.1
```

---

### IEC Checker
The [IEC Checker](https://github.com/jubnzv/iec-checker) is an external open source tool for static code analysis of IEC 61131-3 POUs. It is integrated in this project with following features:

  + [PLCOpen Guidelines](https://plcopen.org/software-construction-guidelines) checks:
    - CP1: Access to a member shall be by name
    - CP2: All code shall be used in the application
    - CP3: All variables shall be initialized before being used
    - CP4: Direct addressing should not overlap
    - CP6: Avoid external variables in functions, function blocks and classes
    - CP8: Floating point comparison shall not be equality or inequality
    - CP9: Limit the complexity of POU code
    - CP13: POUs shall not call themselves directly or indirectly
    - CP25: Data type conversion should be explicit
    - CP28: Time and physical measures comparisons shall not be equality or inequality
    - L10: Usage of CONTINUE and EXIT instruction should be avoid
    - L17: Each IF instruction should have an ELSE clause
  + Declaration analysis for derived types
  + Intraprocedural control flow analysis: detection of unreachable code blocks inside the POUs
  + Detection of unused variables
  
Print IEC Checker `--help` to see all implemented features:
>`(venv) C:\Python\plcrex_project>python -m plcrex iec-checker --help`

```
Usage: PLCreX iec-checker [OPTIONS] SRC

Arguments:
  SRC  [required]

Options:
  -v                  call iec-checker with '--verbose' OPTION  [default: False]
  -q                  call iec-checker with '--quiet' OPTION  [default: False]
  --help_iec_checker  call iec-checker help  [default: False]
  --help              Show this message and exit.
```

###### Example
````
01| PROGRAM TC083
02|   VAR_ACCESS
03|     Var1 : DINT;
04|     Var2 : DINT;
05|     Var3 : DINT;
06|   END_VAR
07| 
08|   Var1 := 19 / 0;
09|   Var2 := Var1 / 1;
10| END_PROGRAM
````

>`(venv) C:\Python\plcrex_project>python -m plcrex iec-checker ".\tests\st_examples\TC083.st" -q`
````
5:8 UnusedVariable: Found unused local variable: VAR3
8:12 ZeroDivision: Constant 19 is divided by zero!
3:8 PLCOPEN-CP3: Variable VAR1 shall be initialized before being used
4:8 PLCOPEN-CP3: Variable VAR2 shall be initialized before being used
5:8 PLCOPEN-CP3: Variable VAR3 shall be initialized before being used
Success!
````

----------------
### PLCopen XML Exchange Validator
The [PLCopen XML Exchange Validator](https://plcopen.org/technical-activities/xml-exchange) validates on basis of `tc6_xml_v201.xsd` and `tc6_xml_v10.xsd` whether the PLCopen XML exchange format meets the PLCopen specification.

Print PLCopen XML Exchange Validator `--help` to see all implemented features:

>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker --help`
```
Usage: PLCreX xml-checker [OPTIONS] SRC

Arguments:
  SRC  [required]

Options:
  -v201   use tc6_xml_v201.xsd  [default: False]
  -v10    use tc6_xml_v10.xsd  [default: False]
  --help  Show this message and exit.
```

###### Example <font color="green">PASSED</font>
>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker ".\tests\plcopen_examples\TC001.xml" -v201`
```
Success!
````

###### Example <font color="red">FAILED</font>
>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker ".\tests\plcopen_examples\TC001_failed.xml" -v201`
```xml
Traceback (most recent call last):

...
xmlschema.validators.exceptions.XMLSchemaDecodeError: failed validating '2022-09-01 14:53:16' with XsdAtomicBuiltin(name='xs:dateTime'):
Reason: attribute modificationDateTime='2022-09-01 14:53:16': Invalid datetime string '2022-09-01 14:53:16' for <class 'elementpath.datatypes.datetime.DateTime10'>

Schema:
  <xs:simpleType xmlns:hfp="http://www.w3.org/2001/XMLSchema-hasFacetAndProperty" xmlns:xs="http://www.w3.org/2001/XMLSchema" name="dateTime" id="dateTime">
        ...
````

----------------
### ST Parser
The ST parser includes an executable grammar for IEC 61131-3 ST POUs as well as the possibility to save the resulting syntax tree visually or as plain text and reuse it for subsequent analysis. The embedded grammar includes the following constructs:
+ IEC 61131-3 POU-Types: `Program, Functionblock, Function`
+ Sections (each available only once): `VAR_INPUT, VAR, VAR_OUTPUT, VAR_IN_OUT, VAR_EXTERNAL`
+ Data types: `BOOL, INT, DINT, UINT, REAL, TIME, ARRAY`
+ Operators: `*, /, MOD, +, -, NOT, AND, XOR, OR, <=, >=, <, >, =, <>, FALSE, TRUE, external function/functionblocks, variable, constant`
+ Statements: `assignments, if/else, case, macro, for, while, repeat, exit, return`

Print ST Parser `--help` to see all implemented features:
>`(venv) C:\Python\plcrex_project>python -m plcrex st2tree --help`
```
Usage: PLCreX st2tree [OPTIONS] SRC

Arguments:
  SRC  [required]

Options:
  -txt    Enable *.txt export  [default: False]
  -dot    Enable *.dot export  [default: False]
  --help  Show this message and exit.
```

###### Example

````
01| FUNCTION_BLOCK TC081
02|   VAR_INPUT
03|     IN1 : INT;
04|     IN2 : INT;
05|     IN3 : INT;
06|     IN4 : BOOL;
07|   END_VAR
08|   VAR_OUTPUT
09|     Wrn : BOOL;
10|     Err : BOOL;
11|     Ctr : INT;
12|     iOut2 : INT;
13|   END_VAR
14|   VAR
15|     SR1 : SR;
16|     TON1 : TON;
17|     TON2 : TON;
18|   END_VAR
19|   
20|   SR1(((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100),IN4);
21|   TON1((((((20*IN1)+(6*IN2)+IN3))=(100*2)) AND (IN1+IN2+IN3=100)),2);
22|   TON2((IN1+IN2+IN3=42) AND SR1.Q,3);
23|   Ctr := TON2.ET;
24|   Err := TON1.Q;
25|   Wrn := SR1.Q;
26| END_FUNCTION_BLOCK
````

>`(venv) C:\Python\plcrex_project>python -m plcrex st2tree ".\tests\st_examples\TC081.st" -dot -txt`
```
Success!
```

###### ./exports/tree/dot/TC081.st.dot
![TC081](https://user-images.githubusercontent.com/92115516/197394792-e7ef807f-0d39-4b74-b0db-e43d4b38b1b8.svg)

###### ./exports/tree/txt/TC081.st.txt
```
start
  module
    name	TC081
    idcl
      var_input
        dcllist
          declaration
            variable	IN1
            datatype	INT
          declaration
            variable	IN2
            datatype	INT
          declaration
            variable	IN3
            datatype	INT
          declaration
            variable	IN4
            datatype	BOOL
      var_output
        dcllist
          declaration
            variable	Wrn
            datatype	BOOL
          declaration
            variable	Err
            datatype	BOOL
          declaration
            variable	Ctr
            datatype	INT
          declaration
            variable	iOut2
            datatype	INT
    vdcl
      var_local
        dcllist
          declaration
            variable	SR1
            datatype
              macro_name	SR
          declaration
            variable	TON1
            datatype
              macro_name	TON
          declaration
            variable	TON2
            datatype
              macro_name	TON
    statlist
      statement
        macro
          SR1
          and
            equalitiy
              adding
                adding
                  multiply_with
                    constant	20
                    variable	IN1
                  multiply_with
                    constant	6
                    variable	IN2
                variable	IN3
              multiply_with
                constant	100
                constant	2
            equalitiy
              adding
                adding
                  variable	IN1
                  variable	IN2
                variable	IN3
              constant	100
          variable	IN4
      statement
        macro
          TON1
          and
            equalitiy
              adding
                adding
                  multiply_with
                    constant	20
                    variable	IN1
                  multiply_with
                    constant	6
                    variable	IN2
                variable	IN3
              multiply_with
                constant	100
                constant	2
            equalitiy
              adding
                variable	IN1
                adding
                  variable	IN2
                  variable	IN3
              constant	100
          constant	2
      statement
        macro
          TON2
          equalitiy
            adding
              adding
                variable	IN1
                variable	IN2
              variable	IN3
            and
              constant	42
              variable	SR1
              macro_out	Q
          constant	3
      statement
        immediate_assignment
          variable	Ctr
          macro
            TON2
            equalitiy
              adding
                adding
                  variable	IN1
                  variable	IN2
                variable	IN3
              and
                constant	42
                variable	SR1
                macro_out	Q
            constant	3
            macro_out	ET
      statement
        immediate_assignment
          variable	Err
          variable	TON1
          macro_out	Q
      statement
        immediate_assignment
          variable	Wrn
          variable	SR1
          macro_out	Q
```

<!---![diagram-20220810](https://user-images.githubusercontent.com/92115516/183861475-20193d0d-9102-4257-932a-40e32f06ad96.png)--->

### Licenses
- PLCreX v0.0.1 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- IEC Checker v0.4  [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)





