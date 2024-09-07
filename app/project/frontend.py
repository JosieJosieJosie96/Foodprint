from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

# BackgroundColor class to set the background color
class BackgroundColor(BoxLayout):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Homepage with emissions overview
class HomePage(Screen):
    def __init__(self, color, content, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=color, orientation='vertical')
        layout.add_widget(content)
        self.add_widget(layout)

# QR Code Scanner Page
class QRPage(Screen):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=color, orientation='vertical')

        content=Label(text="Page 2 - Light Green")

        switch_button = Button(text="Go to Second Page")
        switch_button.bind(on_press=self.switch_to_second_page)
        
        layout.add_widget(content)
        layout.add_widget(switch_button)
        self.add_widget(layout)

    def switch_to_second_page(self, instance):
        if self.manager:
            self.manager.current = 'second'

# Search Bar Page
class SearchPage(Screen):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=color, orientation='vertical')

        content=Label(text="Page 3 - Search Bar")

        layout.add_widget(content)
        self.add_widget(layout)

# First page (screen) with its own background color
class FirstPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # PageLayout to hold two pages
        layout = PageLayout()
        
        # Create two pages with different background colors
        page1 = HomePage(color=[0.5, 0.5, 1, 1], content=Label(text="Page 1 - Your Carbon Emissions"))
        page2 = QRPage(color=[0.5, 1, 0.5, 1])
        page3 = SearchPage(color=[0.5, 0.5, 1, 1])

        # Add pages to PageLayout
        layout.add_widget(page1)
        layout.add_widget(page2)
        layout.add_widget(page3)
        
        # Add PageLayout to the FirstPage screen
        self.add_widget(layout)

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
