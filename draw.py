import kivy

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Ellipse
from kivy.core.window import Window

from canvas import Canvas

class DrawApp(App):
    def build(self):
        self.title = 'Simple Drawing App'
        return DrawAppLayout()

class DrawAppLayout(BoxLayout):
    #Window.clearcolor = (1, 1, 1, 1)
    sm = ScreenManager()

    def next_canvas(self):
        if int(self.sm.current) < len(self.sm.screen_names):
            self.sm.transition.direction = 'left'
            self.sm.current = str(int(self.sm.current) + 1)

    def prev_canvas(self):
        if int(self.sm.current) > 1:
            self.sm.transition.direction = 'right'
            self.sm.current = str(int(self.sm.current) - 1)

    def clear_canvas(self):
        for child in self.sm.screens:
            child.clear_canvas()

    def open_color_picker(self):
        content = ColorPickerDialog(change_color=self.change_color)
        self._popup = Popup(title='Choose your color', content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def change_color(self, color):
        for child in self.sm.screens:
            child.change_tool_color(color)
        self._popup.dismiss()

    def change_tool_size(self, size):
        for child in self.sm.screens:
            child.change_tool_size(size)

    def change_tool(self, tool):
        for child in self.sm.screens:
            child.change_tool(tool)

class Canvas1(Canvas):
    pass

class Canvas2(Canvas):
    pass

class Canvas3(Canvas):
    pass

class ColorPickerDialog(FloatLayout):
    change_color = ObjectProperty(None)

if __name__ == '__main__':
    DrawApp().run()