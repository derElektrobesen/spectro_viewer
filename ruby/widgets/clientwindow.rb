require 'Qt4'
require 'client_widget'

module Windows
    class ClientWindow < Qt::Widget
        def initialize parent = nil
            super
            @ui = Ui::Patient_widget.new
            @ui.setupUi self
        end
    end
end
