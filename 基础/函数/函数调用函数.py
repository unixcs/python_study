def bar():
    print ('in the bar')
def foo(a):
    res=a()
#    return res
foo(bar)
