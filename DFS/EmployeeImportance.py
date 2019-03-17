
class Solution:
    def getImportance(self, employees, id):
#         emap = {e.id: e for e in employees}
#         _sum = 0
        
#         def dfs(eid, _sum):
            
#             employee = emap[eid]
#             _sum += employee.importance
#             for _sub in employee.subordinates:
#                 dfs(_sub, _sum)
#             return _sum
                
#         return dfs(id, _sum)
            
    
        stack = []
        _sum = 0
        
        for employee in employees:
            if employee.id == id:
                stack.append((employee.importance, employee.subordinates))
                
        while stack:
            imp, sub = stack.pop()
            _sum += imp
            for ele in sub:
                for employee in employees:
                    if employee.id == ele:
                        stack.append((employee.importance, employee.subordinates))
        
        return _sum
        