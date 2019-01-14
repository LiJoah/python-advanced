# -*- coding: utf-8 -*-

__author__ = 'bobby'


class Student(object):
    # def __init__(self):
    #     pass

    def say(self):
        print("i am student")


stu = Student()


def say_teacher():
    print("i am teacher")


stu.say = say_teacher

stu.say()
