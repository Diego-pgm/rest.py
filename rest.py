from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen, NoTransition
from kivy.core.window import Window

Builder.load_string("""
<MenuScreen> 
    GridLayout:
        rows: 3
        orientation: 'vertical'
        Button:
            background_normal: 'taco.jpg'
            text: 'Taco $25'
            color: 0,0,0,1
            on_press: root.manager.current = 'taco'
        Button:
            background_normal: 'quesadilla.jpg'
            text: 'Quesadilla $35'
            color: 0,0,0,1
            on_press: root.manager.current = 'quesadilla'
        Button:
            background_normal: 'cheve.jpg'
            text: 'Cerveza $35'
            color: 0,0,0,1
            on_press: root.manager.current = 'chela'
        Button:
            background_normal: 'chelato.jpg'
            text: 'Chelato $45'
            color: 0,0,0,1
            on_press: root.manager.current = 'chelato'
        Button:
            background_normal: 'cubita.jpg'
            text: 'Cuba $65'
            color: 0,0,0,1
            on_press: root.manager.current = 'cuba'
            
            
<TacoScreen>:
    FloatLayout:
        color: 1,1,1,1
        spacing: .3
        Label:
            text: 'Cuantos tacos?'
            color: 0,0,0,1
            size_hint: .1, .1
            pos_hint: {"x": .45, "y": .8}
        Button:
            text: '+'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .55, "y": .7}
            on_press: root.mas()
        Button:
            text: '-'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .35, "y": .7}
            on_press: root.menos()
        Button:
            text: 'Calcular'
            color:0,0,0,1
            size_hint: .3, .1
            pos_hint: {"x": .35, "y": .45}
            on_press: root.calcula()
        Button:
            text: 'Menu'
            color:0,0,0,1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .15
            pos_hint: {"x": .35, "y": .1}
        
<QuesadillaScreen>:
    FloatLayout:
        color: 1,1,1,1
        spacing: .3
        Label:
            text: 'Cuantas quesadillas?'
            color: 0,0,0,1
            size_hint: .1, .1
            pos_hint: {"x": .45, "y": .8}
        Button:
            text: '+'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .55, "y": .7}
            on_press: root.mas()
        Button:
            text: '-'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .35, "y": .7}
            on_press: root.menos()
        Button:
            text: 'Calcular'
            color:0,0,0,1
            size_hint: .3, .1
            pos_hint: {"x": .35, "y": .45}
            on_press: root.calcula()
        Button:
            text: 'Menu'
            color:0,0,0,1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .15
            pos_hint: {"x": .35, "y": .1} 
            
<ChelaScreen>:
    FloatLayout:
        color: 1,1,1,1
        spacing: .3
        Label:
            text: 'Cuantas cervezas?'
            color: 0,0,0,1
            size_hint: .1, .1
            pos_hint: {"x": .45, "y": .8}
        Button:
            text: '+'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .55, "y": .7}
            on_press: root.mas()
        Button:
            text: '-'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .35, "y": .7}
            on_press: root.menos()
        Button:
            text: 'Calcular'
            color:0,0,0,1
            size_hint: .3, .1
            pos_hint: {"x": .35, "y": .45}
            on_press: root.calcula()
        Button:
            text: 'Menu'
            color:0,0,0,1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .15
            pos_hint: {"x": .35, "y": .1}
            
<ChelatoScreen>:
    FloatLayout:
        color: 1,1,1,1
        spacing: .3
        Label:
            text: 'Cuantos chelatos?'
            color: 0,0,0,1
            size_hint: .1, .1
            pos_hint: {"x": .45, "y": .8}
        Button:
            text: '+'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .55, "y": .7}
            on_press: root.mas()
        Button:
            text: '-'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .35, "y": .7}
            on_press: root.menos()
        Button:
            text: 'Calcular'
            color:0,0,0,1
            size_hint: .3, .1
            pos_hint: {"x": .35, "y": .45}
            on_press: root.calcula()
        Button:
            text: 'Menu'
            color:0,0,0,1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .15
            pos_hint: {"x": .35, "y": .1}

<CubaScreen>:
    FloatLayout:
        color: 1,1,1,1
        spacing: .3
        Label:
            text: 'Cuantas cubas?'
            color: 0,0,0,1
            size_hint: .1, .1
            pos_hint: {"x": .45, "y": .8}
        Button:
            text: '+'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .55, "y": .7}
            on_press: root.mas()
        Button:
            text: '-'
            color: 0,0,0,1
            size_hint: .1, .05
            pos_hint: {"x": .35, "y": .7}
            on_press: root.menos()
        Button:
            text: 'Calcular'
            color:0,0,0,1
            size_hint: .3, .1
            pos_hint: {"x": .35, "y": .45}
            on_press: root.calcula()
        Button:
            text: 'Menu'
            color:0,0,0,1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .15
            pos_hint: {"x": .35, "y": .1}
                
""")

class MenuScreen(Screen):
    pass

class TacoScreen(Screen):
    def __init__(self, **kwargs):
        super(TacoScreen, self).__init__(**kwargs)
        self.cont = 1
        self.ti = TextInput(text=str(self.cont), multiline=False, readonly=True)
        self.ti.size_hint = .1,.05
        self.ti.pos_hint = {"x": .45,"y": .7}
        self.add_widget(self.ti)
        self.ti2 = TextInput(size_hint=(.5,.1), pos_hint={"x":.25,"y":.35}, multiline=False,  readonly=True)
        self.add_widget(self.ti2)

    def mas(self):
        self.cont = self.cont+1
        self.ti.text = str(self.cont)

    def menos(self):
        self.cont = self.cont-1
        self.ti.text = str(self.cont)

    def calcula(self):
        self.calc = int(self.ti.text)*25
        self.ti2.text = "Tu total es de: %s" %str(self.calc)


class QuesadillaScreen(Screen):
    def __init__(self, **kwargs):
        super(QuesadillaScreen, self).__init__(**kwargs)
        self.cont = 1
        self.ti = TextInput(text=str(self.cont), multiline=False, readonly=True)
        self.ti.size_hint = .1,.05
        self.ti.pos_hint = {"x": .45,"y": .7}
        self.add_widget(self.ti)
        self.ti2 = TextInput(size_hint=(.5,.1), pos_hint={"x":.25,"y":.35}, multiline=False,  readonly=True)
        self.add_widget(self.ti2)

    def mas(self):
        self.cont = self.cont+1
        self.ti.text = str(self.cont)

    def menos(self):
        self.cont = self.cont-1
        self.ti.text = str(self.cont)

    def calcula(self):
        self.calc = int(self.ti.text)*35
        self.ti2.text = "Tu total es de: %s" %str(self.calc)

class ChelaScreen(Screen):
    def __init__(self, **kwargs):
        super(ChelaScreen, self).__init__(**kwargs)
        self.cont = 1
        self.ti = TextInput(text=str(self.cont), multiline=False, readonly=True)
        self.ti.size_hint = .1,.05
        self.ti.pos_hint = {"x": .45,"y": .7}
        self.add_widget(self.ti)
        self.ti2 = TextInput(size_hint=(.5,.1), pos_hint={"x":.25,"y":.35}, multiline=False,  readonly=True)
        self.add_widget(self.ti2)

    def mas(self):
        self.cont = self.cont+1
        self.ti.text = str(self.cont)

    def menos(self):
        self.cont = self.cont-1
        self.ti.text = str(self.cont)

    def calcula(self):
        self.calc = int(self.ti.text)*35
        self.ti2.text = "Tu total es de: %s" %str(self.calc)

class ChelatoScreen(Screen):
    def __init__(self, **kwargs):
        super(ChelatoScreen, self).__init__(**kwargs)
        self.cont = 1
        self.ti = TextInput(text=str(self.cont), multiline=False, readonly=True)
        self.ti.size_hint = .1,.05
        self.ti.pos_hint = {"x": .45,"y": .7}
        self.add_widget(self.ti)
        self.ti2 = TextInput(size_hint=(.5,.1), pos_hint={"x":.25,"y":.35}, multiline=False,  readonly=True)
        self.add_widget(self.ti2)

    def mas(self):
        self.cont = self.cont+1
        self.ti.text = str(self.cont)

    def menos(self):
        self.cont = self.cont-1
        self.ti.text = str(self.cont)

    def calcula(self):
        self.calc = int(self.ti.text)*45
        self.ti2.text = "Tu total es de: %s" %str(self.calc)

class CubaScreen(Screen):
    def __init__(self, **kwargs):
        super(CubaScreen, self).__init__(**kwargs)
        self.cont = 1
        self.ti = TextInput(text=str(self.cont), multiline=False, readonly=True)
        self.ti.size_hint = .1,.05
        self.ti.pos_hint = {"x": .45,"y": .7}
        self.add_widget(self.ti)
        self.ti2 = TextInput(size_hint=(.5,.1), pos_hint={"x":.25,"y":.35}, multiline=False,  readonly=True)
        self.add_widget(self.ti2)

    def mas(self):
        self.cont = self.cont+1
        self.ti.text = str(self.cont)

    def menos(self):
        self.cont = self.cont-1
        self.ti.text = str(self.cont)

    def calcula(self):
        self.calc = int(self.ti.text)*25
        self.ti2.text = "Tu total es de: %s" %str(self.calc)

screen_manager = ScreenManager(transition=NoTransition())
screen_manager.add_widget(MenuScreen(name="menu"))
screen_manager.add_widget(TacoScreen(name="taco"))
screen_manager.add_widget(QuesadillaScreen(name="quesadilla"))
screen_manager.add_widget(ChelaScreen(name="chela"))
screen_manager.add_widget(ChelatoScreen(name="chelato"))
screen_manager.add_widget(CubaScreen(name="cuba"))

class VillasApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return screen_manager

villas = VillasApp()
villas.run()
