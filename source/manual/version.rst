Version V1.4.0
===================
Date：2026-04-27

.. toctree:: 
    :maxdepth: 5


- Added AIRLab Gantry Welding System Functionality;
    Path: AIRLab Software Analysis -> AIRLab Gantry Welding System

    Description: For welding scenarios involving a mix of small workpieces of various types as well as large workpieces, the AIRLab Gantry Welding System is added. Through arbitrary combinations of multiple cameras or laser sensors, it enables rapid mapping of large workpieces or large working spaces, as well as collaborative welding by multiple robots.

- Added Weld Seam Inference Function;
    Path: AIRLab Software Analysis -> Pop-ups and Other Pages -> Welding seam edit pop-up window

    Description: In practical welding applications, the weld seam inference function can be used to automatically complete missing weld seam information in the following scenarios:

                1.The camera interferes with the workpiece, fixture, or environment, resulting in incomplete point cloud data;

                2.The weld seam features of the workpiece are not obvious or local features are missing, making some weld seams unable to be effectively recognized.

                This function intelligently infers missing weld seam trajectories based on existing weld seam data and geometric relationships, thereby improving the adaptability and robustness of the welding system.

- Added Palletizing Plugin V1.0 Functionality;
    Path: Plug-in -> Palletizing Plugin

    Description: The palletizing plugin enables automatic object recognition and gripping, as well as automatic placement according to a preset stacking pattern.

- Optimized Environmental Requirements
    Path: Preamble -> Environmental Requirements
    
    Description: Compatible with the latest version 3.9.5 of the controller software.