from kivy.app import App
from kivy.lang import Builder

class mileToKilometersConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_kilometers_converter.kv')
        return self.root

mileToKilometersConverter().run()