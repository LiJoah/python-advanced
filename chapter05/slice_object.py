import numbers


class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        print("__reversed__")
        self.staffs.reverse()

    def __getitem__(self, item):
        print("__getitem__")
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        print("__len__")
        return len(self.staffs)

    def __iter__(self):
        print("__iter__")
        return iter(self.staffs)

    def __contains__(self, item):
        print("__contains__")
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["bobby1", "imooc", "bobby2", "bobby3"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)

# __reversed__
# reversed(group)
# __iter__
for user in group:
    print(user)
