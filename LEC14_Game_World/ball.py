from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    speed = 10

    def __init__(self, x, y, dir):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.dir = dir

    def update(self):
        self.x += self.dir * Ball.speed
        if self.x < -20 or self.x > get_canvas_width() + 20:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
