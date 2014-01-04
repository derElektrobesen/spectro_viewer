require 'Qt4'
require 'clients_table_widget'

module Windows
    class ClientsListWindow < Qt::Widget
        def initialize parent = nil
            super
            @ui = Ui::Clients_widget.new
            @ui.setupUi self
        end
    end
end
