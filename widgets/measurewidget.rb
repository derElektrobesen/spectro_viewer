require 'Qt4'
require 'dia'
require 'settings'

module Widgets
    class MeasureWidget < Qt::Widget
        @@colors = nil
        @diagrams = {}
        def initialize parent = nil
            super parent
            if !@@colors
                read_colors
            end
        end
        
        def read_colors
        end

        def push key, dia
            @diagrams[key] = {
                :dia    => dia,
            }
        end
    end
end
