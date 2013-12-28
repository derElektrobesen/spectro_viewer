#!/usr/bin/ruby -W2

$LOAD_PATH.unshift File.expand_path("#{File.dirname(__FILE__)}")
$LOAD_PATH.unshift File.expand_path("#{File.dirname(__FILE__)}/forms")

require 'Qt4'
require 'main_form.rb'

class MainWindow < Qt::MainWindow
    def initialize parent = nil
        super
        @ui = Ui_MainWindow.new
        @ui.setupUi self
    end
end

if $0 == __FILE__
    app = Qt::Application.new(ARGV)
    mainwindow = MainWindow.new
    mainwindow.show
    app.exec
end
