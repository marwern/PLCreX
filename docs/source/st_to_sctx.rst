ST-to-SCCharts Compiler
=======================

.. st_to_sctx:

The ST-to-SCCharts Compiler translates imperative sequential ST models to Sequentially Constructive Statecharts (SCCharts).
The results are intended for reuse in model-based design and formal verification using `KIELER <https://rtsys.informatik.uni-kiel.de/confluence/
display/KIELER/Overview>`_ [1,2].

**Usage**

.. code-block:: console

    python -m plcrex st-to-sctx --help


.. code:: console

     Usage: plcrex st-to-sctx [OPTIONS] SOURCE EXPORT BAT_DIR

     ST-to-SCCharts Compiler (Control-Flow)  *.st → *.sctx

    ╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
    │ *    source       PATH  source path [default: None] [required]                               │
    │ *    export       PATH  export path [default: None] [required]                               │
    │ *    bat_dir      PATH  kicodia-win.bat path [default: None] [required]                      │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
    │ --help          Show this message and exit.                                                  │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────╯

|

Example: ``REPEAT-UNTIL`` loop
------------------------------------------

The following POU was manually implemented using Beremiz [`.url <https://github.com/beremiz/beremiz>`_].

.. code-block:: console

    FUNCTION_BLOCK TC21
      VAR_OUTPUT
        y : INT;
      END_VAR
      VAR
        x : INT := 1;
        i : INT;
        i0 : INT := 0;
        i1 : INT := 10;
      END_VAR

      i:=i0;
      REPEAT
        y := i;
        i := i+1;
      UNTIL i>i1
      END_REPEAT;
      y := x;
    END_FUNCTION_BLOCK

|


**Command**

.. code-block:: console

    python -m plcrex st-to-sctx "tests/st_to_synchr_models/TC21.st" "exports/TC21.sctx" "./bin\kicodia-win.bat"

**Result**

``TC21.sctx``

.. code-block:: console

    scchart TC21 {
        output int y
        int x
        int i
        int i0
        int i1

        region region0 {
            initial state state1
            immediate do i1 = 10; i0 = 0; x = 1; i = i0 go to state5

            state state5
            immediate do y = i go to state6

            state state6
            do i = i + 1 go to state9

            state state9
            immediate if !(i > i1) go to state5
            immediate do y = x go to finalState10

            final state finalState10
        }
    }

.. figure:: ../fig/TC21.png
        :align: center
        :width: 300px


|