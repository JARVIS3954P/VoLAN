
from kivy.app import App
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        # Create a button widget
        button = Button(
            text="Press Me",
            font_size=24,
            size_hint=(0.5, 0.5),  # Half the size of the parent window
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Center the button
        )
        # Bind the button's on_press event to a function
        button.bind(on_press=self.say_hello)
        return button

    def say_hello(self, instance):
        print("Hello!")

# Run the app
if __name__ == "__main__":
    HelloApp().run()
