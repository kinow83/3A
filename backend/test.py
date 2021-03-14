

def foo(s, **v):
    str = s % v
    print(str)


foo("aaaa %(k)", k="aaaaaaaaaa")