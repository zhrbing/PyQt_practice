from PyQt5.Qt import *
import sys
# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件

window.setWindowTitle("QButtonGroup-查看按钮")
window.resize(500, 500)
window.move(400, 250)

rb_male = QRadioButton("男", window)
rb_male.move(100, 100)
rb_male.setChecked(True)
rb_female = QRadioButton("女", window)
rb_female.move(180, 100)

sex_group = QButtonGroup(window)
sex_group.addButton(rb_male, 1)  # 1 为设置的 id，默认为-1 系统会自动分配
sex_group.addButton(rb_female, 2)
sex_group.removeButton(rb_female)  # 从组中移除按钮

rb_yes = QRadioButton("yes", window)
rb_yes.move(100, 220)
rb_no = QRadioButton("no", window)
rb_no.move(180, 220)

answer_group = QButtonGroup(window)
answer_group.addButton(rb_yes)
answer_group.addButton(rb_no)

print(sex_group.buttons())
print(sex_group.button(2))  # sex_group 中 id 为 2 的按钮
print(sex_group.checkedButton())  # 被选中的按钮

# 2.3展示控件
window.show()

# 3.应用程序的执行， 进入到消息循环
sys.exit(app.exec_())
