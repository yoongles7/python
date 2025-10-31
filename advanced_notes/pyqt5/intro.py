# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")        # Caption the window
        self.setGeometry(700, 300, 200, 200)    # where and how big the window should open
        self.setWindowIcon(QIcon("yoongles.jpg"))   # Icon with title
        
        #label = QLabel("Hello", self)                         |
        #label.setFont(QFont("Arial", 40))
        #abel.setGeometry(0, 0, 200, 100)
        #label.setStyleSheet("color: red;"
        #                    "background-color: cyan;" 
        #                    "font-weight: bold;" 
        #                    "font-style: italic;" 
        #                    "text-decoration: underline;")
        
        #label.setAlignment(Qt.AlignTop)     # Vertically Top
        #label.setAlignment(Qt.AlignBottom)  # Vertically Bottom
        #label.setAlignment(Qt.AlignCenter)  # Vertically Center
        
        #label.setAlignment(Qt.AlignRight)   # Horizontally Right
        #label.setAlignment(Qt.AlignHCenter) # Horizontally Center
        #label.setAlignment(Qt.AlignLeft)    # Horizontally Left
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("yoongles.jpg")
        label.setPixmap(pixmap)         # Set the image to the window
        
        label.setScaledContents(True)   # Enable scaling of the picture
        
        label.setGeometry((self.width() - label.width()) // 2, 
                          (self.height() - label.height()) // 2,    # self.width() and self.height() Gets width & height  of window automatically
                          label.width(),        # label.width() and label.height() Gets width & height  of image automatically
                          label.height())
        
    
def main():
    app = QApplication(sys.argv)        # Provides necessary system arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()