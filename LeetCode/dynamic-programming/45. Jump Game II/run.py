class Position:
    def __init__(self, pos, num):
        self.pos = pos

        self.child = []
        self.n = 0
        self.num = num
        self.length = len(self.num)

    def pos_jump(self, step, min_step):

        self.step = step
        self.min_step = min_step
        self.n += 1
        next_pos = self.pos + self.n
        # print (self.pos,self.n,self.num[self.pos],self.step)

        if min(self.min_step) > self.step + 1 and (self.n <= self.num[self.pos]):
            if max(next_pos, self.num[self.pos] + self.pos) >= self.length - 1:
                self.min_step.append(self.step + 1)
            else:
                if (next_pos <= self.length - 1):
                    if next_pos + self.num[next_pos] > self.pos + self.num[self.pos]:

                        self.child.append(Position(pos=self.pos + self.n, num=self.num))
                    self.pos_jump(self.step, self.min_step)
        elif min(self.min_step) > self.step + 1:
            des = 0
            jump = 0
            for node in self.child:
                if node.pos + self.num[node.pos] > jump:
                    jump = node.pos + self.num[node.pos]
                    des = node.pos
            self.next = Position(pos=des, num=self.num)
            self.next.pos_jump(self.step + 1, self.min_step)


class Solution:

    def jump(self, nums: List[int]) -> int:
        p = Position(0, nums)
        p.pos_jump(0, [len(nums) - 1])
        return min(p.min_step)
