Command Line Interface
======================

.. cli:

..
    .. figure:: ../fig/cli_demo.png
        :align: center
        :width: 600px

.. code:: console

        (venv) C:\PLCreX>python -m plcrex --help

         Usage: plcrex [OPTIONS] COMMAND [ARGS]...

        ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
        │ --version                                                                                                                                                │
        │ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                                 │
        │ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the installation.          │
        │                                                              [default: None]                                                                             │
        │ --help                                                       Show this message and exit.                                                                 │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
        ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
        │ fbd-optimizer                  FBD-Optimizer           *.xml → fbd2st → *.st → st2x → *.st/*.sctx                                                        │
        │ fbd-to-st                      FBD-to-ST Compiler      *.xml → fbd2st → *.st                                                                             │
        │ iec-checker                    IEC-Checker             *.st → iecchecker → *.log                                                                         │
        │ impact-analysis                I/O-Impact Analysis     *.xml → fbd2st → *.st → st2ia → *.dot                                                             │
        │ st-parser                      ST-Parser               *.st → st2ast → *.dot/*.txt                                                                       │
        │ test-case-gen                  Test-Case-Generator     FORMULA:str → ds2ts → stdout                                                                      │
        │ xml-validator                  XML-Validator           *.xml → xmlval → stdout                                                                           │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


|

Installed via PyPI
------------------

1. Run the following command to call PLCreX's help

.. code:: console

    python -m plcrex --help

Installed via GitHub
--------------------

1. Run the following command to activate virtual environment (venv)

.. code:: console

    run.bat

2. Run the following command to call PLCreX's help

.. code-block:: console

    python -m plcrex --help