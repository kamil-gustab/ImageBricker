import window_ui
import sys

if __name__ == "__main__":
    app = window_ui.QtWidgets.QApplication(sys.argv)
    MainWindow = window_ui.QtWidgets.QMainWindow()
    ui = window_ui.My_window()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
