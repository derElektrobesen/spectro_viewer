from PyQt4.QtGui import *
from PyQt4.QtSql import QSqlQuery
from pr_core import translate
import DB

class AddPatientWindow(QMainWindow, Ui_add_patient_form):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.__prepare_queries()

    def __prepare_queries(self):
        def f(text):
            q = QSqlQuery(DB.con())
            q.prepare(text)
        self.__queries = {
                'add_patient':  f('call add_patient(:lastname, :name, :surname, :card_no, ' +
                    ':birthdate, :eco, :diagnosis, :treatment)'),
                'has_card':     f('select has_card(?)'),
        }

    def __on_empty_field_found(self, name):
        QMessageBox.critical(self, translate("Error", "Ошибка"),
                translate("Incorrect_field", "Поле %s не должно быть пустым" % name))

    @pyqtSlot()
    def on_save_btn_clicked(self):
        this = self.__dict__
        f_names = {
            'name_edt': translate("Name", "Имя"),
            'surname_edt': translate("Surname", "Фамилия"),
            'lastname_edt': translate("Lastname", "Отчество"),
            'card_no_edt': translate("Card_no", "Номер карты"),
        }
        results = {}
        for key in ('name_edt', 'surname_edt', 'lastname_edt', 'card_no_edt'):
            val = this[key].text().strip()
            if len(val) == 0:
                return self.__on_empty_field_found(fnames[key])
            results[key[:-4]] = val

        for key in ('diagnosis_edt', 'treatment_edt'):
            val = this[key].plainText().strip()
            if len(val) > 0:
                results[key[:-4]] = val
            else:
                results[key[:-4]] = ''

        results['birthdate'] = self.birth_date_edt.date()
        results['eco'] = self.eco_count_edt.value()

        q = self.__queries['has_card']
        q.bindValue(0, results['card_no'])
        q.exec_()
        q.next()
        v = q.isNull(0)
        q.finish()
        if not v:
            QMessageBox.critical(self, translate("Error", "Ошибка"),
                    translate("Incorrect_card", "Пациент с указанной картой уже существует в базе"))
            return

        q = self.__queries['add_patient']
        for key, val in results.items():
            q.bindValue(key, val)
        q.exec_()
        q.finish()
