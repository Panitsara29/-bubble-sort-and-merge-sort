# Import โมดูลที่จำเป็นจากไลบรารี Pyglet
import pyglet
from pyglet.window import Window
from pyglet.graphics import Batch
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet import clock

# ฟังก์ชันแปลงรหัสสีฐานสิบหกเป็นรูปแบบ RGB
def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

# ฟังก์ชันที่นำ Bubble Sort algorithm มาใช้เพื่อเรียงลำดับอาร์เรย์
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# คลาสสำหรับการแสดงผลแบบภาพของอัลกอริทึม Bubble Sort
class Renderer(Window):
    def __init__(self):
        super().__init__(640, 640, "Bubble_sort") # กำหนดค่าหน้าต่างขนาด 640x640 และชื่อ "Bubble_sort"
        self.batch = Batch()   
        self.x = [3, 4, 2, 1, 5]
        self.bars = []
        self.colors = ['#FFC555', '#FF8D67', '#FF5891', '#E844C2', '#7857E8'] # สีสำหรับแต่ละบาร์
        for e, i in enumerate(self.x):
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=hex_to_rgb(self.colors[e])))
        self.sorted_bars = list(self.bars)
        self.is_swapping = False
        self.swap_positions = []

    # ฟังก์ชันเรียกกลับสำหรับการอัปเดตหน้าต่าง
    def on_update(self, deltatime):
        if self.is_swapping: # ถ้ากำลังสลับบาร์ ให้ทำอนิเมชันการสลับ
            self.swap_bars()
        else:
            n = len(self.x)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if self.x[j] > self.x[j + 1]:
                        self.is_swapping = True
                        self.swap_positions = [j, j + 1]
                        
        # อัปเดตสีของบาร์ตามตำแหน่งของพวกเขา
        for e, bar in enumerate(self.bars):
            if e in self.swap_positions:
                bar.color = (255, 255, 255, 255) # ตั้งค่าสีเป็นขาวระหว่างการสลับ
            else:
                bar.color = hex_to_rgb(self.colors[e]) # คืนสีเดิม
                
    # ฟังก์ชันทำอนิเมชันการสลับบาร์
    def swap_bars(self):
        i, j = self.swap_positions
        
        # ถ้าบาร์ทางซ้ายสูงกว่า ให้ทำการสลับ
        if self.x[i] > self.x[j]:
            self.x[i], self.x[j] = self.x[j], self.x[i]
            self.bars[i].x, self.bars[j].x = self.bars[j].x, self.bars[i].x
            self.bars[i], self.bars[j] = self.bars[j], self.bars[i]
        self.is_swapping = False
        self.swap_positions = []
        
    # ฟังก์ชันเรียกกลับสำหรับการวาดหน้าต่าง
    def on_draw(self):
        self.clear()
        self.batch.draw() 

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1) # ตั้งเวลาเรียกฟังก์ชัน on_update ทุก 1 วินาที
run()