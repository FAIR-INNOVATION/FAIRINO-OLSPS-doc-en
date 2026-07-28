Preamble
=========

.. toctree:: 
    :maxdepth: 5

Preamble
------------------

First of all, thank you very much for using our company's AIRLab software. Please read this product user manual carefully to ensure that you can use our product correctly and get the best experience. If you have any problems that are difficult to solve, please contact our after-sales personnel. We appreciate your support and trust and look forward to providing you with better service and products.


Environment and Version Management Requirements
------------------------------------------------

Applicable Robots and Version Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applicable robots: FR3, FR3-WMS, FR3-WML, FR5, FR5-WML, FR10, FR16, and FR20.

Applicable controller software versions: v3.8.2.11, v3.9.0, v3.9.4, v3.9.5, v3.9.6, v3.9.7, and v3.9.8. For compatibility with AIRLab, see Table 1-1.

.. table:: Compatibility Between AIRLab and Robot Controller Software Versions
   :align: center

   +--------------------+-------------------------------------+
   | AIRLab Version     | Robot Controller Software Version   |
   +====================+=====================================+
   | ≤ v1.2.0           | v3.9.0                              |
   +--------------------+-------------------------------------+
   | v1.3.0             | v3.9.4                              |
   +--------------------+-------------------------------------+
   | v1.4.0             | v3.9.5, v3.9.5.2                    |
   +--------------------+-------------------------------------+
   | v2.0.0             | v3.9.6                              |
   +--------------------+-------------------------------------+
   | v2.1.0             | v3.9.7                              |
   +--------------------+-------------------------------------+
   | v2.2.0             | v3.9.8                              |
   +--------------------+-------------------------------------+

Version Upgrade Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the current version is earlier than v1.2.0, refresh the system image by referring to the RD33-AIRLab System Image Installation and Factory Test Procedure-V1.1-2026.02.08.

If the current version is v1.2.0 or later, upgrade sequentially according to Table 1-2. Required intermediate versions must not be skipped. Before upgrading to v1.3.0 or v1.4.0, install the corresponding prerequisite package.

.. table:: General Version Upgrade Path
   :align: center

   +-------------------------+-------------------------+--------------------------------------------------+
   | Current Version         | Next Required Version   | Upgrade Method                                   |
   | Condition               |                         |                                                  |
   +=========================+=========================+==================================================+
   | < v1.2.0                | Refresh the system      | Refer to the system image installation and       |
   |                         | image                   | factory test procedure                           |
   +-------------------------+-------------------------+--------------------------------------------------+
   | < v1.3.0                | v1.3.0                  | Install the v1.3.0 prerequisite package, then    |
   |                         |                         | use the AIRLab upgrade function                  |
   +-------------------------+-------------------------+--------------------------------------------------+
   | < v1.4.0                | v1.4.0                  | Install the v1.4.0 prerequisite package, then    |
   |                         |                         | use the AIRLab upgrade function                  |
   +-------------------------+-------------------------+--------------------------------------------------+
   | < v2.0.0                | v2.0.0                  | Use the AIRLab upgrade function                  |
   +-------------------------+-------------------------+--------------------------------------------------+
   | < v2.1.0                | v2.1.0                  | Use the AIRLab upgrade function                  |
   +-------------------------+-------------------------+--------------------------------------------------+
   | < v2.2.0                | v2.2.0                  | Use the AIRLab upgrade function                  |
   +-------------------------+-------------------------+--------------------------------------------------+

Version Downgrade and Recovery Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AIRLab supports cross-version downgrades. To restore a specified version after a downgrade, upgrade sequentially according to Table 1-2. No required intermediate version or corresponding prerequisite package may be skipped.

Restore to v1.4.0: Install the v1.3.0 prerequisite package, v1.3.0, the v1.4.0 prerequisite package, and v1.4.0 in sequence.

Restore to v2.1.0: After completing the preceding steps, continue upgrading to v2.0.0 and then v2.1.0.
