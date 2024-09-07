from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

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

        layout = FloatLayout(size_hint=(1, 1))

        # Create a background color
        background = BackgroundColor(color=[0.5, 1, 0.5, 1], size_hint=(1, 1))
        layout.add_widget(background)

        content = Label(
            text="Your Carbon Emissions",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=50,
            pos_hint={'center_y': 0.9}
        )
        layout.add_widget(content)

        background_image1 = Image(source='Diagram.png', allow_stretch=True, keep_ratio=False,
                                 size_hint=(None, None), size=(500, 300),
                                 pos_hint={'center_x': 0.25, 'center_y': 0.65})
        layout.add_widget(background_image1)

        background_image2 = Image(source='Percent.png', allow_stretch=True, keep_ratio=False,
                                 size_hint=(None, None), size=(500, 300),
                                 pos_hint={'center_x': 0.75, 'center_y': 0.65})
        layout.add_widget(background_image2)

        background_image1_description = Button(
            text="So much of your carbon emissions you have used up this year.",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.75, 'center_y': 0.4},
            background_color=(1, 1, 1, 1),
        )
        layout.add_widget(background_image1_description)

        background_image1_description = Button(
            text="These are your weekly carbon emissions.",
            size_hint=(0.4, 0.1),
            pos_hint={'center_x': 0.25, 'center_y': 0.4},
            background_color=(1, 1, 1, 1),
        )
        layout.add_widget(background_image1_description)

        background_image1_description = Button(
            text="You are great. You're well on your way to emitting significantly less CO2 this year than would be harmful to the earth.",
            size_hint=(0.99, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            background_color=(1, 1, 1, 1),
        )
        layout.add_widget(background_image1_description)

        # Create buttons for navigation
        qr_button = Button(
            # text="QR Scanner",
            size_hint=(0.1, 0.1),
            size=(50, 50),
            bold=True,
            background_normal = 'cameraIcon.png',
        )
        
        qr_button.bind(on_press=self.go_to_qr_page)

        search_button = Button(
            # text="Search Tool",
            size_hint=(0.1, 0.1),
            size=(50, 30),
            background_color=(1, 0.75, 0.8, 1),
            bold=True,
            background_normal = 'searchIcon.png'
        )
        search_button.bind(on_press=self.go_to_search_page)

        # Position buttons in the middle of the y-axis
        qr_button.pos_hint = {'center_x': 0.1, 'center_y': 0.9}
        search_button.pos_hint = {'center_x': 0.9, 'center_y': 0.9}

        # Add buttons to layout
        layout.add_widget(qr_button)
        layout.add_widget(search_button)

        self.add_widget(layout)

    def go_to_qr_page(self, instance):
        self.manager.current = 'qr'

    def go_to_search_page(self, instance):
        self.manager.current = 'search'

# QR Code Scanner Page
class QRPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = layout = FloatLayout(size_hint=(1, 1))

        switch_button = Button(
            size_hint=(0.12, 0.13),
            size=(50, 50),
            pos_hint={'center_x': 0.95, 'center_y': 0.95},
            bold=True,
            background_normal='Rightarrow.png',
            )
        switch_button.bind(on_press=self.switch_to_home_page)

        camera_button = Button(
            size_hint=(0.12, 0.13),
            size=(50, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            bold=True,
            background_normal='CameraIcon2.png',
        )

        describe_button = Button(
            text="Scan QR-Code",
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.95},
            background_color=(1, 1, 1, 1),
        )

        co2_button = Button(
            size_hint=(0.1, 0.1),
            size=(50, 50),
            pos_hint={'center_x': 0.05, 'center_y': 0.95},
            bold=True,
            background_normal='CO2.png',
        )


        layout.add_widget(switch_button)
        layout.add_widget(camera_button)
        layout.add_widget(describe_button)
        layout.add_widget(co2_button)
        self.add_widget(layout)

    def switch_to_home_page(self, instance):
        if self.manager:
            self.manager.current = 'home'

# Search Bar Page
class SearchPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BackgroundColor(color=[0.5, 0.5, 1, 1])
        switch_button = Button(
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={'center_x': 0.05, 'center_y': 0.95},
            bold=True,
            background_normal='Leftarrow.png',
        )
        switch_button.bind(on_press=self.switch_to_home_page)

        # TextInput and buttons in a horizontal row
        self.text_input = TextInput(
            hint_text='Search by Product..',
            multiline=False,
            size_hint=(None, None),
            size=(1000, 40),
            pos_hint={'center_x': 0.15, 'center_y': 0.95},
        )
        self.text_input.bind(on_text_validate=self.on_submit)

        submit_button = Button(
            text="Search",
            size_hint=(None, None),
            size=(100, 50),
            background_color =(1, 0.75, 0.8, 1),
            pos_hint={'center_x': 0.85, 'center_y': 0.95},
        )
        submit_button.bind(on_press=self.on_submit)
        
        layout.add_widget(switch_button)
        layout.add_widget(self.text_input)
        layout.add_widget(submit_button)
        self.add_widget(layout)

    def switch_to_home_page(self, instance):
        if self.manager:
            self.manager.current = 'home'

    def on_submit(self, instance):
        user_input = self.text_input.text
        self.output_label.text = f"{user_input}"

# Second page (screen) for demonstration
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class WelcomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = FloatLayout()  # Use FloatLayout for precise positioning

        # Create a background color
        background = BackgroundColor(color=[0.9, 0.75, 0.9, 1], size_hint=(1, 1))
        layout.add_widget(background)
        
        # Add the label
        label = Label(
            text="Welcome Back Sam!",
            font_size=32,
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(self.width * 0.8, self.height * 0.1),  # Adjust size relative to the screen size
            pos_hint={'center_x': 0.5, 'center_y': 0.8}  # Position the label higher up
        )
        layout.add_widget(label)
        
        # Add the continue button
        switch_button = Button(
            text="Continue",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.2},  # Position the button higher up
            background_color=(0.8, 0.6, 0.8, 1),
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
        self.add_widget(WelcomePage(name='welcome'))
        self.add_widget(HomePage(name='home'))
        self.add_widget(QRPage(name='qr'))
        self.add_widget(SearchPage(name='search'))
        

# Main application class
class MyApp(App):
    def build(self):
        return MyScreenManager()

# Run the application
if __name__ == '__main__':
    MyApp().run()
