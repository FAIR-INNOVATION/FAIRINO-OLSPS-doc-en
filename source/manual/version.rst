Version V2.1.0
===================
Date：2026-06-30

.. toctree:: 
    :maxdepth: 5


- Added visual feature types for lap joint and vertical lap joint;
    Path: AIRLab Software Analysis -> Pop-ups & Other Pages -> Welding Feature Parameter Settings

    Description: The software now includes visual feature configurations for two new weld seam types: lap joint and vertical lap joint, with corresponding UI interaction updates completed. The software overall now supports workpieces with these two visual features, enabling the complete welding process through visual recognition.

- Optimized Palletizing Plugin V2.0 functionality;
    Path: Plugins -> Palletizing

    Description: Resolved defects identified during field testing of Palletizing V1.0, and improved usability and ease of use. The robot, in coordination with the camera, can now accurately locate and identify paper boxes, pallets, and spacers for material picking. Under regular stacking scenarios, palletizing accuracy reaches within 3mm, with strong versatility and scalability to accommodate various palletizing tasks.

- Optimized environment requirements;
    Path: Preface -> Environment Requirements

    Description: Compatible with the latest controller software version 3.9.7.

- Optimized AIRLab welding functionality (usability improvements);
    Path: AIRLab Software Analysis -> Engineering Module Analysis -> Fine Positioning

    Description: Resolved the issue of prolonged fine positioning time in AIRLab welding usability. Added resume functionality for fine positioning interrupted during obstacle avoidance planning, and optimized the obstacle avoidance logic in welding programs.

- Optimized AIRLab Gantry Welding System functionality;
    Path: AIRLab Software Analysis -> AIRLab Gantry Welding System

    Description: Added an extended-axis + end-of-arm camera line-scan mapping method; resolved outstanding issues from Phase 1; achieved full-process business logic closure for gantry welding workstations at the interaction level.