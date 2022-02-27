from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import config
import operations

class save_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Save")
        MainWindow.resize(300, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(95, 0, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 270, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(100, 80, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.saveButton.clicked.connect(lambda: self.save_file())
        self.saveButton.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Save", "Save"))
        self.label.setText(_translate("Save", "Are you sure?"))
        self.label_2.setText(_translate("Save", "Saving file will overwrite previous version!"))
        self.saveButton.setText(_translate("Save", "Save"))

    @staticmethod
    def save_file():
        operations.save_photo(source_path=config.temp_image_path, target_path=config.original_image_path)

class about_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("About")
        MainWindow.resize(400, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.label.setPixmap(QtGui.QPixmap("imgs/GK.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 130, 130))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("About", "About"))
        self.label_2.setText(_translate("About", "Image Bricker\n"
            "Created by\n"
            "Kamil Gustab\n"))


class My_window(QMainWindow):
    def open_about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = about_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_save(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = save_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("Image Bricker")
        MainWindow.resize(1000, 1000)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("Image Bricker")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photoFrame = QtWidgets.QLabel(self.centralwidget)
        self.photoFrame.setEnabled(True)
        self.photoFrame.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        pixmap = QtGui.QPixmap("imgs/default.png")
        pixmap_scaled = pixmap.scaled(1000, 750, QtCore.Qt.KeepAspectRatio)
        self.photoFrame.setPixmap(pixmap_scaled)
        self.photoFrame.setScaledContents(False)
        self.photoFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.photoFrame.setWordWrap(False)
        self.photoFrame.setObjectName("photoFrame")

        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setEnabled(True)
        self.goButton.setGeometry(QtCore.QRect(835, 835, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.goButton.setFont(font)
        self.goButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.goButton.setIconSize(QtCore.QSize(16, 16))
        self.goButton.setAutoDefault(False)
        self.goButton.setDefault(False)
        self.goButton.setFlat(False)
        self.goButton.setObjectName("goButton")
        self.goButton.setShortcut("Ctrl+G")

        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(85, 835, 80, 80))

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.chooseFileButton.setFont(font)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 800, 220, 20))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 835, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("16")
        self.comboBox.addItem("32")
        self.comboBox.addItem("64")
        self.comboBox.addItem("128")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 800, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(577, 800, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(630, 835, 15, 15))
        self.checkBox.setObjectName("checkBox")

        self.rotateButton = QtWidgets.QPushButton(self.centralwidget)
        self.rotateButton.setGeometry(QtCore.QRect(760, 850, 50, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/rotate_arrow.png"))
        self.rotateButton.setIcon(icon)
        self.rotateButton.setIconSize(QtCore.QSize(25, 25))
        self.rotateButton.setObjectName("rotateButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.setTitle("File")
        self.menubar.addAction(self.menuFile.menuAction())

        self.previewButton = QtWidgets.QPushButton(self.centralwidget)
        self.previewButton.setGeometry(QtCore.QRect(440, 765, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.previewButton.setFont(font)
        self.previewButton.setObjectName("previewButton")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.make_funct()
        self.set_texts()

    def make_funct(self):
        self.goButton.clicked.connect(lambda: self.scale_down_image())
        self.goButton.clicked.connect(lambda: self.bricking(config.temp_image_path))
        self.goButton.clicked.connect(lambda: self.change_image(config.temp_image_path))
        self.goButton.clicked.connect(lambda: self.show_popup(title="Done!", text="Operation done!"))

        self.chooseFileButton.clicked.connect(self.browse_files)

        self.previewButton.clicked.connect(lambda: self.open_image(config.temp_image_path))

        self.rotateButton.clicked.connect(lambda: self.rotate_image())
        self.rotateButton.clicked.connect(lambda: self.change_image(config.temp_image_path))

        self.actionAbout.triggered.connect(self.open_about)

        self.actionSave.triggered.connect(self.open_save)

        self.actionSaveAs.triggered.connect(lambda: self.save_as())

    def set_texts(self):
        self.label_3.setText("Add Brick effect:")
        self.previewButton.setText("Open Preview")
        self.actionSave.setText("Save")
        self.actionSaveAs.setText("Save as...")
        self.actionAbout.setText("About...")
        self.goButton.setText("GO!")
        self.label_2.setText("Choose width of target image:")
        self.label.setText("Choose file to transfer into Bricks!")
        self.chooseFileButton.setText("Add file...")

    def change_image(self, file_path):
        if operations.return_image_size(file_path)[0] > 1000 or operations.return_image_size(file_path)[1] > 750:
            pixmap = QtGui.QPixmap(file_path)
            pixmap_scaled = pixmap.scaled(1000, 750, QtCore.Qt.KeepAspectRatio)
            self.photoFrame.setPixmap(pixmap_scaled)
        elif operations.return_image_size(file_path)[0] <= 128:  # needed for after scaled images
            pixmap = QtGui.QPixmap(file_path)
            pixmap_scaled = pixmap.scaled(1000, 750, QtCore.Qt.KeepAspectRatio)
            self.photoFrame.setPixmap(pixmap_scaled)
        else:  # if image is larger than our photo frame size then scaled down
            self.photoFrame.setPixmap(QtGui.QPixmap(file_path))
        config.image_path = file_path

    @staticmethod
    def rotate_image():
        operations.rotate_image(180)

    def open_image(self, file_path):
        operations.open_full_image(image_path=file_path)

    def browse_files(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Add file...', QtCore.QDir.rootPath(),
                                                             "Image files (*.jpg;*.jpeg;*.png;*.gif;*.bmp)")
        config.image_extension = f'.{file_path.split(".", -1)[-1]}'
        config.temp_image_path = file_path
        config.original_image_path = file_path
        if file_path:
            self.change_image(file_path)
            config.temp_image_path = file_path
        config.is_bricked = 0

    def show_popup(self, title, text, type_="NoIcon"):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        if type_ == "info":
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        elif type_ == "warning":
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif type_ == "question":
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            push = msg.exec_()
            if push == 1024:    # checking if pressed OK
                pass
        else:
            msg.setIcon(QMessageBox.NoIcon)
            msg.exec_()

    def resize_image(self, width=1000, height=750):
        pixmap = QtGui.QPixmap(self)
        pixmap_resized = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        pixmap_resized.save(config.temp_image_path)

    def scale_down_image(self):
        if not config.is_bricked:
            operations.scale_image(config.temp_image_path, int(self.comboBox.currentText()))

    def bricking(self, file_path):
        if self.checkBox.isChecked() and not config.is_bricked:
            operations.apply_brick_effect(file_path)
            config.is_bricked = 1

    def save_as(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Image')
        operations.save_photo(source_path=config.temp_image_path, target_path=(file_name + config.image_extension))
