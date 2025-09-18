import heapq
class TaskManager(object):
    def __init__(self, tasks):
        self.heap = []
        self.tp = {}
        self.to = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId))
        self.tp[taskId] = priority
        self.to[taskId] = userId

    def edit(self, taskId, newp):
        heapq.heappush(self.heap, (-newp, -taskId))
        self.tp[taskId] = newp

    def rmv(self, taskId):
        self.tp[taskId] = -1

    def execTop(self):
        while self.heap:
            np, nid = heapq.heappop(self.heap)
            p = -np
            tid = -nid
            if self.tp.get(tid, -2) == p:
                self.tp[tid] = -1
                return self.to.get(tid, -1)
        return -1