class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Feet:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, torso):
        self.torso = torso


#Hands
right_hand = Hand()
left_hand = Hand()
#Feet
right_feet = Feet()
left_feet = Feet()
#Arms
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
#Legs
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)
#Head
head = Head()
#Torso
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
#Human
human = Human(torso)

print(human.torso.head)
print(human.torso.right_arm.hand)
print(human.torso.left_arm)
print(human.torso.right_leg.feet)