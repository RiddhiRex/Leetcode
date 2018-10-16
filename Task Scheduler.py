import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt=0
        lt = len(tasks)
        taskdic = collections.Counter(tasks)
        max_task_cnt=max(taskdic.values())
        for v in taskdic.values():
            if v==max_task_cnt:
                cnt+=1
        return max(lt, ((max_task_cnt-1)*(n+1))+cnt)
