# 부모 클래스 정의
class Animal:
    def __init__(self, name):
        """생성자 메서드: 인스턴스 초기화"""
        self.name = name    # 인스턴스 변수: 이름

    def speak(self):
        """기본적인 동물의 소리를 반환하는 메서드"""
        return "Animal sound"

class Elephant(Animal):
    def speak(self):
        """코끼리가 내는 소리를 반환하는 메서드 (재정의)"""
        return f"{self.name} says Trumpet!"

# 자식 클래스 정의 (Animal 클래스를 상속)
class Dog(Animal):
    def speak(self):
        """개가 짖는 소리를 반환하는 메서드 (재정의)"""
        return f"{self.name} says Woof!"


# 또 다른 자식 클래스 정의 (Animal 클래스를 상속)
class Cat(Animal):
    def speak(self):
        """고양이가 내는 소리를 반환하는 메서드 (재정의)"""
        return f"{self.name} says Meow!"


# 인스턴스 생성
my_dog = Dog(name="Buddy")
my_cat = Cat(name="Whiskers")
my_elephant = Elephant(name="Ellie")


# 메서드 호출
print(my_dog.speak())    # 출력: Buddy says Woof!
print(my_cat.speak())    # 출력: Whiskers says Meow!
print(my_elephant.speak()) # 출력: Ellie says Trumpet!