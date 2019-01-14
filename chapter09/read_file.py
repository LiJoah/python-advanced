# 500G, 特殊 一行
def myreadlines(file, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = file.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    # 这里是遍历一个生成器函数
    for line in myreadlines(f, "\n"):
        print(line)
