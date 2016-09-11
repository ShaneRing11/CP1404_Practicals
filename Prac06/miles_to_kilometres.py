from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresApp(App):
    def build(self):
        Window.size = (375, 150)
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_increment(self, current_value, increment):
        try:
            new_value = int(current_value) + increment
            self.root.ids.input_miles.text = str(new_value)
            result = int(new_value) * 1.60934
            self.root.ids.output_kilometres.text = str(result)
        except ValueError:
            new_value = 0 + increment
            self.root.ids.input_miles.text = str(new_value)
            result = int(new_value) * 1.60934
            self.root.ids.output_kilometres.text = str(result)


MilesToKilometresApp().run()
