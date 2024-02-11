# Import โมดูลที่จำเป็นจากไลบรารี Pyglet
import pyglet
from pyglet.window import Window
from pyglet.graphics import Batch
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet import clock

# ฟังก์ชันที่ใช้ในการทำ Merge Sort บนอาร์เรย์
def merge_sort(arr):
    if len(arr) <= 5:
        clock.schedule_once(lambda dt: None, 0.5)
        return sorted(arr)
    
    # หาค่ากึ่งกลางของอาร์เรย์และแบ่งเป็นสองอาร์เรย์ย่อย
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# ฟังก์ชันที่ใช้ในการผนวกสองอาร์เรย์ย่อย
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

# ฟังก์ชันแปลงรหัสสีฐานสิบหกเป็นรูปแบบ RGB
def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

# คลาสสำหรับการแสดงผลแบบภาพของอัลกอริทึม Merge Sort
class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Merge Sort") # กำหนดค่าหน้าต่างขนาด 640x640 และชื่อ "Merge Sort"
        self.batch = Batch()
        self.x = [3, 4, 2, 1, 5]
        self.bars = []
        self.colors = ['#FFC555', '#FF8D67', '#FF5891', '#E844C2', '#7857E8']  # สีสำหรับแต่ละบาร์
        for e, i in enumerate(self.x):
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=hex_to_rgb(self.colors[e])))
        self.merged_x = self.x
        self.prev_merged_x = self.x
        self.is_sorted = False

    # ฟังก์ชันเรียกกลับสำหรับการอัปเดตหน้าต่าง
    def on_update(self, dt):
        self.prev_merged_x = self.merged_x
        self.merged_x = merge_sort(self.x)
        if self.prev_merged_x != self.merged_x:
            self.is_sorted = False
            self.bars = []
            for e, i in enumerate(self.merged_x):
                self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=(255, 255, 255, 255)))
        elif not self.is_sorted:
            self.is_sorted = True
            for e, i in enumerate(self.merged_x):
                self.bars[e].color = hex_to_rgb(self.colors[e])

    # ฟังก์ชันเรียกกลับสำหรับการวาดหน้าต่าง
    def on_draw(self):
        self.clear()
        self.batch.draw()

# สร้างอ็อบเจ็กต์ Renderer และเริ่มการทำงานของ Pyglet
renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()