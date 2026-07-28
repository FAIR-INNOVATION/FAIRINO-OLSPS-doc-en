Version V2.2.0
===================
Date: 2026-07-27

.. toctree::
    :maxdepth: 5


- Added support for multi-layer multi-pass and weaving welding processes for spline welds;
    Path: AIRLab Software Analysis -> Pop-Ups and Other Pages -> Welding Seam Edit Pop-up Window

    Description: Added support for multi-layer multi-pass and weaving processes for spline curves; added smooth orientation interpolation to eliminate jerky transitions between segments; introduced a weld seam local coordinate system to make multi-layer multi-pass programming more intuitive and convenient.

- Added weld seam database generation based on OCC parsing and prior weld seam information;
    Path: AIRLab Software Analysis -> Engineering Module Analysis -> Model Construction

    Description: Enables rapid conversion from models to data. After a model is imported and prior information (such as length and arc length) is configured, the system can automatically parse the model and generate a weld seam database, eliminating tedious manual data entry.

- Added node editing;
    Path: AIRLab Software Analysis -> Engineering Module Analysis -> Fine Positioning

    Description: Eliminates the need to delete and recreate nodes. Once a node has been added, it can be modified and adjusted at any time, making program optimization more flexible and significantly improving efficiency.

- Optimized the description of environment requirements;
    Path: Preamble -> Environment and Version Management Requirements

    Description: Added information about AIRLab version compatibility and the corresponding upgrade and downgrade requirements.

- Optimized weld editing interactions;
    Path: AIRLab Software Analysis -> Engineering Module Analysis -> Weld Editing

    Description: Supports batch creation, filtering and grouping, and batch property modification, eliminating the need to configure similar weld seams individually. Filtering enables weld seams of the same type to be grouped quickly, while shared properties such as indentation and welding processes can be modified in batches to reduce repetitive operations. Automatic weld seam sorting has also been added, significantly reducing the overall operation time.
