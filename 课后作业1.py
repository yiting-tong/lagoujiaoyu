'''
创建一个类Animal【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】
重写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=短毛
添加一个新的方法，会捉老鼠
重写父类的【会叫】的方法，改成【喵喵叫】
'''


class Animal:
    def __init__(self, name, colour, age, gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender
        print(f"我的名字是{self.name},我的颜色是{self.colour},我的年龄是{self.age}岁,我的性别是{self.gender}")

    def shout(self):
        print(f"{self.name} can shout!")

    def run(self):
        print(f"{self.name} can run!")


class Cat(Animal):
    def __init__(self, hair, name, colour, age, gender):
        self.hair = hair
        super().__init__(name, colour, age, gender)
        print(f"我的毛发是{self.hair}")

    def catch_mouse(self):
        print(f"{self.name} can catch a mouse!")

    def shout(self):
        print(f"{self.name} can shout like 'meow,meow'!")


if __name__ == "__main__":
    cat = Cat(name="球猫", colour="orange", age=2, gender="公", hair="短毛")
    cat.run()
    cat.shout()
    cat.catch_mouse()
