from random import *

#일반유닛 ex메딕
class Unit:
    def __init__(self, name, hp, speed):      
        self.name = name                        
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))


    def move(self, location):
        #print("[지상 유닛 이동]")
        print(f"{self.name}: {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name}: {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name}: 파괴되었습니다.")

#공격유닛
class AttackUnit(Unit):     #Unit을 상속받고 싶을때 class선언시 ()안에 상속받을 class를 선언
    def __init__(self, name, hp, speed, damage):      
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):     #메소드 앞에는 항상 self를 적어주어야 함
        print(f"{self.name}: {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩을 사용합니다. (HP: 10 감소)".format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False: 
            return
        if self.seize_mode == False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0}: 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


#공중유닛에 대한 클래스 추가
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name}: {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

#공중유닛 공격 클래스 추가
class Flyable_Attack_Unit(AttackUnit, Flyable):     #다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  #지상 speed=0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        #print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(Flyable_Attack_Unit):
    def __init__(self):
        Flyable_Attack_Unit.__init__(self, "레이스",80,20,5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked == True:
            print("{0}: 클로킹 모드를 해제합니다.".format(self.name))
            self.cloaked = False
        else:
            print("{0}: 클로킹 모드를 설정합니다.".format(self.name))
            self.cloaked = True

#건물
class Building_Unit(Unit):
    def __init__(self, name, hp, location):
        Unit.__init__(self, name, hp, 0) #아래와 동일/건물은 이동 불가하니 스피드=0 
        self.location = location

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("Player: gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")

#실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림]: 탱크 시즈모드 개발이 완료되었습니다.")

#공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):     #이 객체가 특정 클래스의 instance인지 확인하는 과정
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))
    
game_over()