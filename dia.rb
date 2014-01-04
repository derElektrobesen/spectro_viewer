require 'Qt'

module Dia
    class Point < Qt::PointF
        def to_s
            return "Point: (#{x}, #{y})"
        end
    end

    class Matrix < Qt::Matrix
        def to_s
            return "Matrix:\n| %7.2f %7.2f 0 |\n| %7.2f %7.2f 0 |\n| %7.2f %7.2f 1 |" % \
                [m11(), m12, m21, m22, dx, dy]
        end
    end

    class Diagram
        def initialize dia = nil
            if dia.class == self.class
                dia = dia.dia
            end
            @dia = dia || []
            @mem = {}
        end

        def dia= d
            @dia = d
            @mem = {}
        end

        def dia
            return @dia
        end

        def [] index
            return @dia[index]
        end

        def []= index, value
            @dia[index] = value
            @mem = {}
        end

        def push value
            @dia.push value
            @mem = {}
        end

        def each
            @dia.each { |pnt| yield pnt }
        end

        def derivative
            d = @mem[:derivative]
            return d if d
            d = Diagram.new
            prev = nil
            @dia.each do |pnt|
                unless prev
                    prev = pnt
                else
                    d.push(Point.new pnt.x - prev.x, (pnt.y - prev.y) / (pnt.x - prev.x))
                end
            end
            @mem[:derivative] = d
            return d
        end

        def smooth
            # TODO
        end
        
        def bounds
            top_b, bot_b = vert_bounds
            return {
                :top    => top_b,
                :bottom => bot_b,
                :left   => left_bound,
                :right  => right_bound,
            }
        end

        def left_bound
            return @dia[0].x
        end

        def right_bound
            return @dia[@dia.length - 1].x
        end

        def vert_bounds
            min, max = @mem[:min_y], @mem[:max_y]
            if min && !max
                return min, top_bound
            elsif max && !min
                return bottom_bound, max
            elsif max && min
                return min, max
            end
            @dia.each do |pnt|
                if !min || pnt.y < min.y
                    min = pnt
                end
                if !max || pnt.y > max.y
                    max = pnt
                end
            end
            @mem[:min_y] = min.y
            @mem[:max_y] = max.y
            return min.y, max.y
        end

        def top_bound
            res = @mem[:max_y]
            return res if res

            @dia.each do |pnt|
                if !res || pnt.y > res.y
                    res = pnt
                end
            end
            @mem[:max_y] = res.y
            return res.y
        end

        def bottom_bound
            res = @mem[:min_y]
            return res if res

            @dia.each do |pnt|
                if !res || pnt.y < res.y
                    res = pnt
                end
            end
            @mem[:min_y] = res.y
            return res.y
        end

        def value x
            res = @mem["val_#{x}"]
            r_bound = 0
            l_bound = @dia.length
            while !res
                l = @dia[l_bound]
                r = @dia[r_bound]
                if x == r.x
                    res = r
                elsif x == l.x
                    res = l
                elsif r_bound == l_bound + 1
                    r = Point.new x, l.y + (r.y - l.y) * (r.x - l.x) / (x - l.x)
                else
                    mid_i = l_bound + ((r_bound - l_bound) / 2).to_i
                    mid = @dia[mid_i]
                    if x > mid.x
                        l_bound = mid_i
                    else
                        r_bound = mid_i
                    end
                end
            end
            @mem["val_#{x}"] = res
            return res
        end
    end

    class DiagramRenderer < Diagram
        def initialize dia = nil
            super dia
        end

        def map matr
            str = matr.to_s
            unless @mem[:transformed] && @mem[:current_matr] == str
                r = DiagramRenderer.new
                @dia.each { |pnt| r.push(Point.new(matr.map pnt)) }
                @mem[:transformed] = r
                @mem[:current_matr] = str
                @mem[:painter_path] = nil
            end
            return @mem[:transformed]
        end

        def to_path
            unless @mem[:painter_path]
                path = Qt::PainterPath.new
                @dia.each_with_index do |val, index|
                    if index == 0
                        path.moveTo val
                    else
                        path.lineTo val
                    end
                end
                @mem[:painter_path] = path
            end
            return @mem[:painter_path]
        end
    end
end
