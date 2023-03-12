  -----------------------------------------------------------------------
  ENPM661 - Spring 2023

  Project 2

  Implementation of the Dijkstra Algorithm for a Point Robot
  -----------------------------------------------------------------------

Name: Poojan N. Desai UID: 119455760 Email: pndesai9@umd.edu

------------------------------------------------------------------------

GitHub Link:
https://github.com/PoojanDesaii99/Project-661/blob/main/dijkstra_Poojan_Desai.py

Video is included in zip file named as proj2_Poojan_Desai

Code: - Code consists of: 'Generating Map and it's Obstacles', 'Movement
in 8 Directions', 'Using Search Algorithm and Back Tracking' and
'Visualizing the Tracked Path' - The Search Algorithm used here is '
Dijkstra Algorithm' to reach end goal and obtain the path. - The code
has been delineated very clearly in the comments provided in the Code.

Dependencies: - Works for any python 3 version) - Python running IDE. (I
used Visual Studio Code to program the Code and Execute the Code) -
Libraries: numpy, matplotlib.pyplot, heapq, time

The visualization of the plotting is not smooth as it should be. I have
included a video of node exploring and reaching to the goal. It takes
time, therefore, I have added only first few minutes of video and
entered initial node and goal node close to each other for visualization
purpose. The code will work for any random start and goal nodes

Instructions to Run the Code:

To get the Output (without Visualization) - Open the
'dijkstra_Poojan_Desai.py' file in any IDE. (I used VS Code) - Run the
Program - In the terminal, the program will ask user to provide the x
and y coordinates of Start and Goal Node. Enter as prompted. Example:
Start: 0, 200; Goal: 410, 10 - The Output Plot with planned Path should
be Visible. The shortest path is highlighted with red dashed line.

To get the Output (with Visualization) - Open the
'dijkstra_Poojan_Desai.py' file in any IDE. (I used VS Code) - UnComment
the line used for Visualization i.e. '340', which says-
"plt.pause(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)" -
Run the Program - In the terminal, the program will ask user to provide
the x and y coordinates of Start and Goal Node. Enter as prompted.
Example: Start: 0, 200; Goal: 410, 10 - The Visualization should be
Displayed but takes a long duartion to move across a short space.

Understanding the Output Plot - The Blue region represents the Robot's
moving space, while the Red areas (2 rectangles, 1 hexagon, and 1
triangle) represent the Obstacles. - The white pixels represent the 5 mm
BUffer Space. - The yellow pixels represent the explored path. - Red
Dotted Lines represent the Intended Route.
