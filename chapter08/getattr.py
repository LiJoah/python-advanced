#__getattr__, __getattribute__
# __getattr__ 就是在查找不到属性的时候调用
from datetime import date


class User:
    def __init__(self, info={}):
        self.info = info

    # __getattr__ 就是在查找不到属性的时候调用
    def __getattr__(self, item):
        print("enter")
        return self.info[item]

    # 获取属性的时候调用
    def __getattribute__(self, item):
        return "bobby"


if __name__ == "__main__":
    user = User(info={"company_name": "imooc", "name": "bobby"})
    print(user.test) # bobby
