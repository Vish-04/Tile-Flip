from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')

from kivy.metrics import dp
from kivy.core.window import Window
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.bubble import Bubble, BubbleButton
import random
import time


class WindowManager(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class DiffScreen(Screen):
    pass

class InstructionsScreen(Screen):
    pass

class CreditsScreen(Screen):
    pass

class HomeWidget(BoxLayout):
    # play = ObjectProperty(None)
    # difficulty = ObjectProperty()
    # instructions = ObjectProperty()
    # credit = ObjectProperty()
    window_size = Window.size


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def button_release_play(self):
        pass

    def button_release_difficulty(self):
        pass

    def button_release_instructions(self):
        pass

    def button_release_credits(self):
        pass

class DiffWidget(BoxLayout):

    
    def update_difficulty(self):
        game_widget.defeat(self.difficulty)
        if self.difficulty == 1000:
            self.ids.diff.text = "Selected Difficulty: BABY"
            self.ids.diff_description.text = "BABY: 1000 clicks to beat the game. This is for new players."

        if self.difficulty == 30:
            self.ids.diff.text = "Selected Difficulty: EASY"
            self.ids.diff_description.text = "EASY: 30 clicks to beat the game. This is for beginners looking for a challenge"

        if self.difficulty == 20:
            self.ids.diff.text = "Selected Difficulty: MEDIUM"
            self.ids.diff_description.text = "MEDIUM: 20 clicks to beat the game. This is for players who have a hang for the game"

        if self.difficulty == 10:
            self.ids.diff.text = "Selected Difficulty: HARD"
            self.ids.diff_description.text = "HARD: 10 clicks to beat the game. This is only for well seasoned players"

        if self.difficulty == 7:
            self.ids.diff.text = "Selected Difficulty: INSANE"
            self.ids.diff_description.text = "INSANE: 7 clicks to beat the game. This is next to impossible!"

    def baby_mode(self):
        self.difficulty = 1000
        self.update_difficulty()

    def easy_mode(self):
        self.difficulty = 30
        self.update_difficulty()

    def medium_mode(self):
        self.difficulty = 20
        self.update_difficulty()

    def hard_mode(self):
        self.difficulty = 10
        self.update_difficulty()

    def insane_mode(self):
        self.difficulty = 7
        self.update_difficulty()

class InstructionsWidget(BoxLayout):
    pass

class CreditsWidget(BoxLayout):
    pass

class GameWidget(BoxLayout):
    v = 0
    victory_screen_border_x = .8
    victory_screen_border_y = .3
    victory_screen_x = 0.775
    victory_screen_y = 0.290625
    victory_image_x = 0.75
    victory_image_y = 0.28125
    # wm = WindowManager()
    #victory_label_text = ""

    window_size = Window.size #put in update
    gcolor = (0.02, 0.6, 0.2)
    bcolor = (13/255, 111/255, 209/255)
    number_clicks = 0
    game_difficulty = 1000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_screen()
        self.random_tile()

        Clock.schedule_interval(self.update, 1/60)
    
    def update_canvas(self):
        with self.grid.canvas:
            Color(0,0,0)
            grid_bg_size_x, grid_bg_size_y = self.window_size[0]*.63  ,self.window_size[1]*.315
            self.grid_bg.size = (grid_bg_size_x, grid_bg_size_y)
            self.grid_bg.pos =  (self.window_size[0]*0.1844, self.window_size[1]*0.392)
        
        if self.v == 1:
            with self.bottom_layout.canvas:
                dropdown_border_size = (self.victory_screen_border_x*self.window_size[0], self.victory_screen_border_y*self.window_size[1])
                dropdown_border_pos =  (((self.window_size[0]-self.victory_screen_border_x*self.window_size[0])/2),(self.window_size[1]/3-(self.victory_screen_border_y*self.window_size[1])/2))

                dropdown_size = (self.victory_screen_x*self.window_size[0], self.victory_screen_y*self.window_size[1])
                dropdown_pos =  (((self.window_size[0]-self.victory_screen_x*self.window_size[0])/2),(self.window_size[1]/3-(self.victory_screen_y*self.window_size[1])/2))

                image_size = (self.victory_image_x*self.window_size[0], self.victory_image_y*self.window_size[1])
                image_pos =  (((self.window_size[0]-self.victory_image_x*self.window_size[0])/2),(self.window_size[1]/3-(self.victory_image_y*self.window_size[1])/2))


                Color(22/255, 36/255,0)
                self.victory_screen_dropdown_border = Rectangle(size = dropdown_border_size, pos = dropdown_border_pos)
                Color(204/255,158/255,101/255)
                self.victory_screen_dropdown = Rectangle( size = dropdown_size, pos = dropdown_pos)
                Color(1,1,1)
                victory_image = Rectangle(source="Images/VICTORY.jpg", size = image_size, pos = image_pos)

    def update_clicks(self):

        self.clicks_label.text ="Clicks: " +  str(self.number_clicks)
        if self.number_clicks > self.game_difficulty:
            print("Game Over")
        
    def restart(self, instance):
        self.clear_widgets()
        self.init_screen()
        self.random_tile()
        self.number_clicks = 0
        self.v = 0

    def change_screen(self, instance):
        greenscreengame.screen_manager.current = 'home'

    def defeat(self, d):
        self.game_difficulty = d

    def init_screen(self):

        self.orientation = 'vertical'

        #top screen boxlayout
        main_layout = BoxLayout(size_hint= (1, 0.2))
        self.add_widget(main_layout)
        home_button = Button(text='HOME', size_hint=(.5,1), background_normal="", background_color=self.bcolor, outline_color=(0,0,0), outline_width = 1)
        self.clicks_label = Label(text='Clicks: 0', font_name= "fonts/Lcd.ttf", font_size= dp(30), color= (0, 1, 146/255,1), outline_color=(0,0,0), outline_width=2 )
        restart_button = Button(text='RESTART', size_hint=(.5,1), background_normal="",  background_color=self.bcolor,  outline_color=(0,0,0), outline_width = 1)
        main_layout.add_widget(home_button)
        main_layout.add_widget(self.clicks_label)
        main_layout.add_widget(restart_button)
        home_button.bind(on_release=self.change_screen)
        restart_button.bind(on_release=self.restart)

        #middle screen 
        middle_box = BoxLayout()
        self.add_widget(middle_box)

        placement1 = BoxLayout()
        middle_box.add_widget(placement1)
        

        middle_layout = AnchorLayout(size_hint=(3,.6))
        middle_box.add_widget(middle_layout)

        placement2 = BoxLayout()
        middle_box.add_widget(placement2)

        self.grid = GridLayout(rows=3, spacing=5)
        middle_layout.add_widget(self.grid)
        
        with self.grid.canvas:
            Color(0,0,0)
            self.grid_bg = Rectangle(size = (self.window_size[0]*.63 ,self.window_size[1]*.315), pos=(self.window_size[0]*0.1844, self.window_size[1]*0.392))
        
        self.b1 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b2 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b3 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b4 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b5 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b6 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b7 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b8 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.b9 = Button(background_normal='', background_color= (0.02, 0.6, 0.2))
        self.grid.add_widget(self.b1)
        self.b1.bind(on_release=self.btn1)
        self.grid.add_widget(self.b2)
        self.b2.bind(on_release=self.btn2)
        self.grid.add_widget(self.b3)
        self.b3.bind(on_release=self.btn3)
        self.grid.add_widget(self.b4)
        self.b4.bind(on_release=self.btn4)
        self.grid.add_widget(self.b5)
        self.b5.bind(on_release=self.btn5)
        self.grid.add_widget(self.b6)
        self.b6.bind(on_release=self.btn6)
        self.grid.add_widget(self.b7)
        self.b7.bind(on_release=self.btn7)
        self.grid.add_widget(self.b8)
        self.b8.bind(on_release=self.btn8)
        self.grid.add_widget(self.b9)
        self.b9.bind(on_release=self.btn9)

        #bottom layer
        self.bottom_layout = BoxLayout(size_hint=(1,.8), orientation = 'vertical')
        self.add_widget(self.bottom_layout)

        self.fade_canvas = BoxLayout()
        self.bottom_layout.add_widget(self.fade_canvas)

    def btn1(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch1()
        self.ColorSwitch2()
        self.ColorSwitch4()

    def btn2(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch1()
        self.ColorSwitch2()
        self.ColorSwitch3()
        self.ColorSwitch5()

        
    def btn3(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch3()
        self.ColorSwitch2()
        self.ColorSwitch6()
       
    
    def btn4(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch1()
        self.ColorSwitch4()
        self.ColorSwitch5()
        self.ColorSwitch7()


    def btn5(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch2()
        self.ColorSwitch4()
        self.ColorSwitch5()
        self.ColorSwitch6()
        self.ColorSwitch8()


    def btn6(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch3()
        self.ColorSwitch5()
        self.ColorSwitch6()
        self.ColorSwitch9()


    def btn7(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch4()
        self.ColorSwitch7()
        self.ColorSwitch8()


    def btn8(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch5()
        self.ColorSwitch7()
        self.ColorSwitch8()
        self.ColorSwitch9()


    def btn9(self, instance):
        self.number_clicks += 1
        self.update_clicks()
        self.ColorSwitch6()
        self.ColorSwitch8()
        self.ColorSwitch9()

    def ColorSwitch1(self):
        if self.counter[0] == 0:
            self.b1.background_color = self.bcolor
            self.counter[0] = 1
        else: 
            self.b1.background_color = self.gcolor
            self.counter[0] = 0

    def ColorSwitch2(self):
        if self.counter[1] == 0:
            self.b2.background_color = self.bcolor
            self.counter[1] = 1
        else: 
            self.b2.background_color = self.gcolor
            self.counter[1] = 0

    def ColorSwitch3(self):
        if self.counter[2] == 0:
            self.b3.background_color = self.bcolor
            self.counter[2] = 1
        else: 
            self.b3.background_color = self.gcolor
            self.counter[2] = 0

    def ColorSwitch4(self):
        if self.counter[3] == 0:
            self.b4.background_color = self.bcolor
            self.counter[3] = 1
        else: 
            self.b4.background_color = self.gcolor
            self.counter[3] = 0

    def ColorSwitch5(self):
        if self.counter[4] == 0:
            self.b5.background_color = self.bcolor
            self.counter[4] = 1
        else: 
            self.b5.background_color = self.gcolor
            self.counter[4] = 0

    def ColorSwitch6(self):
        if self.counter[5] == 0:
            self.b6.background_color = self.bcolor
            self.counter[5] = 1
        else: 
            self.b6.background_color = self.gcolor
            self.counter[5] = 0

    def ColorSwitch7(self):
        if self.counter[6] == 0:
            self.b7.background_color = self.bcolor
            self.counter[6] = 1
        else: 
            self.b7.background_color = self.gcolor
            self.counter[6] = 0

    def ColorSwitch8(self):
        if self.counter[7] == 0:
            self.b8.background_color = self.bcolor
            self.counter[7] = 1
        else: 
            self.b8.background_color = self.gcolor
            self.counter[7] = 0

    def ColorSwitch9(self):
        if self.counter[8] == 0:
            self.b9.background_color = self.bcolor
            self.counter[8] = 1
        else: 
            self.b9.background_color = self.gcolor
            self.counter[8] = 0

    def random_tile(self):
        self.counter = []
        x = 0
        while x in range(0,9):
            x = x + 1
            self.counter.append(random.randint(0,1))
        self.ColorSwitch1()
        self.ColorSwitch2()
        self.ColorSwitch3()
        self.ColorSwitch4()
        self.ColorSwitch5()
        self.ColorSwitch6()
        self.ColorSwitch7()
        self.ColorSwitch8()
        self.ColorSwitch9()

    def victory(self):
        self.b1.disabled = True
        self.b1.background_disabled_normal = ''
        self.b1.background_color = (255,69,0)
        self.b2.disabled = True
        self.b2.background_disabled_normal = ''
        self.b2.background_color = (255,69,0)
        self.b3.disabled = True
        self.b3.background_disabled_normal = ''
        self.b3.background_color = (255,69,0)
        self.b4.disabled = True
        self.b4.background_disabled_normal = ''
        self.b4.background_color = (255,69,0)
        self.b5.disabled = True
        self.b5.background_disabled_normal = ''
        self.b5.background_color = (255,69,0)
        self.b6.disabled = True
        self.b6.background_disabled_normal = ''
        self.b6.background_color = (255,69,0)
        self.b7.disabled = True
        self.b7.background_disabled_normal = ''
        self.b7.background_color = (255,69,0)
        self.b8.disabled = True
        self.b8.background_disabled_normal = ''
        self.b8.background_color = (255,69,0)
        self.b9.disabled = True
        self.b9.background_disabled_normal = ''
        self.b9.background_color = (255,69,0)

    def update(self, dt):
        self.window_size = Window.size
        self.update_canvas()
        # self.update_clicks()
        
        
        if (sum(self.counter) == 0 and self.v == 0):
            self.v = 1
            self.victory() 
                
class GreenScreenGameApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.home_widget = HomeWidget()
        screen = Screen(name='home')
        screen.add_widget(self.home_widget)
        self.screen_manager.add_widget(screen)

        game_widget = GameWidget()
        screen = Screen(name='game')
        screen.add_widget(game_widget)
        self.screen_manager.add_widget(screen)

        diff_widget = DiffWidget()
        screen = Screen(name='diff')
        screen.add_widget(diff_widget)
        self.screen_manager.add_widget(screen)

        self.instructions_widget = InstructionsWidget()
        screen = Screen(name='instructions')
        screen.add_widget(self.instructions_widget)
        self.screen_manager.add_widget(screen)

        self.credits_widget = CreditsWidget()
        screen = Screen(name='credits')
        screen.add_widget(self.credits_widget)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
        
    



if __name__ == "__main__":
    game_widget = GameWidget()
    diff_widget = DiffWidget()
    greenscreengame = GreenScreenGameApp()
    greenscreengame.run()