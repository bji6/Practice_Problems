import pdb
import time
from collections import deque

# Definition for a tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        start = time.clock()
        tree_heights = {}
        
        edge_dict = {}

        for i in range(n):
            if (i not in edge_dict):
                edge_dict[i] = []
            
            for tupp in edges:
                if (i in tupp):
                    edge_dict[i].append(tupp)
        
        used_dict = {}
        min_height = None

        temp_edges = {}

        #calculate tree heights
        for i in range(0,n,1):
            #build a tree first, from perspective of node i
            nodes = {}

            used_dict = {}

            myqueue = deque()
            queue2 = deque()
            height = 1
            myqueue.append(i)
            counter = -1
            level_count = -1

            #create all tree nodes, assign children
            while (len(myqueue) > 0):
                j = myqueue.popleft()
                counter += 1
                temp = TreeNode(j)
                used_dict[j] = 1
                to_remove = []
                #pdb.set_trace()
                temp_edges = edge_dict[j]
                
                for k in temp_edges:
                    tupp = temp_edges[k]
                    if (j == tupp[0] and tupp[1] not in used_dict):
                        temp.children.append(tupp[1])
                        myqueue.append(tupp[1])
                        used_dict[tupp[1]] = 1
                        to_remove.append(k)
                    elif (j == tupp[1] and tupp[0] not in used_dict):
                        temp.children.append(tupp[0])
                        myqueue.append(tupp[0])
                        used_dict[tupp[0]] = 1
                        to_remove.append(k)

                for k in to_remove:
                    del temp_edges[k]

                #pdb.set_trace()
                nodes[j] = temp
                if (len(temp.children) > 0):
                    queue2.append(len(temp.children))
                    # we are on first level
                    if (level_count == -1):
                        level_count = queue2.popleft()
                
                #pdb.set_trace()
                if (counter == level_count):
                    height += 1
                    if (min_height is not None and height > min_height):
                        break
                    counter = 0
                    if (len(queue2) > 0):
                        level_count = sum(queue2)
                        queue2.clear()
            
                #pdb.set_trace()

            #print("i == %d" % i)
            tree_heights[i] = height
            if (min_height is None or height < min_height):
                min_height = height

            #print(i)
            #print(tree_heights[i])
        
        min_height = None
        result = []
        
        for k in tree_heights:
            #print(k)
            #print(tree_heights[k])
            if (min_height is None or tree_heights[k] < min_height):
                min_height = tree_heights[k]
        
        for k in tree_heights:
            if (tree_heights[k] == min_height):
                result.append(k)
        
        end = time.clock()
        print("time = %f" % (end - start))

        return result

def main():
    test = Solution()

    #print(test.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))

    #print(test.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

    #print(test.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))

    #print(test.findMinHeightTrees(210, [[0,1],[1,2],[0,3],[3,4],[4,5],[3,6],[6,7],[7,8],[0,9],[7,10],[6,11],[3,12],[5,13],[8,14],[7,15],[11,16],[12,17],[12,18],[18,19],[7,20],[8,21],[18,22],[7,23],[15,24],[21,25],[14,26],[11,27],[5,28],[15,29],[21,30],[12,31],[22,32],[1,33],[14,34],[14,35],[33,36],[14,37],[18,38],[19,39],[6,40],[29,41],[27,42],[25,43],[0,44],[26,45],[3,46],[1,47],[34,48],[26,49],[9,50],[34,51],[18,52],[41,53],[6,54],[25,55],[55,56],[47,57],[34,58],[58,59],[48,60],[24,61],[43,62],[51,63],[30,64],[24,65],[27,66],[30,67],[41,68],[64,69],[46,70],[49,71],[58,72],[43,73],[24,74],[43,75],[3,76],[32,77],[74,78],[31,79],[59,80],[25,81],[12,82],[26,83],[21,84],[35,85],[37,86],[39,87],[36,88],[67,89],[58,90],[22,91],[91,92],[56,93],[92,94],[3,95],[94,96],[89,97],[81,98],[6,99],[75,100],[56,101],[41,102],[68,103],[46,104],[3,105],[104,106],[56,107],[104,108],[83,109],[9,110],[0,111],[2,112],[53,113],[21,114],[76,115],[34,116],[26,117],[117,118],[116,119],[82,120],[27,121],[101,122],[8,123],[99,124],[79,125],[116,126],[53,127],[46,128],[116,129],[6,130],[46,131],[113,132],[25,133],[79,134],[38,135],[68,136],[116,137],[66,138],[56,139],[102,140],[36,141],[0,142],[126,143],[9,144],[36,145],[34,146],[140,147],[70,148],[117,149],[1,150],[5,151],[38,152],[48,153],[20,154],[145,155],[126,156],[54,157],[21,158],[155,159],[128,160],[34,161],[61,162],[72,163],[64,164],[144,165],[165,166],[60,167],[139,168],[85,169],[133,170],[60,171],[163,172],[120,173],[69,174],[21,175],[84,176],[24,177],[3,178],[131,179],[129,180],[35,181],[159,182],[31,183],[100,184],[110,185],[9,186],[6,187],[149,188],[141,189],[112,190],[22,191],[125,192],[174,193],[19,194],[156,195],[124,196],[88,197],[195,198],[187,199],[164,200],[179,201],[95,202],[48,203],[25,204],[53,205],[13,206],[127,207],[71,208],[119,209]]))

    print(test.findMinHeightTrees(231, [[0,1],[0,2],[0,3],[1,4],[1,5],[1,6],[2,7],[6,8],[3,9],[0,10],[3,11],[5,12],[7,13],[5,14],[8,15],[11,16],[2,17],[10,18],[17,19],[5,20],[14,21],[14,22],[4,23],[0,24],[1,25],[10,26],[24,27],[1,28],[18,29],[18,30],[12,31],[26,32],[10,33],[30,34],[27,35],[7,36],[23,37],[17,38],[37,39],[4,40],[12,41],[1,42],[5,43],[22,44],[35,45],[2,46],[19,47],[28,48],[1,49],[37,50],[1,51],[17,52],[17,53],[44,54],[4,55],[1,56],[19,57],[25,58],[0,59],[58,60],[43,61],[0,62],[59,63],[50,64],[43,65],[7,66],[17,67],[56,68],[25,69],[55,70],[30,71],[30,72],[72,73],[0,74],[14,75],[17,76],[55,77],[66,78],[51,79],[48,80],[20,81],[59,82],[23,83],[12,84],[32,85],[16,86],[17,87],[5,88],[87,89],[33,90],[22,91],[15,92],[0,93],[47,94],[65,95],[88,96],[11,97],[32,98],[38,99],[69,100],[63,101],[15,102],[68,103],[20,104],[94,105],[77,106],[84,107],[81,108],[0,109],[21,110],[4,111],[41,112],[12,113],[97,114],[86,115],[9,116],[27,117],[105,118],[16,119],[16,120],[36,121],[90,122],[61,123],[83,124],[118,125],[45,126],[48,127],[111,128],[49,129],[15,130],[26,131],[2,132],[26,133],[92,134],[132,135],[108,136],[32,137],[0,138],[31,139],[69,140],[68,141],[131,142],[135,143],[108,144],[19,145],[119,146],[118,147],[139,148],[101,149],[67,150],[98,151],[13,152],[132,153],[14,154],[90,155],[85,156],[70,157],[147,158],[113,159],[151,160],[126,161],[62,162],[60,163],[71,164],[98,165],[12,166],[76,167],[151,168],[91,169],[3,170],[90,171],[59,172],[25,173],[104,174],[65,175],[157,176],[151,177],[91,178],[48,179],[116,180],[84,181],[37,182],[162,183],[24,184],[48,185],[44,186],[185,187],[147,188],[118,189],[38,190],[70,191],[155,192],[54,193],[148,194],[120,195],[109,196],[3,197],[12,198],[193,199],[131,200],[25,201],[187,202],[153,203],[170,204],[131,205],[31,206],[182,207],[127,208],[100,209],[146,210],[56,211],[54,212],[147,213],[163,214],[110,215],[190,216],[173,217],[145,218],[187,219],[124,220],[181,221],[85,222],[209,223],[20,224],[215,225],[117,226],[193,227],[226,228],[57,229],[1,230]]))


main()