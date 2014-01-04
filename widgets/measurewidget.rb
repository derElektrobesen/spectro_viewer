require 'Qt4'
require 'dia'
require 'settings'

module Widgets
    class MeasureWidget < Qt::Widget
        @matrix = nil

        def initialize parent = nil
            super parent
            @diagrams = {}
        end
        
        def get_color index = nil
            index = @diagrams.length unless index
            colors = Settings[:colors]
            changed = false
            while index >= colors.length
                color = Random.rand 0xffffff
                unless colors.include? color
                    colors.push color
                    changed = true
                end
            end
            if changed
                Settings[:colors] = colors
                Settings.dump
            end
            return colors[index]
        end

        def push key, dia
            @diagrams[key] = {
                :dia    => dia,
                :color  => Qt::Color.new(Qt::Rgb.new(get_color)),
            }
        end

        def paintEvent event
            painter = Qt::Painter.new self
            painter.setBrush Qt::NoBrush
            @diagrams.values.each do |dia|
                painter.setPen dia[:color]
                last_p = nil
                dia[:dia].each do |p|
                    painter.drawLine(Qt::LineF.new last_p, p) if last_p
                    last_p = p
                end
            end
        end

        def recount_matrix
            @matrix = Dia::Matrix.new
            bounds = nil
            @diagrams.values.each do |dia|
                cur_bounds = dia.bounds
                if !bounds
                    bounds = cur_bounds
                else
                    change_bound = lambda do |key|
                        if yield cur_bounds[key], bounds[key]
                            bounds[key] = cur_bounds[key]
                        end
                    end
                    change_bound.call :top, &:>
                    change_bound.call :right, &:>
                    change_bound.call :bottom, &:<
                    change_bound.call :left, &:<
                end
            end
            if bounds
                sx = width / (bounds[:right] - bounds[:left])
                sy = height / (bounds[:top] - bounds[:bottom])
                dx = bounds[:left]
                dy = bounds[:bottom]
                @matrix.scale(sx, -sy)
                @matrix.translate(dx * sx, dy * sy)
            end
        end
    end
end
