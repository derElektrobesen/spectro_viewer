=begin
** Form generated from reading ui file 'client_widget.ui'
**
** Created:   29 16:04:05 2013
**      by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
=end

require 'measurewidget'
require 'measurewidget'
require 'Qt4'

class Ui_Patient_widget
    attr_reader :horizontalLayout
    attr_reader :info_frame
    attr_reader :verticalLayout_2
    attr_reader :frame_2
    attr_reader :verticalLayout_3
    attr_reader :gridWidget
    attr_reader :gridLayout
    attr_reader :label_3
    attr_reader :label_4
    attr_reader :diagnosis_lbl
    attr_reader :incomes_lbl
    attr_reader :label_2
    attr_reader :name_lbl
    attr_reader :label
    attr_reader :age_lbl
    attr_reader :results_btn
    attr_reader :points_sca
    attr_reader :scrollAreaWidget
    attr_reader :verticalLayout_12
    attr_reader :horizontalLayout_4
    attr_reader :last_btn
    attr_reader :remove_btn
    attr_reader :measuref_frame
    attr_reader :verticalLayout
    attr_reader :frame
    attr_reader :horizontalLayout_2
    attr_reader :tabWidget
    attr_reader :tab
    attr_reader :verticalLayout_4
    attr_reader :label_11
    attr_reader :blue_sp_w
    attr_reader :tab_2
    attr_reader :verticalLayout_5
    attr_reader :label_12
    attr_reader :red_sp_w
    attr_reader :tab_5
    attr_reader :verticalLayout_6
    attr_reader :label_13
    attr_reader :original_blue_sp_w
    attr_reader :tab_6
    attr_reader :verticalLayout_11
    attr_reader :label_18
    attr_reader :original_red_sp_w
    attr_reader :colors_frame
    attr_reader :horizontalLayout_5
    attr_reader :gridLayout_2
    attr_reader :widget
    attr_reader :label_9
    attr_reader :verticalSpacer
    attr_reader :label_10
    attr_reader :widget_2
    attr_reader :frame_3
    attr_reader :horizontalLayout_3
    attr_reader :tabWidget_2
    attr_reader :tab_3
    attr_reader :verticalLayout_9
    attr_reader :label_16
    attr_reader :differentiated_blue_sp_w
    attr_reader :tab_4
    attr_reader :verticalLayout_10
    attr_reader :label_17
    attr_reader :differentiated_red_sp_w
    attr_reader :tab_7
    attr_reader :verticalLayout_8
    attr_reader :label_15
    attr_reader :intact_blue_sp_w
    attr_reader :tab_8
    attr_reader :verticalLayout_7
    attr_reader :label_14
    attr_reader :intact_red_sp_w

    def setupUi(patient_widget)
    if patient_widget.objectName.nil?
        patient_widget.objectName = "patient_widget"
    end
    patient_widget.resize(909, 480)
    @horizontalLayout = Qt::HBoxLayout.new(patient_widget)
    @horizontalLayout.objectName = "horizontalLayout"
    @info_frame = Qt::Frame.new(patient_widget)
    @info_frame.objectName = "info_frame"
    @info_frame.minimumSize = Qt::Size.new(200, 0)
    @info_frame.maximumSize = Qt::Size.new(250, 16777215)
    @info_frame.frameShape = Qt::Frame::Box
    @info_frame.frameShadow = Qt::Frame::Raised
    @verticalLayout_2 = Qt::VBoxLayout.new(@info_frame)
    @verticalLayout_2.margin = 0
    @verticalLayout_2.objectName = "verticalLayout_2"
    @frame_2 = Qt::Frame.new(@info_frame)
    @frame_2.objectName = "frame_2"
    @frame_2.frameShape = Qt::Frame::Box
    @verticalLayout_3 = Qt::VBoxLayout.new(@frame_2)
    @verticalLayout_3.objectName = "verticalLayout_3"
    @gridWidget = Qt::Widget.new(@frame_2)
    @gridWidget.objectName = "gridWidget"
    @gridLayout = Qt::GridLayout.new(@gridWidget)
    @gridLayout.objectName = "gridLayout"
    @label_3 = Qt::Label.new(@gridWidget)
    @label_3.objectName = "label_3"

    @gridLayout.addWidget(@label_3, 2, 0, 1, 1)

    @label_4 = Qt::Label.new(@gridWidget)
    @label_4.objectName = "label_4"

    @gridLayout.addWidget(@label_4, 3, 0, 1, 1)

    @diagnosis_lbl = Qt::Label.new(@gridWidget)
    @diagnosis_lbl.objectName = "diagnosis_lbl"

    @gridLayout.addWidget(@diagnosis_lbl, 3, 1, 1, 1)

    @incomes_lbl = Qt::Label.new(@gridWidget)
    @incomes_lbl.objectName = "incomes_lbl"

    @gridLayout.addWidget(@incomes_lbl, 2, 1, 1, 1)

    @label_2 = Qt::Label.new(@gridWidget)
    @label_2.objectName = "label_2"

    @gridLayout.addWidget(@label_2, 1, 0, 1, 1)

    @name_lbl = Qt::Label.new(@gridWidget)
    @name_lbl.objectName = "name_lbl"

    @gridLayout.addWidget(@name_lbl, 0, 1, 1, 1)

    @label = Qt::Label.new(@gridWidget)
    @label.objectName = "label"

    @gridLayout.addWidget(@label, 0, 0, 1, 1)

    @age_lbl = Qt::Label.new(@gridWidget)
    @age_lbl.objectName = "age_lbl"

    @gridLayout.addWidget(@age_lbl, 1, 1, 1, 1)

    @results_btn = Qt::PushButton.new(@gridWidget)
    @results_btn.objectName = "results_btn"

    @gridLayout.addWidget(@results_btn, 4, 1, 1, 1)


    @verticalLayout_3.addWidget(@gridWidget)

    @points_sca = Qt::ScrollArea.new(@frame_2)
    @points_sca.objectName = "points_sca"
    @points_sca.widgetResizable = true
    @scrollAreaWidget = Qt::Widget.new()
    @scrollAreaWidget.objectName = "scrollAreaWidget"
    @scrollAreaWidget.geometry = Qt::Rect.new(0, 0, 226, 252)
    @verticalLayout_12 = Qt::VBoxLayout.new(@scrollAreaWidget)
    @verticalLayout_12.objectName = "verticalLayout_12"
    @points_sca.setWidget(@scrollAreaWidget)

    @verticalLayout_3.addWidget(@points_sca)

    @horizontalLayout_4 = Qt::HBoxLayout.new()
    @horizontalLayout_4.objectName = "horizontalLayout_4"
    @last_btn = Qt::PushButton.new(@frame_2)
    @last_btn.objectName = "last_btn"

    @horizontalLayout_4.addWidget(@last_btn)

    @remove_btn = Qt::PushButton.new(@frame_2)
    @remove_btn.objectName = "remove_btn"

    @horizontalLayout_4.addWidget(@remove_btn)


    @verticalLayout_3.addLayout(@horizontalLayout_4)


    @verticalLayout_2.addWidget(@frame_2)


    @horizontalLayout.addWidget(@info_frame)

    @measuref_frame = Qt::Frame.new(patient_widget)
    @measuref_frame.objectName = "measuref_frame"
    @measuref_frame.frameShape = Qt::Frame::StyledPanel
    @measuref_frame.frameShadow = Qt::Frame::Raised
    @verticalLayout = Qt::VBoxLayout.new(@measuref_frame)
    @verticalLayout.objectName = "verticalLayout"
    @frame = Qt::Frame.new(@measuref_frame)
    @frame.objectName = "frame"
    @frame.frameShape = Qt::Frame::Box
    @horizontalLayout_2 = Qt::HBoxLayout.new(@frame)
    @horizontalLayout_2.objectName = "horizontalLayout_2"
    @tabWidget = Qt::TabWidget.new(@frame)
    @tabWidget.objectName = "tabWidget"
    @tab = Qt::Widget.new()
    @tab.objectName = "tab"
    @verticalLayout_4 = Qt::VBoxLayout.new(@tab)
    @verticalLayout_4.objectName = "verticalLayout_4"
    @label_11 = Qt::Label.new(@tab)
    @label_11.objectName = "label_11"
    @sizePolicy = Qt::SizePolicy.new(Qt::SizePolicy::Minimum, Qt::SizePolicy::Minimum)
    @sizePolicy.setHorizontalStretch(0)
    @sizePolicy.setVerticalStretch(0)
    @sizePolicy.heightForWidth = @label_11.sizePolicy.hasHeightForWidth
    @label_11.sizePolicy = @sizePolicy

    @verticalLayout_4.addWidget(@label_11)

    @blue_sp_w = Widgets::MeasureWidget.new(@tab)
    @blue_sp_w.objectName = "blue_sp_w"
    @sizePolicy1 = Qt::SizePolicy.new(Qt::SizePolicy::Expanding, Qt::SizePolicy::Expanding)
    @sizePolicy1.setHorizontalStretch(0)
    @sizePolicy1.setVerticalStretch(0)
    @sizePolicy1.heightForWidth = @blue_sp_w.sizePolicy.hasHeightForWidth
    @blue_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_4.addWidget(@blue_sp_w)

    @tabWidget.addTab(@tab, Qt::Application.translate("patient_widget", "\320\241\320\270\320\275\320\270\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275", nil, Qt::Application::UnicodeUTF8))
    @tab_2 = Qt::Widget.new()
    @tab_2.objectName = "tab_2"
    @verticalLayout_5 = Qt::VBoxLayout.new(@tab_2)
    @verticalLayout_5.objectName = "verticalLayout_5"
    @label_12 = Qt::Label.new(@tab_2)
    @label_12.objectName = "label_12"
    @sizePolicy.heightForWidth = @label_12.sizePolicy.hasHeightForWidth
    @label_12.sizePolicy = @sizePolicy

    @verticalLayout_5.addWidget(@label_12)

    @red_sp_w = Widgets::MeasureWidget.new(@tab_2)
    @red_sp_w.objectName = "red_sp_w"
    @sizePolicy1.heightForWidth = @red_sp_w.sizePolicy.hasHeightForWidth
    @red_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_5.addWidget(@red_sp_w)

    @tabWidget.addTab(@tab_2, Qt::Application.translate("patient_widget", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275", nil, Qt::Application::UnicodeUTF8))
    @tab_5 = Qt::Widget.new()
    @tab_5.objectName = "tab_5"
    @verticalLayout_6 = Qt::VBoxLayout.new(@tab_5)
    @verticalLayout_6.objectName = "verticalLayout_6"
    @label_13 = Qt::Label.new(@tab_5)
    @label_13.objectName = "label_13"
    @sizePolicy.heightForWidth = @label_13.sizePolicy.hasHeightForWidth
    @label_13.sizePolicy = @sizePolicy

    @verticalLayout_6.addWidget(@label_13)

    @original_blue_sp_w = Widgets::MeasureWidget.new(@tab_5)
    @original_blue_sp_w.objectName = "original_blue_sp_w"
    @sizePolicy1.heightForWidth = @original_blue_sp_w.sizePolicy.hasHeightForWidth
    @original_blue_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_6.addWidget(@original_blue_sp_w)

    @tabWidget.addTab(@tab_5, Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @tab_6 = Qt::Widget.new()
    @tab_6.objectName = "tab_6"
    @verticalLayout_11 = Qt::VBoxLayout.new(@tab_6)
    @verticalLayout_11.objectName = "verticalLayout_11"
    @label_18 = Qt::Label.new(@tab_6)
    @label_18.objectName = "label_18"
    @sizePolicy.heightForWidth = @label_18.sizePolicy.hasHeightForWidth
    @label_18.sizePolicy = @sizePolicy

    @verticalLayout_11.addWidget(@label_18)

    @original_red_sp_w = Widgets::MeasureWidget.new(@tab_6)
    @original_red_sp_w.objectName = "original_red_sp_w"
    @sizePolicy1.heightForWidth = @original_red_sp_w.sizePolicy.hasHeightForWidth
    @original_red_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_11.addWidget(@original_red_sp_w)

    @tabWidget.addTab(@tab_6, Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))

    @horizontalLayout_2.addWidget(@tabWidget)

    @colors_frame = Qt::Frame.new(@frame)
    @colors_frame.objectName = "colors_frame"
    @colors_frame.minimumSize = Qt::Size.new(150, 0)
    @colors_frame.maximumSize = Qt::Size.new(200, 16777215)
    @colors_frame.frameShape = Qt::Frame::Box
    @colors_frame.frameShadow = Qt::Frame::Plain
    @horizontalLayout_5 = Qt::HBoxLayout.new(@colors_frame)
    @horizontalLayout_5.margin = 2
    @horizontalLayout_5.objectName = "horizontalLayout_5"
    @gridLayout_2 = Qt::GridLayout.new()
    @gridLayout_2.objectName = "gridLayout_2"
    @widget = Qt::Widget.new(@colors_frame)
    @widget.objectName = "widget"

    @gridLayout_2.addWidget(@widget, 0, 1, 1, 1)

    @label_9 = Qt::Label.new(@colors_frame)
    @label_9.objectName = "label_9"

    @gridLayout_2.addWidget(@label_9, 0, 2, 1, 1)

    @verticalSpacer = Qt::SpacerItem.new(20, 40, Qt::SizePolicy::Minimum, Qt::SizePolicy::Expanding)

    @gridLayout_2.addItem(@verticalSpacer, 1, 2, 1, 1)

    @label_10 = Qt::Label.new(@colors_frame)
    @label_10.objectName = "label_10"

    @gridLayout_2.addWidget(@label_10, 0, 3, 1, 1)

    @widget_2 = Qt::Widget.new(@colors_frame)
    @widget_2.objectName = "widget_2"

    @gridLayout_2.addWidget(@widget_2, 0, 0, 1, 1)


    @horizontalLayout_5.addLayout(@gridLayout_2)


    @horizontalLayout_2.addWidget(@colors_frame)


    @verticalLayout.addWidget(@frame)

    @frame_3 = Qt::Frame.new(@measuref_frame)
    @frame_3.objectName = "frame_3"
    @frame_3.frameShape = Qt::Frame::Box
    @horizontalLayout_3 = Qt::HBoxLayout.new(@frame_3)
    @horizontalLayout_3.objectName = "horizontalLayout_3"
    @tabWidget_2 = Qt::TabWidget.new(@frame_3)
    @tabWidget_2.objectName = "tabWidget_2"
    @tab_3 = Qt::Widget.new()
    @tab_3.objectName = "tab_3"
    @verticalLayout_9 = Qt::VBoxLayout.new(@tab_3)
    @verticalLayout_9.objectName = "verticalLayout_9"
    @label_16 = Qt::Label.new(@tab_3)
    @label_16.objectName = "label_16"
    @sizePolicy.heightForWidth = @label_16.sizePolicy.hasHeightForWidth
    @label_16.sizePolicy = @sizePolicy

    @verticalLayout_9.addWidget(@label_16)

    @differentiated_blue_sp_w = Widgets::MeasureWidget.new(@tab_3)
    @differentiated_blue_sp_w.objectName = "differentiated_blue_sp_w"
    @sizePolicy1.heightForWidth = @differentiated_blue_sp_w.sizePolicy.hasHeightForWidth
    @differentiated_blue_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_9.addWidget(@differentiated_blue_sp_w)

    @tabWidget_2.addTab(@tab_3, Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @tab_4 = Qt::Widget.new()
    @tab_4.objectName = "tab_4"
    @verticalLayout_10 = Qt::VBoxLayout.new(@tab_4)
    @verticalLayout_10.objectName = "verticalLayout_10"
    @label_17 = Qt::Label.new(@tab_4)
    @label_17.objectName = "label_17"
    @sizePolicy.heightForWidth = @label_17.sizePolicy.hasHeightForWidth
    @label_17.sizePolicy = @sizePolicy

    @verticalLayout_10.addWidget(@label_17)

    @differentiated_red_sp_w = Widgets::MeasureWidget.new(@tab_4)
    @differentiated_red_sp_w.objectName = "differentiated_red_sp_w"
    @sizePolicy1.heightForWidth = @differentiated_red_sp_w.sizePolicy.hasHeightForWidth
    @differentiated_red_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_10.addWidget(@differentiated_red_sp_w)

    @tabWidget_2.addTab(@tab_4, Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @tab_7 = Qt::Widget.new()
    @tab_7.objectName = "tab_7"
    @verticalLayout_8 = Qt::VBoxLayout.new(@tab_7)
    @verticalLayout_8.objectName = "verticalLayout_8"
    @label_15 = Qt::Label.new(@tab_7)
    @label_15.objectName = "label_15"
    @sizePolicy.heightForWidth = @label_15.sizePolicy.hasHeightForWidth
    @label_15.sizePolicy = @sizePolicy

    @verticalLayout_8.addWidget(@label_15)

    @intact_blue_sp_w = Widgets::MeasureWidget.new(@tab_7)
    @intact_blue_sp_w.objectName = "intact_blue_sp_w"
    @sizePolicy1.heightForWidth = @intact_blue_sp_w.sizePolicy.hasHeightForWidth
    @intact_blue_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_8.addWidget(@intact_blue_sp_w)

    @tabWidget_2.addTab(@tab_7, Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @tab_8 = Qt::Widget.new()
    @tab_8.objectName = "tab_8"
    @verticalLayout_7 = Qt::VBoxLayout.new(@tab_8)
    @verticalLayout_7.objectName = "verticalLayout_7"
    @label_14 = Qt::Label.new(@tab_8)
    @label_14.objectName = "label_14"
    @sizePolicy.heightForWidth = @label_14.sizePolicy.hasHeightForWidth
    @label_14.sizePolicy = @sizePolicy

    @verticalLayout_7.addWidget(@label_14)

    @intact_red_sp_w = Widgets::MeasureWidget.new(@tab_8)
    @intact_red_sp_w.objectName = "intact_red_sp_w"
    @sizePolicy1.heightForWidth = @intact_red_sp_w.sizePolicy.hasHeightForWidth
    @intact_red_sp_w.sizePolicy = @sizePolicy1

    @verticalLayout_7.addWidget(@intact_red_sp_w)

    @tabWidget_2.addTab(@tab_8, Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))

    @horizontalLayout_3.addWidget(@tabWidget_2)


    @verticalLayout.addWidget(@frame_3)


    @horizontalLayout.addWidget(@measuref_frame)


    retranslateUi(patient_widget)

    @tabWidget.setCurrentIndex(0)
    @tabWidget_2.setCurrentIndex(0)


    Qt::MetaObject.connectSlotsByName(patient_widget)
    end # setupUi

    def setup_ui(patient_widget)
        setupUi(patient_widget)
    end

    def retranslateUi(patient_widget)
    patient_widget.windowTitle = Qt::Application.translate("patient_widget", "Form", nil, Qt::Application::UnicodeUTF8)
    @label_3.text = Qt::Application.translate("patient_widget", "\320\237\320\276\321\201\320\265\321\211\320\265\320\275\320\270\321\217", nil, Qt::Application::UnicodeUTF8)
    @label_4.text = Qt::Application.translate("patient_widget", "\320\224\320\270\320\260\320\263\320\275\320\276\320\267", nil, Qt::Application::UnicodeUTF8)
    @diagnosis_lbl.text = Qt::Application.translate("patient_widget", "TextLabel", nil, Qt::Application::UnicodeUTF8)
    @incomes_lbl.text = Qt::Application.translate("patient_widget", "TextLabel", nil, Qt::Application::UnicodeUTF8)
    @label_2.text = Qt::Application.translate("patient_widget", "\320\222\320\276\320\267\321\200\320\260\321\201\321\202", nil, Qt::Application::UnicodeUTF8)
    @name_lbl.text = Qt::Application.translate("patient_widget", "TextLabel", nil, Qt::Application::UnicodeUTF8)
    @label.text = Qt::Application.translate("patient_widget", "\320\237\320\260\321\206\320\270\320\265\320\275\321\202", nil, Qt::Application::UnicodeUTF8)
    @age_lbl.text = Qt::Application.translate("patient_widget", "TextLabel", nil, Qt::Application::UnicodeUTF8)
    @results_btn.text = Qt::Application.translate("patient_widget", "\320\240\320\265\320\267\321\203\320\273\321\214\321\202\320\260\321\202\321\213", nil, Qt::Application::UnicodeUTF8)
    @last_btn.text = Qt::Application.translate("patient_widget", "\320\237\320\276\321\201\320\273\320\265\320\264\320\275\320\270\320\265", nil, Qt::Application::UnicodeUTF8)
    @remove_btn.text = Qt::Application.translate("patient_widget", "\320\243\320\261\321\200\320\260\321\202\321\214", nil, Qt::Application::UnicodeUTF8)
    @label_11.text = Qt::Application.translate("patient_widget", "\320\241\320\270\320\275\320\270\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275 (\320\264\320\265\320\273).", nil, Qt::Application::UnicodeUTF8)
    @tabWidget.setTabText(@tabWidget.indexOf(@tab), Qt::Application.translate("patient_widget", "\320\241\320\270\320\275\320\270\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275", nil, Qt::Application::UnicodeUTF8))
    @label_12.text = Qt::Application.translate("patient_widget", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275 (\320\264\320\265\320\273.)", nil, Qt::Application::UnicodeUTF8)
    @tabWidget.setTabText(@tabWidget.indexOf(@tab_2), Qt::Application.translate("patient_widget", "\320\232\321\200\320\260\321\201\320\275\321\213\320\271 \320\264\320\270\320\260\320\277\320\260\320\267\320\276\320\275", nil, Qt::Application::UnicodeUTF8))
    @label_13.text = Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget.setTabText(@tabWidget.indexOf(@tab_5), Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @label_18.text = Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget.setTabText(@tabWidget.indexOf(@tab_6), Qt::Application.translate("patient_widget", "\320\230\321\201\321\205\320\276\320\264\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @label_9.text = Qt::Application.translate("patient_widget", "\320\230\320\220", nil, Qt::Application::UnicodeUTF8)
    @label_10.text = Qt::Application.translate("patient_widget", "\320\244\320\233", nil, Qt::Application::UnicodeUTF8)
    @label_16.text = Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget_2.setTabText(@tabWidget_2.indexOf(@tab_3), Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @label_17.text = Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget_2.setTabText(@tabWidget_2.indexOf(@tab_4), Qt::Application.translate("patient_widget", "\320\224\320\270\321\204\321\204\320\265\321\200\320\265\320\275\321\206\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @label_15.text = Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget_2.setTabText(@tabWidget_2.indexOf(@tab_7), Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \321\201\320\270\320\275\320\270\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    @label_14.text = Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8)
    @tabWidget_2.setTabText(@tabWidget_2.indexOf(@tab_8), Qt::Application.translate("patient_widget", "\320\235\320\276\321\200\320\274\320\270\321\200\320\276\320\262\320\260\320\275\320\275\321\213\320\271 \320\275\320\260 \320\270\320\275\321\202\320\260\320\272\321\202 \320\272\321\200\320\260\321\201\320\275\321\213\320\271 \321\201\320\277\320\265\320\272\321\202\321\200", nil, Qt::Application::UnicodeUTF8))
    end # retranslateUi

    def retranslate_ui(patient_widget)
        retranslateUi(patient_widget)
    end

end

module Ui
    class Patient_widget < Ui_Patient_widget
    end
end  # module Ui

if $0 == __FILE__
    a = Qt::Application.new(ARGV)
    u = Ui_Patient_widget.new
    w = Qt::Widget.new
    u.setupUi(w)
    w.show
    a.exec
end
