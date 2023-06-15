import inspect

def foo():
    bar()

def bar():
    frame = inspect.currentframe().f_back
    print(frame.f_code.co_name)  # 输出 "foo"

foo()
