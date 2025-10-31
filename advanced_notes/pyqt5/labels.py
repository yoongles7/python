# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 200, 200)   
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: red;" 
                            "background: cyan;"
                            "font-weight: bold;" 
                            "font-style: italic;" 
                            "text-decoration: underline;")
        
        #label.setAlignment(Qt.AlignTop)     # Vertically top
        # label.setAlignment(Qt.AlignBottom) # Vertically bottom
        # label.setAlignment(Qt.AlignCenter) # Vertically center
        #label.setAlignment(Qt.AlignRight)   # Horizontally right
        #label.setAlignment(Qt.AlignLeft)    # Horizontally left
        # label.setAlignment(Qt.AlignHCenter)# Horizontally center
        label.setAlignment(Qt.AlignCenter)   # Center of the window

    
def main():
    app = QApplication(sys.argv)        # Provides necessary system arguments
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()