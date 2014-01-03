require 'Qt4'
require 'dia'

module Widgets
    class MeasureWidget < Qt::Widget
        @graphs = []
        def initialize parent = nil
            super
        end
    end
end
