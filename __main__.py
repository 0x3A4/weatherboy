import gui
import sys

if __name__ == "__main__":
    app = gui.QApplication(sys.argv)
    guiWindow = gui.Window()
    guiWindow.show()
    app.exec()
