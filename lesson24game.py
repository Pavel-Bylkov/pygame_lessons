import arcade
from arcade.experimental.lights import Light, LightLayer

WIDTH = 1200
HEIGHT = 750
TITLE = "light demo"

HERO_IMG = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
BRICK_IMG = ":resources:images/tiles/brickTextureWhite.png"

MOVEMENT_SPEED = 5
VIEW_MARGIN = 200
default_color = (10, 10, 10)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE, resizable=True)

        self.player_sprite = None
        self.player_sprite_list = None
        self.light_layer = None
        self.background_list = None
        self.wall_list = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        self.player_sprite_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(HERO_IMG, scale=0.4,
                                           center_x=200, center_y=300)
        self.player_sprite_list.append(self.player_sprite)

        self.light_layer = LightLayer(WIDTH, HEIGHT)

        # создание маленького белого луча
        light = Light(center_x=100, center_y=200, radius=100,
                      color=arcade.color.WHITE, mode="soft")
        self.light_layer.add(light)  # - добавления луча на световой слой

        # создание большого белого луча
        self.light_layer.add(Light(center_x=300, center_y=150, radius=200,
                                   color=arcade.color.WHITE, mode="soft"))

        # создание пересекающегося красного луча
        self.light_layer.add(Light(center_x=630, center_y=450, radius=120,
                                   color=arcade.color.RED, mode="soft"))

        # создание пересекающегося синего луча
        self.light_layer.add(Light(center_x=750, center_y=450, radius=120,
                                   color=arcade.color.BLUE, mode="soft"))

        # создание пересекающегося зеленого луча
        self.light_layer.add(Light(center_x=870, center_y=450, radius=120,
                                   color=arcade.color.GREEN, mode="soft"))

        # создание пересекающегося зеленого hard луча
        self.light_layer.add(Light(center_x=870, center_y=150, radius=120,
                                   color=arcade.color.GREEN, mode="hard"))

        # создание пересекающегося синий hard луча
        self.light_layer.add(Light(center_x=750, center_y=150, radius=120,
                                   color=arcade.color.BLUE, mode="hard"))

        # создание пересекающегося красный hard луча
        self.light_layer.add(Light(center_x=630, center_y=150, radius=120,
                                   color=arcade.color.RED, mode="hard"))

        # создание пересекающегося зеленого hard луча
        self.player_light = Light(center_x=0, center_y=0, radius=120,
                                  color=arcade.color.WHITE, mode="soft")
        self.light_layer.add(self.player_light)

        #создание бекграунда из кирпичей
        for x in range(-128, 1328, 128):
            for y in range(-128, 1000, 128):
                brick = arcade.Sprite(BRICK_IMG, center_x=x, center_y=y)
                self.background_list.append(brick)

    def on_draw(self):
        self.clear()

        with self.light_layer: #отрисовка бекграунда вместо со световым слоем(всё что должно быть освещено световым слоем должно быть внутри оператора with)
            self.background_list.draw()
            self.player_sprite_list.draw()

        self.light_layer.draw(ambient_color=default_color)

        arcade.draw_text("press space to turn on light",
                         start_x=10+self.view_left,
                         start_y=20+self.view_bottom,
                         color=arcade.color.WHITE, font_size=20)

    def on_update(self, delta_time: float):
        self.player_sprite.update()
        self.player_light.position = self.player_sprite.position
        self.view_point()

    def view_point(self):
        #создание границ для персонажа и камеры
        self.left_boundary = self.view_left + VIEW_MARGIN
        if self.player_sprite.left < self.left_boundary:
            self.view_left -= self.left_boundary - self.player_sprite.left

        self.right_boundary = self.view_left + self.width - VIEW_MARGIN
        if self.player_sprite.right > self.right_boundary:
            self.view_left += self.player_sprite.right - self.right_boundary

        self.bottom_boundary = self.view_bottom + VIEW_MARGIN
        if self.player_sprite.bottom < self.bottom_boundary:
            self.view_bottom -= self.bottom_boundary - self.player_sprite.bottom

        self.top_boundary = self.view_bottom + self.height - VIEW_MARGIN
        if self.player_sprite.top > self.top_boundary:
            self.view_bottom += self.player_sprite.top - self.top_boundary

        arcade.set_viewport(self.view_left,
                            self.view_left + self.width,
                            self.view_bottom,
                            self.view_bottom + self.height)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

        elif key == arcade.key.SPACE:
            if self.player_light in self.light_layer:
                self.light_layer.remove(self.player_light)
            else:
                self.light_layer.add(self.player_light)

    def on_key_release(self, key: int, modifiers: int):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


window = MyGame()
window.setup()
arcade.run()


"""
from arcade.experimental.lights import Light,LightLayer
-импорт класса для создания лучей и светового слоя

self.light_layer = LightLayer(WIDTH,HEIGHT)
-создание светового слоя

self.light = Light(x,y,radius,color,mode)
-создание луча света

with self.light_layer:
    -отрисовка бекграунда вместо со световым слоем
    (всё что должно быть освещено световым слоем должно быть внутри оператора with)
    self.background_list.draw()
    self.player_sprite_list.draw()

self.light_layer.draw(ambient_color=default_color)
-отрисовка светового слоя с общим светом на весь слой

arcade.set_viewport(
    self.view_left,self.view_left + self.width,
    self.view_bottom,
    self.view_bottom + self.height)
-установка координат которые будут охватывать текущее окно
"""