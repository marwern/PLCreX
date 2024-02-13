Command Line Interface
======================

.. cli:


.. code:: console

     Usage: plcrex [OPTIONS] COMMAND [ARGS]...

    ╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
    │ --version                                                                                    │
    │ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the      │
    │                                                              specified shell.                │
    │                                                              [default: None]                 │
    │ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the         │
    │                                                              specified shell, to copy it or  │
    │                                                              customize the installation.     │
    │                                                              [default: None]                 │
    │ --help                                                       Show this message and exit.     │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────╯
    ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────╮
    │ fbd-to-sctx          FBD-to-SCCharts Compiler (Data-Flow)    *.xml → *.sctx                  │
    │ fbd-to-st            FBD-to-ST Compiler                      *.xml → *.st                    │
    │ fbd-to-st-ext        FBD-to-ST Compiler (extended)           *.xml → *.st                    │
    │ iec-check            IEC-Checker                             *.st → *.log                    │
    │ impact-analysis      I/O-Impact Analysis                     *.xml → *.dot                   │
    │ st-parser            ST-Parser                               *.st → *.dot/*.txt              │
    │ st-to-qrz            ST-to-Quartz Compiler                   *.st → *.qrz                    │
    │ st-to-scl            ST-to-SCL Compiler                      *.st → *.scl                    │
    │ st-to-sctx           ST-to-SCCharts Compiler (Control-Flow)  *.st → *.sctx                   │
    │ test-case-gen        Test-Case-Generator                     stdin → stdout                  │
    │ xml-validator        XML-Validator                           *.xml → stdout                  │
    ╰──────────────────────────────────────────────────────────────────────────────────────────────╯


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