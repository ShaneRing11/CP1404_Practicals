from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class DynamicWidgetApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.string_list = {"0.5 metre string", "1 metre string", "2 metre string", "5 metre string",
                            "string sized string"}

    def build(self):
        self.title = "Dynamic string list"
        self.root = Builder.load_file('dynamic.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.string_list:
            temp_button = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_button)

DynamicWidgetApp().run()