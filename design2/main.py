from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    RectangularElevationBehavior,
)

from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton

class RectangularElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatIconButton):
    md_bg_color = [0, 0, 1, 1]

class TodayScreenElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatButton):
    pass

class RectangularElevationListItem(RectangularElevationBehavior,
                                    BackgroundColorBehavior,
                                    TwoLineAvatarIconListItem):
    md_bg_color = [1, 1, 1, 1]

class MyApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')

MyApp().run()