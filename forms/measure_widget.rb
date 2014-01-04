=begin
** Form generated from reading ui file 'measure_widget.ui'
**
** Created:   29 16:04:05 2013
**      by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
=end

require 'measurewidget'
require 'measurewidget'
require 'Qt4'

class Ui_Measure_widget
    attr_reader :verticalLayout
    attr_reader :frame
    attr_reader :horizontalLayout_2
    attr_reader :start_measure_btn
    attr_reader :process_measure_btn
    attr_reader :continiously_chb
    attr_reader :remove_voice_chb
    attr_reader :horizontalSpacer
    attr_reader :label
    attr_reader :exposition_time_spb
    attr_reader :clean_hist_btn
    attr_reader :frame_2
    attr_reader :verticalLayout_3
    attr_reader :measure_viewer

    def setupUi(measure_widget)
    if measure_widget.objectName.nil?
        measure_widget.objectName = "measure_widget"
    end
    measure_widget.resize(726, 480)
    @verticalLayout = Qt::VBoxLayout.new(measure_widget)
    @verticalLayout.objectName = "verticalLayout"
    @frame = Qt::Frame.new(measure_widget)
    @frame.objectName = "frame"
    @frame.minimumSize = Qt::Size.new(0, 37)
    @frame.maximumSize = Qt::Size.new(16777215, 37)
    @frame.frameShape = Qt::Frame::Box
    @frame.frameShadow = Qt::Frame::Plain
    @horizontalLayout_2 = Qt::HBoxLayout.new(@frame)
    @horizontalLayout_2.objectName = "horizontalLayout_2"
    @horizontalLayout_2.setContentsMargins(-1, 4, -1, 4)
    @start_measure_btn = Qt::PushButton.new(@frame)
    @start_measure_btn.objectName = "start_measure_btn"

    @horizontalLayout_2.addWidget(@start_measure_btn)

    @process_measure_btn = Qt::PushButton.new(@frame)
    @process_measure_btn.objectName = "process_measure_btn"

    @horizontalLayout_2.addWidget(@process_measure_btn)

    @continiously_chb = Qt::CheckBox.new(@frame)
    @continiously_chb.objectName = "continiously_chb"

    @horizontalLayout_2.addWidget(@continiously_chb)

    @remove_voice_chb = Qt::CheckBox.new(@frame)
    @remove_voice_chb.objectName = "remove_voice_chb"
    @remove_voice_chb.checked = true

    @horizontalLayout_2.addWidget(@remove_voice_chb)

    @horizontalSpacer = Qt::SpacerItem.new(40, 20, Qt::SizePolicy::Expanding, Qt::SizePolicy::Minimum)

    @horizontalLayout_2.addItem(@horizontalSpacer)

    @label = Qt::Label.new(@frame)
    @label.objectName = "label"

    @horizontalLayout_2.addWidget(@label)

    @exposition_time_spb = Qt::SpinBox.new(@frame)
    @exposition_time_spb.objectName = "exposition_time_spb"
    @exposition_time_spb.minimum = 20
    @exposition_time_spb.maximum = 2000
    @exposition_time_spb.singleStep = 10
    @exposition_time_spb.value = 50

    @horizontalLayout_2.addWidget(@exposition_time_spb)

    @clean_hist_btn = Qt::PushButton.new(@frame)
    @clean_hist_btn.objectName = "clean_hist_btn"

    @horizontalLayout_2.addWidget(@clean_hist_btn)


    @verticalLayout.addWidget(@frame)

    @frame_2 = Qt::Frame.new(measure_widget)
    @frame_2.objectName = "frame_2"
    @frame_2.frameShape = Qt::Frame::Box
    @frame_2.frameShadow = Qt::Frame::Plain
    @verticalLayout_3 = Qt::VBoxLayout.new(@frame_2)
    @verticalLayout_3.margin = 0
    @verticalLayout_3.objectName = "verticalLayout_3"
    @measure_viewer = Widgets::MeasureWidget.new(@frame_2)
    @measure_viewer.objectName = "measure_viewer"

    @verticalLayout_3.addWidget(@measure_viewer)


    @verticalLayout.addWidget(@frame_2)


    retranslateUi(measure_widget)

    Qt::MetaObject.connectSlotsByName(measure_widget)
    end # setupUi

    def setup_ui(measure_widget)
        setupUi(measure_widget)
    end

    def retranslateUi(measure_widget)
    measure_widget.windowTitle = Qt::Application.translate("measure_widget", "Form", nil, Qt::Application::UnicodeUTF8)
    @start_measure_btn.text = Qt::Application.translate("measure_widget", "\320\241\321\202\320\260\321\200\321\202", nil, Qt::Application::UnicodeUTF8)
    @process_measure_btn.text = Qt::Application.translate("measure_widget", "\320\236\320\261\321\200\320\260\320\261\320\276\321\202\320\260\321\202\321\214", nil, Qt::Application::UnicodeUTF8)
    @continiously_chb.text = Qt::Application.translate("measure_widget", "\320\235\320\265\320\277\321\200\320\265\321\200\321\213\320\262\320\275\320\276", nil, Qt::Application::UnicodeUTF8)
    @remove_voice_chb.text = Qt::Application.translate("measure_widget", "\320\243\320\261\321\200\320\260\321\202\321\214 \321\210\321\203\320\274", nil, Qt::Application::UnicodeUTF8)
    @label.text = Qt::Application.translate("measure_widget", "\320\255\320\272\321\201\320\277.", nil, Qt::Application::UnicodeUTF8)
    @clean_hist_btn.text = Qt::Application.translate("measure_widget", "\320\236\321\207\320\270\321\201\321\202\320\270\321\202\321\214 \320\270\321\201\321\202\320\276\321\200\320\270\321\216", nil, Qt::Application::UnicodeUTF8)
    end # retranslateUi

    def retranslate_ui(measure_widget)
        retranslateUi(measure_widget)
    end

end

module Ui
    class Measure_widget < Ui_Measure_widget
    end
end  # module Ui

if $0 == __FILE__
    a = Qt::Application.new(ARGV)
    u = Ui_Measure_widget.new
    w = Qt::Widget.new
    u.setupUi(w)
    w.show
    a.exec
end
