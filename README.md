# PLCreX - a modular IEC 61131-3 PLC analysis CLI application

PLCreX is a modular CLI application for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)), designed to support on topics such '**re**view', '**re**design', '**re**use', '**re**liability', and more.

This project is motivated by our research and will be extended by further features step by step. Together with integrated external tools, PLCreX represents a collection of numerous analysis and reuse features for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))), implemented in IEC 61131-3 Function Block Diagrams (FBDs) and Structured Text (ST).


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
  * [FBD-to-ST Transpiler](#fbd-to-st-transpiler)
  * [ST Parser](#st-parser)
* [Licenses](#licenses)


### Setup PLCreX
1. Download or clone repository
2. Create a virtual environment in the project root directory: 
    >`C:\Python\plcrex_project>python -m venv venv`
3. Activate virtual environment:
   >`C:\Python\plcrex_project>venv\Scripts\activate.bat`
4. Install the dependencies (`requirements.txt`):
   >`(venv) C:\Python\plcrex_project>python -m pip install -r requirements.txt`



### Test PLCreX
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)


Run the following command for some local tests (and coverage report): 
>`(venv) C:\Python\plcrex_project>python -m pytest ./tests/`

>`(venv) C:\Python\plcrex_project>coverage run -m pytest ./tests/`

>`(venv) C:\Python\plcrex_project>coverage report -m`

```
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
plcrex\__init__.py              2      0   100%
plcrex\_fbd2st.py             231      0   100%
plcrex\_iec_checker.py          5      0   100%
plcrex\_st2tree.py             14      0   100%
plcrex\_xml_checker.py          7      0   100%
plcrex\cli.py                  56      1    98%   94
tests\__init__.py               0      0   100%
tests\test_fbd2st.py           25      0   100%
tests\test_help.py              6      0   100%
tests\test_iec_checker.py      33      0   100%
tests\test_st2tree.py          21      0   100%
tests\test_version.py          11      0   100%
tests\test_xml_checker.py      19      0   100%
---------------------------------------------------------
TOTAL                         430      1    99%
```



# Features
The current version of PLCreX includes the features shown below, of which external tools are referenced accordingly. Due to the architecture of PLCreX it is quite easy to integrate external tools and updates. This means, topics related to external tools, like feature requests, bugs, discussions, etc. should be raised in the respective project and not in PLCreX.

![Overview](https://user-images.githubusercontent.com/92115516/198993824-9993836e-e9de-4013-a244-ce3566e5b8f4.svg)

  * [Print PLCreX Help](#print-plcrex-help)
  * [Print PLCreX Version](#print-plcrex-version)
  * [Static Analysis (IEC Checker)](#iec-checker)
  * [XML Validator (PLCopen XML Exchange Validator)](#plcopen-xml-exchange-validator)
  * [FBD-to-ST Transpiler](#fbd-to-st-transpiler)
  * [ST Parser](#st-parser)

## Print PLCreX Help
<!--- Print PLCreX `--help` by command:--->
>`(venv) C:\Python\plcrex_project>python -m plcrex --help`


## Print PLCreX Version
<!--- Print PLCreXs' *version* by command: --->
>`(venv) C:\Python\plcrex_project>python -m plcrex --version`


# IEC Checker
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
    - L10: Usage of CONTINUE and EXIT instruction should be avoided
    - L17: Each IF instruction should have an ELSE clause
  + Declaration analysis for derived types
  + Intraprocedural control flow analysis: detection of unreachable code blocks inside the POUs
  + Detection of unused variables
  
Print IEC Checker `--help` to see all implemented features:
>`(venv) C:\Python\plcrex_project>python -m plcrex iec-checker --help`


### Example
###### .\tests\st_examples\TC083.st
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
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex iec-checker ".\tests\st_examples\TC083.st" -q`
###### Output
````
5:8 UnusedVariable: Found unused local variable: VAR3
8:12 ZeroDivision: Constant 19 is divided by zero!
3:8 PLCOPEN-CP3: Variable VAR1 shall be initialized before being used
4:8 PLCOPEN-CP3: Variable VAR2 shall be initialized before being used
5:8 PLCOPEN-CP3: Variable VAR3 shall be initialized before being used
Success!
````

# PLCopen XML Exchange Validator
The [PLCopen XML Exchange Validator](https://plcopen.org/technical-activities/xml-exchange) validates on basis of `tc6_xml_v201.xsd` and `tc6_xml_v10.xsd` whether the PLCopen XML exchange format meets the PLCopen specification.

Print PLCopen XML Exchange Validator `--help` to see all implemented features:

>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker --help`


### Example PASSED
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker ".\tests\plcopen_examples\TC001.xml" -v201`
###### Output
```
Success!
````

### Example FAILED <!--<font color="red">FAILED</font>-->
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex xml-checker ".\tests\plcopen_examples\TC001_failed.xml" -v201`

###### Output
```xml
Traceback (most recent call last):

...
xmlschema.validators.exceptions.XMLSchemaDecodeError: failed validating '2022-09-01 14:53:16' with XsdAtomicBuiltin(name='xs:dateTime'):
Reason: attribute modificationDateTime='2022-09-01 14:53:16': Invalid datetime string '2022-09-01 14:53:16' for <class 'elementpath.datatypes.datetime.DateTime10'>

Schema:
  <xs:simpleType xmlns:hfp="http://www.w3.org/2001/XMLSchema-hasFacetAndProperty" xmlns:xs="http://www.w3.org/2001/XMLSchema" name="dateTime" id="dateTime">
        ...
````

# FBD-to-ST Transpiler
The FBD-to-ST Transpiler translates FBDs stored in PLCopen XML format into equivalent ST POUs. The user can additionally run a static code analysis with [IEC Checker](#iec-checker).

##### Restrictions
- without database additional local variables are declared as 'BOOL' by default, unless the data type is implicit from the connections
- static code analysis with [IEC Checker](#iec-checker) expects a specific format. Functions like `AND(A,B)` will lead to parser errors and have to be changed by a subsequent code refactoring

Print FBD-to-ST Transpiler `--help` to see all implemented features:
>`(venv) C:\Python\plcrex_project>python -m plcrex fbd2st --help`

### Example (with static code analysis)
###### .\tests\plcopen_examples\TC004.xml
The following example was implemented manually using [Beremiz](https://github.com/beremiz/beremiz).
![TC004](https://user-images.githubusercontent.com/92115516/198979137-7562d3c1-1729-4a39-99f3-49c4dfb6ae62.PNG)
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex fbd2st ".\tests\plcopen_examples\TC004.xml" -static-tests`

###### ./exports/st/txt/TC004.xml.st
```
//--- This file was generated by PLCreX ---
//--- https://github.com/marwern/plcrex ---
//-----------------------------------------

FUNCTION_BLOCK TC004
        VAR_INPUT
                i1 : BOOL;
                i2 : BOOL := FALSE;
        END_VAR
        VAR_OUTPUT
                o1 : BOOL := FALSE;
        END_VAR
        VAR
                i3 : TIME := T#5s;
                i4 : TIME := T#2s;
                o4 : BOOL;
                TON0 : TON;
                TON1 : TON;
                TOF0 : TOF;
        END_VAR

        TON0(IN := i2,PT := i3);
        TOF0(IN := TON0.Q,PT := i4);
        TON1(IN := TOF0.Q,PT := i3);
        o4 := TON1.Q;
END_FUNCTION_BLOCK
```

###### Output
```
7:4 UnusedVariable: Found unused local variable: I1
...
16:4 PLCOPEN-CP3: Variable O4 shall be initialized before being used
Success!
```

### Example (without static code analysis)
###### .\tests\plcopen_examples\TC005_FB.xml
The following example was implemented manually using [Beremiz](https://github.com/beremiz/beremiz).
![TC005](https://user-images.githubusercontent.com/92115516/198979162-4cc887ca-9754-4223-b2f7-7e3e67fb7143.PNG)
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex fbd2st ".\tests\plcopen_examples\TC005_FB.xml"`

###### ./exports/st/txt/TC005_FB.xml.st
```
//--- This file was generated by PLCreX ---
//--- https://github.com/marwern/plcrex ---
//-----------------------------------------

FUNCTION_BLOCK TC005
        VAR_INPUT
                i1 : BOOL;
                i2 : BOOL := FALSE;
        END_VAR
        VAR_OUTPUT
                o1 : BOOL := FALSE;
                o2 : BOOL := FALSE;
        END_VAR
        VAR
                i3 : TIME := T#5s;
                o4 : BOOL;
                TON0 : TON;
                AND1_OUT : BOOL;
                XOR3_OUT : BOOL;
        END_VAR

        AND1_OUT := AND(i1,i2);
        XOR3_OUT := XOR(AND1_OUT,TON0.Q);
        TON0(IN := AND1_OUT,PT := i3);
        o1 := XOR3_OUT;
        o4 := TON0.Q;
END_FUNCTION_BLOCK
```

# ST Parser
The ST parser includes an executable grammar for IEC 61131-3 ST POUs as well as the possibility to save the resulting syntax tree visually or as plain text and reuse it for subsequent analysis. The embedded grammar includes the following constructs:
+ IEC 61131-3 POU-Types: `Program, Functionblock, Function`
+ Sections (each available only once): `VAR_INPUT, VAR, VAR_OUTPUT, VAR_IN_OUT, VAR_EXTERNAL`
+ Data types: `BOOL, INT, DINT, UINT, REAL, TIME, ARRAY`
+ Operators: `*, /, MOD, +, -, NOT, AND, XOR, OR, <=, >=, <, >, =, <>, FALSE, TRUE, external function/functionblocks, variable, constant`
+ Statements: `assignments, if/else, case, macro, for, while, repeat, exit, return`

Print ST Parser `--help` to see all implemented features:
>`(venv) C:\Python\plcrex_project>python -m plcrex st2tree --help`

### Example
###### .\tests\st_examples\TC081.st
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
###### Command
>`(venv) C:\Python\plcrex_project>python -m plcrex st2tree ".\tests\st_examples\TC081.st" -dot -txt`


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

<!--## Change tracking
This section summarizes the changes since the last release.
- [x] Feature: FBD-to-ST transpiler
- [x] Tests: FBD-to-ST compiler
-->

# Licenses
- PLCreX v0.2.1 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- IEC Checker v0.4  [![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
