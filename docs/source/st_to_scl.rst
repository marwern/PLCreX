ST-to-SCL Compiler
==================

.. st_to_scl:

The ST-to-SCL Compiler translates imperative sequential ST models to Sequentially Constructive Language (SCL) models.
The results are intended for reuse in model-based design and formal verification using `KIELER <https://rtsys.informatik.uni-kiel.de/confluence/
display/KIELER/Overview>`_ [1,2].

**Usage**

.. code-block:: console

    python -m plcrex st-to-scl --help


.. code:: console

         Usage: plcrex st-to-scl [OPTIONS] SOURCE EXPORT

         ST-to-SCL Compiler                      *.st → *.scl

        ╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
        │ *    source      PATH  source path [default: None] [required]                                │
        │ *    export      PATH  export path [default: None] [required]                                │
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

    python -m plcrex st-to-scl "tests/st_to_synchr_models/TC21.st" "exports/TC21.scl"

**Result**

``TC21.scl``

.. code-block:: console

    //--- This file was generated by PLCreX ---
    //--- https://github.com/marwern/PLCreX ---
    //-----------------------------------------

     module TC21{
     output int y;
     int x=1;
     int i;
     int i0=0;
     int i1=10;
     i=i0;
     do:
     y=i;
     pause;
     i=i+1;
     if(!(i>i1)){
     goto do;
    }else{
     y=x;
    }
    }
