class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self) -> None:
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()  # 상속받는 맨 처음 class를 지칭됨
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍십
dropship = FlyableUnit()
