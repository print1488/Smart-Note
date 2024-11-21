from PyQt5.QtWidgets import (
  QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QTextEdit, QLabel, QInputDialog, QMessageBox
)
from PyQt5.QtCore import Qt

app = QApplication([])
app.setStyleSheet('''  QWidget {background-color: #d7eaef}
                       QPushButton {background-color: #ffeaaf}''')

window = QWidget()

window.setFixedSize(800, 600)
window.setWindowTitle("Розумні Замітки")

create_note = QPushButton("Створити замітку")
save_note = QPushButton("Зберегти замітку")
delete_note = QPushButton("Видалити замітку")
create_tag = QPushButton("Створити тег")
delete_tag = QPushButton("Видалити тег")
search_tag = QPushButton("Пошук по тегу")
label_list_notes = QLabel("Список заміток")
label_list_tag = QLabel("Список тегів")
note_list_widget = QListWidget()
tag_list_widget = QListWidget()
line_edit_search_tag = QLineEdit()
text_edit = QTextEdit()

layout1 = QHBoxLayout()
layout1.addWidget(create_note)
layout1.addWidget(save_note)

layout2 = QHBoxLayout()
layout2.addWidget(create_note)
layout2.addWidget(delete_note)

vertical_layout = QVBoxLayout()
vertical_layout.addWidget(label_list_notes)
vertical_layout.addWidget(note_list_widget)
vertical_layout.addLayout(layout1)
vertical_layout.addWidget(delete_note)
vertical_layout.addWidget(label_list_tag)
vertical_layout.addWidget(tag_list_widget)
vertical_layout.addWidget(line_edit_search_tag)
vertical_layout.addLayout(layout2)
vertical_layout.addWidget(search_tag)

main_layout = QHBoxLayout()
main_layout.addWidget(text_edit, stretch=4)
main_layout.addWidget(vertical_layout, stretch=2)

window.setLayout(main_layout)

window.show()
