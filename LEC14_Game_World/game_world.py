world = [[], []]  # 0번(배경 등), 1번(캐릭터 등) 레이어를 가지는 2차원 리스트

def add_object(o, depth=0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def clear():
    for layer in world:
        layer.clear()

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()  # Boy, Grass 등의 클래스에 draw() 메서드가 존재해야 함