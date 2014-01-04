=begin
** Form generated from reading ui file 'main_form.ui'
**
** Created:   4 18:44:15 2014
**      by: Qt User Interface Compiler version 4.8.5
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
=end

require 'clientslistwindow'
require 'measurewindow'
require 'Qt4'

class Ui_MainWindow
    attr_reader :act_exit
    attr_reader :act_add_client
    attr_reader :act_settings
    attr_reader :act_about
    attr_reader :centralwidget
    attr_reader :horizontalLayout
    attr_reader :tabWidget
    attr_reader :tab_measure
    attr_reader :verticalLayout_2
    attr_reader :widget
    attr_reader :tab_clients
    attr_reader :verticalLayout
    attr_reader :widget_2
    attr_reader :menubar
    attr_reader :menuAfqk
    attr_reader :menu
    attr_reader :menu_2
    attr_reader :statusbar

    def setupUi(mainWindow)
    if mainWindow.objectName.nil?
        mainWindow.objectName = "mainWindow"
    end
    mainWindow.resize(995, 538)
    @act_exit = Qt::Action.new(mainWindow)
    @act_exit.objectName = "act_exit"
    @act_add_client = Qt::Action.new(mainWindow)
    @act_add_client.objectName = "act_add_client"
    @act_settings = Qt::Action.new(mainWindow)
    @act_settings.objectName = "act_settings"
    @act_about = Qt::Action.new(mainWindow)
    @act_about.objectName = "act_about"
    @centralwidget = Qt::Widget.new(mainWindow)
    @centralwidget.objectName = "centralwidget"
    @horizontalLayout = Qt::HBoxLayout.new(@centralwidget)
    @horizontalLayout.objectName = "horizontalLayout"
    @tabWidget = Qt::TabWidget.new(@centralwidget)
    @tabWidget.objectName = "tabWidget"
    @tab_measure = Qt::Widget.new()
    @tab_measure.objectName = "tab_measure"
    @verticalLayout_2 = Qt::VBoxLayout.new(@tab_measure)
    @verticalLayout_2.objectName = "verticalLayout_2"
    @widget = Windows::MeasureWindow.new(@tab_measure)
    @widget.objectName = "widget"

    @verticalLayout_2.addWidget(@widget)

    @tabWidget.addTab(@tab_measure, Qt::Application.translate("MainWindow", "\320\230\320\267\320\274\320\265\321\200\320\265\320\275\320\270\320\265", nil, Qt::Application::UnicodeUTF8))
    @tab_clients = Qt::Widget.new()
    @tab_clients.objectName = "tab_clients"
    @verticalLayout = Qt::VBoxLayout.new(@tab_clients)
    @verticalLayout.objectName = "verticalLayout"
    @widget_2 = Windows::ClientsListWindow.new(@tab_clients)
    @widget_2.objectName = "widget_2"

    @verticalLayout.addWidget(@widget_2)

    @tabWidget.addTab(@tab_clients, Qt::Application.translate("MainWindow", "\320\232\320\273\320\270\320\265\320\275\321\202\321\213", nil, Qt::Application::UnicodeUTF8))

    @horizontalLayout.addWidget(@tabWidget)

    mainWindow.centralWidget = @centralwidget
    @menubar = Qt::MenuBar.new(mainWindow)
    @menubar.objectName = "menubar"
    @menubar.geometry = Qt::Rect.new(0, 0, 995, 27)
    @menuAfqk = Qt::Menu.new(@menubar)
    @menuAfqk.objectName = "menuAfqk"
    @menu = Qt::Menu.new(@menubar)
    @menu.objectName = "menu"
    @menu_2 = Qt::Menu.new(@menubar)
    @menu_2.objectName = "menu_2"
    mainWindow.setMenuBar(@menubar)
    @statusbar = Qt::StatusBar.new(mainWindow)
    @statusbar.objectName = "statusbar"
    mainWindow.statusBar = @statusbar

    @menubar.addAction(@menuAfqk.menuAction())
    @menubar.addAction(@menu.menuAction())
    @menubar.addAction(@menu_2.menuAction())
    @menuAfqk.addAction(@act_exit)
    @menu.addAction(@act_add_client)
    @menu.addAction(@act_settings)
    @menu_2.addAction(@act_about)

    retranslateUi(mainWindow)
    Qt::Object.connect(@act_exit, SIGNAL('triggered()'), mainWindow, SLOT('close()'))

    @tabWidget.setCurrentIndex(0)


    Qt::MetaObject.connectSlotsByName(mainWindow)
    end # setupUi

    def setup_ui(mainWindow)
        setupUi(mainWindow)
    end

    def retranslateUi(mainWindow)
    mainWindow.windowTitle = Qt::Application.translate("MainWindow", "SpectroViewer", nil, Qt::Application::UnicodeUTF8)
    @act_exit.text = Qt::Application.translate("MainWindow", "\320\222\321\213\321\205\320\276\320\264", nil, Qt::Application::UnicodeUTF8)
    @act_add_client.text = Qt::Application.translate("MainWindow", "\320\224\320\276\320\261\320\260\320\262\320\270\321\202\321\214 \320\277\320\260\321\206\320\270\320\265\320\275\321\202\320\260", nil, Qt::Application::UnicodeUTF8)
    @act_settings.text = Qt::Application.translate("MainWindow", "\320\235\320\260\321\201\321\202\321\200\320\276\320\271\320\272\320\270", nil, Qt::Application::UnicodeUTF8)
    @act_about.text = Qt::Application.translate("MainWindow", "\320\240\320\260\320\267\321\200\320\260\320\261\320\276\321\202\321\207\320\270\320\272\320\270", nil, Qt::Application::UnicodeUTF8)
    @tabWidget.setTabText(@tabWidget.indexOf(@tab_measure), Qt::Application.translate("MainWindow", "\320\230\320\267\320\274\320\265\321\200\320\265\320\275\320\270\320\265", nil, Qt::Application::UnicodeUTF8))
    @tabWidget.setTabText(@tabWidget.indexOf(@tab_clients), Qt::Application.translate("MainWindow", "\320\232\320\273\320\270\320\265\320\275\321\202\321\213", nil, Qt::Application::UnicodeUTF8))
    @menuAfqk.title = Qt::Application.translate("MainWindow", "\320\244\320\260\320\271\320\273", nil, Qt::Application::UnicodeUTF8)
    @menu.title = Qt::Application.translate("MainWindow", "\320\230\320\275\321\201\321\202\321\200\321\203\320\274\320\265\320\275\321\202\321\213", nil, Qt::Application::UnicodeUTF8)
    @menu_2.title = Qt::Application.translate("MainWindow", "\320\230\320\275\321\204\320\276\321\200\320\274\320\260\321\206\320\270\321\217", nil, Qt::Application::UnicodeUTF8)
    end # retranslateUi

    def retranslate_ui(mainWindow)
        retranslateUi(mainWindow)
    end

end

module Ui
    class MainWindow < Ui_MainWindow
    end
end  # module Ui

if $0 == __FILE__
    a = Qt::Application.new(ARGV)
    u = Ui_MainWindow.new
    w = Qt::MainWindow.new
    u.setupUi(w)
    w.show
    a.exec
end
