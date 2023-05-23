Welcome to PLCreX's documentation!
===================================

PLCreX is a modular command-line interface (CLI) application for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)), designed to support on topics such '**re**view', '**re**design', '**re**use', '**re**liability', and more.

This project is motivated by our research and new features will be added incrementally. Together with external tools, PLCreX represents a collection of numerous analysis and reuse features for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))), implemented in Function Block Diagrams (FBDs) and Structured Text (ST).

.. note::
    The PLCreX GitHub-Repository is located at `github.com/marwern/PLCreX <https://github.com/marwern/PLCreX>`_

..
    ..  toctree::
        :glob:
        :titlesonly:

        *


..  toctree::
    :caption: Getting Started
    :maxdepth: 1

    setup

..  toctree::
    :caption: Features & Examples
    :maxdepth: 1

    features
    xml_checker
    iec_checker
    st2tree
    fbd2st
    test_case_gen