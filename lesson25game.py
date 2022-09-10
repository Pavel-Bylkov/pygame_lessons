import arcade
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Particle"
IMG = ":resources:images/pinball/bumper.png"

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.BLACK)
        self.example_dict = {
            # варианты изменения change_xy
            "controller=EmitBurst, factory=EternalParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(50),
                               particle_factory=lambda emitter: arcade.EternalParticle(
                                   filename_or_texture=IMG,
                                   change_xy=arcade.rand_on_circle((0, 0), 0.2),
                                   scale=0.2,
                                   alpha=127)),
            "controller=EmitBurst, factory=EternalParticle, change_xy=rand_in_rect": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(5000),
                           particle_factory=lambda emitter: arcade.EternalParticle(
                               filename_or_texture=IMG,
                               change_xy=arcade.rand_in_rect((-2, -2), 4, 4),
                               scale=0.2,
                               alpha=127)),
            "controller=EmitBurst, factory=EternalParticle, change_xy=rand_on_line": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(500),
                           particle_factory=lambda emitter: arcade.EternalParticle(
                               filename_or_texture=IMG,
                               change_xy=arcade.rand_on_line((0, 0), (1, 1)),
                               scale=0.2,
                               alpha=127)),
            "controller=EmitBurst, factory=EternalParticle, change_xy=rand_vec_spread_deg": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(500),
                           particle_factory=lambda emitter: arcade.EternalParticle(
                               filename_or_texture=IMG,
                               change_xy=arcade.rand_vec_spread_deg(45, 90, 5.0),
                               scale=0.2,
                               alpha=127)),
            "controller=EmitBurst, factory=EternalParticle, change_xy=rand_vec_magnitude": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(500),
                           particle_factory=lambda emitter: arcade.EternalParticle(
                               filename_or_texture=IMG,
                               change_xy=arcade.rand_vec_magnitude(90, 0, 2),
                               scale=0.2,
                               alpha=127)),
            # варианты изменения particle_factory
            "controller=EmitBurst, factory=LifetimeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(500),
                               particle_factory=lambda emitter: arcade.LifetimeParticle(
                                   filename_or_texture=IMG,
                                   change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                   lifetime=5.0,
                                   scale=0.2,
                                   alpha=127)),
            "controller=EmitBurst, factory=FadeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitBurst(50),
                               particle_factory=lambda emitter: arcade.FadeParticle(
                                   filename_or_texture=IMG,
                                   change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                   lifetime=5.0,
                                   scale=0.6,
                                   angle=300,
                                   change_angle=3)),
            # варианты изменения emit_controller
            "controller=EmitInterval, factory=LifetimeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300), emit_controller=arcade.EmitInterval(0.02),
                               particle_factory=lambda emitter: arcade.LifetimeParticle(
                                   filename_or_texture=IMG,
                                   change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                   lifetime=5.0,
                                   scale=0.2,
                                   alpha=127)),
            "controller=EmitterIntervalWithTime, factory=LifetimeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300),
                               emit_controller=arcade.EmitterIntervalWithTime(0.02, 1.5),
                               particle_factory=lambda emitter: arcade.LifetimeParticle(
                                   filename_or_texture=IMG,
                                   change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                   lifetime=5.0,
                                   scale=0.2,
                                   alpha=127)),
            "controller=EmitterIntervalWithCount, factory=LifetimeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300),
                           emit_controller=arcade.EmitterIntervalWithCount(0.02, 100),
                           particle_factory=lambda emitter: arcade.LifetimeParticle(
                               filename_or_texture=IMG,
                               change_xy=arcade.rand_on_circle((0, 0), 0.9),
                               lifetime=5.0,
                               scale=0.2,
                               alpha=127)),
            "controller=EmitMaintainCount, factory=LifetimeParticle, change_xy=rand_on_circle": \
                arcade.Emitter((400, 300),
                               emit_controller=arcade.EmitMaintainCount(500),
                               particle_factory=lambda emitter: arcade.LifetimeParticle(
                                   filename_or_texture=IMG,
                                   change_xy=(-2, 2),
                                   lifetime=5.0,
                                   scale=0.2,
                                   alpha=127))
            }
        self.example_keys = list(self.example_dict.keys())
        self.current_example = self.example_keys[0]
        self.count = 0
        self.timer = time.time()

    def on_update(self, delta_time: float):
        if self.count + 1 < len(self.example_keys) and time.time() - self.timer > 6:
            self.count += 1
            self.current_example = self.example_keys[self.count]
            self.timer = time.time()
        self.example_dict[self.current_example].update()

    def on_draw(self):
        arcade.start_render()
        self.example_dict[self.current_example].draw()
        arcade.draw_text(self.current_example,
                         start_x=10,
                         start_y=20,
                         color=arcade.color.WHITE, font_size=15)


game = MyGame()
time.sleep(3)
arcade.run()

"""
arcade.Emitter(#точка создания системы частиц,
    #emit_controller -вид выпуска частиц(в зависимости от интервала и количества),
    #particle_factor  -длительность жизни и вид угасания(
        filename_or_texture -файл в которым лежит картинка которая будет частицей,
        change_xy -вектор изменение скорости и пути частиц,
        scale -коэф. масштабирования,
        alpha -прозрачность), )
-фундаментальный класс для построения частиц

#emit_controller()
1)arcade.EmitBurst(#количество частиц)
-мнгновенно выпускает указанное количество частиц

2)arcade.EmitInterval(#задержка между выпуском чатицы)
-бесконечный выпуск частиц с указанной задержкой

3)arcade.EmitterIntervalWithTime(#задержка между выпуском чатицы,
        #длительность выпуска частиц)
    -бесконечный выпуск частиц с указанной задержкой и длительностью

4)arcade.EmitterIntervalWithCount(#задержка между выпуском чатицы,
        #количество выпускаемых частиц)
    -выпуск частиц с указанной задержкой и указ. количеством

5)arcade.EmitMaintainCount(#количество частиц )
-фиксированный выпуск указ кол-ва частиц

#particle_factor
1)arcade.EternalParticle(
    filename_or_texture -файл в которым лежит картинка которая будет частицей,
    change_xy -вектор изменение скорости и пути частиц,
    scale -коэф. масштабирования,
    alpha -прозрачность) -бесконечная жизнь частиц

2)arcade.LifeTimeParticle(
    filename_or_texture -файл в которым лежит картинка которая будет частицей,
    change_xy -вектор изменение скорости и пути частиц,
    scale -коэф. масштабирования,
    alpha -прозрачность,
    lifetime -длительность жизни )
    -частицы живут с указ. длительностью, затем мгновенно исчезают

3)arcade.FadeParticle(
    filename_or_texture -файл в которым лежит картинка которая будет частицей,
    change_xy -вектор изменение скорости и пути частиц,
    scale -коэф. масштабирования,
    start_alpha -прозрачность с которой частица появляется,
    end_alpha -прозрачность с которой частица исчезает,
    lifetime -длительность жизни )
    -частицы живут с указ. длительностью, затем постепенно исчезают

#change_xy
1)arcade.rand_on_circle(#центр,#скорость распространения)
-появляются из точки, растут по кругу

2)arcade.rand_in_rect(
    #кортеж с координатами левого верхнего угла относительно начала координат,
    #ширина,
    #выоста)
    -появляются из прямоуголника, растут по увеличиванию прямоугольнику

3)arcade.rand_on_line(
    #вектор роста в один конец относительно начала,
    #вектор роста во второй конец относительно начала)
    -появляются из линии, растут по направлению линии

4)arcade.rand_vec_spread_deg(
    #направление в градусах,
    #ширина распределиня в градусах, скорость развития)
    -появляются параболой, развивается параболой

5)arcade.rand_vec_magnitude(
    #направление в градусах,
    #самая низкая величина,
    #самая высокая величина)
    -рандомное расположение и скорость частиц и от самого до самого значения

5)(кортеж из точки) -ветор перемещения всех частиц в одной точке
"""