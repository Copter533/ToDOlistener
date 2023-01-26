import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QEasingCurve, QPropertyAnimation, QPoint, QSize
from PyQt5.QtGui import QCursor, QTransform, QPixmap, QColor, QPainter, QIcon
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QApplication, QGroupBox, QVBoxLayout, QFrame, \
    QSizePolicy, QHBoxLayout, QAction, QMenu, QStyle


class ComplexWidget(QWidget):
    def __init__(self, old_column):
        super().__init__()

        print("SUPER")

        # Create a black rect widget
        rect = QFrame()
        rect.setAutoFillBackground(False)
        rect.setStyleSheet("background-color: #cec4c8; padding: 10px 20px; border-radius: 5px;")
        rect.setMaximumWidth(600)
        rect.setMinimumSize(300, 100)

        # Create the context menu
        context_menu = QMenu(rect)

        # Create actions for the context menu
        action1 = QAction("Action 1", rect)
        action2 = QAction("Action 2", rect)

        # Add the actions to the context menu
        context_menu.addAction(action1)
        context_menu.addAction(action2)

        # Set the context menu policy
        rect.setContextMenuPolicy(Qt.ActionsContextMenu)

        # Connect the context menu request signal to a function
        rect.customContextMenuRequested.connect(lambda: context_menu.exec_(QCursor.pos()))

        upper_frame = QFrame()
        lower_frame = QFrame()

        main_layout = QVBoxLayout()
        upper_layout = QHBoxLayout()
        lower_layout = QGridLayout()

        title = QLabel("There is some desc for the task,\nit includes a meaning of task, additional info and e.t.c.")
        title.setWordWrap(True)
        label3 = QLabel("LABEL 3")

        self.del_button = QPushButton()
        self.del_button.setIcon(QIcon("icons/tile_buttons/trash.svg"))
        self.next_button = QPushButton()
        self.next_button.setIcon(QIcon("icons/tile_buttons/arrows/next.svg"))
        self.prev_button = QPushButton()
        self.prev_button.setIcon(QIcon("icons/tile_buttons/arrows/prev.svg"))

        ico_size = 40
        self.next_button.setIconSize(QSize(ico_size, ico_size))
        self.prev_button.setIconSize(QSize(ico_size, ico_size))
        self.del_button.setIconSize(QSize(ico_size, ico_size))

        # self.next_button.setStyleSheet("background-color: darkred; border-radius: 3px;")
        # self.prev_button.setStyleSheet("background-color: red; border-radius: 3px;")
        lower_layout.addWidget(self.prev_button, 0, 0, alignment=Qt.AlignLeft)
        lower_layout.addWidget(self.next_button, 0, 2, alignment=Qt.AlignRight)

        upper_layout.addWidget(title)
        upper_layout.addWidget(self.del_button)

        upper_frame.setMinimumHeight(70)
        upper_frame.setMaximumHeight(200)
        upper_frame.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        upper_frame.setStyleSheet("background-color: #559911; border-radius: 3px;")
        upper_frame.setLayout(upper_layout)

        lower_frame.setFixedHeight(50)
        lower_frame.setStyleSheet("background-color: #ffffff; border-radius: 3px;")
        lower_layout.setContentsMargins(0,0,0,0)
        lower_frame.setContentsMargins(0, 0, 0, 0)
        lower_frame.setLayout(lower_layout)

        print("OK")

        main_layout.addWidget(upper_frame)
        main_layout.addWidget(label3)
        main_layout.addWidget(lower_frame)
        # main_layout.addWidget(lower_frame)

        # # Create the grid layout
        # grid = QGridLayout()
        #
        # # Create the label and button widgets
        # label = QLabel("Title")
        # desc = QLabel("There is some desc for the task,\nit includes a meaning of task, additional info and e.t.c.")
        # label.setStyleSheet("color: white; font-size: 20px")
        # desc.setStyleSheet("color: white; font-size: 17px")
        #
        # desc.setWordWrap(True)
        # desc.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # self.proceed_button = QPushButton("->")
        # self.proceed_button.setStyleSheet("color: green; font-size: 20px; border: red 2px;"
        #                                   "background-color: #3C4A4A;")
        # label.setStyleSheet("color: white; font-size: 20px; border: red 2px; background-color: #3C4A4A;")
        # label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # # Add the label and button to the grid layout
        # grid.addWidget(label, 0, 0)
        # grid.addWidget(desc, 1, 0)
        # grid.addWidget(self.proceed_button, 2, 0)
        # grid.setColumnStretch(0, 100)

        # Create the parent layout
        parent_layout = QVBoxLayout()

        # Add the grid layout to the rect widget
        rect.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        rect.setLayout(main_layout)

        # Add the rect widget to the parent layout
        parent_layout.addWidget(rect)
        rect.setContentsMargins(0, 0, 0, 0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        rect.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        # Assign the parent layout to the parent widget
        self.setLayout(parent_layout)


class RoundedRectWidget(QWidget):
    def __init__(self, title: str, desc: str, reward: str = None, parent=None):
        super().__init__(parent)
        self.setMaximumSize(600, 400)

        # Title
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Description
        self.desc_label = QLabel(desc)
        self.desc_label.setStyleSheet("color: white; background-color: transparent; padding: 10px;")

        # Reward
        self.reward_label = QLabel(reward) if reward else None
        if self.reward_label:
            self.reward_label.setStyleSheet("color: white; background-color: transparent; padding: 10px;")
            # Button
        self.button = QPushButton("=>")
        self.button.setFixedWidth(50)

        # Icons
        self.icon1 = QLabel()
        self.icon1.setPixmap(QtGui.QPixmap("path/to/icon1.png"))
        self.icon2 = QLabel()
        self.icon2.setPixmap(QtGui.QPixmap("path/to/icon2.png"))

        # Main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Title layout
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.icon1)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.icon2)
        self.title_layout.addWidget(self.button)
        self.title_layout.addStretch()

        # Main layout
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.desc_label)
        if self.reward_label:
            self.main_layout.addWidget(self.reward_label)
        self.setLayout(self.main_layout)

        # Stylesheet
        self.setStyleSheet("""
                    QWidget {
                        background-color: #2d2d2d;
                        border-radius: 10px;
                    }
                """)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout(self)
        self.label1 = ComplexWidget(0)
        self.label2 = ComplexWidget(1)
        self.label3 = ComplexWidget(2)

        pixmap = QPixmap("icons/gui/move_cursor.svg")
        pixmap = pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Create a painter for the pixmap
        painter = QPainter(pixmap)

        # Apply color effect to cursor image
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor(255, 0, 0))
        painter.end()

        transform = QTransform()
        transform.rotate(270)

        cursor = QCursor(pixmap.transformed(transform))

        self.label1.next_button.setCursor(cursor)
        #
        self.label1.next_button.clicked.connect(self.on_button_clicked)

        # Create a label to display the current column number
        self.column_label = QLabel("Column: 1", self)
        self.column_label.setAlignment(Qt.AlignCenter)

        self.setWindowTitle("Columns Example")
        self.create_layout()
        self.resize(500, 250)

        self.animation = QPropertyAnimation(self.label1, b"geometry")
        self.animation.setDuration(300)  # 1 second
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        self.show()

    def create_layout(self):
        self.main_layout.addWidget(self.column_label, 0, 1)
        self.main_layout.addWidget(self.label1, 1, 0)
        self.main_layout.addWidget(self.label2, 1, 1)
        self.main_layout.addWidget(self.label3, 1, 2)

        self.main_layout.setColumnMinimumWidth(0, 200)
        self.main_layout.setColumnMinimumWidth(1, 200)
        self.main_layout.setColumnMinimumWidth(2, 200)

        self.setLayout(self.main_layout)

    def on_button_clicked(self):
        self.animation.setStartValue(self.label1.geometry())
        old_column = self.label1.old_column
        new_column = (old_column + 1) % self.main_layout.columnCount()
        self.main_layout.removeWidget(self.label1)
        self.label1.old_column = new_column

        new_row = 0
        while self.main_layout.itemAtPosition(new_row, new_column) is not None:
            new_row += 1
        self.main_layout.addWidget(self.label1, new_row, new_column)
        self.main_layout.update()
        new_widget = self.main_layout.itemAtPosition(new_row, new_column).widget()

        # Update the column label to display the new column number
        self.column_label.setText(f"Column: {new_column + 1}")
        new_widget.updateGeometry()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.after_click)

        self.timer.start(1000)

    def after_click(self):
        print("timeouted")
        self.timer.stop()
        geo2 = self.label1.geometry()
        self.animation.setEndValue(geo2)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
