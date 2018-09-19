from kivy.app import App
from kivy.lang import Builder


class mileToKilometersConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('miles_to_kilometers_converter.kv')
        return self.root

    def handle_conversion(self, value):
        value = self.validate_miles()
        result = int(value) * 1.60934
        self.root.ids.output_label.text = "{:.2f}".format(result)

    def handle_increment(self, change):
        value = self.validate_miles() + change
        self.root.ids.miles_input.text = str(value)

    def handle_decrement(self, change):
        value = self.validate_miles() + change
        self.root.ids.miles_input.text = str(value)

    def validate_miles(self):
        try:
            value = int(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0


mileToKilometersConverter().run()
