ST Parser
=====

.. st2tree:

The ST parser includes an executable grammar for IEC 61131-3 ST POUs as well as the possibility to save the
resulting syntax tree visually or as plain text and reuse it for subsequent analysis.
The embedded grammar covers the following constructs:

* IEC 61131-3 POU-Types: ``Program``, ``Functionblock``, ``Function``
* Sections (each available only once): ``VAR_INPUT``, ``VAR``, ``VAR_OUTPUT``, ``VAR_IN_OUT``, ``VAR_EXTERNAL``
* Data types: ``BOOL``, ``INT``, ``DINT``, ``UINT``, ``REAL``, ``TIME``, ``ARRAY``
* Operators: ``*``, ``/``, ``MOD``, ``+``, ``-``, ``NOT``, ``AND``, ``XOR``, ``OR``, ``<=``, ``>=``, ``<``, ``>``, ``=``, ``<>``, ``FALSE``, ``TRUE``, ``external function/functionblocks``, ``variable``, ``constant````
* Statements: ``assignments``, ``if/else``, ``case``, ``macro``, ``for``, ``while``, ``repeat``, ``exit``, ``return``
* Parameter list: informal, e.g. ``TONx(A,B);`` instead of ``TONx(IN := A, PT := B);``

Print help of ST Parser with ``COMMAND`` ``st2tree`` and ``[OPTIONS]`` ``--help`` to see all features and usage:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex st2tree --help

    Usage: PLCreX st2tree [OPTIONS] SRC

    Arguments:
      SRC  [required]

    Options:
      --txt / --no-txt  tree export as *.txt  [default: True]
      --dot / --no-dot  tree export as *.dot  [default: True]
      --help            Show this message and exit.

.. note::
    ``txt`` and ``dot`` are ``true`` by default. If you don't want to generate them, this must be reset with the options
    ``--no-txt`` and ``--no-dot`` options respectively.


.. st_example:

Example: TC081.st
----

.. code-block:: console

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


Command and Result:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex st2tree ".\tests\st_examples\TC081.st"

    Success!

The following ``dot`` file was created: ``./exports/tree/dot/TC081.st.dot``

.. raw:: html

    <img src="https://user-images.githubusercontent.com/92115516/200537632-9b172dab-7853-45e1-91bb-7ba6c352a5bf.svg"></img>



The following ``txt`` file was created: ``./exports/tree/txt/TC081.st.txt``

.. code-block:: console

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
