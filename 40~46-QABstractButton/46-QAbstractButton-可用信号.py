from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QAbstractButton 信号")
window.resize(500, 500)
window.move(400, 250)

btn = QPushButton(window)
btn.setText("按钮1")
btn.move(200, 200)
btn.setCheckable(True)
# btn.pressed.connect(lambda: print("按钮被按下了"))
# btn.released.connect(lambda: print("按钮被释放了"))  # 控件内部松开鼠标，或者鼠标移出控件时发送released信号
# btn.clicked.connect(lambda value: print("按钮被点击了", value))
# 只在控件有效范围内按下，在控件有效范围内松开，才发送该信号；value值为按钮是否被选中
btn.toggled.connect(lambda value: print("按钮选中状态发生了变化", value))  # 按钮选中状态变化时发送信号； value值为按钮是否被选中


# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
