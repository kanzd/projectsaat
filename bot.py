class per:
    n=0
    def __init__(self):
        self.a=""
        per.yo()
    def get(self):
        self.a=input("..>")
        return self.a
    def show(self):
        print(self.a)
    def chk(self,st):
        if self.a.find(st)==0:
            return True
        else:
            return False
    @classmethod
    def yo(cls):
        cls.n=cls.n+1