from kivy.app import App 
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Slide 34
'''class MinhaApp(App):
    def build(self):
        return Slider(min=0, max=100, value=50)

if __name__ =='__main__':
    MinhaApp().run()'''

# Slide 35 - Slider + Label
class MinhaApp(App):
    def build(self):
        # Layout Principal
        layout = BoxLayout(orientation='vertical', padding=20)

        # Slider
        slider = Slider(min=0, max=100, value=50, step=1)
        # Definindo step=1 para permitir apenas valores inteiros
        slider.bind(value=self.atualizar_label)

        # Label para mostrar o valor do slider
        self.label = Label(text='Valor do Slider: {}'.format(int(slider.value)))
        # Exibir apenas o valor inteiro

        # Adicionando os widgets ao layout
        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout
    def atualizar_label (self, instance, valor):
        # Atualize o texto do label com o valor inteiro atual do slider
        self.label.text = 'Valor do Slider: {}'.format(int(valor))

if __name__ == '__main__':
    MinhaApp().run()