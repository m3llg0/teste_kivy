from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
# Slide 66
'''class MinhaApp(App):
    def build(self):
        # Criando um Carousel
        carousel = Carousel()

        # Adicionando widgets ao Carousel
        for i in range(3):
            label = Label(text=f'Slide {i+1}')
            carousel.add_widget(label)
        
        return carousel'''

# Slide 67
class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right', loop=True)
        
        # Adicionando imagens ao Carousel
        imagens = ['senai.png', 'sesi.png', 'iel.jpg']
        for imagem in imagens:
            imagem_widget = AsyncImage(source=imagem)
            carousel.add_widget(imagem_widget)

        return carousel

if __name__ == '__main__':
    CarouselApp().run()