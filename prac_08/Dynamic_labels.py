from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label  # Added import for Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names_to_phone = {"Bob Brown": "0441411211", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file("Dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names_to_phone:
            temp_label = Label(text=name)
            temp_label.color = (0, 0, 1, 1)  # Example: Set label color to blue (R,G,B,A)
            self.root.ids.main_box.add_widget(temp_label)

DynamicLabelsApp().run()




