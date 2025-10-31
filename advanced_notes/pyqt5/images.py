# PyQt5 Images
import sys
from PyQt5.QtWidgets import QApllication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("yoongles.jpg")        # Pixmap object
        label.setPixmap(pixmap)                 # Setting pixmap object to the screen
        
        label.setScaledContents(True)   # Enabling scaling
        
        label.setGeometry((self.width() - label.width()) // 2, 
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())
        
        
def main():
    app = QApllication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()