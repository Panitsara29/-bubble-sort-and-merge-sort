import pyglet
from pyglet.window import Window
from pyglet.graphics import Batch
from pyglet.app import run
from pyglet.shapes import Circle, Rectangle
from pyglet import clock

def merge_sort(arr):
    if len(arr) <= 5:
        clock.schedule_once(lambda dt: None, 0.5)
        return sorted(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Merge Sort")
        self.batch = Batch()
        self.x = [3, 4, 2, 1, 5]
        self.bars = []
        self.colors = ['#FFC555', '#FF8D67', '#FF5891', '#E844C2', '#7857E8']
        for e, i in enumerate(self.x):
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=hex_to_rgb(self.colors[e])))
        self.merged_x = self.x

    def on_update(self, dt):
        self.merged_x = merge_sort(self.x)
        self.bars = []
        for e, i in enumerate(self.merged_x):
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=hex_to_rgb(self.colors[e])))

    def on_draw(self):
        self.clear()
        self.batch.draw()


renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()