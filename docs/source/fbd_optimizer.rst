FBD-Optimizer
=============

.. fbd_optimizer:

The FBD-Optimizer represents a feature for identifying and optimizing potentially optimizable submodels of real-world dataflow models, where the behavior of the instantiated function blocks is unknown and can be treated as a black box. The optimization approach is shown in figure below and involves configuration with respect
to Halstead’s metrics N (number of edges) ``--edge-opt``, N1 (number of operators) ``--op-opt``, and N2 (variable accesses) ``--var-opt``.

.. figure:: ../fig/fbd_optimizer_designflow_HL.png
    :align: center
    :width: 400px

**Usage**

.. code-block:: console

    python -m plcrex fbd-optimizer --help


.. code:: console

         Usage: plcrex fbd-optimizer [OPTIONS] SOURCE EXE EXPORT FILENAME

         FBD-Optimizer           *.xml → fbd2st → *.st → st2x → *.st/*.sctx

        ╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
        │ *    source        PATH  source path [default: None] [required]                                                                                          │
        │ *    exe           PATH  NuSMV.exe path [default: None] [required]                                                                                       │
        │ *    export        PATH  export path [default: None] [required]                                                                                          │
        │ *    filename      TEXT  filename without file extension [default: None] [required]                                                                      │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
        ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
        │ --edge-opt    --no-edge-opt      optimize edges [default: no-edge-opt]                                                                                   │
        │ --var-opt     --no-var-opt       optimize variables [default: no-var-opt]                                                                                │
        │ --op-opt      --no-op-opt        optimize operators [default: no-op-opt]                                                                                 │
        │ --help                           Show this message and exit.                                                                                             │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

..
    .. figure:: ../fig/fbd_optimizer_demo.png
        :align: center
        :width: 600px

|

POU ``Pollutant_Indicator_WITH_ERROR.xml``
------------------------------------------

The following POU was manually implemented using Beremiz [`.url <https://github.com/beremiz/beremiz>`_].

.. figure:: ../fig/Pollutant_Indicator_WITH_ERROR.png
    :align: center
    :width: 450px

|

Equivalent IEC 61131-3 ST representation using PLCreX's FBD-to-ST translation (``--backward`` ``--formal``)

.. code-block:: console

        ...
        OUT1 := OR(AND(NOT(IN3),NOT(IN2),IN1),AND(NOT(IN3),IN2,NOT(IN1),AND(IN3,NOT(IN2),NOT(IN1))));
        OUT2 := OR(AND(NOT(IN3),IN2,IN1),AND(IN3,NOT(IN2),IN1),AND(IN3,IN2,NOT(IN1)));
        OUT3 := AND(IN1,IN2,IN3);
        ...


Example 1: ``--edge-opt``
-------------------------

**Command**

.. code-block:: console

    python -m plcrex fbd-optimizer --edge-opt "tests/real_world_FBDs/Pollutant_Indicator_WITH_ERROR.xml" "bin/NuSMV.exe" ".\exports" "01"

**Results**

``01.st``

.. code-block:: console

        ...
        OUT1:=AND(IN1,NOT(IN2),NOT(IN3));
        OUT2:=SEL(IN1,NOT(EQ(IN3,IN2)),AND(IN2,IN3));
        OUT3:=AND(IN1,IN2,IN3);
        ...

Example 2: ``--op-opt``
-------------------------

**Command**

.. code-block:: console

    python -m plcrex fbd-optimizer --op-opt "tests/real_world_FBDs/Pollutant_Indicator_WITH_ERROR.xml" "bin/NuSMV.exe" ".\exports" "02"

**Results**

``02.st``

.. code-block:: console

        ...
        OUT1:=AND(IN1,NOT(IN2),NOT(IN3));
        OUT2:=SEL(IN1,SEL(IN2,NOT(IN3),IN3),AND(IN2,IN3));
        OUT3:=AND(IN1,IN2,IN3);
        ...

Example 3: ``--var-opt``
-------------------------

**Command**

.. code-block:: console

    python -m plcrex fbd-optimizer --var-opt "tests/real_world_FBDs/Pollutant_Indicator_WITH_ERROR.xml" "bin/NuSMV.exe" ".\exports" "03"

**Results**

``03.st``

.. code-block:: console

        ...
        OUT1:=AND(AND(IN1,NOT(IN2)),NOT(IN3));
        OUT2:=SEL(IN1,NOT(EQ(IN3,IN2)),AND(IN2,IN3));
        OUT3:=AND(IN1,IN2,IN3);
        ...
