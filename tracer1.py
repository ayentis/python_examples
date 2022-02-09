# class tracer:
#     def __init__(self, func):
#         self.calls = 0
#         self. func = func
#
#     def __call__(self, *args):
#         self.calls += 1
#         print('call %s to %s' % (self.calls, self.func.__name__))
#         return self.func(*args)
#
#
# @tracer
# def spam(a, b, с):
#     return a + b + с
#
#
# print(spam(1, 2, 3))
# print(spam('а', 'b', 'с'))



def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self,a, b, c) : return a + b + c

x = C()
print(x.spam(1, 2, 3))
print(x.spam('а', 'b', 'с'))