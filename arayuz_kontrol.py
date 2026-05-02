import os

# --- BU SATIRLAR HATAYI ENGELLER (EN TEPEDE OLMALI) ---
os.environ['KIVY_NO_CONFIG'] = '1'
os.environ['KIVY_NO_FILELOG'] = '1'
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ['KIVY_WINDOW'] = 'sdl2'

from kivy.config import Config
# Dokunmatik sürücüleri yerine standart girdiyi zorunlu kılar
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView

class SaygaArayuz(App):
    def on_start(self):
        # Klavye modu ayarı (Pencere oluştuktan sonra)
        Window.softinput_mode = 'below_target'

    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        self.ana_konteyner = FloatLayout()
        
        # --- MEGA AÇILIŞ EKRANI (Ekranı Kaplayan Boyut) ---
        self.splash_logo = Image(
            source='sayga_logo.png',
            size_hint=(None, None),
            # Ekran genişliğinin %95'i kadar devasa
            size=(Window.width * 0.95, Window.width * 0.95), 
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            opacity=0 
        )
        self.ana_konteyner.add_widget(self.splash_logo)
        
        anim = Animation(opacity=1, duration=2.5)
        anim.start(self.splash_logo)
        Clock.schedule_once(self.kontrol_panelini_yukle, 5.0)
        
        return self.ana_konteyner

    def kontrol_panelini_yukle(self, dt):
        self.ana_konteyner.clear_widgets()
        
        kaydirici = ScrollView(size_hint=(1, 1))
        panel_layout = BoxLayout(orientation='vertical', padding=[40, 40, 40, 40], spacing=25, size_hint_y=None)
        panel_layout.bind(minimum_height=panel_layout.setter('height'))
        
        # Panel Logosu
        logo_mini = Image(
            source='sayga_logo.png',
            size_hint=(None, None),
            size=(Window.width * 0.5, Window.width * 0.5),
            pos_hint={'center_x': 0.5}
        )
        panel_layout.add_widget(logo_mini)
        
        panel_layout.add_widget(Label(
            text='SAYGA STUDIO', 
            font_size='38sp', 
            bold=True, 
            color=(1, 0.7, 0, 1),
            size_hint_y=None,
            height=70
        ))
        
        self.txt = TextInput(
            hint_text='Destansı senaryonuzu yazın...',
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            multiline=True,
            size_hint_y=None,
            height=350, 
            font_size='20sp',
            padding=[20, 20, 20, 20]
        )
        panel_layout.add_widget(self.txt)
        
        self.durum_etiketi = Label(text='', color=(0, 1, 0, 1), size_hint_y=None, height=40)
        panel_layout.add_widget(self.durum_etiketi)
        
        btn = Button(
            text='4K RENDERI BAŞLAT', 
            background_color=(0, 0.5, 1, 1), 
            bold=True,
            size_hint_y=None,
            height=110,
            font_size='24sp'
        )
        btn.bind(on_press=self.render_tetikle)
        panel_layout.add_widget(btn)
        
        kaydirici.add_widget(panel_layout)
        self.ana_konteyner.add_widget(kaydirici)

    def render_tetikle(self, instance):
        self.durum_etiketi.text = ">> RENDER BAŞLATILDI"
        print(">> [SAYGA]: GPU RENDER SUCCESSFUL")

if __name__ == "__main__":
    SaygaArayuz().run()
