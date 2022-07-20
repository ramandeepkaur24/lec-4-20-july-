class A:
    def f1(self,a,b):
        print(a+b)
        return a+b
obj=A()
result=obj.f1(10,20)
print(result)
