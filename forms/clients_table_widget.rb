=begin
** Form generated from reading ui file 'clients_table_widget.ui'
**
** Created:   29 16:04:05 2013
**      by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
=end

require 'clientstable'
require 'clientstable'
require 'Qt4'

class Ui_Clients_widget
    attr_reader :verticalLayout
    attr_reader :frame_3
    attr_reader :horizontalLayout_3
    attr_reader :label_2
    attr_reader :lineEdit
    attr_reader :tableView

    def setupUi(clients_widget)
    if clients_widget.objectName.nil?
        clients_widget.objectName = "clients_widget"
    end
    clients_widget.resize(640, 480)
    @verticalLayout = Qt::VBoxLayout.new(clients_widget)
    @verticalLayout.objectName = "verticalLayout"
    @frame_3 = Qt::Frame.new(clients_widget)
    @frame_3.objectName = "frame_3"
    @frame_3.minimumSize = Qt::Size.new(0, 37)
    @frame_3.maximumSize = Qt::Size.new(16777215, 37)
    @frame_3.frameShape = Qt::Frame::Box
    @frame_3.frameShadow = Qt::Frame::Plain
    @horizontalLayout_3 = Qt::HBoxLayout.new(@frame_3)
    @horizontalLayout_3.objectName = "horizontalLayout_3"
    @horizontalLayout_3.setContentsMargins(-1, 4, -1, 4)
    @label_2 = Qt::Label.new(@frame_3)
    @label_2.objectName = "label_2"

    @horizontalLayout_3.addWidget(@label_2)

    @lineEdit = Qt::LineEdit.new(@frame_3)
    @lineEdit.objectName = "lineEdit"

    @horizontalLayout_3.addWidget(@lineEdit)


    @verticalLayout.addWidget(@frame_3)

    @tableView = Widgets::ClientsTable.new(clients_widget)
    @tableView.objectName = "tableView"
    @tableView.frameShape = Qt::Frame::Box
    @tableView.frameShadow = Qt::Frame::Plain

    @verticalLayout.addWidget(@tableView)


    retranslateUi(clients_widget)

    Qt::MetaObject.connectSlotsByName(clients_widget)
    end # setupUi

    def setup_ui(clients_widget)
        setupUi(clients_widget)
    end

    def retranslateUi(clients_widget)
    clients_widget.windowTitle = Qt::Application.translate("clients_widget", "Form", nil, Qt::Application::UnicodeUTF8)
    @label_2.text = Qt::Application.translate("clients_widget", "\320\237\320\276\320\270\321\201\320\272:", nil, Qt::Application::UnicodeUTF8)
    end # retranslateUi

    def retranslate_ui(clients_widget)
        retranslateUi(clients_widget)
    end

end

module Ui
    class Clients_widget < Ui_Clients_widget
    end
end  # module Ui

if $0 == __FILE__
    a = Qt::Application.new(ARGV)
    u = Ui_Clients_widget.new
    w = Qt::Widget.new
    u.setupUi(w)
    w.show
    a.exec
end
