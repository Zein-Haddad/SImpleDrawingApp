import kivy

from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Ellipse, Rectangle, Line

class Canvas(Screen):
    tool_color = [1, 1, 1, 1]
    tool_size = 5
    def on_touch_down(self, touch):
        if self.transition_progress == 0.0 or self.transition_progress == 1.0:
            with self.canvas:
                Color(self.tool_color[0], self.tool_color[1], self.tool_color[2], self.tool_color[3])
                Ellipse(pos=(touch.x - self.tool_size / 2, touch.y - self.tool_size / 2), size=(self.tool_size, self.tool_size))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=(self.tool_size / 2))

    def on_touch_move(self, touch):
        if self.transition_progress == 0.0 or self.transition_progress == 1.0:
            try:
                touch.ud['line'].points += [touch.x, touch.y]
            except:
                pass

    def change_tool_color(self, color):
        self.tool_color = color

    def change_tool_size(self, size):
        self.tool_size = size
    
    def clear_canvas(self):
        self.canvas.clear()