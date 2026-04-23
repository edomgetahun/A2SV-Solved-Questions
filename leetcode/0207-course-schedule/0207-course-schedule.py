class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a,b in pre:
            graph[b].append(a)
        color = ["white"] * numCourses
        
        def dfs(course):
                if color[course] == "gray":
                    return False
                if color[course] == "black":
                    return True
                
                color[course] = "gray"
                for negh in graph[course]:
                    if not dfs(negh):
                        return False
                color[course] = "black"
                return True
            
        for i in range(numCourses):
            if color[i] == "white":
                if not dfs(i):
                    return False
        return True


                    
                
            
            
            # cycle = False
            # color = ["white"] * # all the nodes or courses here
            # def dfs(#node):
            #     # if node is not visted means the color is white so 
            #         # color it gray
            #     # else if was visited before 
            #         # check  the color is gray we get cycle here
            #         # so return Fale we can't take the course
            #     # but if there is detected no cyle yet we can make the the node black and return back 
            #     # and if finally this possible we can return True
            # for i in range(pre):
        #     if not visted:
        #         dfs(pre)

                 
