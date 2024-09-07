from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
# Set default background color
Window.clearcolor = (0.9, 1, 0.9, 1)  # Light green background
# JSON store to save user data
store = JsonStore('user_data.json')
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Title
        title = Label(text='Sign In', font_size='32sp', bold=True, color=(0, 0.5, 0, 1))
        register_label = Label(text='Register', font_size='24sp', color=(0, 0.5, 0, 1))
        # Input fields
        self.username = TextInput(hint_text='Username', multiline=False, font_size='20sp', size_hint_y=None, height=40)
        self.email = TextInput(hint_text='Email', multiline=False, font_size='20sp', size_hint_y=None, height=40)
        self.password = TextInput(hint_text='Password', multiline=False, password=True, font_size='20sp', size_hint_y=None, height=40)
        # Submit button
        submit = Button(text='Submit', on_press=self.save_user, font_size='20sp', size_hint_y=None, height=50, background_color=(0, 0.7, 0, 1))
        # Add widgets
        layout.add_widget(title)
        layout.add_widget(register_label)
        layout.add_widget(self.username)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(submit)
        # Add background image (e.g., plant leaves)
        background = Image(source='plant_leaves.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        self.add_widget(layout)
    def save_user(self, instance):
        # Save user details and switch to home screen
        store.put('user', username=self.username.text, password=self.password.text, email=self.email.text)
        self.manager.current = 'home'
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Retrieve user data and display a welcome message
        if store.exists('user'):
            user_data = store.get('user')
            welcome_message = f'Welcome, {user_data["username"]}!'
        else:
            welcome_message = 'Welcome, Guest!'
        layout.add_widget(Label(text=welcome_message, font_size='24sp', color=(0, 0.5, 0, 1)))
        self.add_widget(layout)
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm
if __name__ == '__main__':
    MyApp().run()


