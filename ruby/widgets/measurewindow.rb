require 'Qt4'
require 'measure_widget'

module Windows
    class MeasureWindow < Qt::Widget
        def initialize parent = nil
            super
            @ui = Ui::Measure_widget.new
            @ui.setupUi self
        end
    end
end
