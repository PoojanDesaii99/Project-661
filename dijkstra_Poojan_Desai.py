# Importing Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt 
import time 
import heapq 


# Creating a Class for Node with it's parameters as X,Y Coordinates, Cost at each Node, it's Parent
class Node:
    
    # Initialize Data
	def __init__(self, x, y, cost, parent_node):

		self.x = x
		self.y = y
		self.cost = cost
		self.parent_node = parent_node
	
    # To support Node Comparision
	def __lt__(self,other):
		return self.cost < other.cost


'''Below functions will define the moves for up, down, left and right
    '''
def move_up(x,y,cost):
	y += 1
	cost += 1
	return x,y,cost

def move_down(x,y,cost):
	y -= 1
	cost += 1
	return x,y,cost

def move_left(x,y,cost):
	x -= 1
	cost += 1
	return x,y,cost

def move_right(x,y,cost):
	x += 1
	cost += 1
	return x,y,cost


'''Below functions will define the diagonal moves for upright, upleft, downright and downleft
    '''
def move_upright(x,y,cost):
	x += 1
	y += 1
	cost += np.sqrt(2)
	return x,y,cost

def move_downright(x,y,cost):
	x += 1
	y -= 1
	cost += np.sqrt(2)
	return x,y,cost

def move_upleft(x,y,cost):
	x -= 1
	y += 1
	cost += np.sqrt(2)
	return x,y,cost

def move_downleft(x,y,cost):
	x -= 1
	y -= 1
	cost += np.sqrt(2)
	return x,y,cost
    
    
''' This function will nodes according to the action set define above.
    '''
def move_node(move,x,y,cost):
    if move == 'Up':    # Move up
        return move_up(x,y,cost)
    elif move == 'UpRight':    # Move upright
        return move_upright(x,y,cost)
    elif move == 'Right':    # Move right
        return move_right(x,y,cost)
    elif move == 'DownRight':    # Move downright
        return move_downright(x,y,cost)
    elif move == 'Down':    # Move down
        return move_down(x,y,cost)
    elif move == 'DownLeft':    # Move downleft
        return move_downleft(x,y,cost)
    elif move == 'Left':    # Move left
        return move_left(x,y,cost)
    elif move == 'UpLeft':    # Move upleft
        return move_upleft(x,y,cost)
    else:
        return None


''' This function will define an Obsatcle space and buffer space using Half plane equation method
    '''
def plot_map(width, height):
    
    # Generating Obstacle Space
    obstacle_space = np.full((height, width),0)
    
    for y in range(0, height) :
        for x in range(0, width):
            
            # Plotting Buffer Space for the Obstacles using Half Plane Equations
            
            # Rectangle 1 Obastacle
            r11_buffer = (x + 5) - 100  
            r12_buffer = (y - 5) - 100
            r13_buffer = (x - 5) - 150
            # r14_buffer = y - 0    # No need to define lower most line at boundry
            
            # Rectangle 2 Obastacle
            r21_buffer = (x + 5) - 100  
            # r22_buffer = y - 250  # No need to define upper most line at boundry
            r23_buffer = (x - 5) - 150
            r24_buffer = (y + 5) - 150 
            
            # Hexagon Obstacle
            h6_buffer = (y + 5) +  0.58*(x + 5) - 223.18
            h5_buffer = (y + 5) - 0.58*(x - 5) + 123.21
            h4_buffer = (x - 6.5) - 364.95
            h3_buffer = (y - 5) + 0.58*(x - 5) - 373.21
            h2_buffer = (y - 5) - 0.58*(x + 5) - 26.82
            h1_buffer = (x + 6.5) - 235.040
            
            # Triangle Obstacle
            t1_buffer = (x + 5) - 460
            t2_buffer = (y - 5) + 2*(x - 5) - 1145
            t3_buffer = (y + 5) - 2*(x - 5) + 895
            
            # Setting the line constrain to obatain the obstacle space with buffer
            if((h6_buffer>0 and h5_buffer>0 and h4_buffer<0 and h3_buffer<0 and h2_buffer<0 and h1_buffer>0) or (r11_buffer>0 and r12_buffer<0 and r13_buffer<0) or (r21_buffer>0 and r23_buffer<0 and r24_buffer>0) or (t1_buffer>0 and t2_buffer<0 and t3_buffer>0)):
                obstacle_space[y, x] = 1
             
             
            # Plotting Actual Object Space Half Plane Equations
            
            # Rectangle 1 Obastacle
            r11 = (x) - 100  
            r12 = (y) - 100
            r13 = (x) - 150
            # r14 = y - 0
            
            # Rectangle 2 Obastacle
            r21 = (x) - 100  
            # r22 = (y) - 250
            r23 = (x) - 150
            r24 = (y) - 150 
            
            # Hexagon Obstacle
            h6 = (y) +  0.58*(x) - 223.18
            h5 = (y) - 0.58*(x) + 123.21
            h4 = (x) - 364.95
            h3 = (y) + 0.58*(x) - 373.21
            h2 = (y) - 0.58*(x) - 26.82
            h1 = (x) - 235.04  
            
            # Triangle Obstacle
            t1 = (x) - 460
            t2 = (y) + 2*(x) - 1145
            t3 = (y) - 2*(x) + 895

            # Setting the line constrain to obatain the obstacle space with buffer
            if((h6>0 and h5>0 and h4<0 and h3<0 and h2<0 and h1>0) or (r11>0 and r12<0 and r13<0 ) or (r21>0  and r23<0 and r24>0) or (t1>0 and t2<0 and t3>0)):
                obstacle_space[y, x] = 2    

    return obstacle_space


'''Check if the Goal Node is Reached
    '''
def check_goal(current, goal): 
    
	if (current.x == goal.x) and (current.y == goal.y):
		return True
	else:
		return False


'''Check if the Move made is a Valid Move
    '''
def check_valid(x, y, obstacle_space):
    
    # Obstacle space limit
	size = obstacle_space.shape
    
    # Check the Boundary 
	if( x > size[1] or x < 0 or y > size[0] or y < 0 ):
		return False
    
	# Check if the given node is in Obstacle Space
	else:
		try:
			if(obstacle_space[y][x] == 1) or (obstacle_space[y][x] == 2):
				return False
		except:
			pass
	return True


'''Function for Generating a Unique ID
    '''
def unique_id(node):
    id = 3333*node.x + 113*node.y 
    return id


'''Dijkstra Algorithm
    '''
def dijkstra_algorithm(start, goal, obstacle_space):
    
    ## Check if given Node is the Goal Node
    if check_goal(start, goal):
        return None, 1
    
    # Storing as Nodes only when Start is not Goal
    goal_node = goal
    start_node = start
    
    # Data Handlers
    unexplored_nodes = {}
    all_nodes = []
    explored_nodes = {} 
    open_list = []
    
    # All possible Movements for a Node
    possible_moves = ['Up','UpRight','Right','DownRight','Down','DownLeft','Left','UpLeft']
        
    # Assigning Unique Key to Start Node
    start_key = unique_id(start_node)
    unexplored_nodes[(start_key)] = start_node
    
    # Push the Start Node into the Heap Queue
    heapq.heappush(open_list, [start_node.cost, start_node])
    
    # Loops until all the Nodes have been Explored, i.e. until open_list becomes empty
    while (len(open_list) != 0):

        current_node = (heapq.heappop(open_list))[1]
        all_nodes.append([current_node.x, current_node.y])
        current_id = unique_id(current_node)

        if check_goal(current_node, goal_node):
            goal_node.parent_node = current_node.parent_node
            goal_node.cost = current_node.cost
            print("Goal Node found")
            return all_nodes,1

        if current_id in explored_nodes:
            continue
        else:
            explored_nodes[current_id] = current_node
		
        del unexplored_nodes[current_id]
        
        # Looping through all possible nodes obtained through movements
        for moves in possible_moves:
            
            # New x,y,cost after moving.
            x,y,cost = move_node(moves, current_node.x, current_node.y, current_node.cost)
            
            # Updating Node with the New Values
            new_node = Node(x, y, cost, current_node)
            
            # New ID
            new_node_id = unique_id(new_node)
            
            # Checking Validity
            if not check_valid(new_node.x, new_node.y, obstacle_space):
                continue
            elif new_node_id in explored_nodes:
                continue
            
            # Updating Cost and Parent, if lesser cost is found.
            if new_node_id in unexplored_nodes:
                if new_node.cost < unexplored_nodes[new_node_id].cost: 
                    unexplored_nodes[new_node_id].cost = new_node.cost
                    unexplored_nodes[new_node_id].parent_node = new_node.parent_node
            else:
                unexplored_nodes[new_node_id] = new_node
   			
            # Pushing all the open nodes in Heap Queue to get the least costing node.
            heapq.heappush(open_list, [ new_node.cost, new_node])
   
    return  all_nodes, 0


'''Function to Back Track position from Goal Node to Start Node.
    '''
def back_track_path(goal_node):
    
    # Creating a Stack to hold the Backtracked Nodes
    backtrack_stack = []
    
    # Storing the Goal Node
    backtrack_stack.append(goal_node)
    
    # Backtracking to the Preceeding Nodes until Start Node is Reached
    while backtrack_stack[-1].parent_node != -1:
        parent = backtrack_stack[-1].parent_node
        backtrack_stack.append(parent)
        
    # Since the Backtracking was done from Goal to Start Node, Reversing the Stack to get path from Start to Goal
    backtrack_stack.reverse()
    
    # Extracting the x, y coordinates of the path from the Backtracked Nodes
    x_path = [node.x for node in backtrack_stack]
    y_path = [node.y for node in backtrack_stack]
    
    return x_path, y_path


''' This class is used to plot and see the explored nodes as an animation
    '''
class PathPlotter:
    def __init__(self, start_node, goal_node, obstacle_space):
        self.start_node = start_node
        self.goal_node = goal_node
        self.obstacle_space = obstacle_space
        
        ## Plot the Start and Goal Positions
        plt.plot(start_node.x, start_node.y, "Db")
        plt.plot(goal_node.x, goal_node.y, "Dg")
        
        ## Plot Map
        plt.imshow(obstacle_space, "seismic")
        self.ax = plt.gca()
        self.ax.invert_yaxis()
        
    # Plot the explored nodes
    def plot_explored_nodes(self, explored_nodes):
        # Plotting the Explored Nodes
        for i in range(len(explored_nodes)):
            plt.plot(explored_nodes[i][0], explored_nodes[i][1], "3y")
            
            # Un-comment below line to visualize the nodes expanding and searching and reaching the goal node. It will take time to reach goal node.
            plt.pause(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001) 
            
    # Plot the shortest path    
    def plot_path(self, x_path, y_path):
        plt.plot(x_path, y_path,"--r")
        plt.show()
        plt.pause(3)
        plt.close('all')


'''----------------------------------------------------------------------------------------------------------------------------------------'''

# Main Function to Execute the Program
if __name__ == '__main__':
    
    # Robot Space width and Height
    width = 600
    height = 250
    
    # Getting the Coordinates of Obstacles
    obstacle_space = plot_map(width, height)
    
    # Getting the Start and Goal Coordinates from the User    
    start_x = int(input("Enter Start Position's X Coordinate: "))
    start_y = int(input("Enter Start Position's Y Coordinate: "))

    goal_x = int(input("Enter Goal Position's X Coordinate: "))
    goal_y = int(input("Enter Goal Position's Y Coordinate: "))
    
    # Start Timer to Check the Time of Execution
    start_time = time.time()
    
    # Validating the Start Node if it is in Permitted Robot Space
    if not check_valid(start_x, start_y, obstacle_space):
        print("Enter Start Node within the permitted Robot Space")
        exit(-1)
    
    # Validating the Goal Node if it is in Permitted Robot Space
    if not check_valid(goal_x, goal_y, obstacle_space):
        print("Enter Goal Node within the permitted Robot Space")
        exit(-1)
    
    ## Creating Start Node which has attributes start (x,y) coordinates, cost = 0 and parent_node = -1
    start_node = Node(start_x, start_y, 0.0, -1)
    
    ## Creating Goal Node which has attributes goal (x,y) coordinates, cost = 0 and parent_node = -1
    goal_node = Node(goal_x, goal_y, 0.0, -1)
    
    # Implementing Dijkstra Algorithm
    explored_nodes, goal_status = dijkstra_algorithm(start_node, goal_node, obstacle_space)
    
    # Back Track only if the Goal Node is reached.
    if (goal_status == 1):
        x_path, y_path = back_track_path(goal_node)
        
        # Plotting the Map, Obstacles and the Generated Path
        plotter = PathPlotter(start_node, goal_node, obstacle_space)
        plotter.plot_explored_nodes(explored_nodes)
        plotter.plot_path(x_path, y_path)
        cost = goal_node.cost
        print(f"Cost of reaching the goal: {cost:.2f}")
    else:
        print("Goal could not be planned for the given points")

    # Stopping the Timer after Program Execution
    end_time = time.time()
    print(f"Time Taken to Execute the Program is: {end_time - start_time}")


##---------------------End of Program##---------------------##	




	








