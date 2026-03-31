AIRLab Software Analysis
============================
.. toctree:: 
	:maxdepth: 5

The initial interface of the AIRLab software is shown in Figure 3-1 and is divided into five main sections. In the middle of the interface is the main display box (divided into scene display and camera display), on the top is the menu bar, on the leftmost side is the engineering module area, on the rightmost side is the operation area, and at the bottom of the interface is the command feedback area. This section will provide a detailed description of the functions and usage of the above areas, the pop-up windows and other pages that appear in the AIRLab software, and the sub-page functions.

.. figure:: analysis/4/1.png
	:align: center
	:width: 7.5in

	AIRLab Software Initial Interface

Menu Bar
--------------------------
The content included in the menu bar is shown in Figure below, mainly consisting of the buttons: "File," "View," "Window," "Simulation," "Plugins," "Welding," "Process," as well as icon buttons (in order from left to right): Add Point, Add Coordinate System, Mode Switch, Pause Run, Start Run, Stop Run.

.. figure:: analysis/4/2.png
	:align: center
	:width: 7.5in

	AIRLab Menu Bar

File
~~~~~~~~~~~~~~~~~~~
Click the“File”button, the menu shown below will appear:“New”,“Open”, “Export”. How to use it is described below:

.. figure:: analysis/4/3.png
	:align: center
	:width: 2in

	AIRLab Menu Bar - File

Select “New” click, “New Project” pop-up window will show, select the type of weld project in the pop-up window, then click “Confirm” button to complete the project new.

.. figure:: analysis/4/4.png
	:align: center
	:width: 2in

	AIRLab Menu Bar - File - New 

Select “Open” click, the “Select Project” pop-up window appears, find the path of your project, select the double-click or click on the pop-up window after clicking the “Open” button, that is, import the project successfully.

.. figure:: analysis/4/5.png
	:align: center
	:width: 4in

	AIRLab Menu Bar - File - Open

Select “Export” click, “Save Project” pop-up window appears, this function will save AIRLab's current project under user-defined path. After naming the project in the “File name” column of the popup window, click “Save” to complete the export of the current project.

.. figure:: analysis/4/6.png
	:align: center
	:width: 4in

	AIRLab Menu Bar - File - Export

If exported when there is currently no project present, AIRLab will provide a pop-up message prompt, as shown in the following figure.

.. figure:: analysis/4/7.png
	:align: center
	:width: 2.5in

	AIRLab export failed

View
~~~~~~~~~~~~~~~~~~~
View contains 12 functions, as shown in Figure 3-8, the main function is to adjust the viewing angle of the robot in the main display frame. They are: Zoom, Pan, Rotate, Reset, Fit all, Front view, Back view, Top view, Bottom view, Left view, Right view, and Full view.

.. figure:: analysis/4/8.png
	:align: center
	:width: 2in

	AIRLab Menu Bar - View

See Table 3-1 for a description of the specific functions of the view.

.. centered:: Table 3-1  View Function Description Table

.. image:: analysis/4/表3-1.png
	:align: center
	:width: 6in

Window
~~~~~~~~~~~~~~~~~~~
The "Window" menu contains six secondary options: "Software/Firmware Upgrade", "About", "Version Verification", "Log", "Virtual Camera", and "TCF and Camera Hand-Eye Calibration",and "Data source export". Clicking on different options will trigger different functional pop-up windows in AIRLab. For detailed functions and usage instructions, refer to the pop-up window introduction in Section 3.6.

.. figure:: analysis/4/window.png
	:align: center
	:width: 2.5in

	AIRLab Menu Bar-Window

Simulation
~~~~~~~~~~~~~~~~~~~
This button is used to switch between the simulation robot and the real robot. Before using this button, you need to successfully import or create a project and successfully establish Ros2 communication connection with the real robot. Clicking this button after completing the above prerequisites will enable switching between the virtual robot and the physical robot both. After switching the real robot, the robot pose displayed in the AIRLab scene will be synchronized with the actual robot, as shown in Figure 3-11.

.. figure:: analysis/4/11.png
	:align: center
	:width: 3in

	AIRLab display after live switching

Simulation Scene: used for simulation will not synchronize and update the robot position in the 3D scene in real time; 

Real Scene: update the current tool coordinate system, DH compensation parameters are consistent with the actual robot, and the robot position in the 3D scene is consistent with the physical robot.

Plugin
~~~~~~~~~~~~~~~~~~~
To enhance the scalability and user experience of the AIRLab software, AIRLab provides a plug-in module that allows users to develop customized plug-ins according to their requirements. These plug-ins can be loaded into AIRLab via dynamic library files (.so) to extend and enhance the software functions.

The existing plug-ins consist of five functional modules: the welding plug-in, bin picking plug-in.Users can enable or disable each plug-in as needed. Meanwhile, Plug-in Authorization enables users to check the authorization status of all plug-ins and complete authorization activation. For detailed introductions and specific operating procedures of each plug-in, refer to the plug-in section in Chapter 4.

.. figure:: analysis/4/plugin_menu_en.png
	:align: center
	:width: 3in

	AIRLab-Plugin

Weld
~~~~~~~~~~~~~~~~~~~
Under the main Welding function, the secondary options include:Welding Program Configuration, Welding Data Acquisition, Global Settings, Torch Cleaning & Wire Cutting, Automatic Cycle Operation, User Data Backup, 3D File Parsing, MultiStation Automatic Operation, Wire Stickout Compensation, Welding Feature Parameter Configuration, and Welder Configuration.

Click any option, and AIRLab will pop up the corresponding welding function setting window.For detailed descriptions and operating procedures of each function, refer to the popup introduction in Section 3.6.

.. figure:: analysis/4/weld.png
	:align: center
	:width: 3in

	AIRLab-Plugin

Process
~~~~~~~~~~~~~~~~~~~
The “Process” includes “Welding Process” and “Cylindrical Filling”, according to the process need to select different processes, click the option to appear corresponding function pop-up window.For a detailed introduction,please refer to section 4.6 on the analysis of engineering modules.

.. figure:: analysis/4/10.png
	:align: center
	:width: 3in

	AIRLab Menu Bar - Process

Mode switching
~~~~~~~~~~~~~~~~~~~
After the AIRLab software establishes Ros2 communication with the physical robot, the user can switch the mode status of the physical robot by clicking on this button. “A” means that the current robot is in automatic mode, and “M” means that the current robot is in manual mode. In addition, clicking this icon in automatic mode will switch the robot mode to manual, and clicking this icon in manual mode will switch the robot mode to automatic.

Points added
~~~~~~~~~~~~~~~~~~~~~~~~~
This function is used to quickly record the current position of the robot. After clicking this button, a new position targetX will be added under the position information section of the engineering module on the left side of AIRLab. The function of X is to prevent duplicate names of newly added positions, as shown in Figure 3-13. The j1, j2, j3, j4, j5, j6, x, y, z, rx, ry, and rz information of this point are the current joint coordinates and Cartesian coordinates of the robot.

.. figure:: analysis/4/13.png
	:align: center
	:width: 2in

	AIRLab Menu Bar - Point Additions

.. figure:: analysis/4/14.png
	:align: center
	:width: 4.5in

	AIRLab Terminal - Printing of Point Addition Successful Information

Coordinate system creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click this button, and AIRLab will create a new reference coordinate system. The newly created reference coordinate system will be displayed on the left side of the AIRLab interface under the module - coordinate system, which is used for weld offset and welding process, assisting users in quickly and accurately setting weld/bead offset.

Click the reference coordinate system icon on the far left to enter the reference coordinate system module. Select a reference coordinate system and click the "Edit" button above to configure it. You can then set parameters such as selecting the reference base (workpiece coordinate system, base coordinate system, or world coordinate system), adjusting the coordinate system's position, and choosing whether to display the reference coordinate system.

Click the Delete button above to remove the selected reference coordinate system.

.. figure:: analysis/4/15.png
	:align: center
	:width: 6in

	AIRLab - Reference Coordinate System

Figure 3-16 shows the coordinate system displayed, and Figure 3-17 shows the coordinate system not displayed.

.. figure:: analysis/4/16.png
	:align: center
	:width: 3in

	AIRLab Menu Bar-RCS-Display CS

.. figure:: analysis/4/17.png
	:align: center
	:width: 3in

	AIRLab menu bar-RCS-Not show CS


Offline Simulation
~~~~~~~~~~~~~~~~~~~~~~~~~

To enable intelligent recommendation of offline welding postures and improve simulation efficiency, AIRLab has added an "Offline Simulation" function. As shown in the figure, click the "Offline Simulation" icon button in the toolbar to enter the simulation state, and the icon color will turn yellow and highlighted.Click the icon again,exit the simulation state.

.. figure:: analysis/4/open-Offline-Simulation-state.png
	:align: center
	:width: 6in

	open "Offline Simulation" state 

After importing the robot, tool, and workpiece, click "Weld Seam Editing". Select a weld seam for editing, and after completion, click the "Offline Simulation" button in the pop-up window. AIRLab will dynamically simulate the path trajectory of the current weld seam from the approach point to the exit point in the 3D scene, showing whether the welding torch posture and robot position of the weld seam are reasonable, as shown in the figure.

.. figure:: analysis/4/offlin-simulation2.png
	:align: center
	:width: 6in

	Offline Simulate one weld seam

After editing all the weld seams to be welded, click the "Weld Seam Editing" icon button, and click "Weld Seams Edited in Offline Simulation " in the triggered menu, as shown in the figure. 

.. figure:: analysis/4/offlin-simulation3.png
	:align: center
	:width: 3in

	the menu content

AIRLab will automatically generate a Lua program under the program module, and display the offline simulated welding torch posture, weld seam position, welding process, trajectory planning and other contents in the 3D scene.

.. figure:: analysis/4/offlin-simulation4.png
	:align: center
	:width: 6in

	Offline Simulation of Edited Weld Seams

To prevent users from mistakenly running programs in the offline simulation state, AIRLab has added a running prompt when in the offline simulation state, as shown in the figure.

.. figure:: analysis/4/offlin-simulation5.png
	:align: center
	:width: 3in

	running prompt in offline simulation state



Pause running
~~~~~~~~~~~~~~~~~~~

Pause/Resume button. Clicking this button will immediately pause the robot that is running a program, and pressing the button again will resume the robot to continue running the program it was running before the pause.

Start running
~~~~~~~~~~~~~~~~~~~
By clicking this button, the robot will first run all the commands under the “Workpiece Positioning” module on the left side of AIRLab, and after successful positioning of the workpiece, the robot will start to run the weld recognition; after successful recognition of the weld seam, the robot will run or not run the program automatically according to the parameters set by the user in the program configuration.

Stop running
~~~~~~~~~~~~~~~~~~~
Clicking the button immediately stops the robot that is running the program. The difference between this button and the pause/resume button is that by pressing the button again, the robot cannot resume running and can only be restarted with the start running button.

Main Frame
--------------------------
The main display box is divided into scene display and camera display, where the scene mainly displays the robot, tool, workpiece, extended axis model, etc., as in Figure 3-20. the camera mainly displays the obtained point cloud map, as in Figure 3-21.

.. figure:: analysis/4/20.png
	:align: center
	:width: 5.5in

	AIRLab Main Display Box - Scene Display

.. figure:: analysis/4/21.png
	:align: center
	:width: 5.5in

	AIRLab Main Display Frame - Camera Display

Command Feedback Area
--------------------------
The instruction feedback area displays the execution results of program instructions, as shown in Figure 3-22.

.. figure:: analysis/4/22.png
	:align: center
	:width: 6.5in

	AIRLab Command Feedback Area-Terminal

Operating Area
--------------------------

Cartesian space movement
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This area includes two parts: tool coordinate system relative to the reference coordinate system, and long press tap trigger, move step and rotate step settings, as shown in Figure 3-23.

.. figure:: analysis/4/23.png
	:align: center
	:width: 3in

	AIRLab Operation Area - Cartesian Space Movements

- The Tool Coordinate System Relative to Reference Coordinate System section, which shows the value of the tool coordinate system relative to the reference coordinate system.

- Long press tap trigger, move step and rotate step setting section. As shown in Figure 3-24, if the currently imported robot model is a solid robot, long press the X+ button, the solid robot will execute the X+ tap command; if the currently imported robot model is not a solid robot, long press the X+ button, the simulation robot will execute the X+ tap command.

.. important::
	To control the robot's JOG pointing by long-pressing the buttons, if the buttons are released while the robot is running, the robot will stop moving immediately; if the buttons are held down all the way and not released, the robot will run the value of the set rotation step and then stop moving. the X-, Y+, Y-, Z+, Z- buttons operate in the same way. If the Rx+, Rx-, Ry+, Ry-, Rz+, Rz- buttons are pressed and held down, the robot will otherwise remain unchanged, except that it will move according to the set value of the rotation step.

.. figure:: analysis/4/24.png
	:align: center
	:width: 3in

	AIRLab Operation Area-Long Press Tap

Joint space space movement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This area includes 12 joint coordinate long press trigger buttons for joints J1-J6, 6 joint coordinate change text boxes and 6 joint sliders in three parts, as shown in Figure 3-25.

.. figure:: analysis/4/25.png
	:align: center
	:width: 3in

	AIRLab Operating Area - Joint Space Space Mobility

- You can control the movement of the solid robot J1 joints in manual mode and joint coordinate system by long-pressing the "+" or "-" button of J1. " button to control the movement of the J1 joints of the solid robot in manual mode and in the joint coordinate system. The "+" or "-" buttons of the other joints operate in the same way.

.. important::
	The robot operation is controlled by long-pressing the button. If the button is released while the robot is running, the robot will stop moving immediately; if the button is held down all the time, the robot will run the set value of Move Step/Rotate Step and then stop moving.

- The 6 text boxes are updated in real time to show the angle values of the 6 joints of the robot. In addition, editing the values in the 6 textboxes can also be used to control the movement of the robot's joints (care should be taken not to exceed the soft limits of the robot's joint angles when editing).

- The function of the joint slots is that the user can slide the joint slots to realize the movement of each joint of the robot, and the joint angles represented by the slots are displayed by the values in the text box.

Moving extended axis settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This section includes "exaxis+", "exaxis-" and the step setting box, as shown in Figure 3-26. "exaxis+", "exaxis-" functions are similar to the pointing X+ and X- under the tool coordinate system, and the motion of the extended axis can be controlled by the above two buttons. Long press the button to control the extended axis running, if you release the button during the extended axis running, the extended axis will stop moving immediately; if you keep pressing the button and do not release it, the extended axis will run the value set in the Step Setting box and then stop moving.

.. figure:: analysis/4/26.png
	:align: center
	:width: 3in

	AIRLab Operation Area - Moving the Extended Axis Position

Engineering Module Analysis
-----------------------------------
Click New Welding Project or Import Existing Welding Project. The AIRLab interface will prompt whether to use the configured welding features.

- For a new project, the configured welding features displayed are those currently in use by AIRLab.

- For an imported existing project, the configured welding features displayed are those recorded in the project.

.. figure:: analysis/4/new.png
	:align: center
	:width: 6in

	New Welding Project - Configured Features

.. figure:: analysis/4/import.png
	:align: center
	:width: 6in

	import Existing Welding Project - Configured Features

The user needs to click the Confirm Use or Reselect Features button according to the actual workpiece characteristics. For detailed instructions on reselecting features, refer to Section 3.6.25.

To weld a workpiece, you must first perform an import: import models such as the robot, tool, and workpiece. If no workpiece model is currently available, model-free construction must be carried out first.

Next, perform workpiece positioning and weld seam editing. Once both are completed, set the automatic photographing pose, run the program for weld seam recognition, and generate the welding program.

This chapter provides a detailed description of each module in the project module.

Import module
~~~~~~~~~~~~~~~~~~~
Click the Import icon on the far left to enter the import module, where users can import robots, tools, workpieces, extension axes, or connect cameras.

.. figure:: analysis/4/27.png
	:align: center
	:width: 6in

	Module Setup Page

- Import Robot: Select the robot, and the interface will display the robot settings page. Switching the robot model will show a schematic diagram and basic information of the selected robot on the page, as illustrated in the figure.

.. figure:: analysis/4/28.png
	:align: center
	:width: 6in

	Robot Settings Page

If the selected robot is not currently compatible with AIRLab software, a prompt interface will pop up, as shown in the figure.

.. figure:: analysis/4/Robot_Imp_Tip.png
	:align: center
	:width: 2.5in

	Robot Incompatibility Warning Pop-up

Taking the FR5 as an example, select the FR5 model robot and its version number (currently only V6.0 is supported), then click "Import". The FR5 robot model will be imported into the 3D scene, and a "Robot imported successfully" message displayed in the terminal confirms the successful import of the robot model.

.. figure:: analysis/4/29.png
	:align: center
	:width: 6in

	Successful introduction of the robot

Considering more flexible and rich robot deployment scenarios, we provide a free installation function. The user setting module sets the tilt angle and rotation angle in the page, and the robot model in the 3D scene or shows the corresponding installation effect. After modification, click Set to complete the robot installation method settings.

.. figure:: analysis/4/30.png
	:align: center
	:width: 6in

	Setting the robot tilt and rotation angles

.. important::
	After the robot is installed, the robot must be set up correctly, otherwise it will affect the use of the robot's drag function as well as the collision detection function.

You can delete the currently imported robot model by clicking the “Delete” button on the Robot Settings page.

- Import tool: Select the tool button, AIRLab interface will display the tool setting page.

.. figure:: analysis/4/31.png
	:align: center
	:width: 6in

	Tool Setup Page

Click Open, select the tool model you want to import under the corresponding path, and click “Open”.

.. figure:: analysis/4/32.png
	:align: center
	:width: 3in

	Selection Tool Model

The imported tool model is displayed in the 3D scene, and the terminal displays “Successful tool import”, which means that the tool model has been successfully imported.

.. figure:: analysis/4/33.png
	:align: center
	:width: 6in

	Import Tool Success

After importing a tool, you can set the current coordinate system of the tool and the appearance position of the tool;

Click the “Get Current” button under the tool coordinate system on the tool setting page to get the current coordinate system of the tool, and then click “Save” to modify the tool coordinate system.

.. figure:: analysis/4/34.png
	:align: center
	:width: 6in

	Get the current tool coordinate system

If you need to modify the appearance position of the tool, modify the coordinates under Appearance Position on the Tool Settings page, and then click the “Set Tool Appearance” button to finish setting the appearance position of the tool.

.. figure:: analysis/4/35.png
	:align: center
	:width: 6in

	Setting the Tool Appearance Position

You can delete the currently imported tool model by clicking the “Delete” button on the tool settings page.

- Import artifacts: Select the artifact,AIRLab interface will display the artifact setup page.

.. figure:: analysis/4/36.png
	:align: center
	:width: 6in

	Workpiece Setting Page

Click “Open” button, select the workpiece model to be imported under the corresponding path, click “Open”, the imported workpiece model will be displayed in the 3D scene, and the workpiece will be imported successfully.

Set workpiece coordinate system: After setting workpiece coordinate system in the workpiece setting page, click “Save Workpiece Coordinate System” to set workpiece coordinate system.

Delete workpiece: Click “Delete Workpiece” button in the workpiece setting page to delete the imported workpiece in the current 3D scene.

.. figure:: analysis/4/37.png
	:align: center
	:width: 6in

	Imported artifacts successfully

- Import Extended Axis: Select the Extended Axis.The AIRLab interface displays the Extended Axis Settings page, select the Extended Axis and click Import.

.. figure:: analysis/4/38.png
	:align: center
	:width: 6in

	Extended Axis Setup Page

The imported extended axis model is displayed in the 3D scene of AIRLab software, and the extended axis is imported successfully.

.. important::
	If the robot system version in use is **3.8.2.11 or higher**, enable the acceleration smoothing mode on the web platform first, as shown in the figure. Otherwise, synchronization failure of the extended axis motion will occur subsequently.

.. figure:: analysis/4/39.png
	:align: center
	:width: 6in

	Extended axis imported successfully

After the extended axis is imported successfully, communication configuration for the extended axis peripherals is required. Two communication methods are currently supported: Controller + PLC (UDP Communication) and Controller + Servo Drive (485 Communication).

The usage methods and detailed descriptions of the configuration for both methods are provided in Section 3.6.28.

Delete Extended Axis: Click “Delete Extended Axis” in the Extended Axis Settings page to delete the extended axis imported in the current 3D scene.

- Connect Camera: Click the Camera button, and a "Camera Settings" pop-up window will appear in the 3D scene. The camera settings pop-up is divided into three sections: Camera Configuration, Device Information, and Device Debugging.

Click the “Search Devices”, AIRLab will search for connected cameras and automatically connect them. If the connection is successful, the interface will be as shown in the figure Figure 3-40; If the connection fails, it will be displayed as not connected in the connection status column, and there will be no camera related parameters.

.. figure:: analysis/4/40.png
	:align: center
	:width: 3in

	Camera settings page

After successful camera connection:Click "Get Parameters" to retrieve the current camera configuration settings. If need to modify the desired parameters, click "Set Parameters" will successfully update them.The follow descriptions are parameter descriptions:

Structured Light Exposure Time:Increase when images are too dark in structured light mode;Decrease when images are overexposed.

Line Scan Time:Increase when reflective workpieces cause hollow artifacts in imaging.

Line Scan Exposure Time:Increase when images are too dark in line scan mode; Decrease when images are overexposed.

Brightness Level:Increase when images are too dark to see details;Decrease when images appear washed out.

Protective Shield:Welding protection cover prevents spark/spatter during welding; Enabled by default during imaging.

Device Information:Click "Device Info" to view connected camera details (name, model, connection status, etc.) as shown in the follow figure.

.. figure:: analysis/4/camera_info_en.png
	:align: center
	:width: 3in

	Camera Infomation

Device Debugging:Click "Device Debugging" to access camera calibration functions, including:Aging Debug,Single Capture,Save Point Cloud.

.. figure:: analysis/4/42.png
	:align: center
	:width: 3in

	Camera Debugging

Filter distance threshold:When the image contains excessive noise, increase the threshold; when preserving fine edges is required, decrease the threshold.

Below are detailed function descriptions:

Aging Debug:Click the "Aging Debug" button to initiate continuous camera testing - the camera will automatically capture images at regular intervals. Click again to stop. Results display in the Main Display Panel - Camera View.

Single Capture:Takes one image at the current position. Results show in the Main Display Panel - Camera View with two display modes.And the raw Point Cloud is the direct camera output;Base Coordinate Point Cloud is the point cloud converted to robot base coordinates.Toggle between views as needed.

Save Point Cloud:After single capture,Click "Save Point Cloud",Select output path to save point cloud data.

Save Image:After single capture,Click "Save Image",Select output path to save 2D image.

Camera Calibration:Include Calibration and verification.Refer to Section 2.5 "Point Cloud Camera Hand-Eye Calibration" for detailed procedures.

Capture Ground: Control the camera to align with the plane where the workpiece is located, then click the button to complete ground plane acquisition.

Obtain Ground Plane Equation: After "Capture Ground", click to obtain the ground plane equation.

Ground Effect Verification: Perform visual verification of the captured and calculated ground plane. For detailed operations, please refer to Section 2.6, "Ground Plane Acquisition and Verification".

SLAM mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, click the SLAM Mapping Module in the Project Module to configure the method and image capture settings for the entire process. Click the + icon, and the SLAM Mapping Image Capture Settings pop-up window will appear. The main steps of the entire SLAM mapping process are described in detail below.

Step 1: Configure SLAM Mapping Scanning Settings

After entering the pop-up window, click the SLAM Mapping Scanning tab. Two sensor options are currently available: Camera and Lidar. Note: The Lidar mode is not yet implemented; please select Camera for now. Two scanning methods are provided: Oscillating Scan and Fixed Scan—please select Oscillating Scan. Finally, enter a name for the SLAM mapping workpiece model (no Chinese characters allowed in the name), as shown in Figure below..

Scanning Method Explanation:

Oscillating Scan: The camera projects a laser and rotates 120° around the far-point position.

Fixed Scan: The camera moves to the central position and remains stationary; real-time data can be acquired by moving the camera.

.. figure:: analysis/4/slam1.png
	:align: center
	:width: 6in

	SLAM Mapping Scanning

Step 2: Start SLAM Mapping

Click the SLAM Mapping Supplementary Image Capture tab. You can either manually move the robot to the first position and click the First Capture button, or select a pre-recorded position and click Move to This Position (Note: No collision will occur during the robot s position movement), then click First Capture after the robot reaches the position.

After the first capture, continue moving the robot to the next position and click the Scan button. The button will be hidden until the scan is completed and reappear automatically after the scan ends. Repeat the robot movement + scan operation until the SLAM mapping scan of the workpiece is finished. After all scans are completed, click the Rebuild SLAM Map button—the generated model will be displayed in the 3D scene on the main AIRLab interface.

.. figure:: analysis/4/slam2.png
	:align: center
	:width: 6in

	SLAM Mapping Supplementary Image Capture

Step 3: Perform Supplementary Scanning

If the obtained SLAM map is incomplete, supplementary scanning and reconstruction are required. Click the Supplementary Scan Initialization button under the SLAM Mapping Supplementary Image Capture tab (there is no need to click the First Capture button again). Move the robot to the incomplete area of the model and click the Scan button. After all supplementary scans are completed, click Rebuild SLAM Map to obtain the reconstructed model.

Step 4: SLAM Parametric Modeling (Model Completion)

Click the SLAM Parametric Modeling tab, as shown in Figure below.. Click the Start Point Selection button to enable the selectable attribute of points on the model. You can set the point size in the Weld Seam Endpoint Scaling Factor field, then select four points as prompted.

The four selected points will form a thin surface—set the Thickness, Direction, and Expansion Thickness according to the actual workpiece structure. After completing the settings, click Set Attributes, then click Model to finish modeling the solid. Repeat the above steps to model other solids. After all modeling is completed, click End Point Selection to restore the points on the model to the non-selectable attribute.

.. important::
	Selected points will turn yellow. Before all four points are selected, re-clicking a selected point will deselect it. If the generated solid is incorrect after selecting the four points, click Delete to clear the selected solid and reselect the points.

.. figure:: analysis/4/slam3.png
	:align: center
	:width: 6in

	SLAM Parametric Modeling

Key Parameter Explanations:

Show All Solids: Displays all modeled solids in the 3D scene of the interface.

Hide All Solids: Hides all modeled solids from the 3D scene.

Thickness: The thickness of the thin surface formed by the four points; the thin surface will be thickened along the Z-axis after setting.

Direction: Divided into Positive and Negative—select according to the actual workpiece structure and the thickening direction of the model in the 3D scene.

Expansion Thickness: If the edge of the thin surface formed by the four points is inconsistent with the actual workpiece structure, set the expansion thickness—the thin surface will expand outward with the center point of the surface as the reference.

Important Note:The modeling of solids will affect the effect of the obstacle avoidance function in subsequent steps. Ensure that the solids are as consistent as possible with the actual workpiece structure.

Step 5: SLAM Mapping Result Accuracy Verification

Verify whether the accuracy of the SLAM mapping result meets the requirements, as shown in the figure. After the SLAM map is successfully obtained, click Start Verification. Move the robot to a diagonal position of the workpiece and click Verification Capture to take a photo of a three-surface structure on the workpiece.

After the first photo is taken successfully, move the robot to the opposite diagonal position and click Verification Capture again to take a photo of the three-surface structure at the opposite diagonal of the workpiece. After both photos are taken successfully, click Obtain Verification Result—the result will be displayed in a pop-up window. If the verification is passed, proceed to subsequent operations; if the verification fails, troubleshoot the cause of the accuracy failure and rebuild the SLAM map.

.. figure:: analysis/4/slam4.png
	:align: center
	:width: 6in

	SLAM Mapping Result Accuracy Verification

Step 6: Calculation Rule Configuration Parameter Settings

Open the Global Settings pop-up window to set the following parameters:

1. The Idle Movement Threshold (recommended value: 5 mm) in Self-Collision Detection;

2. Parameters in Welding Torch Pose Calculation Rule Configuration;

3. Camera parameters in Image Capture Pose Calculation Rule Configuration.

As shown in Figures below. For detailed descriptions, refer to Section 3.6.8 Global Settings in this manual.

If an extended axis is imported, it is also necessary to set the Distance between Extended Axis Zero Point and Actual Zero Point on the right interface of AIRLab.

Setting Method: Move the robot to the set extended axis zero point, then move the robot to the outermost position of the extended axis as far as possible, and set the moving distance (absolute value) as the Distance between Extended Axis Zero Point and Actual Zero Point.

.. figure:: analysis/4/slam5.png
	:align: center
	:width: 6in

	Welding Self-Collision Detection Rule Configuration

.. figure:: analysis/4/slam6.png
	:align: center
	:width: 6in

	Welding Torch Pose Calculation Rule Configuration

.. figure:: analysis/4/slam7.png
	:align: center
	:width: 6in

	Image Capture Pose Calculation Rule Configuration

Step 7: Weld Seam Selection

Enter the Weld Seam Editing module and click the + icon to open the Weld Seam Selection pop-up window, as shown in the figure. Select the weld seam number, enable filtering, set the filter parameters, and click Confirm to add the weld seam. It is mandatory to add weld seam numbers in the actual welding sequence to avoid unnecessary filtering failures and collisions.

.. important::
	If a Weld Seam Addition Failed prompt appears after clicking Confirm, it indicates that the algorithm has no qualified recommended pose for the weld seam. You need to select the weld seam in the weld seam list, open the Weld Seam Editing pop-up window, and manually teach the welding poses of the start point, end point and safety point of the weld seam. For the introduction of the Weld Seam Editing pop-up window, refer to Section 3.6.11 in this manual.

Filter Parameter Explanations:

Enable Filtering: When enabled, AIRLab will further filter the algorithm-recommended welding poses and output the optimal result; when disabled, AIRLab will directly output the first algorithm-recommended welding pose without filtering. It is recommended to enable this function.

Reference Weld Seam Number for Calculation: Includes Reference Current Position and Reference Added Weld Seams. Reference Current Position means the robot s current joints will be referenced for welding pose filtering; Reference Added Weld Seams means AIRLab will reference the safety points of the specified weld seams for filtering the current weld seam s welding pose.

Enable Reachability Filtering: Filters the reachability of the robot s Move L motion from the start point to the end point of the weld seam. It is recommended to enable this function.

Enable Joint Pose Filtering: Prevents collisions or inaccessibility caused by large changes in the robot s welding pose when moving inside the workpiece. It is recommended to enable this function. Setting Method: Move the robot to a position near the start point of the first weld seam, adjust the robot joints to the welding pose, check the current J3 and J5 joint values of the robot on the right interface of AIRLab, and determine the selection of J3 Joint Angle and J5 Joint Angle in the figure based on these values.

.. important:: 
	After the joint filter parameters for the first weld seam are determined, the remaining weld seams must use the same parameters as the first one.

Enable Collision Detection Filtering: Prevents collisions between the recommended welding pose and the workpiece or the robot itself. It is recommended to enable this function.

Extended Axis Position at Start Point: The position of the robot on the extended axis when it reaches the start point of the weld seam.

Extended Axis Position at End Point: The position of the robot on the extended axis when it reaches the end point of the weld seam.

Extended Axis Position at Safety Point: The position of the robot on the extended axis when it reaches the safety point of the weld seam.

.. figure:: analysis/4/slam8.png
	:align: center
	:width: 6in

	Weld Seam Recommended Pose Filter Configuration and Weld Seam Addition

Step 8: Set SLAM Image Capture Pose Filter Conditions

After completing the weld seam addition, enter the Fine Positioning module and click the Fine Positioning tab to display the menu as shown in the figure. Select and click Set SLAM Image Capture Pose Filter Conditions to open the Image Capture Pose Filter Settings pop-up window, as shown in Figures below.. Click Confirm after completing the parameter settings.

Filter Parameter Explanations:

Enable Filtering: When enabled, AIRLab will further filter the algorithm-recommended fine positioning image capture poses. It is recommended to enable this function.

Enable Joint Pose Filtering: Serves the same purpose as the item in the Weld Seam Selection pop-up window—prevents collisions or inaccessibility caused by large changes in the robot s pose during fine positioning image capture. Setting Method: Move the robot to a position near the first weld seam, adjust the robot joints to the image capture pose, check the current J3 and J5 joint values of the robot on the right interface of AIRLab, and determine the selection of J3 Joint Angle and J5 Joint Angle in the figure based on these values.

Enable Collision Detection Filtering: Prevents collisions between the recommended image capture pose and the workpiece or the robot itself. It is recommended to enable this function.

Enable Path Planning Filtering: When enabled, AIRLab will reference the previous image capture position to filter the current one, ensuring a collision-free path between the two positions. It is recommended to enable this function.

.. figure:: analysis/4/slam9.png
	:align: center
	:width: 6in

	Fine Positioning Menu

.. figure:: analysis/4/slam10.png
	:align: center
	:width: 6in

	SLAM Image Capture Pose Filter Condition Settings

Step 9: Obtain Automatic Image Capture Poses

Click the Fine Positioning tab, select and click Obtain Automatic Image Capture Poses in the pop-up menu—AIRLab will calculate and output the fine positioning image capture positions that meet the filter conditions.

Capture positions that pass the filter will be automatically added to the fine positioning list;

Capture positions that fail the filter will display the failure reason and corresponding weld seam number on the interface (solutions are described in Step 10), as shown in Figure below..

.. figure:: analysis/4/slam9.png
	:align: center
	:width: 6in

	Obtain Automatic Image Capture Poses

Step 10: Fine Positioning Parameter Configuration and Manual Teaching of Failed Positions

After obtaining the automatic image capture poses, click the + icon to open the Fine Positioning pop-up window, as shown in Figure below..

If you need to set fine positioning parameter nodes, enter the parameters and click Confirm;

If you need to perform collision detection on the added capture positions, set Enable Collision Detection to Yes (recommended).

For the capture positions that failed the filter in the previous step, perform manual teaching here:

1. Click Add New Capture Point—AIRLab will record the robot s current position and add it to the last position of the fine positioning list;

2. According to the weld seam number of the failed filter, select the newly added position and click the ↑ icon to move it to the correct position.

.. important::
	Manually add several transition points at the end of the fine positioning position list to ensure the robot can safely return from the capture end point of the last weld seam to the capture start point of the first weld seam.

.. figure:: analysis/4/slam11.png
	:align: center
	:width: 6in

	Fine Positioning Pop-up Window

Step 11: Collision-Free Trajectory Planning for Fine Positioning Positions

Click the Fine Positioning tab, select and click Collision-Free Trajectory Planning in the menu, and wait for the AIRLab planning result.

If the planning is successful, open the menu and click Generate Collision-Free Trajectory to display the planned trajectory;

If the planning fails, AIRLab will display the name of the failed position—you can modify the position or add a transition point.

Modification Methods:

1. Modify Position: Enter the Position Information module, find and select the failed position, open the Position Information Modification pop-up window, modify the parameters and save;

2. Add Transition Point: Select the failed position, click Add Transition Point Before Current Point in the pop-up submenu, and the Add Path Point pop-up window will appear, as shown in the figure.

Step 12: Run the Fine Positioning Program

Click the Fine Positioning tab, select and click Run Program in the menu to execute the fine positioning program.

Step 13: Run the Welding Program

After the fine positioning program runs successfully, enter the Program module and click the Program tab, as shown in Figures below..

If collision-free trajectory planning is required: First click Generate Collision-Free Trajectory in the menu, then click Run Collision-Free Trajectory after successful planning;

If collision-free trajectory planning is not required: First click Generate Trajectory in the menu to check whether the trajectory is normal, then click Run Program to start welding if there is no error.

.. important::
	After the program is generated, do not modify the program nodes; do not modify the list information of weld seam editing unless necessary. If the weld seam order in the weld seam list is modified or weld seams are added/deleted, return to Step 8 and reconfigure the relevant settings.

.. figure:: analysis/4/slam12.png
	:align: center
	:width: 6in

	Run Program

Model Construction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the workpiece to be welded does not have a model file, you need to perform a model-less build of the workpiece first, otherwise, you can directly import the workpiece model to perform the 3.5.4 weld editing operation.

Click the Model Construction icon button on the far right to enter the module, then select the Add icon at the top. A "Modeless Construct" pop-up window will appear in the AIRLab interface.

.. figure:: analysis/4/model_less2.png
	:align: center
	:width: 6in

	Model-Free Construction Pop-up--Workpiece

If a non-spline feature is selected in the Welding Feature Parameter Configuration module, the Model-Free Construction pop-up window will appear as shown in the first figure below; if a spline feature is selected, the pop-up window will appear as shown in the second figure below.

.. figure:: analysis/4/model_struct_non_spline.png
	:align: center
	:width: 6in

	Model-Free Construction Pop-up--Workpiece with Non-spline Features

.. figure:: analysis/4/modelLess_popup_en.png
	:align: center
	:width: 3in

	Model-Free Construction Pop-up--Workpiece with Spline Features

You can select to add a new Model-Free Construction parameter node, add a new image capture node, add a new movement node, or add a new model construction node.Spline and non-spline features are identical in terms of node addition and meaning, with no differences.

The meanings and addition methods of various nodes are described below using non-spline features as an example.

Add moving node: select the photo target point to be moved, click the “Confirm” button, and “Move(target)” will appear under the Model Construction module, that is, it is added successfully.

Alternatively, click “Add Current Position” to create a new waypoint at the current location, which will automatically generate a Move(target) node under Model Construction.

.. figure:: analysis/4/model_struct_non_spline.png
	:align: center
	:width: 6in

	Adding Move nodes

The principle of the model-less photo point of demonstration is that the camera is able to clearly and completely capture all positions of the model-less workpiece, especially the position of the weld seam that needs to be welded.

.. figure:: analysis/4/44.png
	:align: center
	:width: 3.5in

	Photographic points of the workpiece at different angles    

Add photo node:Click the Confirm button under Add Capture Node to create a new image capture node in Model Construction.

.. figure:: analysis/4/model_less1.png
	:align: center
	:width: 3.5in

	Add Photo Node

Add Modeless construction node: After adding several groups of “Move+Photo” nodes,enter the model construction name,and click “Confirm” button of model construction part.“Model Const” node appears under the Model Const module, that is to say, adding successful.

.. figure:: analysis/4/model_less3.png
	:align: center
	:width: 6in

	Adding Modeless cons nodes

.. important::
	Note: If the workpiece has symmetrical features, integrity judgment must be enabled when adding model construction nodes, as shown in the figure. Additionally, the entire workpiece must be completely captured during the model building process.

.. figure:: analysis/4/model_less4.png
	:align: center
	:width: 3in

	Enable Integrity Judgment

After adding nodes, you can perform the following adjustments,

Reorder Nodes: Move nodes up/down the workflow sequence;

Delete Nodes: Remove unnecessary nodes.

The model-free construction program will be completed.

After the model construction program is completed, click the “Model Const” module, click “Generate Trajectory” to view the simulation trajectory of the model construction program, and after confirming that the trajectory of the model construction program is correct, click Run program to start running the model construction program.

.. figure:: analysis/4/46.png
	:align: center
	:width: 2.5in

	Click on the model const blocks

For symmetrical workpieces with integrity judgment enabled, the software will assess the completeness of the constructed model after the model-free construction process is completed. If the constructed model is determined to be incomplete, the software will prompt "Integrity judgment failed," as shown in the figure. The user will then need to perform additional captures of the workpiece until the model is fully constructed.

.. figure:: analysis/4/Integrity_Fail.png
	:align: center
	:width: 6in

	Integrity Judgment Failed

At the same time, the current integrity judgment point cloud will be displayed on the interface, as shown in the following figure. Here, blue and yellow represent the two symmetrical parts of the point cloud, while red indicates asymmetrical sections where no corresponding points were found. It is necessary to recapture the symmetrical areas corresponding to the red points or use the stitched point cloud in the small window to determine the recapture positions.

.. figure:: analysis/4/complete_cloud.png
	:align: center
	:width: 6in

	Integrity Judgment Point Cloud

After the symmetrical workpiece model is fully constructed, the software will display a "Integrity judgment successful" prompt, as shown in the figure. The user can then proceed to the next operation.

.. figure:: analysis/4/Integrity_Pass.png
	:align: center
	:width: 6in

	Integrity Judgment Successful

After the model construction program has finished running, the built model workpiece model will be displayed in the AIRLab 3D scene. Check whether the model is correct or not, the model is correct, the modelless construction is successfully constructed, and the model that has been successfully constructed can be directly imported in the next time, and there is no need to model the workpiece again for the modelless workpiece modeling.

.. figure:: analysis/4/47.png
	:align: center
	:width: 6in

	Model-free construct successfully

If the model is built incorrectly, you need to click the “Model Construction” module, click “Clear Model Data”, and then build the model again until the modelless artifact model is created correctly.

When weld seam acquisition fails due to inappropriate model construction parameter settings, you can first edit and adjust the parameters, then issue the model-free modeling command, and subsequently acquire secondary recognition data. Afterward, click "Acquire Model Data" to reload the model data updated with the adjusted parameters.

By clicking on the No Model Build module, the user can select options such as Get Modeling Data, and the functions of each option are described below.

- Supplementary shooting: After generating the workpiece model by running the model-free program, if there are incomplete parts in the workpiece model that need supplementary shooting, move the robot to the position where supplementary shooting is required and click "Supplementary Shooting". Then click "Acquire Modeling Data" to re-import the workpiece model after supplementary shooting.

- Get Modeling Data: Click “Get Modeling Data”, after clearing the modeling data, click Get Modeling Data to get the modeled artifact model again.

- Clear Modeling Data: Click “Clear Modeling Data” to clear the modelless workpiece model in the 3D scene.

- Run Program: Click “Run Program” to run the current program of the modelless building module.

- Stop Program: Click “Stop Program”, the robot will stop running immediately.

- Generate Trajectory: Click “Generate Trajectory” button to generate the simulation trajectory of the program in AIRLab 3D scene.

- Clear trajectory:Clicked this button will delete the generated tarjectory in AIRLab 3D scene.

- Show Tool: Click “Show Tool”, the virtual tool model will be shown in AIRLab 3D scene.

- Clear Tool: Click “Clear Tool”, the virtual tool model displayed in AIRLab 3D scene is cleared.


Weld editing
~~~~~~~~~~~~~~~~~~~~~~~
After importing the workpiece or successfully constructing the workpiece without a model, the workpiece model and weld seam data will be displayed in the 3D scene.

Click the plus sign under "Weld Seam Editing" to bring up the Weld Seam Selection pop-up window. Select a weld seam number; the weld seam type field will automatically display the type of the selected weld seam, including straight weld seams, arc weld seams, spline curve weld seams, and plug weld seams. Click the "Confirm" button to add the weld seam, and repeat this until all weld seams are added.

The successfully added welds here do not indent, reverse, shift, or bind to any welding process, and the progression and retreat point strategies are set to a custom distance of 100mm.

.. figure:: analysis/4/48.png
	:align: center
	:width: 6in

	Weld Seam Selection Pop-up --Workpiece with Non-spline Features

For the welding of workpieces with spline features, Spline Feature must be selected first in the Welding Feature Parameter Configuration module. When adding weld seams, the Weld Seam Selection pop-up window is displayed as shown in the figure below. The Number of Selected Weld Seam Points on the page is non-editable, as it is a result of model construction.

.. figure:: analysis/4/seamedit11.png
	:align: center
	:width: 6in

	Weld Seam Selection Pop-up--Workpiece with Spline Features

If segmentation is required, set Enable Segmentation to Yes in the figure, and the page will be displayed as shown below.

.. figure:: analysis/4/seamedit12.png
	:align: center
	:width: 6in

	Spline Curve Weld Seam--Segmentation

First, set the Start Point and End Point, ensuring they fall within the range of the total number of points of the entire weld seam. For example, if the selected weld seam in the figure has a total of 36 points, the range of the number of points for the start and end points is [1,36]. After completing the settings, click the + icon on the page to add the segmented weld seam, as shown in the figure below.

.. figure:: analysis/4/seamedit13.png
	:align: center
	:width: 6in

	Add Segmented Weld Seam

If additional segments need to be added to the current weld seam, reset the Start Point and End Point and follow the same steps as above, as shown in the figure below. Note: Segmentation must be complete, and the end point of one segment must coincide with the start point of the next segment.

.. figure:: analysis/4/seamedit14.png
	:align: center
	:width: 6in

	Continue Adding Segmented Weld Seams

After completing the weld seam segmentation, click the Confirm button in the figure, and the added segmented weld seams will be displayed in the weld seam list.

If the weld needs to be re-edited, select the weld, click the edit icon at the top of the module, and complete the parameter settings in the 'Seam edit' popup.

.. figure:: analysis/4/seamedit15.png
	:align: center
	:width: 6in

	Weld Seam Editing--Spline Weld Seam

.. figure:: analysis/4/49.png
	:align: center
	:width: 6in

	Weld Seam Editing--Non-spline Weld Seam

The meaning of each editing item in Weld Seam Editing is detailed in Section 3.6.9. Perform workpiece positioning or fine positioning operations only after all weld seams have been edited.

.. important::
	For the editing of plug workpieces, it is only necessary to bind the plug workpiece process.

After completing the weld seam editing for plug workpieces, click the "Weld Seam Editing" module and then click the "Generate Welding Program" button. A plug welding program will be generated under the "Program" node. Subsequent operations such as generating trajectories for the created welding nodes or running the program can be performed; details are provided in Section 3.4.6.

.. important::
	If AIRLab provides too many automatic photo poses (such as far more than the number of welds), some points should be deleted or manually taught again. The teaching points only need to capture the starting and ending points of the welds.


Workpiece positioning
~~~~~~~~~~~~~~~~~~~~~~~~
Workpiece positioning: After editing all the welds to be welded, workpiece positioning is required. Firstly, it is necessary to create a workpiece positioning program; Click on the workpiece positioning module, click on the plus sign under workpiece positioning, and the AIRLab interface will display the workpiece positioning page as shown in the figure.

.. figure:: analysis/4/regisiter_addnode.png
	:align: center
	:width: 6in

	Adding a coarse positioning node

The workpiece positioning program consists of three node types:Capture Node,Move Node,Coarse Positioning Node.The Capture and Move nodes function identically to those in the Model-Free Construction module (see Section 4.5.2 for details).

Add a rough positioning node: After adding multiple sets of "movement + photo" nodes, add a rough positioning node and select a workpiece positioning algorithm. The rough positioning algorithms include Model-based, Cylinder Positioning, Depth Model, Depth Model 2, and Plug Recognition. The applicable scenarios for each algorithm are as follows:

- Model-based: Used for rough positioning of workpieces after model-free construction or workpiece import.
  
- Cylinder Positioning: Not yet available.
  
- Depth Model: Used for workpiece recognition in the automatic cycle operation of template programs.
  
- Depth Model 2: Applicable to the same scenarios as "Model-based", used for rough positioning of workpieces after model-free construction or workpiece import.
  
- Plug Recognition: Used for recognition and positioning of plug workpieces.
  
After selecting the workpiece positioning algorithm, click "Confirm", and a "Rough Positioning" node will be generated under the workpiece positioning program.

.. figure:: analysis/4/51.png
	:align: center
	:width: 2in

	Workpiece positioning program

After adding these nodes, you can adjust the added nodes as needed. Once completed, the workpiece positioning program will be successfully created.The entire program functions as follows:The robot will move to multiple capture positions and take photos until the workpiece is fully captured. Then, the program will perform coarse positioning of the workpiece.The created workpiece positioning program is shown in the figure below.

After creating the workpiece positioning program,click the "POS_WP" module. The options that appear,as shown in the figure.

.. figure:: analysis/4/52.png
	:align: center
	:width: 2.5in

	Click on the pos_wp blocks

.. important::
	For symmetrical workpieces, it is only necessary to capture the point cloud of the workpiece section indicated by the red cutting line in the interface, as shown in the figure below.

.. figure:: analysis/4/coarse_position_note_en.png
	:align: center
	:width: 4in

	Point Cloud Display & Symmetrical Workpiece Prompt

The functions of the remaining options are as follows:

- Generate the workpiece positioning program directly: Click this button, and AIRLab will automatically generate a workpiece positioning program with reference to the points created through model-free construction.

- Clear Cutting Point Cloud: Remove the cutting point cloud of symmetrical workpieces in the 3D scene.

.. figure:: analysis/4/clear_cut_pcd.png
	:align: center
	:width: 6in

	Clear Cutting Point Cloud

- Display Cutting Point Cloud: Show the cutting point cloud of symmetrical workpieces in the 3D scene.

.. figure:: analysis/4/display_cut_pcd.png
	:align: center
	:width: 6in

	Display Cutting Point Cloud

Click "Generate trajectory" to view the simulated trajectory of the workpiece positioning program. After confirming the trajectory is correct, click "Run Program" to execute the workpiece positioning program for coarse workpiece positioning.

Upon successful completion of the workpiece positioning program, the workpiece will move to the actual relative position between the workpiece and the robot.

If no error occurs during the execution of the workpiece positioning program, a colored point cloud of the workpiece will be displayed on the interface upon completion.The meaning of the point cloud colors is as follows:

1.Green: Workpiece positioning angle error < 5°

2.Yellow: 5° ≤ Workpiece positioning angle error ≤ 10°

3.Red: Workpiece positioning angle error > 10°

.. important::
	The colors only represent the visualization of the angle error result and do not affect the actual registration result. The registration result depends only on the actually calculated registration accuracy and overlap rate.

.. figure:: analysis/4/point_clound_green.png
	:align: center
	:width: 3in

	Successful Workpiece Positioning – Green Workpiece Point Cloud

.. figure:: analysis/4/point_clound_color.png
	:align: center
	:width: 3in

	Successful Workpiece Positioning – Colored Workpiece Point Cloud

If workpiece positioning fails, the interface will display a visualization result of the registration error, where blue represents the workpiece positioning point cloud and white represents the workpiece model point cloud, with a corresponding prompt popup window appearing at the same time.

The specific workpiece positioning error types are divided into the following three categories:

1) Low point cloud registration coverage but qualified accuracy, with misalignment.Message: Point cloud registration failed. Local registration accuracy is qualified, but the overall overlapping area is insufficient, and there is a risk of point cloud misalignment. Please compare with the model point cloud, adjust the shooting angle, and perform workpiece positioning again.As shown in the figure below.

2) High point cloud registration coverage but low accuracy, with local roughness.Message: Point cloud registration failed. The overall overlapping area is qualified, but local registration accuracy is insufficient. Please compare with the model point cloud, check whether feature areas were overcaptured or undercaptured, and perform workpiece positioning again.As shown in the figure below.

3) Both point cloud registration coverage and accuracy are low.Message: Point cloud registration failed. Both registration accuracy and overlapping area are unqualified. Please compare with the model point cloud, adjust the shooting angle, and perform workpiece positioning again.As shown in the figure below.

.. figure:: analysis/4/error-1-en.png
	:align: center
	:width: 6in

	Workpiece Positioning Error – Type 1

.. figure:: analysis/4/error-1.png
	:align: center
	:width: 2.5in

	Workpiece Positioning Error – Type 2

.. figure:: analysis/4/error-3-en.png
	:align: center
	:width: 6in

	Workpiece Positioning Error – Type 3

If workpiece positioning fails and the above problems occur, please re-position according to the error message instructions.

If the above problems persist and cannot be resolved, or if other issues arise, please contact after-sales personnel and retain the current data.

Welding Instructions for Plunger Workpieces

Step 1: Add the plunger process, and set up the filling process, reinforcement process, arc starting process, and arc ending process.

.. figure:: analysis/4/82.png
	:align: center
	:width: 3in

	Adding the plunger process

Step 2: Edit the workpiece positioning program and run it.

Open the AIRLab welding software system and import the project. Edit the workpiece positioning program by adding nodes for movement, photographing, and plunger recognition. 

Run the workpiece positioning program to position the plunger workpiece and identify the plunger weld seams. The 3D scene displays the workpiece model and weld seam information of the plunger, as shown in the figure.

.. figure:: analysis/4/pluger1.png
	:align: center
	:width: 3in

	Workpiece positioning result for the plunger workpiece

Step 3: Add the plunger weld seams to be welded, and bind the plunger process to the selected plunger weld seams.

Step 4: After adding all plunger weld seams to be welded, click "Weld Seam Editing → Run Program". A plunger welding program will be generated under the program node.

Step 5: Click "Program → Generate Trajectory". The welding trajectory will be generated in the 3D scene.

.. figure:: analysis/4/pluger2.png
	:align: center
	:width: 3in

	Welding simulation trajectory for the plunger workpiece

Step 6: After confirming that the trajectory is correct, proceed with simulation and then perform a simulated welding test.

Fine pose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After workpiece positioning is completed, fine positioning of the workpiece weld seams is required to obtain weld seam data. After the model-free reconstruction is finished, or after importing a pre-built workpiece model, click the "Fine Positioning" module in the Project Module to create a fine positioning program. Click the "Fine Positioning" module, then click the "Get Automatic Camera Poses" button. The recommended camera poses for the weld seams will then be generated in the pose list.

.. figure:: analysis/4/53.png
	:align: center
	:width: 6in

	Auto Photo Position List

Due to the potentially large number of recommended camera poses, users can improve efficiency by manually reducing some of these camera points and re-teaching others. The principle for teaching camera points is to ensure the start and end points of all weld seams are completely within the camera's field of view. If modifying a point is necessary, open the point information page, make the changes, and click "Save MP" to confirm.

.. figure:: analysis/4/fine_locate_point_set_en.png
	:align: center
	:width: 6in

	Camera Pose Point Modification
	
If precise positioning parameters need to be set, a precise positioning parameter node can be added. Click the plus sign, and the interface will display the precise positioning pop-up window, as shown in the figure.

.. figure:: analysis/4/slam11.png
	:align: center
	:width: 4in

	Fine Positioning Pop-up Window

Retrieve the current parameters, modify them as needed, and then click "Confirm." The precise positioning parameter node will be inserted before the first node by default.

.. figure:: analysis/4/fine_pose_add_en.png
	:align: center
	:width: 3in

	Add Fine Positioning Parameter Node

After completing the fine positioning program, click the "Automatic Camera Poses" module. Options such as "Get Automatic Camera Poses", "Generate Collision-Free Trajectory", and "Generate Trajectory" will appear.

.. figure:: analysis/4/fine_locate_operate_ui_en.png
	:align: center
	:width: 5in

	Click on the FinePos Module

- Options such as “Run Program” and “Stop Program” function in the same way as the model-less build function, which can be described in the model-less build section. Other functions are described here:

- Get automaticcapture pose: After the positioning of the workpiece, the program will get the recommended photo position corresponding to each weld seam, click "Get automatic photo position" to get the recommended photo position.

- Generate Photo Pose with Reference to Model-Free Construction: The photo points taught during the model-free construction process will be automatically acquired as the photo points for fine positioning.  

- Reference SLAM Generated Photo Pose: Automatically generates camera poses corresponding to the existing weld seams in "Weld Editing". To check the camera view for a specific pose, switch AIRLab to simulation mode, enable the "Virtual Camera", and click on the desired point to view it. If obstacle avoidance operation is required later, click "	Barrier-free path planning", "Generate collision-free trajectory ", and then "Run Collision-Free Program" in sequence. Otherwise, click "Run Program" directly to proceed with fine positioning.

- Acquire Weld Seam Recognition Data: Generate a welding program based on the results of fine positioning recognition, as well as the already edited weld seams and their attributes.

- Reference model-free acquisition of weld seam recognition data: Generate a welding program based on the results of model-free construction, as well as the already edited weld seams and their attributes.

- Barrier-free path planning:Click " Barrier-free path planning " to plan the welding program after collision detection.

- Generate collision-free trajectory: Click " Generate collision-free trajectory ", the robot trajectory after collision detection will be generated in the 3D scene.

- Run Collision-Free Program: Click " Run Collision-Free Program ", the robot will move according to the robot motion trajectory after collision detection.

The user chooses to run the program or run the accessibility program for weld identification after selecting the confirmation trajectory. After the fine position program is run, the final weld node is generated under the program module.

Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After running the fine position, the final weld node is generated under the program module, and by clicking on the “Program” module, the user can choose to “run the program”, “stop the program”, “generate the trajectory” and other options, The user can select options such as “Run Program”, “Stop Program”, “Generate Trajectory”, etc. by clicking on the “Program” module. These options function in the same way as the “Run Program” option for model-less builds described above.

.. figure:: analysis/4/55.png
	:align: center
	:width: 2in

	Click on the Program Module

Clicking on “Generate Trajectory” generates a weld trajectory in the AIRLab 3D scene, and the user can choose to run a simulation on the trajectory.

.. figure:: analysis/4/56.png
	:align: center
	:width: 3.5in

	simulation trajectory

Click “Generate Tool”, the tool position of the key node will be displayed in the 3D scene, as shown in the following figure.

.. figure:: analysis/4/57.png
	:align: center
	:width: 3.5in

	Generation Tools

After the simulation and tool position are correct, click “Run Program” to start the actual welding.

The generated program can be adjusted, click on the generated node, you can delete it, add nodes above, add nodes below, edit nodes, move up or down operations. Click on the plus sign to the right of the program module, AIRLab software interface will appear in the program page, you can customize the content of the node, click “confirm”, the program node under the generation of the content of the node.

Point information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Point Information Module: Click the point in the point list, you can delete or edit the point. Click “Edit Points”, the interface of AIRLab software will show the page of point information modification, users can choose to move the direct target point, synchronize the current position or save the modified points.

.. figure:: analysis/4/58.png
	:align: center
	:width: 6in

	Modification of point information

Move to target point: user clicks “Move to target point” button, the robot end will move to the current edited point.
   
Synchronize the current point position: When the user clicks the "Synchronize Current Position" button, the pose of the currently selected point target0 will be modified to the pose of the robot that is actually taught.

Modify and save point position: The user modifies the point information, and then clicks the "Save Modify Point" button to modify the current point coordinates.


Reference coordinate system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Reference coordinate system: click the reference coordinate system icon in the menu bar, a new reference coordinate system will be create, the user can select the reference frame of reference coordinate system for the workpiece coordinate system or base coordinate system;Also can delete the current reference coordinate system, or edit the coordinate system.

.. figure:: analysis/4/59.png
	:align: center
	:width: 6in

	Reference coordinate system page

Select which coordinate system is the reference coordinate system, then set the coordinates of the reference coordinate system, select “Show” and click the “Set” button, the reference coordinate system will be displayed in the AIRLab 3D scene. Select “Do not show” and click “Set”, the displayed coordinate system will be hidden.

Pop-Ups and Other Pages
--------------------------
This section describes the AIRLab software pop-ups and other pages, pop-ups including about pop-ups, log pop-ups, software upgrade pop-ups, virtual camera pop-ups, global settings pop-ups, weld process query pop-ups, clearing the gun shear pop-ups, weld data calculation and collection of pop-ups and so on; Other pages including other control, simulation, debugging page, program configuration and multi-language settings.

About
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When "About" is selected, clicking the button will display the current version and release date of the AIRLab software, middleware, and vision module, as shown in the follow picture.

.. figure:: analysis/4/60.png
	:align: center
	:width: 3in

	AIRLab version information and release date display


Log
~~~~~~~~~~~~~~~~~~~~~~~~~
Logs are used to record the system running process and exception information, enabling quick problem location. Clicking this button opens a Log Management pop-up window.

Logs are divided into four levels: INFO, WARNING, ERROR, and DEBUG. After selecting a log level, set it as the current log level (default: INFO).

As shown in the follow picture,, the specific meanings are listed in Table 3-2.

.. figure:: analysis/4/log-en.png
	:align: center
	:width: 3in

	AIRLab Menu Bar-Logs

File Size: Refers to the size of a single log file. When a log file exceeds this size, the software will automatically generate a new log file.

Daily Retention Count: Refers to the maximum number of logs saved per day. When this limit is exceeded, the software will automatically delete the oldest log file generated on the same day.

Retention Period: Refers to the number of days logs can be stored. When this period expires, the software will automatically delete all logs that have reached the expiration date.

.. centered:: Table 3-2  Log level information

.. image:: analysis/4/表3-2.png
	:align: center
	:width: 6in


Software/Firmware Upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~
Click Window - Software/Firmware Upgrade to open the "Software/Firmware Upgrade" interface.

.. figure:: analysis/4/SF_UI_S_en.png
	:align: center
	:width: 3in

	Software/Firmware Upgrade Interface

- AIRLab Software Upgrade

Click "File Selection" to open the file selection window. Select the AIRLab.tar.gz upgrade file and click "Open". Please ensure the filename and format are correct.

.. figure:: analysis/4/SF_choose_S_en.png
	:align: center
	:width: 6in

	Selecting the AIRLab Software Upgrade Package

After selecting the file, click "Open". Confirm that the upgrade package path is correct, then click the "Upgrade" button to begin the software upgrade.
	
.. figure:: analysis/4/SF_chosen_S_en.png
	:align: center
	:width: 5in

	Click on the "Upgrade" button

Click "Upgrade" and wait for the upgrade package to decompress. The upgrade progress will be displayed in the progress bar. Please wait patiently.

.. figure:: analysis/4/65.png
	:align: center
	:width: 3in

	AIRLab software upgrade in progress

After the upgrade progress reaches 100%, click Confirm and restart the software, the upgrade is complete.

.. figure:: analysis/4/66.png
	:align: center
	:width: 3in

	AIRLab software upgrade completed

If the upgrade package is corrupted or incomplete, the interface will display an upgrade failure message, and the AIRLab version will be rolled back to its state prior to the upgrade. After the rollback is completed, click Confirm to restart the software, recheck the upgrade package, and perform the update again.

.. figure:: analysis/4/sw_update_rollback.png
	:align: center
	:width: 6in

	AIRLab Software Upgrade Failure Interface Feedback

- Camera Firmware Upgrade

Click the "Camera Firmware Upgrade" header to open the corresponding window, as shown below.

.. figure:: analysis/4/SF_UI_F_en.png
	:align: center
	:width: 5in

	Camera Firmware Upgrade

Click "File Selection" to open the file selection window. Select the upgrade file named FRSV_XXX_PRO.tar.gz and click "Open". Please ensure the filename and format are correct.

.. figure:: analysis/4/SF_choose_F_en.png
	:align: center
	:width: 6in

	Selecting the Camera Firmware Upgrade Package

After selecting the file, click "Open". Confirm that the upgrade package path is correct, then click the "Upgrade" button to begin the camera firmware upgrade.

.. figure:: analysis/4/SF_chosen_F_en.png
	:align: center
	:width: 5in

	Clicking the "Upgrade" Button

Click "Upgrade" and wait for the upgrade package to decompress. The upgrade progress will be displayed in the progress bar. Please wait patiently.

.. figure:: analysis/4/SF_process_F_en.png
	:align: center
	:width: 3in

	Camera Firmware Upgrading

Once the upgrade progress reaches 100%, click "Confirm" and restart the camera to complete the upgrade. Afterwards, you can follow the operations described in the "Import Module" section, open the "Device Information" interface, and view the current camera firmware version.

.. figure:: analysis/4/SF_success_F_en.png
	:align: center
	:width: 3in

	Camera Firmware Upgrade Completed

If the upgrade package is corrupted or incomplete, the interface will display upgrade failure feedback and will roll back the camera firmware version to its state before the upgrade. Re-check the upgrade package and try the update again.

.. figure:: analysis/4/SF_fail_F_en.png
	:align: center
	:width: 3in

	Camera Firmware Upgrade Failed

Version Verification
~~~~~~~~~~~~~~~~~~~~~~~
Click “Window” - “Version Verification” to open the version verification dialog. If all versions are displayed with a green check mark, it indicates that the verification is successful and the AIRLab software can run normally, as shown below.

.. figure:: analysis/4/version_verification_ui.png
	:align: center
	:width: 3.5in

	“Version Verification” dialog

If the library shows a red cross status in the version verification pop-up window, it indicates that the version of the library or function package does not match, as shown in the figure below. You can report this issue to the after-sales staff and obtain the latest upgrade package.

.. figure:: analysis/4/version_verification_error.png
	:align: center
	:width: 3.5in

	“Version Verification” error

TCF and Camera Hand-Eye Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click "Window" - "TCF and Camera Hand-Eye Calibration". The corresponding pop-up window will be displayed on the page, as shown below.

.. figure:: analysis/4/TCF_hand_UI_en.png
	:align: center
	:width: 3.5in

	TCF and Camera Hand-Eye Calibration Pop-up

First, configure the hand-eye calibration parameters. After setting the parameters, click "Confirm". The effects of each parameter are as follows:

- End Joint Reachable Angle Range: The safe angular interval within its motion range where the robot's end joint can rotate without colliding with itself or the environment.

- Number of Photo Points: During single-sided visual calibration, the number of poses to which the robot automatically moves and photographs the calibration board. The final number of calculated calibration poses is twice this value.

- Photo Distance: During automatic calibration, the preset working distance between the robot end-effector (camera) and the calibration board.

- Reverse Joint Configuration: An alternative joint state that allows the robot to reach the same point in space. Typically, this is called a reverse configuration when the robot's primary joints (e.g., arm, elbow) are oriented differently from the regular solution (e.g., elbow up or down). Check this option according to the actual robot posture to ensure correct motion planning.

Next, proceed with the camera hand-eye calibration. Manually drag the robot to position the camera directly above the calibration board, at a distance of 400-600mm from the board. Then, click the "Start Calibration" button. After clicking, the following confirmation pop-up will appear. Confirm that the robot is at the start position, then click "OK" to begin calibration.

.. figure:: analysis/4/TCF_hand_start_pop_en.png
	:align: center
	:width: 3.5in

	Camera Hand-Eye Calibration Confirmation Pop-up

After calibration is complete, the results need to be verified. Click the "Start Verification" button. After the program finishes running, the verification accuracy results will be updated in the corresponding fields, as shown below.

.. figure:: analysis/4/TCF_hand_res_en.png
	:align: center
	:width: 3.5in

	Camera Hand-Eye Calibration Verification Results

.. important::
	A camera error ≤ 0.5mm is a normal result; otherwise, camera calibration needs to be repeated. A combined error ≤ 1mm is a normal result; otherwise, accuracy verification needs to be repeated.

After completing the hand-eye calibration, proceed to TCF calibration. Click the "TCF Calibration" header to switch to the corresponding interface, as shown below.

.. figure:: analysis/4/TCF_calib_UI_en.png
	:align: center
	:width: 3.5in

	TCF Calibration

First, configure the TCF photoelectric calibration parameters. Among these, the X, Y, and Z direction offsets refer specifically to the tool's offset in the X, Y, and Z directions respectively. After completing the settings, click the "Confirm" button.

Then, click the "Move to Start Point" button to move the robot arm to the TCP calibration start point obtained from the hand-eye calibration. Then, click the "Start Calibration" button to perform TCF calibration.

Upon completion, the interface will display the corresponding calibration results, as shown below. After confirming they are correct, click the "Apply" button to apply the calibrated TCF results, completing this TCF calibration.

.. figure:: analysis/4/TCF_calib_res_en.png
	:align: center
	:width: 3.5in

	TCF Calibration Results

Virtual Camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Through the display of the virtual camera field of view, it is possible to observe whether the current camera shooting position is appropriate. At the same time, users can adjust the shooting position based on the display of the virtual camera field of view, and then adjust the camera to the optimal shooting position.

Click on the menu bar - Virtual Camera, and a virtual camera pop-up window will appear in the 3D scene, displaying the camera's field of view at the current position, as shown in the figure below.

.. figure:: analysis/4/68.png
	:align: center
	:width: 4in

	Virtual Camera Display Field of View

Adjust the camera position in the 3D scene, and the corresponding virtual camera field of view will also be synchronously transformed.

.. figure:: analysis/4/69.png
	:align: center
	:width: 4in

	Camera field of view transformation

Data Source Export
~~~~~~~~~~~~~~~~~~~~
To achieve complete retention of key data and operation records, and provide reliable data support for subsequent problem location, analysis and closed-loop resolution, AIRLab offers a Data Source Exportfunction. When an error occurs during user operation, click Window (W) → Data Source Export, export all the day’s data using this function and send it to technical staff for problem troubleshooting and resolution. The detailed operation method is described as follows:

Open the Data Source Export pop-up window and click the Select Export Path button to bring up the path selection pop-up window; after confirming the export path, click the Export button to start exporting the data source.

.. figure:: analysis/4/source_data_export1.png
	:align: center
	:width: 4in

	Select Export Path

.. figure:: analysis/4/source_data_export2.png
	:align: center
	:width: 4in

	Click Export after Confirming the Export Path

Once the export starts, a progress prompt pop-up window will appear, displaying the current export progress as shown in the figure. A prompt pop-up window indicating the completion of export will also appear when the export is finished, as shown in the figure.

.. figure:: analysis/4/source_data_export3.png
	:align: center
	:width: 4in

	Export in Progress...

.. figure:: analysis/4/source_data_export4.png
	:align: center
	:width: 4in

	Data Source Export Completed

If the Data Source Export function is used when the available disk space is less than 5GB, AIRLab will prompt the user to free up disk space before exporting.

Global Settings
~~~~~~~~~~~~~~~~~~~~
The "Global Settings" option under the "Window" menu bar in AIRLab provides configurations for Robot Self-Collision Detection, Torch Pose Calculation Rules, and Photo Pose Calculation Rules. These three settings are described below.

1.Self-Collision Detection

The Self-Collision Detection interface is shown below.

.. figure:: analysis/4/global_set_collision_en.png
	:align: center
	:width: 3.5in

	Self-Collision Detection

The Self-Collision Detection interface includes four types of collision thresholds, aimed at reducing the possibility of collisions during the robot's welding movement. Currently, only the "Collision Detection Distance Threshold for the Free-Moving Process" is available. This threshold refers to the collision distance for the robot's free-moving path between the retraction point of the previous weld and the approach point of the next weld.

When Self-Collision Detection is enabled, even if the user does not set a specific "Collision Detection Distance Threshold for the Free-Moving Process (mm)" (i.e., using the default value of 0 mm), AIRLab will still perform collision detection on the robot's free-moving path and plan a collision-free safe path. When the user sets this parameter, AIRLab will plan a free-moving path that maintains a greater distance from obstacles, based on the input threshold value, while still ensuring no collision.

.. figure:: analysis/4/global_set_collision_para_en.png
	:align: center
	:width: 3in

	Self-Collision Detection Parameter Setting

After setting the parameters of collision detection, click “confirm” button to complete the parameter setting and close the “Global Settings” pop-up window. 

.. important::
	After the collision detection is enabled, users need to teach the withdrawal and convergence points for each weld when creating the weld template program.

After completing the settings of the project tree and other related parameters, the user clicks on the “One Click Start” button in the toolbar of AIRLab, and when the program runs into the obstacle avoidance planning section, AIRLab will show a “Progress Alert” pop-up window to display the current progress of the planning. AIRLab will show the progress of the current planning as shown in the figure.    

.. figure:: analysis/4/71.png
	:align: center
	:width: 3.3in

	Obstacle avoidance planning in progress

If the obstacle avoidance planning fails, the pop-up window switches to the following figure, and the user needs to re-teach the exit point and convergence point, and click the “One Click Start” button again.

.. figure:: analysis/4/72.png
	:align: center
	:width: 3.5in

	Failure of obstacle avoidance planning

If the planning is successful, the pop-up window will be switched to the following figure, users can click “View Trajectory” button to generate the simulation trajectory of the motion instruction under the ‘Program’ node; click “Clear Trajectory” button to clear the trajectory in the interface; click “Run Program” button to start running the lua program directly. Click “Clear Trajectory” button to clear the trajectory in the interface; click “Run Program” button to start running the lua program directly.

.. figure:: analysis/4/73.png
	:align: center
	:width: 3.5in

	Progress bar alert popup

After successful obstacle avoidance planning, the relevant “MoveJ()” instruction in the ‘Program’ node of the project tree will be amended to “SplinePTP()”.

The following simulation trajectory diagram as an example to show the actual effect of AIRLab collision detection, Figure 3-76 for the opening of the collision detection function, AIRLab automatic obstacle avoidance planning trajectory; Figure 3-77 for the opening of the collision detection is not open, the trajectory obtained by AIRLab through the motion planning, it can be seen clearly that the robot will be empty moving process and the collision of the workpiece.

.. figure:: analysis/4/74.png
	:align: center
	:width: 4.5in

	Turn on collision detection planning

.. figure:: analysis/4/75.png
	:align: center
	:width: 4.5in

	No collision detection planning

In the case that the obstacle environment does not change, the user can not repeat the obstacle avoidance planning after successfully completing one obstacle avoidance planning, if you need to repeat the instructions under “Program” in the project tree, click “Run Program” in “Work Program” on the sub-page. If you need to run the commands under “Program” in the project tree repeatedly, click “Run Program” in “Work Program” on the subpage. If the obstacle environment changes, you have to click the “Run” button again to plan a new obstacle avoidance path.

2.Torch Pose Calculation Rule Configuration

The Torch Pose Calculation Rule configuration interface is shown below.

.. figure:: analysis/4/global_set_weld_gun_en.png
	:align: center
	:width: 4in

	Torch Pose Calculation Rule Configuration

If the recommended welding torch pose for a weld seam does not meet the actual welding requirements, you can enter this page to configure the calculation rules. If this rule is not set, the parameters from the last setup or the system default parameters will be used.

These parameters primarily affect the recommended welding torch pose for weld seams. Among them, the recommended angle (default angle) between the torch and a linear weld seam is 60°, with the current allowable min-max angle setting range between 40° and 80°. The recommended angle (default angle) between the torch and an arc weld seam is 30°, with the allowable angle setting range between 0° and 90°. The torch tip length, torch body length, angle between the tip and body, and body radius need to be set according to the measured data of the actual torch used. After setting the parameters, click "Get Recommended Weld Pose" to complete the parameter update.

After the parameters are set, click the "Add Weld" button in "Weld Editing", and after selecting a weld seam, the AIRLab 3D scene will display the recommended welding torch pose. If changes to the aforementioned pose are needed, please refer to the operations in the "Weld Editing" page (see Section 3.5.4).

3.Photo Pose Calculation Rule Configuration

The Photo Pose Calculation Rule configuration interface is shown below.

.. figure:: analysis/4/global_set_auto_photo_en.png
	:align: center
	:width: 4in

	Photo Pose Calculation Rule Configuration

These parameters mainly affect the camera pose automatically obtained in the "Fine Positioning" module. Currently, the camera pose calculation rules expose parameters for the camera's length, width, height, maximum shooting distance, minimum shooting distance, and the robot's 6th axis maximum and minimum joint angles. Among them, the camera's length, width, and height parameters affect collision detection and should be set according to the actual camera dimensions. The shooting distance refers to the linear distance between the camera and the weld seam; the default shooting range is between 300mm and 600mm. The maximum and minimum joint angle parameters for the robot's 6th axis are used to set soft limits for the robot's 6th joint, considering that the welding torch protrudes significantly and is prone to collision with other parts of the robot body; thus, they can be set according to the actual end-effector situation.

After successful configuration, click the menu item "Generate Camera Poses with Reference to SLAM" in the "Fine Positioning" module. The software will acquire the camera poses corresponding to the weld seam numbers edited by the user in the previous step.

Welding process query pop-up window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click on Process - Welding Process in the menu bar, and the AIRLab software interface displays the Process Inquiry pop-up window.

.. figure:: analysis/4/76.png
	:align: center
	:width: 3.5in

	Process Inquiry Popup

The left side of the pop-up window is for welding process classification, including flat welding, flat angle welding, vertical upward welding and other 9 categories, click on the welding process under the welding process classification, the right side will display the specific information of the process.

Add welding process: Select the category of welding process to be added, click on the plus sign next to “P_type”, a welding process will be added under the category to be edited;

.. figure:: analysis/4/77.png
	:align: center
	:width: 3.5in

	Newly added welding process

Click the newly added welding process and edit the welding process name and operation logic between weld passes (only applicable for multi-layer and multi-pass welding) on the right side, then add weld pass information. Click the plus button next to the weld pass list to create a new weld pass entry. If the process is multi-layer and multi-pass welding, add multiple weld passes as needed; otherwise, add only one weld pass.

.. figure:: analysis/4/78.png
	:align: center
	:width: 3.5in

	Modify weld channel information

Click the weld channel in the weld channel list, and the information of the currently clicked weld channel will be displayed in the weld channel editing section. Modify the weld channel information by selecting the reference coordinate system, safety point, offset, and binding the welding process and click Finish, and the information of the weld channel in the weld channel list will be modified.

.. figure:: analysis/4/78.png
	:align: center
	:width: 3.5in

	Editing of Multi-layer and Multi-pass Welding

Operation Logic between Weld Passes: Applied for multi-layer and multi-pass welding, including two types: Pause Processing and Continuous Operation.Pause Processing means the system stops after the current weld pass is completed and does not proceed to the next weld pass;Continuous Operation means the system proceeds to the next weld pass immediately after the current weld pass is completed.

Reference Coordinate System: The coordinate system referenced for offset if the weld pass needs to be offset. It is generally divided into the base coordinate system, workpiece coordinate system and custom coordinate system. Users need to add the reference coordinate system on the main interface first.

Safety Point: For multi-layer and multi-pass welding, safety points must be set between weld passes. That is, the robot returns to the safety point first after the completion of the first weld pass, then starts the operation of the second weld pass. The number of safety points can be customized to multiple.

Offset (Relative to Reference Coordinate System): The offset position relative to the previous weld pass when adding a multi-layer and multi-pass welding process.

Bind Welding Process: Set the selected weld pass to be bound or unbound to a welding process. Click the Welding Process Query button to enter the detailed parameter query and setting interface of the process.

After modifying all the welding channel information, click the “Finish” button under the welding channel list, and the terminal will show that the new multi-layer multi-channel welding process has been successful, and then a new welding process will be successfully added.

.. figure:: analysis/4/80.png
	:align: center
	:width: 3.5in

	New Welding Processes Successful

Modify welding process: Click on the welding process to be modified, modify the welding process data as needed, and you can add, modify or delete the list of weld passes.

1)Add a new weld path: Click the plus sign next to the weld path list to add a weld path in the weld path list.

2)Modify weld pass: Click the weld pass that needs to be modified in the list of weld passes, the information of the weld pass will be displayed in the editing of the weld pass, after modifying the information of the weld pass, click the “Finish” button, and the information of the weld pass in the list of weld passes will be modified.

3)Delete Path: Select the weld path that needs to be deleted, click the delete icon next to the list of weld paths, and the weld path will be deleted.

After all the modifications are completed, click the “Finish” button under the list of welding channels, the software page will prompt “Does the process already exist? Click “confirm” button, the terminal displays “Modify Multi-layer Multi-pass Welding Process Successfully”, that is, successfully modify the welding process.

.. figure:: analysis/4/81.png
	:align: center
	:width: 3in

	Modifying Welding Process Tips

Delete Welding Process: Select the welding process to be deleted and click on the delete icon next to the process type and the process will be deleted.


Cylinder Filling Process Query Pop up Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The pop-up window for querying the cylindrical filling process is shown in the figure below. The cylindrical filling process includes two parts: filling the bottom surface of the cylinder and secondary reinforcement.

.. figure:: analysis/4/82.png
	:align: center
	:width: 3in

	Cylinder Filling Process Query Pop up Window

1. Fill the bottom surface of the cylinder

Before performing cylindrical filling welding, users need to set parameters such as welding current, welding voltage, welding speed, spacing, offset, safety point selection, and swing process selection.

2. Secondary reinforcement
   
After the cylindrical filling welding is completed, secondary reinforcement welding is carried out, and the same user needs to set parameters first.

The filling interval refers to the vertical distance between two adjacent filling layers;

Inward filling offset refers to the horizontal distance between the starting point of filling and the edge of the cylinder;

The safety point name is the transition point of the robot during the filling and reinforcement process. After completing one filling or reinforcement, the robot needs to return to that point for the next welding.

Reinforcement interval refers to the vertical distance between adjacent reinforcement layers;

The upward offset of secondary reinforcement refers to the vertical interval between the starting point of the second reinforcement and the starting point of the first reinforcement;

Users can add, modify, or delete cylindrical filling processes,

New: Select "Add" as the change method, then set the process parameters and the name of the new filling process, and click the "Finish" button to add a new filling process;

Modification: Select "Modify", choose a cylindrical filling process name, then reset the process parameters, and click the "Finish" button to modify the parameters of the process;

Delete: Select "Delete", choose a cylindrical filling process name, and then click the "Finish" button to delete the process.


Welding seam edit pop-up window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click the ”weld sem” module. After adding a weld seam, click the edit icon—this will bring up the Weld Seam Editing pop-up window in the 3D scene, as shown in the figure. Below is an introduction to all editing items:

.. figure:: analysis/4/83.png
	:align: center
	:width: 3in

	weld seam edit pop-up window

- Weld Seam Type: Automatically generated based on the selected weld seam. 

- Weld Seam Number: Automatically generated based on the selected weld seam. 

- Reverse Direction: Displays the welding direction of the weld seam in the 3D scene. Select whether to reverse the direction according to actual welding needs. If "Yes" is selected, the direction of the weld seam in the 3D scene will be reversed.

Indentation Settings

- Start Indentation: Set the indentation at the start of the weld seam. When welding this seam, the process will begin from the start point after the indentation. 

- End Indentation: Set the indentation at the end of the weld seam. When welding this seam, the process will stop at the end point after the indentation.

Point Offset and Angle Settings 

If the position of the start point, end point, or intermediate point of the current weld seam is inaccurate, correction can be made through point offset and angle settings:

- Select the point that needs to be offset, set "Offset" to "Yes", and then configure the position offset for the selected point. Offset can be performed in either the base coordinate system or the workpiece coordinate system. 

Welding Posture Strategy

Configure the tool posture for welding; you can either set the welding posture angle directly or use a custom posture: 

- Welding Posture Angle: Adjust the tool posture by modifying the tool's pitch angle, push-pull angle, and rotation angle. 

- Custom Posture: Adjust the tool posture by directly setting the posture of the tool tip. You can teach a suitable posture first, then click the "Acquire Current" button to capture the current posture. 

Approach Point and Retract Point Settings

Configure the approach point and retract point for the weld seam. During welding, the robot will first pass through the approach point before reaching the weld seam’s start point; after welding is completed, it will retract from the weld seam’s end point to the retract point: 

- Approach Point Strategy: Includes custom distance or custom point:

(1)Custom Distance: Refers to the distance along the normal direction of the start point. 

(2)Custom Point: Refers to the approach point position taught manually.

- Retract Point Strategy: Settings for the retract point are similar to those for the approach point: Custom Distance here refers to the distance along the normal direction of the end point. 

Welding Process Settings

For weld seams that require binding to a welding process: 

(1)Set "Bind Welding Process?" to "Yes". 

(2)Select the type of welding process to bind and the specific welding process (parameters, procedures, etc.).

For the editing of spline curve weld seams, when setting points and angles, you can choose the setting method as either overall setting or setting for a specific point:

- If you select "Overall Setting", the configured point offset and welding posture will apply to all points of the weld seam. 

- If you select "Setting for a Specific Point", the configured point offset and welding posture will only apply to the selected point.
 
Other editing items are the same as those for straight + arc weld seams.

.. figure:: analysis/4/yangtiao.png
	:align: center
	:width: 6in

	spline curve weld seams edit



Welding data calculation and collection pop-up window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click on Welding → Welding Data Collection, and the current welding information pop-up window will appear. The window displays real-time welding status information, including welding current, welding voltage, and welding speed. The arc time and arc length are statistical data, showing the total welding duration and total welding length performed using the AIRLab software since the last reset. Click &quot;Reset&quot; to clear the welding duration and arc length. To modify the welding current and voltage in real time, enter the desired values and click &quot;Set.&quot;

.. figure:: analysis/4/84.png
	:align: center
	:width: 3in

	Welding data collection pop-up window


Torch Cleaning and Wire Cutting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Click “Window”–“Torch Cleaning and Wire Cutting” to open the “Torch Cleaning and Wire Cutting Settings” popup, as shown below. The parameters to be configured on this page include: Enable Automatic Torch Cleaning and Wire Cutting, Cleaning Method, Cleaning Cycle, Enable Oil Spray Point, Torch Cleaning Safety Point, Torch Cleaning Point, Wire Cutting Safety Point, and Wire Cutting Point.

.. figure:: analysis/4/85.png
	:align: center
	:width: 2.5in

	Parameter setting for gun clearing and wire cutting

This function supports both manual and automatic operation modes.The manual mode is intended for scenarios where the robot needs to perform torch cleaning or wire cutting immediately.The automatic mode is suitable for scenarios where the robot triggers torch cleaning and wire cutting operations automatically at fixed time intervals during its operation.

The manual mode is divided into Manual Torch Cleaning and Manual Wire Cutting.For manual torch cleaning, the parameters that need to be configured are: Enable Oil Spray Point, Torch Cleaning Safety Point, and Torch Cleaning Point. Once configured, click the Manual Torch Cleaning button to start the cleaning process.For manual wire cutting, only the Wire Cutting Safety Point and Wire Cutting Point need to be set. After configuration, click the Manual Wire Cutting button to initiate the wire cutting operation.

For automatic torch cleaning and wire cutting, all the parameters on the page need to be configured, then click the confirm button. When the cumulative welding time of the robot’s current welding session reaches the set cleaning and cutting cycle, a prompt dialog, as shown below, will appear after the robot stops welding, asking the user whether to proceed with torch cleaning and wire cutting.If Yes is selected, the robot will automatically perform torch cleaning and wire cutting.If No is selected, the robot will skip the cleaning and cutting operations, including the Torch Cleaning Safety Point, Torch Cleaning Point, Wire Cutting Safety Point, and Wire Cutting Point.

.. figure:: analysis/4/86.png
	:align: center
	:width: 3in

	Reach the clear gun shear cycle

.. important::
	If automatic torch cleaning and wire cutting is enabled, the cleaning and cutting cycle cannot be set to 0!

.. figure:: analysis/4/87.png
	:align: center
	:width: 3in

	Popup for unset cycles in auto mode

When using the torch cleaning and wire cutting function for the first time, the user needs to manually teach the Torch Cleaning Safety Point, Torch Cleaning Point, Wire Cutting Safety Point, and Wire Cutting Point.Teaching method: First, open the “Torch Cleaning and Wire Cutting” dialog. According to the point addition method and the torch cleaning and wire cutting station diagram in the dialog, add the four points mentioned above. After successfully adding the points, select the corresponding point names from the dialog, configure the other parameters, and click the confirm button. The parameters on the page, along with the joint values of the four points, will be saved into the configuration file for torch cleaning and wire cutting.

After importing other projects, AIRLab will automatically read the parameters from the configuration file and add the Torch Cleaning Safety Point, Torch Cleaning Point, Wire Cutting Safety Point, and Wire Cutting Point to the point list.

.. important::
	If the position of the torch cleaning and wire cutting station has not changed, the user does not need to teach these four points again.

Automatic loop operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
AIRLab offers the function of automatically cycling through welding projects, allowing users to repeatedly execute welding processes on workpieces. The detailed steps are as follows:

Step 1: Launch AIRLab, import the workpiece registration template project, and open the menu bar—select the automatic cycle operation pop-up window, as shown in the figure below.

.. important::
	AIRLab has specific requirements for the path of the workpiece registration template project. It must be placed in /Data/Work_template under the AIRLab directory. No other USD files are allowed in this folder besides the workpiece registration template project. The project name can be arbitrary.

.. figure:: analysis/4/88.png
	:align: center
	:width: 3in

	AIRLab menu bar - Window - Auto Loop Run

Set loop parameters according to actual needs, and the introduction of each parameter is as follows:   

.. figure:: analysis/4/89.png
	:align: center
	:width: 3in

	Automatic loop operation parameter settings

Enable Automatic Cycle Operation: If automatic cycle operation is required, click this button to activate the function.

Cycle Interval: The waiting time between cycles. For example, after the robot completes the welding process for the current workpiece, it will wait for this interval before importing the template program again to proceed with the next cycle.

Cycle Mode: There are two types,Continuous Cycle: Runs indefinitely. Fixed Cycle: The robot automatically stops after completing the set number of cycles.

Cycle Count: This parameter only needs to be set when the cycle mode is Fixed Cycle. (Note: The cycle count cannot be set to 0.)

.. important::
	Once the automatic cycle operation parameters are configured, they are automatically saved and loaded. If no changes are needed, simply import the workpiece registration template—the system will use the last saved settings without requiring repeated configuration.

Step 2: Click the "One-Click Run" icon button in the AIRLab menu bar to start executing the Workpiece Registration Template Project, initiating workpiece recognition. The recognition process is shown in the figure below.

The progress of workpiece recognition is displayed as shown in the figure below.Upon successful recognition, the matching score of the workpiece is shown Figure 3-93.

AIRLab then automatically searches for the corresponding welding project of the recognized workpiece. If the project exists in the specified path, it will be imported automatically,and terminal will show the path,as shown in the figure below.If recognition fails, AIRLab will display an error message and suggest corrective actions.

.. important::
	Welding projects must be placed in the /Data/Weld_template folder under the AIRLab directory.The welding project name must exactly match the workpiece name. For example, if the workpiece is named ZH-0-01-A, its corresponding welding project must be ZH-0-01-A.usd. If the welding project is not found in the specified path, AIRLab will fail to retrieve it and display a pop-up warning.

.. figure:: analysis/4/90.png
	:align: center
	:width: 6in

	The workpiece is being identified

.. figure:: analysis/4/91.png
	:align: center
	:width: 6in

	The workpiece recognition is successful
	
.. figure:: analysis/4/92.png
	:align: center
	:width: 6in

	Automatically retrieve welding projects and import new projects

Step 3: After the welding project is automatically imported, AIRLab controls the robot to execute the project. Once the program completes, AIRLab and the robot enter the cycle interval wait state.

.. important::
	If different workpieces need to be replaced, users should estimate the replacement time in advance and set the "Cycle Interval" parameter accordingly. If no workpiece replacement is needed, the cycle interval can be set to 0 or 1 (minimal delay).

Step 4: After the waiting period ends, the next cycle begins. AIRLab automatically clears the current project and re-imports the Workpiece Registration Template Project.Upon successful import, AIRLab controls the robot to restart workpiece recognition.f recognition succeeds, AIRLab searches for the corresponding welding project. If the project exists, Step 3 is repeated.

Step 5:AIRLab automatically controls the robot to repeat Step 4 based on the configured Cycle Mode and Cycle Count until all automatic welding cycles are completed，as shown in the figure below.

.. important::
	If a robot controller error or AIRLab error occurs during the cycle, the automatic operation stops immediately, requiring manual troubleshooting before resuming.

.. figure:: analysis/4/93.png
	:align: center
	:width: 4.5in

	Reaching the set number of cycles, ending the automatic loop operation

The above outlines the usage method and steps for AIRLab's Automatic Cycle Operation function.

Wire Stick-out Length Compensation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the wire stick-out length was not accurately set during the welding torch tool calibration, resulting in it being too long or too short, the "Wire Stick-out Length Compensation" function can be used. When enabled, subsequent welding will proceed using the compensated stick-out length. The usage method is as follows:

First, click "Window"-"Wire Stick-out Length Compensation". The "Wire Stick-out Length Correction" pop-up window shown in the figure below will appear.

.. figure:: analysis/4/stickout_off_en.png
	:align: center
	:width: 3in

	Wire Stick-out Length Correction Pop-up

After clicking the "Enable/Disable" button, the "Stick-out Length Compensation" parameter setting becomes available. The value of this parameter affects the final welding trajectory. After setting the parameter, click the "OK" button, as shown below.

.. figure:: analysis/4/stickout_on_en.png
	:align: center
	:width: 3in

	Wire Stick-out Length Parameter Setting Pop-up

If an abnormal compensation value is entered, a warning pop-up will be displayed, and the parameter will be set to the limit value, as shown below.

.. figure:: analysis/4/stickout_popup_en.png
	:align: center
	:width: 4in

	Compensation Parameter Exceeds Limit Pop-up

After completing this parameter setting, both the simulated welding trajectory in the interface and the actual welding trajectory will be calculated and executed based on the compensated wire stick-out length, as shown in the comparison below.

.. figure:: analysis/4/stickout_0_offsets.png
	:align: center
	:width: 4in

	Welding Trajectory Display Before Compensation

.. figure:: analysis/4/stickout_50_offsets.png
	:align: center
	:width: 4in

	Welding Trajectory Display After Compensation

User data backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If a user needs to transfer a pre-configured welding process, template programs, and built workpiece data from one device to another to replicate the environment, AIRLab provides a user data backup feature.  

Click on the AIRLab menu bar - Window - User Data Backup, and a pop-up window titled "User Data Backup" will appear, as shown in the figure below. Below is a detailed introduction to the usage of the user data package import and export functions. 

.. figure:: analysis/4/94.png
	:align: center
	:width: 6in

	Pop up window for user data backup function

First, you need to select the "Data Backup and Restoration Type", choosing between "Single Template Data" and "All Data" as shown in the figure. Once confirmed, you can proceed with the import and export operations.

.. figure:: analysis/4/95.png
	:align: center
	:width: 3in

	Data Backup and Restoration Type

Export Function: 

If the data backup and restoration type is "All Data,click the "Export" button, and AIRLab will first write the version of the current software data package into the version.txt file for version matching verification during import. Then, AIRLab will proceed to copy the following data:  

Located in the Data folder under the executable file directory:

- The Work_template folder (storing workpiece registration templates)  

- The Weld_template folder (storing welding template programs)  

- The entity folder (storing workpiece and tool models)  

- The database file Airlab_weld_process.db(storing user-created welding process data)  

Located in the data folder under the main directory:

- The output folder (for models)  

- The register_model folder (for auto-saved model files)  

- The weld_seam_database folder (for weld seam databases)  

If the data backup and restoration type is "Single Template Data", you need to first open the template project in AIRLab, then click the "Export" button. AIRLab will package and compress the template and its dependent files, and place the output compressed file in the /Downloads directory of the main folder. The file name is the workpiece name with the .tar.gz extension, such as ZH-401-01-A.tar.gz. Similarly, AIRLab will write the version of the current single template data package into the single_version.txt document within the package for version matching verification.

During the export process, AIRLab will display a pop-up window indicating that the data package is being exported, as shown in the figure below. If cancellation is needed, click the "Cancel Export" button in the pop-up.

.. figure:: analysis/4/96.png
	:align: center
	:width: 6in

	User Single Template Data is currently being packaged and exported

Once completed, AIRLab will show another pop-up confirming the export and displaying the export path of the data package, as shown in the figure below.

.. figure:: analysis/4/96-1.png
	:align: center
	:width: 6in

	User Single Template Data export completed

.. important::
	If a user initiates the export function but any of the folders listed above do not exist, AIRLab will display a pop-up notification indicating the names and paths of the missing folders. The user must create these missing files or folders before proceeding with the export.

Additionally, if the permissions for any of the specified folders or files are modified to restrict access or copying, AIRLab will fail to export and provide the file path where the error occurred. Please check the file permissions based on the error message, correct them, and retry. (In some cases, restarting the edge PC may be required for permission changes to take effect.)  

The directory structure of the exported compressed package is shown in the figure below: 

.. figure:: analysis/4/96-2.png
	:align: center
	:width: 2.5in

	the directory structure of single template data

.. figure:: analysis/4/97.png
	:align: center
	:width: 2.5in

	The directory structure of the complete data package

Import Function:Click the "Select File" button to choose the data package to be imported (ensure the directory structure of the data package matches the one shown in the figure below). Then, click the "Import" button.  

AIRLab will first verify the version number in the version.txt file within the imported data package. If the version numbers match, the system will proceed with importing the data package contents.  

If the version numbers do not match, a pop-up message will appear, notifying the user of the version inconsistency and indicating that the data is incompatible and cannot be imported, as shown in the figure below. 

.. figure:: analysis/4/98.png
	:align: center
	:width: 6in

	Select the data package to be imported in the image

.. figure:: analysis/4/99.png
	:align: center
	:width: 6in

	The data package is currently being imported

.. figure:: analysis/4/100.png
	:align: center
	:width: 6in

	Data package import completed

.. figure:: analysis/4/101.png
	:align: center
	:width: 6in

	The imported data package version is inconsistent with the current AIRLab data package version and cannot be imported

.. important::
	The data package import function will first delete the original files and folders. If you still need to keep the files, please make sure to back them up before importing!

3D File Parsing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the user needs to perform welding on a model that has already been built in AIRLab, the software provides the “3D File Parsing” function, which replaces the previous “Model Construction” step and simplifies the workflow. The usage is as follows:

Step 1: Click AIRLab Menu – “Window” – “3D File Parsing”. The 3D File Parsing dialog will appear, as shown below.

.. figure:: analysis/4/3Dfile_prasing_dialog.png
	:align: center
	:width: 3.5in

	“3D File Parsing” dialog

Step 2: Click the “Open” button in the dialog. A file selection window will pop up. Choose the workpiece to be parsed, and then click “Open” again to confirm the selection, as shown below.

.. figure:: analysis/4/3Dfile_prasing_selection.png
	:align: center
	:width: 3.5in

	3D File selection

Step 3: A parsing progress bar will appear. Please wait patiently until the parsing is completed. The process is shown below.

.. figure:: analysis/4/3Dfile_prasing_progress_dialog.png
	:align: center
	:width: 3.5in

	“3D File Parsing” progress dialog

Step 4: After the progress is completed, the corresponding 3D model of the workpiece will be constructed in the scene, along with its associated weld seams, as shown below.

.. figure:: analysis/4/3Dfile_prasing_res_display.png
	:align: center
	:width: 6in

	“3D File Parsing” result display

Step 5: For subsequent operations, please refer to Section 3.5.3 Weld Seam Editing, Section 3.5.4 Workpiece Positioning, and Section 3.5.5 Automatic Photo Pose, to complete the following welding process.

Multi-Station Automatic Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AIRLab provides a Multi-Station Automatic Operation feature for multi-workpiece welding scenarios. If you have already recorded an AIRLab project file for a single workpiece, you can run multiple projects (i.e., multiple workpiece welding jobs) efficiently and automatically by specifying the required external-axis positions for each workpiece.

The following first describes the case where Enable Auto Recognition is set to No:

Step 1: Click AIRLab Menu → “Window” → “Multi-Station Automatic Operation.” The Multi-Station Automatic Operation dialog appears, as shown below.

.. figure:: analysis/4/multi_station_ui.png
	:align: center
	:width: 3.5in

	“Multi-Station Automatic Operation” dialog

Step 2: Move the external axis to the position required to complete welding for a given workpiece. Click “Get Position” to record the current external-axis position, as shown below.

.. figure:: analysis/4/multi_station_setting.png
	:align: center
	:width: 3.5in

	External-axis position setting

Step 3: Select the project file corresponding to the welding task you wish to run at this external-axis position. Click “Select” to open the file chooser, then click “Open” to confirm, as shown below.

.. figure:: analysis/4/multi_station_usda_select.png
	:align: center
	:width: 6in

	Project path selection and result

Step 4: Choose the desired modification mode: Add, Modify, or Delete. After confirming your choice, click “OK” to apply. To modify, select the target entry and click “OK.” Deletion is similar. See below.

.. figure:: analysis/4/multi_station_add_modify.png
	:align: center
	:width: 6in

	Add and Modify

Step 5: After completing all settings, click “Start Auto Run.” The welding job will begin.

Next is the case where Enable Auto Recognition is set to Yes:

Step 1: Similarly, after obtaining the external-axis position, enabling Auto Recognition will change the dialog as shown below. For details on Auto Recognition, refer to Section 3.6.11 Automatic Loop Operation.

.. figure:: analysis/4/multi_station_auto.png
	:align: center
	:width: 3.5in

	Auto Recognition options

Step 2: After choosing the modification mode, click “Confirm.” An Inquiry dialog will appear—please read carefully before proceeding. Click “Confirm” to complete the setup.

.. figure:: analysis/4/multi_station_inquiry_dialog.png
	:align: center
	:width: 3.5in

	Inquiry dialog

Extended axis synchronous motion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If an external axis is required during robotic welding, AIRLab provides external axis synchronization functionality.

After selecting the external axis in the import module, click confirm to open the external axis setting pop-up window, as shown in the figure below. After selecting the external axis, click confirm to import it. Click "Get" to obtain the current external axis coordinate system, and click "Save" to set the external axis coordinate system.

.. figure:: analysis/4/102.png
	:align: center
	:width: 3in

	Extension axis setting pop-up window

When editing long straight welds that require axis linkage extension, set the external axis positions for the starting and ending points, as shown in the figure below. After weld seam recognition, AIRLab will automatically generate a program based on the weld seam recognition results and the position of the external axis, achieving synchronous motion between the external axis and the robot.

.. figure:: analysis/4/103.png
	:align: center
	:width: 6in

	When editing long straight welds, it is necessary to set the position parameter of the extension axis


Other controls
~~~~~~~~~~~~~~~~~~~
Click the "Other Controls" button in the operation area to enter the IO setting interface, which mainly includes two modules of IO control and external axis setting.

(1) IO control module

As shown in Figure 3-116, the IO control module enables manual control of the digital outputs, analog outputs (0-10v) in the robot control box and the end tool digital outputs, analog outputs (0-10v) extended IO digital outputs, analog outputs (0-10v):

.. figure:: analysis/4/104.png
	:align: center
	:width: 3in

	IO Control Module

- DO Setting: Select the port number, click the "On" button to set the corresponding DO high, and click the "Off" button to set the corresponding DO low.
- AO Setting: Select the port number and enter the value (0-100) in the input box on the right, the value is a percentage, setting 100 means setting this AO port to 10v.

(2) Exaxis control

As shown in Figure 3-117, the External Axis Setup module enables control of the robot's external axis.

.. figure:: analysis/4/105.png
	:align: center
	:width: 3in

	exaxis Control

- Select the extended axis numbe: click the "Load" button to load the external axis protocol according to the selected extended axis number. Set the running speed (%), acceleration (%) and the maximum distance of the extended axis (mm).
- Remove Enable: Click on the "Remove Enable" button to remove enable from the external axis.
- Servo Enable: Click the "Servo Enable" button to enable the external axis.
- Forward jog: Click the "Forward jog" button to perform a forward tap of the external axis according to the set running speed, acceleration, and maximum distance of the extended axis.
- Reverse jog: Click the "Reverse jog" button to reverse pivot the external axes according to the set running speed, acceleration, and maximum distance of the extended axes.
- Stop jog: Click the "Stop jog" button to stop the external axis from pivoting.
- Zero Set: Click the "Zero Set" button to zero the external axis according to the zero return method, zero seeking speed and hoop speed.


Simulation
~~~~~~~~~~~~~~
As shown in Figure 3-118, after generating the simulation trajectory of the program, open the operation area - simulation, set the simulation speed and simulation interval, click on the "Run" button to start the simulation of the template program, click on the "Stop" button to stop the template program simulation. Click "Stop" button to stop the template program simulation. At the same time, it will generate the simulation trajectory point table to record the simulation trajectory points. In the table, the type of simulation track endpoints is LINEND, and when you click a line in the table, the virtual simulation robot will move to the clicked simulation track point, and at the same time, it will synchronously display the TCP coordinates of the simulation track point.

.. figure:: analysis/4/106.png
	:align: center
	:width: 6in

	Simulation Page

Program configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The program configuration page is used to configure the program before running it, including the program configuration section and the welding interrupt recovery configuration section, as shown in the figure below.  

.. figure:: analysis/4/107.png
	:align: center
	:width: 3in

	Program Configuration Page

The program configuration section includes program running configuration, program recognition configuration,program arc initiation configuration, no model construction settings, welding machine number selection and so on.

.. figure:: analysis/4/108.png
	:align: center
	:width: 3in

	Program Configuration

For program operation configuration, you can select either "Do Not Run Program After Recognition" or "Run Program After Recognition": 

- Do Not Run Program After Recognition: The welding program will not run automatically after the fine positioning program is executed. 

- Run Program After Recognition: The welding program will run automatically after the fine positioning program is executed.

The program recognition configuration is divided into rough positioning first followed by fine positioning, with the option to run only fine positioning.  

- Rough Positioning Followed by Fine Positioning: After clicking the one-click run button, AIRLab will automatically execute the workpiece positioning program in the current project first, followed by the fine positioning program.  

- Run Only Fine Positioning: After starting with one-click run, AIRLab will skip the workpiece positioning step and directly execute the fine positioning program.

For arc ignition configuration, you can set it to "Arc Ignition" or "No Arc Ignition": 

- Arc Ignition: If there is an arc ignition command in the program, arc ignition and welding will be performed during program operation. 

- No Arc Ignition: No arc ignition will occur during program operation; the robot will only move along the welding trajectory for simulated welding. 

You can set the simulated welding operation speed multiplier to increase the speed of the simulated welding process.

No model building setup: Currently, there are two methods - rebuilding and not rebuilding.

- Rebuilding: Reconstruct the model of the model free workpiece; Suitable for non model artifacts that have not been built before or have poor construction results and need to be rebuilt.

- Not rebuild: If you choose not to rebuild, the model free artifact model will not be rebuilt and will be directly imported from the previously built model. Applicable to previously built model free artifacts, there is no need to re model the model free artifact.

.. important::
	In practical operation, it is recommended to separately carry out the process of building model free artifacts, and after the artifact is successfully built, operate according to the original average model method. In the absence of a model workpiece model, it is recommended to always select "not rebuild" as the parameter for model free construction settings, as the weld seam numbers obtained from model free construction may change during each construction!

After configuring everything, click the "Confirm" button to complete the program configuration.

Welding interruption recovery configuration refers to clearing the parameters that need to be configured to continue welding when the program is interrupted during the welding process; Including the configuration of parameters for detecting unexpected interruptions in welding arc tracking and weld interruption detection.

.. figure:: analysis/4/109.png
	:align: center
	:width: 3in

	Welding interruption recovery configuration

The parameter configuration for detecting unexpected interruptions in welding arc tracking is aimed at configuring parameters for arc interruptions during the welding process, including selecting whether to detect and configuring the duration of arc interruption confirmation.

- Whether to detect: Indicates whether to detect accidental interruption of welding arc tracking.

- Confirmation duration of arc interruption: Define how many milliseconds arc interruption belongs to arc interruption and needs to be restored.

After configuration, click the "Confirm" button to complete the parameter configuration for detecting accidental interruption of welding arc tracking.

The configuration of welding interruption detection parameters is the parameters required to restore the interrupted robot motion after the program interruption during the welding process, including selecting whether to restore the welding interruption, configuring the overlap distance of the weld seam, configuring the speed of the robot returning to the arc starting point, and configuring the robot motion.

- Whether to restore welding interruption: Select restore. After the welding interruption, a pop-up window will pop up indicating the welding interruption. Clear the error before restoring the interruption, otherwise the interruption will not be restored.

- Overlap distance of weld seam: the overlap distance between the interrupted position and the previous interrupted position after resuming welding.

- Robot returning to arc starting point speed: The speed at which the robot returns to the set arc starting point after the interruption is restored.

- Robot movement to arc starting point mode: After restoring the interrupt, the robot returns to the set arc starting point mode, which can be selected as LIN or PTP mode.

After configuration, click the "Confirm" button to complete the configuration of welding interruption detection parameters.

After the welding interruption recovery configuration is fully configured, run the program. When a welding interruption signal is detected, the following pop-up window will pop up.

.. figure:: analysis/4/110.png
	:align: center
	:width: 3in

	Welding interruption pop-up window

After checking the environment and troubleshooting, clicking the "Resume Welding" button will restore the interrupt according to the configured parameters.


Multilingual settings
~~~~~~~~~~~~~~~~~~~~~~~~~
AIRLab software currently provides seven language options: Chinese (Simplified), Chinese (Traditional), English, Japanese, Korean, Russian, and French. The detailed multilingual settings page is shown in the figure below. This page provides three operations: switching languages; Export existing languages in AIRLab software; Import a new language. In order to meet the needs of users to switch between multiple languages, set new languages for AIRLab software, and modify existing language content in AIRLab software.

.. figure:: analysis/4/111.png
	:align: center
	:width: 3in

	"Multilingual Settings" Sub interface

The detailed operation introduction of the above functions is as follows:

(1)Switch the language of AIRLab

Click on the dropdown menu of "Multilingual" in Figure 3-124, select the desired language type, and click the "Confirm" button to immediately switch the AIRLab software language.

(2)User sets new language for AIRLab

Firstly, click the "Export" button to export the language file currently used by AIRLab in CSV format. The exported file path is located in the local Downloads folder, as shown in the figure below. 

.. figure:: analysis/4/112.png
	:align: center
	:width: 4in

	AIRLab Language File Export Path

The content format of the CSV file is shown in the figure below(if opened with a text editor), including four columns: language_id, location, source_text, translation_text. “language_id” represents the language type, “location” represents the position of the text in the source code, 'source_text' represents the text (Chinese) in the source code, and 'translation_text' represents the translation value corresponding to the source text.

.. figure:: analysis/4/113.png
	:align: center
	:width: 5in

	Content and format of AIRLab language CSV file

If you use LibreOfffice software to open it, as shown in Figure 3-126, please note that the opening format is shown in Figure 3-126.

.. figure:: analysis/4/114.png
	:align: center
	:width: 3in

	LibreOffice software

.. figure:: analysis/4/115.png
	:align: center
	:width: 5in

	Opening format of AIRLab multilingual files

Next is to write a CSV file for the user. When setting a new language, the user only needs to modify the contents of the first column language_id and the fourth column translation_text. Assuming the user has added French, replace all "English" in the first column of Figure 3-128 with "Français"; The content of the fourth column translation_text needs to be translated by the user based on the Chinese text of "source_text" to obtain the corresponding target language (for the same string appearing in the source text, please translate it into the same word).

.. important::
	Please do not modify any characters under the "source_text" column!

After completing the translation work, the user needs to rename the CSV file to a file name that is the table name of the language data table in the AIRLab language database. For example, the file name "en_translations table" in Figure 3-129 is the table name of the language type "English" in the database.

.. important::
	It is recommended to preserve the language characteristics of the user CSV file naming to avoid duplication with the names of existing language data tables in the database, which may result in errors where the contents of other language data tables are replaced.

Finally, import the CSV file into the AIRLab software, copy the file to the execution directory of the AIRLab software, click the "Import" button, and select the file to import, as shown in Figure 3-129. The AIRLab terminal displays “CSV file import successful”, indicating that the user's language file has been successfully imported, as shown in Figure 3-128. After restarting AIRLab, select the user's newly added language switch from the drop-down menu in "Language Selection".

.. figure:: analysis/4/116.png
	:align: center
	:width: 6in

	Pop up window of the "Import" button

.. figure:: analysis/4/117.png
	:align: center
	:width: 6in

	Terminal display information when language file import is successful

If the terminal displays "CSV file import failed", you can check the error message in the log record, and carefully check whether the imported CSV file is inconsistent with the originally exported CSV file in terms of the number of rows, columns, and the Chinese delimiter "；" between columns.

.. important::
	When modifying the content of "translation_text", it is necessary to refer to the field length of the Chinese text of "source_text". If the translation value is too long, please use abbreviations appropriately, otherwise the corresponding control text in the AIRLab interface may not be displayed completely.

(3) User modifies existing language in AIRLab

If the user needs to modify an existing language in AIRLab, they first need to click the "Export" button to export the CSV file of that language; After the modification is completed, copy the file to the execution directory of AIRLab software, click the "Import" button, select the modified file to import, and the terminal displays "CSV import successful". After restarting the software, the language modification is completed.

Considering the different usage habits of AIRLab English users, AIRLab-V1.0.2 version has designed the unit of measurement switching as a configuration item for users to choose whether to switch millimeters to inches, as shown in Figure 3-130.

.. figure:: analysis/4/118.png
	:align: center
	:width: 6in

	UI interface for switching measurement units

After the user selects the measurement unit to switch, the input box labeled in millimeters on the AIRLab interface will be converted to inches, as shown in Figure 3-131 and Figure 3-131.

.. figure:: analysis/4/119.png
	:align: center
	:width: 3in

	Before switching units of measurement

.. figure:: analysis/4/120.png
	:align: center
	:width: 3in

	After switching units of measurement

Error prompt pop-up window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
During the operation of AIRLab software, some errors may occur, and an error prompt pop-up window will appear on the interface as shown in the figure.

.. figure:: analysis/4/121.png
	:align: center
	:width: 3in

	Error prompt

After fixing the error based on its type, click the "one-click clear" button, the pop-up window will disappear, and then continue running. 

.. figure:: analysis/4/122.png
	:align: center
	:width: 6in

	Clean the error prompt

Extended Axis Coordinate System Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AIRLab provides a calibration function for the Extended Axis Coordinate System. After normally importing the robot, tools, and external axes, click "Import Module" - "External Axes" on the main interface,open the extended axis settings interface (see Section 3.5.1). Then, select the extended axis coordinate system to calibrate and click “Modify” to enter the Extended Axis Coordinate System Calibration interface, as shown below.

.. figure:: analysis/4/exaxis_calibration_ui.png
	:align: center
	:width: 6in

	Extended Axis Coordinate System Calibration interface

.. important::
	Exaxis0 cannot be calibrated. If you select Exaxis0, an error dialog will appear as shown below.

.. figure:: analysis/4/exaxis_calibration_crd0_error.png
	:align: center
	:width: 2.5in

	Exaxis0 calibration error dialog

A AIRLab provides a calibration method specifically for extended axes of the type “Single Degree-of-Freedom Linear Rail.” The detailed procedure is as follows:

Step 1: First, open the "Extended Axis Coordinate System Calibration" interface mentioned earlier. Click the "Clear Coordinate System" button, and confirm the "Whether the currently applied tool coordinate system has been calibrated" option. The prerequisite for calibrating the external axis is that the tool coordinate system used in the current application has been correctly calibrated. After confirmation, an "Inquiry" pop-up window will appear. Once confirmed, the calibration setup will officially begin.

.. figure:: analysis/4/exaxis_calibration_ui+dialog.png
	:align: center
	:width: 6in

	Calibration interface (left) and Inquiry dialog (right)

Step 2: Click the "Servo Enable" button to activate the extended axis. If successful, the button will turn green; otherwise, it will turn red and an error pop-up will be displayed. If the enable operation is successful, move to an appropriate position and click the "Zero Point Setting" button to complete the initial setup. The process is illustrated in the figure below.

.. figure:: analysis/4/exaxis_calibration_enable_disable.png
	:align: center
	:width: 6in

	Servo enable and zero point setting

Step 3: Keep the extended axis stationary and adjust the posture of the robotic arm's end effector so that the end tool is aligned with a fixed point on the extended axis. Click "Set Point 1." Once the button changes to "Modify Point 1," the setting is complete. If you need to modify this point, repeat the above steps. Similarly, after adjusting the tool posture (with an angle of approximately 30°), complete the "Set Point 2" process. The entire procedure is illustrated in the figure below.

.. figure:: analysis/4/exaxis_calibration_P1+P2.png
	:align: center
	:width: 6in

	Setting Point 1 and Point 2

Step 4: Click "Forward Jog" to move the extended axis by a distance of 200 mm. Once again, align the end tool with the previous fixed reference point, then click "Set Point 3." After the button changes to "Modify Point 3," the setting is complete. If modification of this point is needed, repeat the above steps. The process is illustrated in the figure below.

.. figure:: analysis/4/exaxis_calibration_P3.png
	:align: center
	:width: 3.5in

	Setting Point 3

Step 5: Click "Reverse Jog" to move the extended axis backward by 205 mm, then move it forward by 5 mm. Once again, align the end tool with the previous fixed reference point. Next, jog along the base coordinate system to move the end upward by 100 mm, then click "Set Point 4." After the button changes to "Modify Point 4," the setting is complete. If modification of this point is needed, repeat the above steps. The process is illustrated in the figure below.

.. figure:: analysis/4/exaxis_calibration_P4.png
	:align: center
	:width: 3.5in

	Setting Point 4

Step 6: After completing the above steps, click “Calculate” to compute the tool pose. The results will be displayed as shown below.

.. figure:: analysis/4/exaxis_calibration_cal_res.png
	:align: center
	:width: 3.5in

	Extended Axis Coordinate System Calculation Result

Step 7: Once the calculation results are verified, click “Save.” The results will be stored in the local path:
~/AIRLabExe/Data/import_config/Cleargun_cutwire_settings.config
under [Exaxis_coord_value_list]. In this example, Exaxis1 was calibrated, so the result is saved as <1 = “calibration result”>. At the same time, the Extended Axis Settings will display Exaxis1 as successfully calibrated.

If the calibrated external axis coordinate system is correct (with RX, RY, and RZ values close to 0), click the "Apply" button to send the calibrated external axis coordinate system to the robot controller for application.

.. figure:: analysis/4/exaxis_calibration_save_res.png
	:align: center
	:width: 6in

	Saving Extended Axis Coordinate System Calibration Result

If the selected extended axis coordinate system already exists (i.e., calibration data is already stored in the above path), an Inquiry dialog will appear asking whether to overwrite the previous result. Clicking “Confirm” will overwrite the existing calibration.

.. figure:: analysis/4/exaxis_calibration_inquiry_dialog.png
	:align: center
	:width: 3in

	Extended Axis Coordinate System Inquiry Dialog


Welding Feature Parameter Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When creating a new welding project or importing an existing welding project, AIRLab will pop up the Welding Feature Parameter Settings dialog box. The user shall make selections according to the characteristics of the workpiece used and following the interactive guidance steps on the page. After completing the selection, proceed with the subsequent welding steps in the normal procedure.

The operation method for welding feature configuration is described in detail below:

When creating or importing a welding project, the software interface automatically pops up the Welding Feature Parameter Settings window, which displays the current feature configuration in use by the software or the feature configuration recorded in the project file.

To modify or view the welding feature parameters during project operation, click the menu bar at the top of the page: Welding (W) → Welding Feature Parameter Configuration to reopen the dialog box for operation.

As shown in the figure below:

.. figure:: analysis/4/import.png
	:align: center
	:width: 6in

	Import Existing Welding Project – Welding Feature Parameter Settings Pop-up

.. figure:: analysis/4/new.png
	:align: center
	:width: 6in

	New Welding Project – Welding Feature Parameter Settings Pop-up

If you confirm to use the current feature configuration, click the Confirm Use button in above Figures.If you need to reselect features, click the Reselect Features button in the figure to enter the page shown in the following Figure.

There are three workpiece model construction methods available: Camera Acquisition, 3D File Integration, and SLAM Mapping.Click the corresponding icon; a welding feature description pop-up window (shown in the follow picture) will appear, displaying a detailed description of the currently selected method/feature.Please make a matching selection based on this description and the actual workpiece.

.. figure:: analysis/4/model_struct.png
	:align: center
	:width: 6in

	Reselect Features – Model Construction Method Selection

.. figure:: analysis/4/model_struct_camera.png
	:align: center
	:width: 6in

	Model Construction Method – Camera Acquisition Description Pop-up Display

.. important::
	If SLAM Mapping is selected as the model construction method, the Next button on the page will switch to Finish. Click this button directly to complete the welding feature parameter configuration.

If the model construction method selected is Camera Acquisition or 3D File Integration, continue to click Next to enter the planar feature selection page, as shown in the figure below.

.. figure:: analysis/4/normal.png
	:align: center
	:width: 6in

	Camera Acquisition – Planar Feature

.. figure:: analysis/4/3D_plane_box.png
	:align: center
	:width: 6in

	3D File Integration – Planar Feature

For planar feature selection using camera acquisition, considering the priority characteristics of the four planar types, you need to click the Reselect Features button when selecting planar features.Select Yes or No according to the interactive prompts on the interface and the planar structure of the workpiece, as shown in the figure below.The selected features will appear in the list under Selected Features on the page.

.. figure:: analysis/4/lap.png
	:align: center
	:width: 6in

	Camera Acquisition – Lap Joint Planar Feature

.. figure:: analysis/4/narrow.png
	:align: center
	:width: 6in

	Camera Acquisition – Narrow Planar Feature

.. figure:: analysis/4/box.png
	:align: center
	:width: 6in

	Camera Acquisition – Box Girder Planar Feature

.. figure:: analysis/4/normal.png
	:align: center
	:width: 6in

	Camera Acquisition – General Planar Feature

.. important::
	The interaction of the icon buttons on this page is different from that of other features. Clicking them only opens the welding feature description pop-up window and does not perform a selection operation.Feature selection will only take effect after you click the Reselect Features button!

For planar feature selection using 3D File Integration, there are currently two types: 3D General Plane and 3D Box Girder Plane.Clicking the icon button opens the welding feature description pop-up window, and the corresponding feature will be added to the Selected Features list at the bottom of the page, as shown in the figure below.

.. figure:: analysis/4/3D_plane_box.png
	:align: center
	:width: 6in

	3D File Integration – 3D Box Girder Planar Feature

After completing planar feature selection, click the Next button in above Figures to enter the Cylinder and Cone Feature Selection page, as shown in the figure below.

For the three features: Short Cylinder, Tall Cylinder, and Coexisting Short & Tall Cylinders, you need to actually measure the cylinder radius and enter the maximum radius and minimum radius values in the text boxes.

If the current workpiece does not involve cylinder or cone features, click Deselect and then click Next.If no cylinder or cone features have been selected, you may click Next directly.

.. figure:: analysis/4/short_cylinder.png
	:align: center
	:width: 6in

	Cylinder & Cone Features – Select Short Cylinder Feature

.. figure:: analysis/4/cancle_cylinder.png
	:align: center
	:width: 6in

	Cylinder & Cone Features – Deselect Feature

Following the cylinder and cone features is the planar relationship feature selection, as shown in the figure below.

There are only two types of planar relationship features: small gap and large gap. After selecting according to the actual features of the workpiece, check whether the features listed under Selected Features on the page are correct. If correct, click Confirm Selection to complete the welding feature parameter configuration. The pop-up window will close automatically upon successful setup.

.. figure:: analysis/4/small_gap.png
	:align: center
	:width: 6in

	Planar Relationship Features – Small Gap

.. figure:: analysis/4/large_gap.png
	:align: center
	:width: 6in

	Planar Relationship Features – Large Gap