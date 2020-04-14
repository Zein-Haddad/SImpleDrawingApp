import kivy

from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Ellipse, Rectangle, Line, InstructionGroup

class Canvas(Screen):
    tool_color = [1, 1, 1, 1]
    tool_size = 5
    current_tool = 'Pen tool'

    line_start = []
    lines = []

    def on_touch_down(self, touch):
        if self.current_tool == 'Pen tool':
            with self.canvas:
                Color(self.tool_color[0], self.tool_color[1], self.tool_color[2], self.tool_color[3])
                Ellipse(pos=(touch.x - self.tool_size / 2, touch.y - self.tool_size / 2), size=(self.tool_size, self.tool_size))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=(self.tool_size / 2))

        if self.current_tool == 'Eraser':
            with self.canvas:
                Color(0, 0, 0, 1)
                Ellipse(pos=(touch.x - self.tool_size / 2, touch.y - self.tool_size / 2), size=(self.tool_size * 2, self.tool_size * 2))
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=(self.tool_size))

        if self.current_tool == 'Line tool':
            with self.canvas:
                Color(self.tool_color[0], self.tool_color[1], self.tool_color[2], self.tool_color[3])
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=(self.tool_size / 2))
                self.line_start = [touch.x, touch.y]

    def on_touch_move(self, touch):
        if self.current_tool == 'Pen tool':
            try:
                touch.ud['line'].points += [touch.x, touch.y]
            except:
                pass

        if self.current_tool == 'Eraser':
            try:
                touch.ud['line'].points += [touch.x, touch.y]
            except:
                pass

        if self.current_tool == 'Line tool':
            try:
                if len(self.lines) > 1:
                    item = self.lines.pop(0)
                    self.canvas.remove(item)

                line = InstructionGroup()
                line.add(Color(self.tool_color[0], self.tool_color[1], self.tool_color[2], self.tool_color[3]))
                line.add(Line(points=(self.line_start[0], self.line_start[1], touch.x, touch.y), width=(self.tool_size / 2)))
                self.lines.append(line)
                self.canvas.add(line)
            except:
                pass

    def on_touch_up(self, touch):
        if self.current_tool == 'Line tool':
            try:
                touch.ud['line'].points += [touch.x, touch.y]

                if len(self.lines) > 0:
                    for line in self.lines:
                        self.canvas.remove(line)
                        self.lines.remove(line)
            except:
                pass

    def change_tool_color(self, color):
        self.tool_color = color

    def change_tool_size(self, size):
        self.tool_size = size

    def change_tool(self, tool):
        self.current_tool = tool
    
    def clear_canvas(self):
        self.canvas.clear()