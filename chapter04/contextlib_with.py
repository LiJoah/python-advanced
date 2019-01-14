import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print ("file open")
    yield {}
    print ("file end")

# 这里是 with 语法， 可以在 with 执行前后执行
with file_open("bobby.txt") as f_opened:
    print ("file processing")
