from collections import deque

# Definition for a course
class Course(object):
    def __init__(self, x):
        self.val = x
        self.adj_list = []
        self.prereqs = []


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        visited = []
        # create course objects
        courses = []
        for i in range(numCourses):
            temp = Course(i)
            courses.append(temp)
            visited.append(0)
        
        # assign all prereqs and adjacent courses
        for l in prerequisites:
            courses[l[0]].prereqs.append(l[1])
            courses[l[1]].adj_list.append(l[0])
        
        # travel thru graph using BFS, see if we can reach all courses with no cycles
        myqueue = deque()
        
        # add all courses to queue that have no prereqs
        for i in range(len(courses)):
            if (len(courses[i].prereqs) == 0):
                myqueue.append(courses[i])
        
        # all courses have prereqs, return false
        if (len(myqueue) == 0):
            return False
        
        # variables to keep track if we are stuck in a cycle
        #if we reach same node twice and queue size hasnt changed, we are stuck in a real cycle
        stuck_on = None
        stuck_len = 0
        
        while (len(myqueue) > 0):
            temp = myqueue.popleft()
            
            #print("next vertex %d" % temp.val)
            
            # check if we can visit this course yet
            prereqs_done = False
            
            # we might not be stuck anymore, so reset
            if (len(myqueue) != stuck_len):
                stuck_on = None
                stuck_len = 0
            
            if (len(temp.prereqs) == 0):
                prereqs_done = True
            else:
                count = 0
                for n in temp.prereqs:
                    if (visited[n]):
                        count += 1
                if (count == len(temp.prereqs)):
                    prereqs_done = True
            
            if (prereqs_done == False and visited[temp.val] == False):
                
                #keep track of stuck node
                if (stuck_on is None):
                    stuck_on = temp.val
                    stuck_len = len(myqueue)
                #we've gone thru entire queue, we are still stuck, there is a cycle, return False
                elif (stuck_on == temp.val and len(myqueue) == stuck_len):
                    break
                
                myqueue.append(temp)
                continue
            
            # we found a cycle, return false
            if (visited[temp.val] and temp.val > 0):
                break
            
            # let's visit this course and add its adjacent courses to the queue    
            visited[temp.val] = 1
            
            #we are no longer stuck on this node, reset
            if (stuck_on == temp.val):
                stuck_on = None
                stuck_len = 0
            
            #print("visiting %d" % temp.val)
            
            for n in temp.adj_list:
                if (courses[n] not in myqueue): #dont enter duplicates back into queue
                    myqueue.append(courses[n])
                    
        #make sure we visited every course
        count = 0
        for i in range(len(visited)):
            if (visited[i] == 1):
                count += 1
            if (count == numCourses):
                return True
        
        return False
            
