from kivy.app import App 
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

# Slide 9, 26, 27 e 28
class MyApp(App):
    def build(self):
        return Button(
            text='Hello World!', 
            font_size=50,
            background_color=get_color_from_hex('#3498db')
            )

# Slide 29
def botao_pressionado(instance):
    print('Botão pressionado!')

class MinhaApp(App):
    def build(self):
        btn = Button(text='Clique Aqui')
        btn.bind(on_press=botao_pressionado)
        return btn

# Slide 30
class MinhaApp(App):
    def build(self):
        return Button(text='Clique Aqui', size_hint=(0.5, 0.2))
    

if __name__ == '__main__':
    MinhaApp().run()