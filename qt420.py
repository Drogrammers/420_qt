import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import qtresources

class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        menu = QMenu(parent)
        exitAction = QAction('Exit', self)
        exitMenu = menu.addAction(exitAction)
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle('Where\'s 420?')
        self.setWindowIcon(QIcon(':/icon.svg'))            
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    trayIcon = SystemTrayIcon(QIcon(":/icon.svg"), ex)
    trayIcon.show()
    sys.exit(app.exec_())
