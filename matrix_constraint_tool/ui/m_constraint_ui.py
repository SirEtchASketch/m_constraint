from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel


class M_Constraint_UI(QWidget):
    super()__init__(self, source, target)
    
    self.source = source
    self.target = target
    
    self.setWindowTitle("Matrix Constraint")
    
    self.setMinimumWidth(350)
    self.setMinimumHeight(250)    
    
    self.main_layout = QVBoxLayout()
    self.main_layout.addLayout(self.info_layout)
    self.main_layout.addLayout(self.buttons_layout)
    
    self.set_layout(self.main_layout)


    def info_layout(self):
        
        info_layout = QHBoxLayout()
        
        
        return info_layout
        
        
    def buttons_layout(self):
        
        
        button_layout = QHBoxLayout()

        
        close_button = QPushButton('Close')
        execute_button = QPushButton('Make Constraint')
        
        button_layout.addWidget(close_button)
        button_layout.addWidget(execute_button)
        
        
        return button_layout
    
    
if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.setLayout(widget.create_layout())
    widget.show()
    app.exec_()