=begin
** Form generated from reading ui file 'add_patient_form.ui'
**
** Created:   29 16:04:05 2013
**      by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
=end

require 'Qt4'

class Ui_Add_patient_form
    attr_reader :verticalLayout
    attr_reader :gridLayout
    attr_reader :label
    attr_reader :label_6
    attr_reader :label_7
    attr_reader :label_5
    attr_reader :label_4
    attr_reader :name_edt
    attr_reader :last_name_edt
    attr_reader :label_3
    attr_reader :surname_edt
    attr_reader :card_no_edt
    attr_reader :birth_date_edt
    attr_reader :eco_count_edt
    attr_reader :label_2
    attr_reader :diagnosis_edt
    attr_reader :label_8
    attr_reader :treatment_edt
    attr_reader :horizontalLayout
    attr_reader :horizontalSpacer
    attr_reader :save_btn
    attr_reader :close_btn

    def setupUi(add_patient_form)
    if add_patient_form.objectName.nil?
        add_patient_form.objectName = "add_patient_form"
    end
    add_patient_form.resize(640, 480)
    @verticalLayout = Qt::VBoxLayout.new(add_patient_form)
    @verticalLayout.objectName = "verticalLayout"
    @gridLayout = Qt::GridLayout.new()
    @gridLayout.objectName = "gridLayout"
    @label = Qt::Label.new(add_patient_form)
    @label.objectName = "label"

    @gridLayout.addWidget(@label, 2, 0, 1, 1)

    @label_6 = Qt::Label.new(add_patient_form)
    @label_6.objectName = "label_6"

    @gridLayout.addWidget(@label_6, 1, 2, 1, 1)

    @label_7 = Qt::Label.new(add_patient_form)
    @label_7.objectName = "label_7"

    @gridLayout.addWidget(@label_7, 2, 2, 1, 1)

    @label_5 = Qt::Label.new(add_patient_form)
    @label_5.objectName = "label_5"

    @gridLayout.addWidget(@label_5, 0, 2, 1, 1)

    @label_4 = Qt::Label.new(add_patient_form)
    @label_4.objectName = "label_4"

    @gridLayout.addWidget(@label_4, 0, 0, 1, 1)

    @name_edt = Qt::LineEdit.new(add_patient_form)
    @name_edt.objectName = "name_edt"

    @gridLayout.addWidget(@name_edt, 0, 1, 1, 1)

    @last_name_edt = Qt::LineEdit.new(add_patient_form)
    @last_name_edt.objectName = "last_name_edt"

    @gridLayout.addWidget(@last_name_edt, 2, 1, 1, 1)

    @label_3 = Qt::Label.new(add_patient_form)
    @label_3.objectName = "label_3"

    @gridLayout.addWidget(@label_3, 1, 0, 1, 1)

    @surname_edt = Qt::LineEdit.new(add_patient_form)
    @surname_edt.objectName = "surname_edt"

    @gridLayout.addWidget(@surname_edt, 1, 1, 1, 1)

    @card_no_edt = Qt::LineEdit.new(add_patient_form)
    @card_no_edt.objectName = "card_no_edt"

    @gridLayout.addWidget(@card_no_edt, 1, 3, 1, 1)

    @birth_date_edt = Qt::DateEdit.new(add_patient_form)
    @birth_date_edt.objectName = "birth_date_edt"
    @birth_date_edt.minimumDate = Qt::Date.new(1752, 9, 14)

    @gridLayout.addWidget(@birth_date_edt, 0, 3, 1, 1)

    @eco_count_edt = Qt::SpinBox.new(add_patient_form)
    @eco_count_edt.objectName = "eco_count_edt"

    @gridLayout.addWidget(@eco_count_edt, 2, 3, 1, 1)


    @verticalLayout.addLayout(@gridLayout)

    @label_2 = Qt::Label.new(add_patient_form)
    @label_2.objectName = "label_2"

    @verticalLayout.addWidget(@label_2)

    @diagnosis_edt = Qt::PlainTextEdit.new(add_patient_form)
    @diagnosis_edt.objectName = "diagnosis_edt"

    @verticalLayout.addWidget(@diagnosis_edt)

    @label_8 = Qt::Label.new(add_patient_form)
    @label_8.objectName = "label_8"

    @verticalLayout.addWidget(@label_8)

    @treatment_edt = Qt::PlainTextEdit.new(add_patient_form)
    @treatment_edt.objectName = "treatment_edt"

    @verticalLayout.addWidget(@treatment_edt)

    @horizontalLayout = Qt::HBoxLayout.new()
    @horizontalLayout.objectName = "horizontalLayout"
    @horizontalSpacer = Qt::SpacerItem.new(40, 20, Qt::SizePolicy::Expanding, Qt::SizePolicy::Minimum)

    @horizontalLayout.addItem(@horizontalSpacer)

    @save_btn = Qt::PushButton.new(add_patient_form)
    @save_btn.objectName = "save_btn"

    @horizontalLayout.addWidget(@save_btn)

    @close_btn = Qt::PushButton.new(add_patient_form)
    @close_btn.objectName = "close_btn"

    @horizontalLayout.addWidget(@close_btn)


    @verticalLayout.addLayout(@horizontalLayout)

    Qt::Widget.setTabOrder(@name_edt, @surname_edt)
    Qt::Widget.setTabOrder(@surname_edt, @last_name_edt)
    Qt::Widget.setTabOrder(@last_name_edt, @birth_date_edt)
    Qt::Widget.setTabOrder(@birth_date_edt, @card_no_edt)
    Qt::Widget.setTabOrder(@card_no_edt, @eco_count_edt)
    Qt::Widget.setTabOrder(@eco_count_edt, @diagnosis_edt)
    Qt::Widget.setTabOrder(@diagnosis_edt, @treatment_edt)
    Qt::Widget.setTabOrder(@treatment_edt, @save_btn)
    Qt::Widget.setTabOrder(@save_btn, @close_btn)

    retranslateUi(add_patient_form)
    Qt::Object.connect(@close_btn, SIGNAL('clicked()'), add_patient_form, SLOT('close()'))

    Qt::MetaObject.connectSlotsByName(add_patient_form)
    end # setupUi

    def setup_ui(add_patient_form)
        setupUi(add_patient_form)
    end

    def retranslateUi(add_patient_form)
    add_patient_form.windowTitle = Qt::Application.translate("add_patient_form", "\320\224\320\276\320\261\320\260\320\262\320\270\321\202\321\214 \320\277\320\260\321\206\320\270\320\265\320\275\321\202\320\260", nil, Qt::Application::UnicodeUTF8)
    @label.text = Qt::Application.translate("add_patient_form", "\320\236\321\202\321\207\320\265\321\201\321\202\320\262\320\276:", nil, Qt::Application::UnicodeUTF8)
    @label_6.text = Qt::Application.translate("add_patient_form", "\320\235\320\276\320\274\320\265\321\200 \320\272\320\260\321\200\321\202\321\213:", nil, Qt::Application::UnicodeUTF8)
    @label_7.text = Qt::Application.translate("add_patient_form", "\320\247\320\270\321\201\320\273\320\276 \320\255\320\232\320\236:", nil, Qt::Application::UnicodeUTF8)
    @label_5.text = Qt::Application.translate("add_patient_form", "\320\224\320\260\321\202\320\260 \321\200\320\276\320\266\320\264\320\265\320\275\320\270\321\217:", nil, Qt::Application::UnicodeUTF8)
    @label_4.text = Qt::Application.translate("add_patient_form", "\320\230\320\274\321\217:", nil, Qt::Application::UnicodeUTF8)
    @label_3.text = Qt::Application.translate("add_patient_form", "\320\244\320\260\320\274\320\270\320\273\320\270\321\217:", nil, Qt::Application::UnicodeUTF8)
    @birth_date_edt.displayFormat = Qt::Application.translate("add_patient_form", "dd.MM.yyyy", nil, Qt::Application::UnicodeUTF8)
    @label_2.text = Qt::Application.translate("add_patient_form", "\320\224\320\270\320\260\320\263\320\275\320\276\320\267:", nil, Qt::Application::UnicodeUTF8)
    @label_8.text = Qt::Application.translate("add_patient_form", "\320\237\321\200\320\265\320\264\321\210\320\265\321\201\321\202\320\262\321\203\321\216\321\211\320\265\320\265 \320\273\320\265\321\207\320\265\320\275\320\270\320\265:", nil, Qt::Application::UnicodeUTF8)
    @save_btn.text = Qt::Application.translate("add_patient_form", "\320\241\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", nil, Qt::Application::UnicodeUTF8)
    @close_btn.text = Qt::Application.translate("add_patient_form", "\320\236\321\202\320\274\320\265\320\275\320\260", nil, Qt::Application::UnicodeUTF8)
    end # retranslateUi

    def retranslate_ui(add_patient_form)
        retranslateUi(add_patient_form)
    end

end

module Ui
    class Add_patient_form < Ui_Add_patient_form
    end
end  # module Ui

if $0 == __FILE__
    a = Qt::Application.new(ARGV)
    u = Ui_Add_patient_form.new
    w = Qt::Widget.new
    u.setupUi(w)
    w.show
    a.exec
end
