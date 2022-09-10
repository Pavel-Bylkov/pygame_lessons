import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(600, 800, "button example", resizable=True)

        self.manage = arcade.gui.UIManager()
        self.manage.enable()

        arcade.set_background_color(arcade.color.FAWN)
        self.box = arcade.gui.UIBoxLayout()

        self.slider = UISlider(value=50)
        self.slider_text = arcade.gui.UILabel(text=f"{self.slider.value:02.0f}")

        @self.slider.event()
        def on_change(event: arcade.gui.UIOnChangeEvent):
            self.slider_text.text = f"{self.slider.value:02.0f}"
            self.slider_text.fit_content()

        self.box.add(self.slider)
        self.box.add(self.slider_text)

        mystyle = {"font_name": ("calibri",),
                   "font_size": 15,
                   "font_color": arcade.color.ROSE,
                   "border_width": 6,
                   "border_color": arcade.color.AFRICAN_VIOLET,
                   "bg_color": arcade.color.GREEN,
                   "bg_color_pressed": arcade.color.WHITE,
                   "border_color_pressed": arcade.color.WHITE,
                  "font_color_pressed": arcade.color.BLACK
        }



        text = arcade.gui.UITextArea(text= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget pellentesque velit. "
    "Nam eu rhoncus nulla. Fusce ornare libero eget ex vulputate, vitae mattis orci eleifend. "
    "Donec quis volutpat arcu. Proin lacinia velit id imperdiet ultrices. Fusce porta magna leo, "
    "non maximus justo facilisis vel. Duis pretium sem ut eros scelerisque, a dignissim ante "
    "pellentesque. Cras rutrum aliquam fermentum. Donec id mollis mi.\n"
    "\n"
    "Nullam vitae nunc aliquet, lobortis purus eget, porttitor purus. Curabitur feugiat purus sit "
    "amet finibus accumsan. Proin varius, enim in pretium pulvinar, augue erat pellentesque ipsum, "
    "sit amet varius leo risus quis tellus. Donec posuere ligula risus, et scelerisque nibh cursus "
    "ac. Mauris feugiat tortor turpis, vitae imperdiet mi euismod aliquam. Fusce vel ligula volutpat, "
    "finibus sapien in, lacinia lorem. Proin tincidunt gravida nisl in pellentesque. Aenean sed "
    "arcu ipsum. Vivamus quam arcu, elementum nec auctor non, convallis non elit. Maecenas id "
    "scelerisque lectus. Vivamus eget sem tristique, dictum lorem eget, maximus leo. Mauris lorem "
    "tellus, molestie eu orci ut, porta aliquam est. Nullam lobortis tempor magna, egestas lacinia lectus.\n",
                                        width=400,
                                        height=200,
                                        font_name="Kenney Future",
                                        font_size=10,
                                        text_color=arcade.color.AFRICAN_VIOLET)
        self.box.add(text.with_space_around(bottom=20))
        self.start_button = arcade.gui.UIFlatButton(text="Start Button",width=200,style=mystyle)
        self.box.add(self.start_button.with_space_around(bottom=20))

        self.setting_button = arcade.gui.UIFlatButton(text="Setting Button", width=200)
        self.box.add(self.setting_button.with_space_around(bottom=20))

        self.quit_button = QuitButton(text="Quit Button", width=200)
        self.box.add(self.quit_button.with_space_around(bottom=20))

        self.start_button.on_click = self.on_click_start


        @self.setting_button.event("on_click")
        def setting_on_draw(event):
            print("setting - " , event)

        self.manage.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.box
        ))

    def on_click_start(self,event):
        print("start - " , event)

    def on_draw(self):
        self.clear()
        self.manage.draw()



window =GameWindow()
arcade.run()



"""
self.manage = arcade.gui.UIManager() -класс для управления виджетами
self.manage.enable() -запуск функций on_...
self.box = arcade.gui.UIBoxLayout()
-размещает добавленные виджеты в зависимости от атрибута
vertical(друг под другом и сбоку)

arcade.gui.UIFlatButton(text="Start Button",width=200)
-создание кнопки(виджета) с заданными параметрами

self.box.add(self.start_button.with_space_around(bottom=20))
добавление виджета в box

#1 метод реакции кнопки на клик
start -использование результата работы независимой функции

#2 метод реакции кнопки на клик
setting -использование декоратора к прописанной внутри функции

#3 метод реакции кнопки на клик
quit-использование отедльного класса, в котором прописан метод def on_click

#стиль#
изменение параметров кнопки записанных в виде словаря
mystyle = {"font_name":("calibri"),
    "font_size":15,
    "font_color": arcade.color.ROSE,
    "border_width": 6,
    "border_color": arcade.color.AFRICAN_VIOLET,
    "bg_color": arcade.color.GREEN,
    "bg_color_pressed": arcade.color.WHITE,
    "border_color_pressed": arcade.color.WHITE,
    "font_color_pressed": arcade.color.BLACK}

self.start_button = arcade.gui.UIFlatButton(text="Start Button",width=200,style=mystyle)
-(#style=mystyle)
self.slider = UISlider(value=50) -создание слайдера
self.slider_text = arcade.gui.UILabel(text=f"{self.slider.value:02.0f}")
-создание заголовка слайдера с количеством выводимых единиц

@self.slider.event() -создание декоратора, который будет вызываться при
изменении переменной event виджета слайдера
def on_change(event:arcade.gui.UIOnChangeEvent):
    self.slider_text.text = f"{self.slider.value:02.0f}"
    -установка нового значение виджета загаловка
    self.slider_text.fit_content()
    -увелечение контейнера для отображения всех цифр заголовка
"""