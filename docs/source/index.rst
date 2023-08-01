Welcome to PLCreX's documentation!
===================================

PLCreX is a modular command-line interface (CLI) application tailored for IEC 61131-3 `Programmable Logic Controllers <https://en.wikipedia.org/wiki/Programmable_logic_controller>`_ (PLCs). It's designed with a focus on issues such as review, redesign, reuse, and reliability, among others. This project is driven by our ongoing research and we're committed to progressively integrating new features. PLCreX serves as a comprehensive suite of analysis and reuse capabilities for existing IEC 61131-3 `Program Organization Units <https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU)>`_ (POUs) implemented in Function Block Diagrams (FBDs) or Structured Text (ST).

..
    ..  toctree::
        :glob:
        :titlesonly:

        *

..  toctree::
    ..:caption: 🛠 Getting Started
    ..:maxdepth: 1

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
    test_case_gen
    test