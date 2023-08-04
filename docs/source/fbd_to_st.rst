FBD-to-ST Compiler
==================

.. fbd_to_st:

The FBD-to-ST Compiler translates IEC 61131-3 FBDs stored in PLCopen XML format into ST POUs. In this context, PLCreX supports the translation in different formats, which are shown in the following picture. In general, PLCreX distinguishes between a **formal** representation of the parameter list of instantiated POUs,
for example ``TONx(IN := A, PT := B);`` and a **non formal** representation, ``TONx(A,B);``. Furthermore, we distinguish between a **forward** translation strategy and a **backward** translation strategy.

.. note::
    It should be noted that in the backward translation strategy the semantics can be changed, since the assignment of outputs in this approach is done at the end of a cycle.


Command Line Interface
----------------------

.. code-block:: console

     Usage: plcrex fbd-to-st [OPTIONS] SRC EXPORT

    ┌─ Arguments ───────────────────────────────────────────────────────────────────────────┐
    │ *    src         PATH  [default: None] [required]                                     │
    │ *    export      PATH  [default: None] [required]                                     │
    └───────────────────────────────────────────────────────────────────────────────────────┘
    ┌─ Options ─────────────────────────────────────────────────────────────────────────────┐
    │ --bwd       --no-bwd         use backward translation [default: no-bwd]               │
    │ --formal    --no-formal      formal parameter list [default: no-formal]               │
    │ --help                       Show this message and exit.                              │
    └───────────────────────────────────────────────────────────────────────────────────────┘

Example: --formal --no-bwd
--------------------------
The following example was implemented manually using Beremiz [`.url <https://github.com/beremiz/beremiz>`_].

.. raw:: html

    <img src="https://user-images.githubusercontent.com/92115516/198979137-7562d3c1-1729-4a39-99f3-49c4dfb6ae62.PNG"></img>

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex fbd2st --formal ".\tests\plcopen_examples\TC004.xml"

    Parsing exports\st\TC004.xml_False_True_True_False.st ...
    Running check for function block TC004
    7:4 UnusedVariable: Found unused local variable: I1
    11:4 UnusedVariable: Found unused local variable: O1
    19:6 UnusedVariable: Found unused local variable: TOF0
    17:6 UnusedVariable: Found unused local variable: TON0
    18:6 UnusedVariable: Found unused local variable: TON1
    7:4 PLCOPEN-CP3: Variable I1 shall be initialized before being used
    19:6 PLCOPEN-CP3: Variable TOF0 shall be initialized before being used
    18:6 PLCOPEN-CP3: Variable TON1 shall be initialized before being used
    17:6 PLCOPEN-CP3: Variable TON0 shall be initialized before being used
    16:4 PLCOPEN-CP3: Variable O4 shall be initialized before being used
    Success!

Example: --no-formal --no-bwd
-----------------------------
Command and Result (``--no-formal``, ``--no-backward``, ``--no-iec-check``, ``--no-st-parser``, ``--no-impact-analysis``):

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex fbd2st ".\tests\plcopen_examples\TC005_PRG.xml"

    Success!

The following ``st`` file was created: ``./exports/st/txt/TC005_PRG.xml_False_False_False_False.st``

.. code-block:: console

    ...
            VAR
                    i3 : TIME := T#5s;
                    o4 : BOOL;
                    TON0 : TON;
                    AND1_OUT : BOOL;
                    XOR3_OUT : BOOL;
            END_VAR

            AND1_OUT := AND(i1,i2);
            TON0(AND1_OUT,i3);
            XOR3_OUT := XOR(AND1_OUT,TON0.Q);
            o1 := XOR3_OUT;
            o4 := TON0.Q;
    END_PROGRAM

.. note::
    Without database additional local variables needed for forward translation are declared as ``BOOL`` by default,
    unless the data type is implicit given by connected component. ST Parser is only compatible with
    non formal translation.

Example: --formal --bwd
-----------------------
The following example was implemented manually using `Beremiz <https://github.com/beremiz/beremiz>`_.

.. raw:: html

    <img src="https://user-images.githubusercontent.com/92115516/198979162-4cc887ca-9754-4223-b2f7-7e3e67fb7143.PNG"></img>

Example: --no-formal --bwd
--------------------------
Command and Result (``--no-formal``, ``--backward``, ``--no-iec-check``, ``--no-st-parser``, ``--no-impact-analysis``):

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex fbd2st --backward ".\tests\plcopen_examples\TC005_PRG.xml"

    Success!

The following ``st`` file was created: ``./exports/st/txt/TC005_PRG.xml_True_False_False_False.st``

.. code-block:: console

    ...
            VAR
                    i3 : TIME := T#5s;
                    o4 : BOOL;
                    TON0 : TON;
            END_VAR

            TON0(AND(i1,i2),i3);
            o1 := XOR(AND(i1,i2),TON0.Q);
            o4 := TON0.Q;
    END_PROGRAM