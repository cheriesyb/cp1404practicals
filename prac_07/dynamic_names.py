from kivy.app import App
from kivy.lang import Builder


class ListNames(App):
    def build(self):
        self.title = "List of names"
        self.root = Builder.load_file('dynamic_names.kv')
        return self.root
