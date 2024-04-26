from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

# Slide 32
class MinhaApp(App):
    def build(self):
        return Image(source='\Users\aluno.sesipaulista\Downloads\the heart shaped nose 🫶🏻.jpeg')

if __name__ == '__main__':
    MinhaApp().run()
    
# Slide 33
class MinhaApp(App):
    def build(self):
        return AsyncImage(source='https://www.creativefabrica.com/wp-content/uploads/2022/11/09/Cute-Cats-Digital-Graphic-45821069-1.png')
    
if __name__ == '__main__':
    MinhaApp().run()

