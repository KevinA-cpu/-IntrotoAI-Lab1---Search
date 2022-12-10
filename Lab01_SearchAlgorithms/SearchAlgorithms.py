from cmath import sqrt
from math import inf
from platform import node
from turtle import distance
from Space import *
from Constants import *

def solutionColoring(path, g: Graph, sc: pygame.Surface):
    print("Solution found.")
    g.start.set_color(orange)
    g.draw(sc)
    #remove the start node for accurate coloring
    path.remove(g.start.value)
    previous_node = g.start.value
    for value in path:
        g.grid_cells[value].set_color(grey)
        g.grid_cells[value].draw
        pygame.draw.line(sc,green,
                         (g.grid_cells[previous_node].x, g.grid_cells[previous_node].y), 
                         (g.grid_cells[value].x, g.grid_cells[value].y))
        g.draw(sc)
        previous_node = value
    g.goal.set_color(purple)
    g.draw(sc)

def heuristic(x1,y1,x2,y2,radius):
    return abs((sqrt((x2-x1)**2 + (y2-y1)**2) / radius) * 100_000)

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')
    path = []
    open_set = [g.start.value]
    closed_set = []
    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    #Start node, color the node yellow
    closed_set.append(g.start.value)
    g.grid_cells[open_set[-1]].set_color(yellow)
    g.draw(sc)
    while closed_set:
        s = closed_set.pop()
        #Check if its the goal node
        if g.is_goal(g.grid_cells[s]):
            #Color the path to solution
            solutionColoring(path, g, sc)
            return True;
        g.grid_cells[s].set_color(yellow)
        g.draw(sc)
        #get adjacent node
        neighbours = g.get_neighbors(g.grid_cells[s])
        for neighbour in neighbours:
            if neighbour.value not in open_set:
                #Color discovered node
                open_set.append(neighbour.value)
                neighbour.set_color(red)
                g.draw(sc)
                closed_set.append(neighbour.value)
        #Color completed node
        g.grid_cells[s].set_color(blue)
        g.draw(sc)
        path.append(s)
    print("No solution found.")
    return False;
    #raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')
    path = []
    open_set = [g.start.value]
    closed_set = []
    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    closed_set.append(g.start.value)
    g.grid_cells[open_set[-1]].set_color(yellow)
    g.draw(sc)
    while closed_set:
        s = closed_set.pop(0)
        #Check if its the goal node
        if g.is_goal(g.grid_cells[s]):
            #Color the path to solution
            solutionColoring(path, g, sc)
            return True;
        g.grid_cells[s].set_color(yellow)
        g.draw(sc)
        #get adjacent node
        neighbours = g.get_neighbors(g.grid_cells[s])
        for neighbour in neighbours:
            if neighbour.value not in open_set:
                #Color discovered node
                open_set.append(neighbour.value)
                neighbour.set_color(red)
                g.draw(sc)
                #Color completed node
                closed_set.append(neighbour.value)
        g.grid_cells[s].set_color(blue)
        g.draw(sc)
        path.append(s)
    print("No solution found.")
    return False;
    #raise NotImplementedError('Not implemented')

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')
    path = []
    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    
    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    #Color start node
    g.start.set_color(yellow)
    g.draw(sc)
    while True:
        if open_set == False:
            print("No solution found.") 
            return False
        #Find the smallest cost node
        node = 0
        for n in open_set:
            if open_set[n] == min(open_set.values()):
                node = n
                break
                
        if (g.is_goal(g.grid_cells[node])):
            #Color the path to solution
            solutionColoring(path, g, sc)
            return True;
            
        closed_set.append(node)
        neighbours = g.get_neighbors(g.grid_cells[node])
        g.grid_cells[node].set_color(yellow)
        g.draw(sc)
        if neighbours:
            for neighbour in neighbours:
                neighbour_cost = cost[neighbour.value]
                if neighbour.value not in path:
                    neighbour.set_color(red)
                    g.draw(sc)
                if neighbour.value not in open_set and neighbour.value not in closed_set:
                    father[neighbour.value] = node
                    open_set[neighbour.value] = neighbour_cost
                elif neighbour.value in open_set:
                    if neighbour_cost < open_set[node]:
                        father[neighbour.value] = node
                        open_set[neighbour.value] = neighbour_cost
                
            path.append(node)
            open_set.pop(node)
            g.grid_cells[node].set_color(blue)
            g.draw(sc)
    
    #raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')
    path = []
    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement A* algorithm using open_set, closed_set, and father
    #Color start node
    g.start.set_color(yellow)
    g.draw(sc)
    while True:
        if open_set == False:
            print("No solution found.") 
            return False
        #Find the smallest cost node
        node = 0
        for n in open_set:
            if open_set[n] == min(open_set.values()):
                node = n
                break
    
        if (g.is_goal(g.grid_cells[node])):
            #Color the path to solution
            solutionColoring(path, g, sc)
            return True;
            
        closed_set.append(node)
        neighbours = g.get_neighbors(g.grid_cells[node])
        g.grid_cells[node].set_color(yellow)
        g.draw(sc)
        if neighbours:
            for neighbour in neighbours:
                neighbour_cost = heuristic(neighbour.x, neighbour.y, g.goal.x, g.goal.y, 10) + cost[neighbour.value]
                if neighbour.value not in father:
                    neighbour.set_color(red)
                    g.draw(sc)
                if neighbour.value not in open_set and neighbour.value not in closed_set:
                    father[neighbour.value] = node
                    open_set[neighbour.value] = neighbour_cost
                elif neighbour.value in open_set:
                    if neighbour_cost < open_set[node]:
                        father[neighbour.value] = node
                        open_set[neighbour.value] = neighbour_cost
            path.append(node)
            open_set.pop(node)
            g.grid_cells[node].set_color(blue)
            g.draw(sc)
    #raise NotImplementedError('Not implemented')
    
def Dijkstra(g:Graph, sc:pygame.Surface):
    print('Implement Dijkstra algorithm')
    path = []
    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0
    
    while True:
        if open_set == False:
            print("No solution found.") 
            return False
        #Find the smallest cost node
        node = 0
        for n in open_set:
            if open_set[n] == min(open_set.values()):
                node = n
    
        if (g.is_goal(g.grid_cells[node])):
            #Color the path to solution
            solutionColoring(path, g, sc)
            return True;
            
        closed_set.append(node)
        neighbours = g.get_neighbors(g.grid_cells[node])
        g.grid_cells[node].set_color(yellow)
        g.draw(sc)
        if neighbours:
            for neighbour in neighbours:
                neighbour_cost = cost[neighbour.value]
                if neighbour.value not in path:
                    neighbour.set_color(red)
                    g.draw(sc)
                if neighbour.value not in open_set and neighbour.value not in closed_set:
                    father[neighbour.value] = node
                    open_set[neighbour.value] = neighbour_cost
                elif neighbour.value in open_set:
                    if neighbour_cost < open_set[node]:
                        father[neighbour.value] = node
                        open_set[neighbour.value] = neighbour_cost
                
            path.append(node)
            open_set.pop(node)
            g.grid_cells[node].set_color(blue)
            g.draw(sc)
    #raise NotImplementedError('Not implemented')
