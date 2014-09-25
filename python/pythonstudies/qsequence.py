class qsequence(object):
    def __init__(self, s):
        self.s = s[:]

    def next(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    def current_state(self):
        return self.s
