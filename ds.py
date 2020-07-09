class one:
    n=0
    def __init__(self):
        self.a=0
        one.yo()
    def m1(self):
        print(self.a)
    @classmethod
    def yo(cls):
        cls.n=cls.n+1
        print(cls.n)
o1=one()
o1.m1()
o2=one()
o2.m1()
