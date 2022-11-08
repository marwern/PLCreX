IEC Checker
=====

.. iec_checker:

The `IEC Checker <https://github.com/jubnzv/iec-checker>`_ is an external open source tool for static code
analysis of IEC 61131-3 POUs. Print help of IEC Checker with ``COMMAND`` ``iec-checker`` and
``[OPTIONS]`` ``--help`` to see all features and usage:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex iec-checker --help

    Usage: PLCreX iec-checker [OPTIONS] SRC

    Arguments:
      SRC  [required]

    Options:
      --verbose / --no-verbose  print full log  [default: False]
      --help_iec_checker        call iec-checker help  [default: False]
      --help                    Show this message and exit.


* `PLCOpen Guidelines <https://plcopen.org/software-construction-guidelines>`_
    * CP1: Access to a member shall be by name
    * CP2: All code shall be used in the application
    * CP3: All variables shall be initialized before being used
    * CP4: Direct addressing should not overlap
    * CP6: Avoid external variables in functions, function blocks and classes
    * CP8: Floating point comparison shall not be equality or inequality
    * CP9: Limit the complexity of POU code
    * CP13: POUs shall not call themselves directly or indirectly
    * CP25: Data type conversion should be explicit
    * CP28: Time and physical measures comparisons shall not be equality or inequality
    * L10: Usage of CONTINUE and EXIT instruction should be avoided
    * L17: Each IF instruction should have an ELSE clause
* Declaration analysis for derived types
* Intraprocedural control flow analysis: detection of unreachable code blocks inside the POUs
* Detection of unused variables

.. note::
    IEC Checker can only work with ST supported by the `matiec <https://github.com/beremiz/matiec>`_ compiler.
    Most likely, it will fail on the source code containing non-standard language extensions.


.. iec_example:

Example: TC083.st
----

.. code-block:: console

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


Command and Result:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex iec-checker --verbose ".\tests\st_examples\TC083.st"

    Parsing tests\st_examples\TC083.st ...
    Running check for program TC083
    5:8 UnusedVariable: Found unused local variable: VAR3
    8:12 ZeroDivision: Constant 19 is divided by zero!
    3:8 PLCOPEN-CP3: Variable VAR1 shall be initialized before being used
    4:8 PLCOPEN-CP3: Variable VAR2 shall be initialized before being used
    5:8 PLCOPEN-CP3: Variable VAR3 shall be initialized before being used
    Success!
