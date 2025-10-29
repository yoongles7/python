# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")        # Caption the window
        self.setGeometry(700, 300, 200, 200)    # where and how big the window should open
        self.setWindowIcon(QIcon("yoongles.jpg"))   # Icon with title
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 200, 100)
        label.setStyleSheet("color: red;"
                            "background-color: cyan;" 
                            "font-weight: bold;" 
                            "font-style: italic;" 
                            "text-decoration: underline;")
        
        #label.setAlignment(Qt.AlignTop)     # Vertically Top
        #label.setAlignment(Qt.AlignBottom)  # Vertically Bottom
        #label.setAlignment(Qt.AlignCenter)  # Vertically Center
        
        #label.setAlignment(Qt.AlignRight)   # Horizontally Right
        #label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        #label.setAlignment(Qt.AlignLeft)    # Horizontally Left
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
    
def main():
    app = QApplication(sys.argv)        # Provides necessary system arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()