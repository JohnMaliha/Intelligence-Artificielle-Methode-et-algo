# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    curr_state = problem.getStartState()

    states_to_visit = util.Stack()
    states_to_visit.push(curr_state)

    visited_states = []

    states_path = util.Queue()
    states_path.push((curr_state, []))

    while not states_to_visit.isEmpty():
        curr_state = states_to_visit.pop()
        current_path = next(
            (path for state, path in states_path.list if state == curr_state), [])

        if problem.isGoalState(curr_state):
            return current_path

        for (state, direction, weight) in problem.getSuccessors(curr_state):
            if state not in visited_states:
                visited_states.append(state)
                states_to_visit.push(state)

            new_path = current_path[:]
            new_path.append(direction)

            states_path.push((state,   new_path))


def breadthFirstSearch(problem):
    curr_state = problem.getStartState()

    states_to_visit = util.Queue()
    states_to_visit.push(curr_state)

    visited_states = [curr_state]

    states_path = {curr_state: []}

    while not states_to_visit.isEmpty():
        curr_state = states_to_visit.pop()

        if problem.isGoalState(curr_state):
            return list(states_path[curr_state])

        for (state, direction, weight) in problem.getSuccessors(curr_state):
            if state not in visited_states:
                visited_states.append(state)
                states_to_visit.push(state)

            new_path = list(states_path[curr_state])
            new_path.append(direction)

            path_exists = state in states_path.keys()

            if path_exists:
                shortest_path = min(states_path[state], new_path, key=len)
                states_path.update({state: shortest_path})
            else:
                states_path[state] = new_path


def uniformCostSearch(problem):
    curr_state = problem.getStartState()

    states_to_visit = util.PriorityQueue()
    states_to_visit.push(curr_state, 0)

    visited_states = [curr_state]

    weighted_path = [(curr_state, [], 0)]

    while not states_to_visit.isEmpty():
        curr_state = states_to_visit.pop()

        if problem.isGoalState(curr_state):
            goal_states = [
                state for state in weighted_path if state[0] == curr_state]
            return min(goal_states, key=lambda x: x[2])[1]

        curr_path, curr_weight = next(
            ((path, weight) for state, path, weight in weighted_path if state == curr_state), ([], 0))

        for (state, direction, weight) in problem.getSuccessors(curr_state):

            new_weight = curr_weight + weight
            new_path = curr_path[:]
            new_path.append(direction)

            if state not in visited_states:
                visited_states.append(state)
                states_to_visit.push(state, new_weight)

            weighted_path.append((state, new_path, new_weight))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    current_state = problem.getStartState()
    states_to_visit = util.PriorityQueue()
    states_to_visit.push(current_state, heuristic(current_state, problem))

    current_path = {}
    current_path[current_state] = ([], 0)
    

    while not states_to_visit.isEmpty():
        current = states_to_visit.pop()

        if problem.isGoalState(current):
            return current_path[current][0]

        for coords, direction, weight in problem.getSuccessors(current):
            past_direction, past_weight = current_path[current]
            updated_weight = past_weight + weight
            total_cost = updated_weight + heuristic(coords, problem)
            new_direction = past_direction + [direction]
            
            if coords in current_path:
                if current_path[coords][1] > updated_weight:
                    states_to_visit.update(coords, updated_weight)
                    current_path[coords] = (new_direction, updated_weight)

            else:
                current_path[coords] = (new_direction, updated_weight)
                states_to_visit.push(coords, total_cost) 
                
                 
        
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
