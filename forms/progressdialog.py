from PyQt4.QtGui import *
from PyQt4.QtCore import *
from .progress_dialog import Ui_import_progres_dialog as UI_Dialog

import os.path
from db import DB, SqlException
from pr_core import translate

class ProgressDialog(QMainWindow, UI_Dialog):
    ModeExport = 0
    ModeImport = 1

    def __init__(self, parent = None, mode = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.__mode = mode

    def __show_error(self, text):
        QMessageBox.information(self, translate('Error', 'Ошибка'), text)

    def __set_prb_text(self, text):
        self.progressBar.setFormat(text + ' %p%')

    def __inc_prb_val(self, inc = 10):
        self.progressBar.setValue(self.progressBar.value() + inc)

    def on_action_came(self, **kwargs):
        print(kwargs)
        if 'status' in kwargs:
            st = kwargs['status']
            if st == SqlException.StatusGraphsImporting:
                self.__set_prb_text(translate('Graphs importing', 'Импорт спектров'))
                if 'count' in kwargs and kwargs['count'] != 0:
                    self.__inc_prb_val((100 - self.progressBar.value()) * kwargs['i'] / kwargs['count'])
                else:
                    self.__inc_prb_val((100 - self.progressBar.value()) / 10)
            else:
                self.__inc_prb_val()
                if st == SqlException.StatusDecrypting or st == SqlException.StatusEncypting:
                    self.__set_prb_text(translate('Crypting', 'Шифрование'))
                elif st == SqlException.StatusNamesPreparing:
                    self.__set_prb_text(translate('Names preparing', 'Подготовка пациентов'))
        elif 'err_code' in kwargs and kwargs['err_code'] == SqlException.ErrcodeDuplicateName:
            return kwargs['name_1']     # TODO
                

    @pyqtSlot()
    def on_open_file_btn_clicked(self):
        name = ''
        if self.__mode == ProgressDialog.ModeExport:
            name = QFileDialog.getSaveFileName(self, translate('Save', 'Сохранить файл'),
                    filter = translate('Filter', 'Файл БД (*.spv)'))
            if name[-4:] != '.spv':
                name += '.spv'
        elif self.__mode == ProgressDialog.ModeImport:
            name = QFileDialog.getOpenFileName(self, translate('Open', 'Открыть файл'),
                    filter = translate('Filter', 'Файл БД (*.spv)'))
        self.file_path_edt.setText(name)

    @pyqtSlot()
    def on_cancel_btn_clicked(self):
        self.close()

    @pyqtSlot()
    def on_ok_btn_clicked(self):
        if self.__mode == ProgressDialog.ModeImport and not os.path.isfile(self.file_path_edt.text()):
            self.__show_error(translate('File not found', 'Файл не найден'))
            return

        if not len(self.passw_edt.text()):
            self.__show_error(translate('Input password', 'Необходимо ввести пароль для продолжения'))
            return

        if self.passw_edt.text() != self.passw_1_edt.text():
            self.__show_error(translate('Incorrect passwords', 'Пароли не совподают'))
            return

        self.ok_btn.setEnabled(False)
        self.file_path_edt.setEnabled(False)
        self.passw_edt.setEnabled(False)
        self.passw_1_edt.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.progressBar.setValue(0)
        self.__set_prb_text(translate('Preparing', 'Подготовка'))

        try:
            if self.__mode == ProgressDialog.ModeExport:
                DB.export_db(self.file_path_edt.text(), self.passw_edt.text(), self.on_action_came)
            elif self.__mode == ProgressDialog.ModeImport:
                DB.import_db(self.file_path_edt.text(), self.passw_edt.text(), self.on_action_came)
            self.__set_prb_text(translate('Finished', 'Завершено'))
            self.progressBar.setValue(100)
        except SqlException as e:
            code = e.errcode()
            if code == SqlException.ErrcodeNoFile:
                self.__show_error(translate('File not found', 'Файл не найден'))
            elif code == SqlException.ErrcodeNoData:
                self.__show_error(translate('No data', 'Данный не обнаружено'))
            elif code == SqlException.ErrcodeIncorrectFormat or code == SqlException.ErrcodeDecryptFail:
                self.__show_error(translate('Format error', 'Произошла ошибка при попытке имопорта'))
            self.__set_prb_text(translate('Error', 'Ошибка'))
            self.progressBar.setValue(0)

        self.ok_btn.setEnabled(True)
        self.file_path_edt.setEnabled(True)
        self.passw_edt.setEnabled(True)
        self.passw_1_edt.setEnabled(True)
        self.cancel_btn.setEnabled(True)
