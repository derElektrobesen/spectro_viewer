require 'Qt'

module Dia
    class Point < Qt::PointF
    end

    class Diagram
        def initialize dia = nil
            if dia.class == self.class
                dia = dia.dia
            end
            @dia = dia
            @mem = {}
            @matr = Qt::Matrix.new
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

        def derivative
            d = @mem[:derivative]
            return d if d
            d = Diagram.new
            prev = nil
            @dia.each do |pnt|
                unless prev
                    prev = pnt
                else
                    d.push Point pnt.x - prev.x, (pnt.y - prev.y) / (pnt.x - prev.x)
                end
            end
            @mem[:derivative] = d
            return d
        end

        def smooth
            # TODO
        end
        
        def transform matr
            str = "#{matr.m11}_#{matr.m12}_#{matr.m21}_#{matr.m22}_#{matr.dx}_#{matr.dy}"
            unless @mem[:transformed] || @mem[:current_matr] != str
                r = Diagram.new
                @dia.each { |pnt| r.push(matr.map pnt) }
                @mem[:transformed] = r
                @mem[:current_matr] = str
            end
            return @mem[:transformed]
        end

        def move dx, dy
            @matr.translate dx, dy
            return self
        end

        def scale sx, sy = nil
            sy = sx unless sy
            dx = @matr.dx
            dy = @matr.dy
            move -dx, -dy
            @matr.scale sx, sy
            move dx, dy
            return self
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
            return @dia[0]
        end

        def right_bound
            return @dia[@dia.length - 1]
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
            @mem[:min_y] = min
            @mem[:max_y] = max
            return min, max
        end

        def top_bound
            res = nil
            @dia.each do |pnt|
                if !res || pnt.y > res.y
                    res = pnt
                end
            end
            @mem[:max_y] = res
            return res
        end

        def bottom_bound
            res = nil
            @dia.each do |pnt|
                if !res || pnt.y < res.y
                    res = pnt
                end
            end
            @mem[:min_y] = res
            return res
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
end
