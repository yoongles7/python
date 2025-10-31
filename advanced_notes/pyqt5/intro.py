# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")        # Caption the window
        self.setGeometry(700, 300, 200, 200)    # where and how big the window should open
        self.setWindowIcon(QIcon("yoongles.jpg"))   # Icon with title

    
def main():
    app = QApplication(sys.argv)        # Provides necessary system arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()