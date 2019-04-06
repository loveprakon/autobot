#-*- coding=utf-8 -*-
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():  #def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
   return '<h3>Hello py</h3>' #ให้แสดงข้อความว่า Hello py ออกทางหน้าฟอร์ม

if __name__ == '__main__':
   app.run()