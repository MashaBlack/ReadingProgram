import sys
import pandas as pd
import speech_recognition as sr
from pygame import mixer
import time
import atexit

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QGraphicsDropShadowEffect, \
    QTableWidgetItem, QAbstractItemView, QHeaderView
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont, QPixmap, QColor, QBrush
from PySide6 import QtCore, QtWidgets

from ui.MainWindow import Ui_MainWindow
from ui.Alphabet import Ui_Alphabet
from ui.Syllables import Ui_Syllables
from ui.Reading import Ui_Reading
from ui.Settings import Ui_Settings
from ui.EditForm import Ui_EditForm

# Загрузка данных из файлов --------------------------------------------------------

data = pd.read_csv('words.csv', sep=';')  # слова
progress = pd.read_csv('progress.csv', sep=';')  # прогресс

# Служебные переменные --------------------------------------------------------

letters_up = ("А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О",
              "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я")
syllables = {"u": "у", "o": "о", "a": "а", "e": "э", "y": "ы",
                "yu": "ю", "yo": "ё", "ya": "я", "ye": "е", "i": "и",
             "yyu": "йю", "yyo": "йо", "yya": "йа", "yyya": "йя", "yye": "йе", "yi": "йи", "yy": "й",
             "lu": "лу", "lo": "ло", "la": "ла", "le": "лэ", "ly": "лы", "l": "л",
                "lyu": "лю", "lyo": "лё", "lya": "ля", "lye": "ле", "li": "ли", "l1": "ль",
             "mu": "му", "mo": "мо", "ma": "ма", "me": "мэ", "my": "мы", "m": "м",
                "myu": "мю", "myo": "мё", "mya": "мя", "mye": "ме", "mi": "ми", "m1": "мь",
             "nu": "ну", "no": "но", "na": "на", "ne": "нэ", "ny": "ны", "n": "н", "n2": "нъ",
                "nyu": "ню", "nyo": "нё", "nya": "ня", "nye": "не", "ni": "ни", "n1": "нь",
             "ru": "ру", "ro": "ро", "ra": "ра", "re": "рэ", "ry": "ры", "r": "р", "r2": "ръ",
                "ryu": "рю", "ryo": "рё", "rya": "ря", "rye": "ре", "ri": "ри", "r1": "рь",
             "vu": "ву", "vo": "во", "va": "ва", "ve": "вэ", "vy": "вы", "v": "в", "v2": "въ",
                "vyu": "вю", "vyo": "вё", "vya": "вя", "vye": "ве", "vi": "ви", "v1": "вь",
             "zu": "зу", "zo": "зо", "za": "за", "ze": "зэ", "zy": "зы", "z": "з", "z2": "зъ",
                "zyu": "зю", "zyo": "зё", "zya": "зя", "zye": "зе", "zi": "зи", "z1": "зь",
             "bu": "бу", "bo": "бо", "ba": "ба", "be": "бэ", "by": "бы", "b": "б", "b2": "бъ",
                "byu": "бю", "byo": "бё", "bya": "бя", "bye": "бе", "bi": "би", "b1": "бь",
             "du": "ду", "do": "до", "da": "да", "de": "дэ", "dy": "ды", "d": "д", "d2": "дъ",
                "dyu": "дю", "dyo": "дё", "dya": "дя", "dye": "де", "di": "ди", "d1": "дь",
             "gu": "гу", "go": "го", "ga": "га", "ge": "гэ", "gy": "гы", "g": "г",
                "gyu": "гю", "gyo": "гё", "gya": "гя", "gye": "ге", "gi": "ги", "g1": "гь",
             "zhu": "жу", "zhyo": "жё", "zho": "жо", "zha": "жа", "zhe": "же", "zhi": "жи",
                "zh": "ж", "zh1": "жь", "zh2": "жъ",
             "fu": "фу", "fo": "фо", "fa": "фа", "fe": "фэ", "fy": "фы", "f": "ф",
                "fyu": "фю", "fyo": "фё", "fya": "фя", "fye": "фе", "fi": "фи", "f1": "фь",
             "su": "су", "so": "со", "sa": "са", "se": "сэ", "sy": "сы", "s": "с", "s2": "съ",
                "syu": "сю", "syo": "сё", "sya": "ся", "sye": "се", "si": "си", "s1": "сь",
             "pu": "пу", "po": "по", "pa": "па", "pe": "пэ", "py": "пы", "p": "п",
                "pyu": "пю", "pyo": "пё", "pya": "пя", "pye": "пе", "pi": "пи", "p1": "пь",
             "tu": "ту", "to": "то", "ta": "та", "te": "тэ", "ty": "ты", "t": "т", "t2": "тъ",
                "tyu": "тю", "tyo": "тё", "tya": "тя", "tye": "те", "ti": "ти", "t1": "ть",
             "ku": "ку", "ko": "ко", "ka": "ка", "ke": "кэ", "ky": "кы", "k": "к",
                "kyu": "кю", "kyo": "кё", "kya": "кя", "kye": "ке", "ki": "ки", "k1": "кь",
             "hu": "ху", "ho": "хо", "ha": "ха", "he": "хэ", "hy": "хы", "h": "х", "h2": "хъ",
                "hyu": "хю", "hyo": "хё", "hya": "хя", "hye": "хе", "hi": "хи", "h1": "хь",
             "shu": "шу", "shyo": "шё", "sho": "шо", "sha": "ша", "she": "ше", "shi": "ши",
                "sh": "ш", "sh1": "шь",
             "tsu": "цу", "tso": "цо", "tsa": "ца", "tse": "це", "tsi": "ци", "tsy": "цы", "ts": "ц",
             "chu": "чу", "chyo": "чё", "cho": "чо", "cha": "ча", "che": "че", "chi": "чи", "ch": "ч", "ch1": "чь",
             "shchu": "щу", "shchyo": "щё", "shcho": "що", "shcha": "ща", "shche": "ще", "shchi": "щи",
                "shch": "щ", "shch1": "щь"}
num_of_letter = 0
if progress.at[0, 'word'] == -1:
    num_of_word = 0
    progress_word = -1
else:
    if progress.at[0, 'word'] == len(data.word) - 1:
        num_of_word = progress.at[0, 'word']
    else:
        num_of_word = progress.at[0, 'word'] + 1
    progress_word = progress.at[0, 'word']
is_start = False

# Экземпляры классов окон -----------------------------------------------------

main_window = None
alphabet_window = None
syllables_window = None
reading_window = None
settings_window = None
edit_form = None

class MainWindow(QMainWindow):
    """Основное окно."""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Функционал кнопок
        self.ui.btn_alphabet.clicked.connect(self.show_alphabet)
        self.ui.btn_syllables.clicked.connect(self.show_syllables)
        self.ui.btn_reading.clicked.connect(self.show_reading)
        self.ui.btn_settings.clicked.connect(self.show_settings)

        # Даю элементам интерфейса имена для стилей
        self.ui.btn_alphabet.setObjectName("context-button")
        self.ui.btn_syllables.setObjectName("context-button")
        self.ui.btn_reading.setObjectName("context-button")
        self.ui.btn_about.setObjectName("back-button")
        self.ui.btn_settings.setObjectName("back-button")


    def show_alphabet(self):
        """Запускает окно с алфавитом."""
        global alphabet_window

        alphabet_window = Alphabet()
        alphabet_window.show()
        self.close()

    def show_syllables(self):
        """Запускает окно со складами."""
        global syllables_window

        syllables_window = Syllables()
        syllables_window.show()
        self.close()

    def show_reading(self):
        """Запускает окно со складами."""
        global reading_window

        reading_window = Reading()
        reading_window.show()
        self.close()

    def show_settings(self):
        """Запускает окно со складами."""
        global settings_window

        settings_window = Settings()
        settings_window.show()


class Alphabet(QWidget):
    """Окно с алфавитом."""

    def __init__(self):
        super(Alphabet, self).__init__()

        self.ui = Ui_Alphabet()
        self.ui.setupUi(self)

        # Функционал кнопок
        self.ui.btn_next.clicked.connect(self.show_next_letter)
        self.ui.btn_back.clicked.connect(self.show_previous_letter)
        self.ui.btn_sound.clicked.connect(self.sound_letter)
        self.ui.btn_record.clicked.connect(self.record_sounds)
        self.ui.btn_menu.clicked.connect(self.return_to_menu)

        # Даю элементам интерфейса имена для стилей
        self.ui.letter.setObjectName("letter")
        self.ui.btn_next.setObjectName("arrow")
        self.ui.btn_back.setObjectName("arrow")
        self.ui.btn_sound.setObjectName("context-button")
        self.ui.btn_record.setObjectName("context-button")
        self.ui.btn_menu.setObjectName("back-button")

        global num_of_letter
        self.show_letter()

    def show_letter(self):
        """Отображает буквы в label элементе."""
        global num_of_letter
        if num_of_letter == 0:
            self.ui.btn_back.hide()
        elif num_of_letter == len(letters_up) - 1:
            self.ui.btn_next.hide()
        else:
            self.ui.btn_back.show()
            self.ui.btn_next.show()
        self.ui.letter.setText(letters_up[num_of_letter])

    def show_next_letter(self):
        """Отображает следующую букву алфавита в label элементе."""
        global num_of_letter
        num_of_letter += 1
        self.show_letter()

    def show_previous_letter(self):
        """Отображает предыдущую букву алфавита в label элементе."""
        global num_of_letter
        num_of_letter -= 1
        self.show_letter()

    def sound_letter(self):
        """Отображает следующую букву алфавита в label элементе."""
        global num_of_letter
        path = "audiotapes/letters/letter" + str(num_of_letter) + ".mp3"
        open_tape(path)

    def record_sounds(self):
        """Включает распознавание речи при нажатии на кнопку."""
        global num_of_letter
        text = record_volume()
        if text == letters_up[num_of_letter].lower():
            open_tape("audiotapes/sounds/right_answer.mp3")
        else:
            open_tape("audiotapes/sounds/wrong_answer.mp3")

    def return_to_menu(self):
        """Возвращение в главное меню."""
        global main_window
        main_window = MainWindow()
        main_window.show()
        self.close()


class Syllables(QWidget):
    """Окно со складами."""

    def __init__(self):
        super(Syllables, self).__init__()

        self.ui = Ui_Syllables()
        self.ui.setupUi(self)

        # Функционал кнопок
        self.ui.btn_menu.clicked.connect(self.return_to_menu)
        self.ui.all_syllables.buttonClicked.connect(self.sound_syllable)

        # Даю элементам интерфейса имена для стилей
        self.ui.btn_menu.setObjectName("back-button")

    def return_to_menu(self):
        """Возвращение в главное меню."""
        global main_window
        main_window = MainWindow()
        main_window.show()
        self.close()

    def sound_syllable(self, button):
        """Озвучивает склад при нажатии на него."""
        path = "audiotapes/syllables/" + button.objectName()[4:] + ".mp3"
        open_tape(path)


class Reading(QWidget):
    """Окно с чтением."""

    def __init__(self):
        super(Reading, self).__init__()

        self.ui = Ui_Reading()
        self.ui.setupUi(self)

        # Функционал кнопок
        self.ui.btn_record.clicked.connect(self.record_sounds)
        self.ui.btn_menu.clicked.connect(self.return_to_menu)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_divide.clicked.connect(self.divide_word)
        self.ui.btn_next.clicked.connect(self.next_word)
        self.ui.btn_back.clicked.connect(self.previous_word)

        # Даю элементам интерфейса имена для стилей
        self.ui.btn_next.setObjectName("back-button")
        self.ui.btn_back.setObjectName("back-button")
        self.ui.btn_record.setObjectName("context-button")
        self.ui.btn_divide.setObjectName("context-button")
        self.ui.btn_menu.setObjectName("back-button")
        self.ui.btn_start.setObjectName("context-button")

        # Накладываю эффект тени на изображение
        self.effect = QGraphicsDropShadowEffect(self)
        self.effect.setColor(QColor(0x99, 0x99, 0x99))
        self.effect.setBlurRadius(30)
        self.effect.setXOffset(2)
        self.effect.setYOffset(2)
        self.ui.image.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)

        # Скрываю кнопки и другие элементы
        self.ui.btn_next.hide()
        self.ui.btn_back.hide()
        self.ui.btn_divide.hide()
        self.ui.btn_record.hide()
        self.ui.image.hide()


    def show_word(self):
        """Добавляет слово в layout."""
        word = WordLabel()
        word.setText(data.word[num_of_word].upper())
        self.ui.layout_word.insertWidget(1, word)
        if num_of_word <= progress_word != -1:
            self.ui.image.setPixmap(QPixmap(u"images/words/" + data.file[num_of_word]))
            self.effect.setEnabled(True)
            if num_of_word < len(data.word) - 1:
                self.ui.btn_next.show()
        else:
            self.ui.image.setPixmap(QPixmap(u"images/words/question-mark.png"))
            self.effect.setEnabled(False)
            self.ui.btn_next.hide()
        if num_of_word == 0:
            self.ui.btn_back.hide()
        else:
            self.ui.btn_back.show()

    def start(self):
        """Удаляет стартовую кнопку из layout, добавляет в него слово и отображает кнопки."""
        global is_start
        is_start = True
        self.clear_layout()
        self.show_word()
        self.ui.btn_divide.show()
        self.ui.btn_record.show()
        self.ui.image.show()

    def clear_layout(self):
        """Удаляет все виджеты из layout (кроме spacers)."""
        for i in range(1, self.ui.layout_word.count() - 1):
            self.ui.layout_word.itemAt(i).widget().deleteLater()

    def divide_word(self):
        self.clear_layout()
        syl = divide_into_syllables(data.word[num_of_word])
        for i in range(len(syl)):
            button = SyllableButton(find_button_name(syl[i]), is_big(syl[i]))
            self.ui.layout_word.insertWidget(i + 1, button)
        self.ui.btn_divide.hide()


    def next_word(self):
        """Отображает следующее слово."""
        global num_of_word
        num_of_word += 1
        self.clear_layout()
        self.show_word()
        self.ui.btn_divide.show()

    def previous_word(self):
        """Отображает предыдущее слово."""
        global num_of_word
        num_of_word -= 1
        self.clear_layout()
        self.show_word()
        self.ui.btn_divide.show()

    def if_right_answer(self):
        global progress_word
        self.ui.image.setPixmap(QPixmap(u"images/words/" + data.file[num_of_word]))
        self.effect.setEnabled(True)
        if num_of_word < len(data.word) - 1:
            self.ui.btn_next.show()
        if progress_word < num_of_word:
            progress_word = num_of_word

    def record_sounds(self):
        """Включает распознавание речи при нажатии на кнопку."""
        text = record_volume()
        if text == data.word[num_of_word]:
            open_tape("audiotapes/sounds/right_answer.mp3")
            self.if_right_answer()
        else:
            open_tape("audiotapes/sounds/wrong_answer.mp3")

    def keyPressEvent(self, event):
        """Обрабатывает событие – нажатие на клавишу."""
        if is_start:
            if event.key() == QtCore.Qt.Key_Q:
                self.if_right_answer()
            elif event.key() == QtCore.Qt.Key_Left and num_of_word != 0:
                self.previous_word()
            elif event.key() == QtCore.Qt.Key_Right and num_of_word != len(data.word) - 1 and \
                    num_of_word <= progress_word != -1:
                self.next_word()
            event.accept()

    def return_to_menu(self):
        """Возвращение в главное меню."""
        global main_window
        main_window = MainWindow()
        main_window.show()
        self.close()

class Settings(QWidget):
    """Окно с настройками."""

    def __init__(self):
        super(Settings, self).__init__()

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        # Функционал кнопок
        self.ui.btn_add.clicked.connect(self.add_new_word)
        # self.ui.btn_back.clicked.connect(self.show_previous_letter)

        # Даю элементам интерфейса имена для стилей
        self.ui.btn_add.setObjectName("context-button")
        self.ui.btn_clear.setObjectName("context-button")
        # self.ui.wordsTable.setObjectName("context-button")

        self.ui.wordsTable.setRowCount(len(data["word"]))
        for i in range(len(data["word"])):
            item = QTableWidgetItem(data.word[i])
            item.setForeground(QBrush(QColor(0, 0, 0)))
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item2 = QTableWidgetItem("Редактировать")
            item2.setForeground(QBrush(QColor(23, 114, 69)))
            item2.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item3 = QTableWidgetItem("Удалить")
            item3.setForeground(QBrush(QColor(255, 0, 0)))
            item3.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.ui.wordsTable.setItem(i, 0, item)
            self.ui.wordsTable.setItem(i, 1, item2)
            self.ui.wordsTable.setItem(i, 2, item3)
        self.ui.wordsTable.horizontalHeader().hide()
        self.ui.wordsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.wordsTable.resizeColumnToContents(2)
        self.ui.wordsTable.resizeColumnToContents(3)

    def add_new_word(self):
        """Запускает окно для добавления."""
        global edit_form
        edit_form = Edit()
        edit_form.show()
        edit_form.ui.image.setPixmap(QPixmap(u"images/words/default.png"))
        edit_form.ui.lineEdit.setPlaceholderText("Введите слово")


class Edit(QWidget):
    """Окно с настройками."""

    def __init__(self):
        super(Edit, self).__init__()

        self.ui = Ui_EditForm()
        self.ui.setupUi(self)

        # Функционал кнопок
        # self.ui.btn_add.clicked.connect(self.add_new_word)
        # self.ui.btn_back.clicked.connect(self.show_previous_letter)

        # Даю элементам интерфейса имена для стилей
        self.ui.btn_save.setObjectName("context-button")

        # Накладываю эффект тени на изображение
        self.effect = QGraphicsDropShadowEffect(self)
        self.effect.setColor(QColor(0x99, 0x99, 0x99))
        self.effect.setBlurRadius(30)
        self.effect.setXOffset(2)
        self.effect.setYOffset(2)
        self.ui.image.setGraphicsEffect(self.effect)
        self.ui.lineEdit.setGraphicsEffect(self.effect)
        # self.effect.setEnabled(False)

def open_tape(path):
    """Открывает файл с необходимой записью и проигрывает его."""
    # Инициализируем звуковое устройство
    mixer.init()

    # Проигрываем mp3 файл c нужной записью
    mixer.music.load(path)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)

def record_volume():
    """Распознаёт речь и возвращает её в виде текста."""
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        r.adjust_for_ambient_noise(source, duration=0.5) # настройка посторонних шумов
        open_tape("audiotapes/sounds/start_listen.mp3")
        audio = r.listen(source)
    open_tape("audiotapes/sounds/stop_listen.mp3")
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        return text
    except:
        return "error"

def divide_into_syllables(word):
    """Делит слово на склады и возвращает их в виде списка."""
    consonants = {'й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п',
                  'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б'}
    word_syllables = []
    num = 0
    while num < len(word):
        if word[num] in consonants:
            if (num == len(word) - 1) or (word[num + 1] in consonants):
                word_syllables.append(word[num])
                num += 1
            else:
                word_syllables.append(word[num:num + 2])
                num += 2
        else:
            word_syllables.append(word[num])
            num += 1

    return word_syllables

def find_button_name(sound):
    """Находит имя кнопки-склада."""
    for syl in syllables:
        if syllables[syl] == sound:
            return syl

def is_big(syl):
    """Проверяет, является ли склад большим (из таблицы Зайцева)."""
    if ('ж' in syl) or ('ш' in syl) or ('ц' in syl):
        return True
    elif ('й' in syl) or ('ч' in syl) or ('щ' in syl):
        return False
    elif ('ю' in syl) or ('ё' in syl) or ('я' in syl) or ('е' in syl) or ('и' in syl) or ('ь' in syl):
        return False
    else:
        return True

class ImgWidget(QLabel):

    def __init__(self, path):
        super(ImgWidget, self).__init__()
        pic = QPixmap(path)
        self.setPixmap(pic)
        self.setScaledContents(True)

class WordLabel(QLabel):
    """Класс слова."""
    def __init__(self):
        super(WordLabel, self).__init__()

        self.setObjectName("word")
        font = QFont()
        font.setFamilies([u"Helvetica"])
        font.setPointSize(70)
        font.setBold(False)
        self.setFont(font)

class SyllableButton(QPushButton):
    """Класс кнопки-склада."""
    def __init__(self, name, isBig):
        super(SyllableButton, self).__init__()

        self.clicked.connect(self.sound_syllable)

        self.setObjectName("syl_" + name)
        if isBig:
            self.setMinimumSize(QSize(80, 80))
            self.setMaximumSize(QSize(80, 80))
        else:
            self.setMinimumSize(QSize(60, 60))
            self.setMaximumSize(QSize(60, 60))
        self.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u"images/syllables/" + name +".png", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon)
        if isBig:
            self.setIconSize(QSize(80, 80))
        else:
            self.setIconSize(QSize(60, 60))
        self.setAutoRepeat(False)


    def sound_syllable(self):
        """Озвучивает склад при нажатии на него."""
        path = "audiotapes/syllables/" + self.objectName()[4:] + ".mp3"
        open_tape(path)

def closeHandler():
    """Сохраняет прогресс в файл."""
    progress.at[0, 'word'] = progress_word
    progress.to_csv('progress.csv', sep=';', encoding='utf-8', index=False)

# НАЧАЛО ПРОГРАММЫ
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # main_window = MainWindow()
    # main_window.show()
    settings_window = Settings()
    settings_window.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    atexit.register(closeHandler)
    sys.exit(app.exec())
