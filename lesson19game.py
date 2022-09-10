import arcade, random

WIDTH = 800
HEIGHT = 600
Screen_title = "Man collecting coin"
hero_scale = 0.2
coin_count = 50


class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_x = random.randint(20, 780)
        self.center_y = random.randint(20, 580)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.player_sprite = arcade.Sprite("les2img/boy.png", hero_scale)
        self.coin_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.AMAZON)

        self.score = 0
        self.x = 100
        self.y = 100
        self.speedx = 300
        self.speedy = 300
        self.playerx = 400
        self.playery = 350

        for i in range(coin_count):
            coin = Coin("les2img/coin.png", 0.1)
            coin.center_x = random.randint(30, 770)
            coin.center_y = random.randint(30, 570)
            self.coin_list.append(coin)

        self.right = False
        self.left = False
        self.down = False
        self.up = False

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_sprite.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        if self.right:
            self.playerx += self.speedx * delta_time
        if self.left:
            self.playerx -= self.speedx * delta_time
        if self.up:
            self.playery += self.speedy * delta_time
        if self.down:
            self.playery -= self.speedy * delta_time
        self.player_sprite.set_position(self.playerx, self.playery)

        self.coin_list.update()

        collisions = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for i in collisions:
            i.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True
        if symbol == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
        if symbol == arcade.key.DOWN:
            self.down = False


def main():
    game = MyGame(WIDTH, HEIGHT)
    game.run()


main()



"""
arcade.check_for_collision(#спрайт1, #спрайт2)
-возвращает True или False в зависимости от того, было столкновение 
или нет

arcade.check_for_collision_with_list(#основной спрайт,#список (arcade.SpriteList())
-возвращает список объектов с которыми произошла коллизия(столкновение)

arcade.check_for_collision_with_lists(#основной спрайт,
#список из списков, которые содержат спрайты)
-возвращает список объектов с которыми пересекся основной спрайт

sprite,distance = arcade.get_closest_sprite(#основной спрайт,
#список из спрайтов(arcade.SpriteList())
-возвращает два параметра ближайший спрайт и расстояние до него

if len(self.coin_list) == 0: -условие, когда все спрайты исчезли
    return None

arcade.get_sprites_at_exact_point(#точка, с которой будет искаться коллизия, 
#список спрайтов) 
-возвращает список объектов которые свои центром перескли указанную точку

arcade.get_sprites_at_point(#точка, с которой будет искаться коллизия, 
#список спрайтов) 
-возвращает список объектов которые перескли указанную точку

arcade.draw_text(#надпись с переменными или без,
#Координата икс,игрек, цвет,размер шрифта) 
-выводит надпись на экран
"""