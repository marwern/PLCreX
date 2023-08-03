PLCreX - Analysis of IEC 61131-3 Program Organization Units
===========================================================

About PLCreX
------------

PLCreX is a modular command-line interface application tailored for IEC 61131-3 `Programmable Logic Controllers <https://en.wikipedia.org/wiki/Programmable_logic_controller>`_ (PLCs). It's designed with a focus on issues such as review, redesign, reuse, and reliability, among others. This project is driven by our ongoing research and we're committed to progressively integrating new features. PLCreX serves as a comprehensive suite of analysis and reuse capabilities for existing IEC 61131-3 `Program Organization Units <https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU)>`_ (POUs) implemented in Function Block Diagrams (FBDs) or Structured Text (ST).

.. figure:: ../fig/overview.svg
   :align: center
   :width: 700px


Command-Line Interface
----------------------
PLCreX is used via command line.

.. figure:: ../fig/cli_intro.png
   :align: center
   :width: 500px


..
    ..  toctree::
        :glob:
        :titlesonly:

        *

.. toctree::
    :maxdepth: 2
    :caption: Getting Started
    :hidden:

    install
    test
   
.. toctree::
    :maxdepth: 2
    :caption: Usage and Examples
    :hidden:
   
    fbd_to_st
    iec_checker
    impact_analysis
    st_parser
    test_case_gen
    xml_validator
    combinations

.. toctree::
    :maxdepth: 2
    :caption: Additional Resources
    :hidden:

    publications

    contact