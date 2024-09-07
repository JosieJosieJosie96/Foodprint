from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

# First page (screen) with a search bar
class FirstPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = PageLayout()
        
        # Adding background color to Page 1
        with self.canvas.before:
            Color(0.5, 0.5, 1, 1)  # Change color here (R, G, B, A)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        # Page 1
        layout.add_widget(Label(text="Your Carbon Emissions this week"))
        
        # Page 2
        layout.add_widget(Label(text="This is the first page"))

        # Page 3
        switch_button = Button(text="Go to Second Page")
        
        # Delay the screen switching by using a function that gets the ScreenManager
        switch_button.bind(on_press=self.switch_to_second_page)
        
        layout.add_widget(switch_button)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    # Function to switch to the second page
    def switch_to_second_page(self, instance):
        # Access self.manager safely
        if self.manager:
            self.manager.current = 'second'

# Second page (screen) for demonstration
class SecondPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="This is the second page"))
        
        switch_button = Button(text="Go to First Page")
        switch_button.bind(on_press=self.switch_to_first_page)
        
        layout.add_widget(switch_button)
        self.add_widget(layout)

    # Function to switch back to the first page
    def switch_to_first_page(self, instance):
        if self.manager:
            self.manager.current = 'first'

# Screen manager to handle multiple pages
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add the screens to the ScreenManager
        self.add_widget(FirstPage(name='first'))
        self.add_widget(SecondPage(name='second'))

# Main application class
class MyApp(App):
    def build(self):
        return MyScreenManager()

# Run the application
if __name__ == '__main__':
    MyApp().run()
