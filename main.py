from interface import *
from create_json import write_json, read_json

name_file = "data.json"
try:
  data = read_json(name_file)
except:
  data = dict()

def error(text):
  mb = QMessageBox()
  mb.setText(text)
  mb.exec_()

def show_notes():
  note_list_widget.addItems(list(data.keys()))
def show_tags(name_note):
  tag_list_widget.clear()
  tag_list_widget.addItems(data[name_note]["TAG"])

def new_note():
  name_note = QInputDialog().getText(QInputDialog(),
                                     "Введення назви замітки", "Введіть назву замітки")[0]
  data[name_note] = {"TEXT": "", "TAG": []}
  write_json(name_file, data)
  tag_list_widget.addItem(name_tag)
except:
  error("Щоб створити тег, спочатку виберіть замітку.")

def saves_note():
  try:
    name_note = note_list_widget.currentItem().text()
    text = text_edit.toPlainText()
    data[name_note]["TEXT"] = text
    write_json(name_file, data)
  except:
    error("Щоб зберегти, спочатку виберіть замітку")

def drop_note():
  try:
    name_note = note_list_widget.currentItem().text()
    del data[name_note]
    write_json(name_file, data)
    note_list_widget.clear()
    text_edit.setPlainText("")
    show_notes()
  except:
    error("Щоб видалити, спочатку виберіть замітку")

def show_text_note():
    name_note = note_list_widget.currentItem().text()
    text = data[name_note]["TEXT"]
    text_edit.setPlainText(text)
    show_tags(name_note)

def new_tag():
  try:
    name_note = note_list_widget.currentItem().text()
    name_tag = QInputDialog().getText(QInputDialog(),
                                      "Введення назви тега", "Введіть назву тега")[0]
    data[name_note]["TAG"].append(name_tag)
    write_json(name_file, data)
    tag_list_widget.addItem(name_tag)
  except:
    error("Щоб створити тег, спочатку виберіть замітку")


def drop_tag():
  try:
    name_note = note_list_widget.currentItem().text()
    name_tag = tag_list_widget.currentItem.text()
    data[name_note]["TAG"].remove(name_tag)
    write_json(name_file, data)
    tag_list_widget.clear()
    show_tags(name_note)
  except:
    error("Щоб видалити тег, спочатку виберіть замітку, а потім її тег")

def searching_tag():
  pass

create_note.clicked.connect(new_note)
save_note.clicked.connect(saves_note)
delete_note.clicked.connect(drop_note)
delete_tag.clicked.connect(drop_tag)
create_tag.clicked.connect(new_tag)
search_tag.clicked.connect(searching_tag)
note_list_widget.clicked.connect(show_text_note)

show_notes()

app.exec_()
