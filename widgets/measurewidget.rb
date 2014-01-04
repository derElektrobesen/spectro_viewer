require 'Qt4'
require 'dia'
require 'settings'

module Widgets
    class MeasureWidget < Qt::Widget
        @matrix = nil

        def initialize parent = nil
            super parent
            @diagrams = {}
            do_test_diagrams
        end

        def test_diagram start, delta, count
            dia = []
            count.times do |i|
                x = start + delta * i
                dia.push(Dia::Point.new x, yield(x))
            end
            push @diagrams.length, Dia::DiagramRenderer.new(dia)
        end

        def do_test_diagrams
            test_diagram(-Math::PI, 0.001, (2 * Math::PI * 1000).to_int){ |x| Math.sin x }
            test_diagram(-Math::PI, 0.001, (2 * Math::PI * 1000).to_int){ |x| Math.cos x }
        end
        
        def get_color
            colors = Settings[:colors]
            used_colors = []
            changed = false
            r = nil
            @diagrams.values.each { |dia| used_colors.push dia[:color_num] }
            used_colors = colors - used_colors
            if used_colors.length == 0
                while !changed
                    color = Random.rand 0xffffff
                    unless colors.include? color
                        colors.push color
                        changed = true
                    end
                end
                Settings[:colors] = colors
                Settings.push
                r = colors.last
            else
                r = used_colors.first
            end
            return r
        end

        def push key, dia
            color = get_color
            @diagrams[key] = {
                :dia        => dia,
                :color_num  => color,
                :color      => Qt::Color.new(Qt::Color.new("##{color.to_s 16}")),
            }
            recount_matrix
        end

        def paintEvent event
            return unless @matrix

            painter = Qt::Painter.new self
            painter.setBrush Qt::NoBrush
            puts "Repaint"
            @diagrams.each_value do |d|
                dia = d[:dia].map @matrix
                painter.setPen d[:color]
                painter.drawPath dia.to_path
            end
        end

        def recount_matrix
            @matrix = Dia::Matrix.new
            bounds = nil
            @diagrams.each_value do |dia|
                cur_bounds = dia[:dia].bounds
                if !bounds
                    bounds = cur_bounds
                else
                    change_bound = lambda do |key, operator|
                        if cur_bounds[key].send operator, bounds[key]
                            bounds[key] = cur_bounds[key]
                        end
                    end
                    change_bound.call :top, :>
                    change_bound.call :right, :>
                    change_bound.call :bottom, :<
                    change_bound.call :left, :<
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
