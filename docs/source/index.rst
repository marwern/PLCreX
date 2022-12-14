Welcome to PLCreX's documentation!
===================================

PLCreX is a modular CLI application for IEC 61131-3
`Programmable Logic Controllers <https://en.wikipedia.org/wiki/Programmable_logic_controller>`_ (PLCs),
designed to support on topics such review, redesign, reuse, reliability, and much more (**reX**).

This project is motivated by our research and will be extended by further features step by step.
Together with integrated external tools, PLCreX represents a collection of numerous analysis and
reuse features for existing IEC 61131-3
`Program Organization Units <https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU)>`_ (POUs),
implemented in IEC 61131-3 Function Block Diagrams (FBDs) and Structured Text (ST).

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
    test

..  toctree::
    :caption: Features & Examples
    :maxdepth: 1

    features
    xml_checker
    iec_checker
    st2tree
    fbd2st