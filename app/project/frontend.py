from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

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

# Homepage with navigation buttons
class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=[0.5, 0.5, 1, 1], orientation='vertical', padding=(20, 50, 20, 20), spacing=20)
        
        content = Label(
            text="Page 1 - Your Carbon Emissions",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),  # Ensure the label doesn't stretch vertically
            height=50,  # Set the height of the label
            pos_hint={'top': 1}  # Align the label to the top of the parent layout
            )
        layout.add_widget(content)
        
        # Create buttons for navigation
        qr_button = Button(
            text="QR Scanner", 
            size_hint=(0.2, 0.1), 
            size=(50, 30), 
            pos_hint={'center_x': 0.5, 'bottom': 1}, 
            background_color =(0.8, 0.6, 0.8, 1),
            bold=True
            )
        qr_button.bind(on_press=self.go_to_qr_page)
        
        search_button = Button(
            text="Search Tool", 
            size_hint=(0.2, 0.1), 
            size=(50, 30), 
            pos_hint={'center_x': 0.5, 'bottom': 1}, 
            background_color =(1, 0.75, 0.8, 1),
            )
        search_button.bind(on_press=self.go_to_search_page)
        
        second_button = Button(
            text="Second Page", 
            size_hint=(0.2, 0.1), 
            size=(50, 30), 
            pos_hint={'center_x': 0.5, 'bottom': 1}, 
            background_color =(0.5, 1, 0.5, 1),
            )
        second_button.bind(on_press=self.go_to_second_page)
        
        # Add buttons to layout
        layout.add_widget(qr_button)
        layout.add_widget(search_button)
        layout.add_widget(second_button)
        
        self.add_widget(layout)
    
    def go_to_qr_page(self, instance):
        self.manager.current = 'qr'
    
    def go_to_search_page(self, instance):
        self.manager.current = 'search'
    
    def go_to_second_page(self, instance):
        self.manager.current = 'second'

# QR Code Scanner Page
class QRPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=[0.5, 1, 0.5, 1], orientation='vertical')

        content = Label(text="Page 2 - Light Green")
        switch_button = Button(
            text="Go to Home Screen",
            size_hint=(0.3, 0.1),
            size=(200, 50),
            pos_hint={'center_x': 0.5},
            background_color =(0.8, 0.6, 0.8, 1),
            )
        switch_button.bind(on_press=self.switch_to_home_page)
        
        layout.add_widget(content)
        layout.add_widget(switch_button)
        self.add_widget(layout)

    def switch_to_home_page(self, instance):
        if self.manager:
            self.manager.current = 'home'

# Search Bar Page
class SearchPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=[0.5, 0.5, 1, 1], orientation='vertical')

        content = Label(text="Page 3 - Search Bar")
        switch_button = Button(
            text="Go to Home Screen",
            size_hint=(0.3, 0.1),
            size=(200, 50),
            pos_hint={'center_x': 0.5},
            background_color =(0.8, 0.6, 0.8, 1),
            )
        switch_button.bind(on_press=self.switch_to_home_page)
        self.text_input = TextInput(
            hint_text='Gib hier etwas ein',  # Platzhaltertext
            multiline=True,
            size_hint=(0.5, 0.5),  # Größe des TextInput
            pos_hint={'center_x': 0.5},
        )
        submit_button = Button(
            text="Eingabe abschicken",
            size_hint=(0.3, 0.1),
            size=(200, 50),
            pos_hint={'center_x': 0.5},
            background_color =(1, 0.75, 0.8, 1),
        )
        submit_button.bind(on_press=self.on_submit)

        self.output_label = Label(text='Deine Eingabe wird hier angezeigt')
        
        layout.add_widget(content)
        layout.add_widget(switch_button)
        layout.add_widget(submit_button)
        layout.add_widget(self.text_input)
        layout.add_widget(self.output_label)
        self.add_widget(layout)

    def switch_to_home_page(self, instance):
        if self.manager:
            self.manager.current = 'home'

    def on_submit(self, instance):
        # Hol den Text vom TextInput
        user_input = self.text_input.text
        # Setze den Text im Label auf den Input-Text
        self.output_label.text = f"Du hast eingegeben: {user_input}"

# Second page (screen) for demonstration
class SecondPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="This is the second page"))
        
        switch_button = Button(
            text="Go to Home Screen",
            size_hint=(0.3, 0.1),
            size=(200, 50),
            pos_hint={'center_x': 0.5},
            background_color =(0.8, 0.6, 0.8, 1),
            )
        switch_button.bind(on_press=self.switch_to_home_page)
        
        layout.add_widget(switch_button)
        self.add_widget(layout)

    def switch_to_home_page(self, instance):
        if self.manager:
            self.manager.current = 'home'

# Screen manager to handle multiple pages
class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add the screens to the ScreenManager
        self.add_widget(HomePage(name='home'))
        self.add_widget(QRPage(name='qr'))
        self.add_widget(SearchPage(name='search'))
        self.add_widget(SecondPage(name='second'))

# Main application class
class MyApp(App):
    def build(self):
        return MyScreenManager()

# Run the application
if __name__ == '__main__':
    MyApp().run()
