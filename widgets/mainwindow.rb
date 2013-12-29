require 'Qt4'
require 'main_form'

module Windows
    class MainWindow < Qt::MainWindow
        def initialize parent = nil
            super
            @ui = Ui::MainWindow.new
            @ui.setupUi self
        end
    end
end
