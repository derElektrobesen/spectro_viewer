import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import QPointF, QPoint, QRectF
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.lines import Line2D

def _composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

_st_prop = _composed(staticmethod, property)

class Params:
    red_int_start = 6600.0
    red_int_end = 8000.0
    a1_start = 6650.0
    a1_end = 6750.0
    a2_start = 6950.0
    a2_end = 7050.0
    normalize_step = 5.0
    normalize_offset = 50.0
    normalize_right_border = 8700.0
    diff_window = 2

class SpectorsCollection:
    def __init__(self):
        self.__graphs = {}

    def add_graph(self, key, graph, intact_gr, color = "#2e8b57"):
        self.__intact_gr = intact_gr

        graph = self.process_graph_bounds(graph)
        graph = self.process_graph_data(graph)

        d = graph.get_data()
        self.__graphs[key] = { 'graph': graph, 'color': color }

    def set_color(self, key, color):
        self.__graphs[key]['color'] = color
        self.render()

    def render(self):
        pass

    def remove_graph(self, key):
        del self.__graphs[key]

    def clear(self):
        self.__graphs = {}

    def set_graph(self, key, graph):
        self.clear()
        self.add_graph(key, graph, None)

    def get_graph(self, key):
        return self.__graphs[key]['graph'] if key in self.__graphs else None

    def graphs(self):
        return self.__graphs

    def process_graph_bounds(self, gr):
        return gr

    def process_graph_data(self, gr):
        return gr

    def get_intact(self):
        return self.__intact_gr

class MeasureWidget(FigureCanvas, SpectorsCollection):
    def __init__(self, parent = None):
        self.__fig = Figure()
        FigureCanvas.__init__(self, self.__fig)
        SpectorsCollection.__init__(self)
        self.__coords = QPointF(0.0, 0.0)
        self.setParent(parent)

        self.__axes = self.__fig.add_subplot(111)
        self.__axes_coords_ref = self.__axes.transAxes
        self.__data_coords_ref = self.__axes.transData

    def set_color(self, key, color):
        g = self.graphs()
        if key in self.graphs():
            g[key]['color'] = color
        self.render()

    def render(self):
        plt = self.__axes
        plt.cla()
        xmin, xmax = 99999999, -1
        count = 0
        for gr in self.graphs().values():
            data = gr['graph'].get_data()
            if len(data) == 0 or len(data[0]) == 0:
                continue
            count += 1

            if data[0][0] < xmin:
                xmin = data[0][0]
            if data[0][-1] > xmax:
                xmax = data[0][-1]
            line = plt.plot(color = gr['color'], *data)
        if (count):
            plt.set_xlim(xmin, xmax)
        self.__fig.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.1)
        self.draw()

    def mouseMoveEvent(self, e):
        FigureCanvas.mouseMoveEvent(self, e)
        self.__coords = e.posF()
        self.repaint()

    def paintEvent(self, e):
        FigureCanvas.paintEvent(self, e)

        if not len(self.graphs()):
            return

        painter = QPainter(self)

        cur_pnt = [self.__coords.x(), self.height() - self.__coords.y()]
        cur_axes_coords = self.__axes_coords_ref.inverted().transform(cur_pnt)
        if 1 >= cur_axes_coords[0] >= 0:
            self.draw_selected_points(painter, cur_pnt)

    def draw_selected_points(self, painter, cur_pnt):
        points = [];
        axes_coords = (self.__axes_coords_ref.transform((0, 0)),
                self.__axes_coords_ref.transform((0, 1)))

        lines_color = QColor("#dedede")

        painter.setPen(lines_color)
        line_coords = ((self.__coords.x(), axes_coords[0][1] + 1),
                (self.__coords.x(), axes_coords[1][1]))
        painter.drawLine(line_coords[0][0], line_coords[0][1], line_coords[1][0], line_coords[1][1])

        painter.setBrush(QColor("#ffffff"))

        cursor_position = self.__data_coords_ref.inverted().transform(cur_pnt)
        for gr in self.graphs().values():
            data = gr['graph'].get_data()
            if len(data) == 0 or len(data[0]) == 0:
                    continue

            point = gr['graph'][cursor_position[0]]
            if point != None:
                points.append({ 'y': "%.1f" % point[1], 'color': gr['color'], })

                point = self.__data_coords_ref.transform(point)
                painter.setPen(QColor(gr['color']))
                painter.drawEllipse(point[0] - 2, self.height() - point[1] - 2, 4, 4)

        if len(points):
            self.draw_selected_points_coords(painter, points, line_coords, cursor_position[0], lines_color)

    def draw_selected_points_coords(self, painter, points, line_coords, x_coord, lines_color):
        font = QFont()
        font.setPixelSize(11)

        metrics = QFontMetrics(font)
        right_border = list(self.__axes_coords_ref.transform((1, 0)))[0]

        painter.save()
        painter.setFont(font)
        painter.setPen(lines_color)

        back_color = QColor("#ffffff")
        back_color.setAlpha(0xaa)
        painter.setBrush(back_color)

        x_coord = "%.1f" % x_coord;
        bounding_rect = metrics.boundingRect(x_coord)

        cond = bounding_rect.width() + line_coords[1][0] + 6 >= right_border

        if cond:
            bounding_rect.moveBottomRight(QPoint(line_coords[1][0] - 5, line_coords[1][1] - 2))
        else:
            bounding_rect.moveBottomLeft(QPoint(line_coords[1][0] + 5, line_coords[1][1] - 2))

        text_rect = QRectF(bounding_rect)

        if cond:
            bounding_rect.setLeft(bounding_rect.left() - 3)
            bounding_rect.setBottomRight(QPoint(line_coords[1][0] - 3, line_coords[1][1] - 2))
        else:
            bounding_rect.setBottomLeft(QPoint(line_coords[1][0] + 2, line_coords[1][1] - 2))
            bounding_rect.setWidth(bounding_rect.width() + 2)

        main_rect = self.count_main_coords_bounding_rect(points, line_coords, metrics, right_border)
        painter.drawRoundedRect(bounding_rect, 3.0, 2.0)
        painter.drawRoundedRect(main_rect, 3.0, 2.0)

        painter.setPen(QColor("#999999"))
        painter.drawText(QRectF(text_rect), x_coord)
        for pnt in points:
            painter.setPen(QColor(pnt['color']))
            painter.drawText(pnt['rect'], pnt['y'])

        painter.restore()

    def count_main_coords_bounding_rect(self, points, line_coords, font_metrics, right_border):
        width = -1
        height = 0

        r = QRectF(line_coords[0][0] + 2, line_coords[0][1] + 2, 10, 10)
        top_left = r.topLeft()

        for pnt in points:
            rect = pnt['rect'] = QRectF(font_metrics.boundingRect(pnt['y']))
            if rect.width() > width:
                width = rect.width()
            rect.moveTopLeft(QPoint(top_left.x() + 2, top_left.y() + 2 + height))
            height += rect.height() + 2

        r.setWidth(width + 5)
        r.setHeight(height + 1)

        if r.right() + 6 >= right_border:
            r.moveRight(line_coords[0][0] - 2)
            for pnt in points:
                pnt['rect'].moveLeft(r.left() + 2)

        return r
