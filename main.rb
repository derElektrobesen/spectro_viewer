#!/usr/bin/ruby -W1

$LOAD_PATH.unshift File.expand_path("#{File.dirname(__FILE__)}")
$LOAD_PATH.unshift File.expand_path("#{File.dirname(__FILE__)}/forms")
$LOAD_PATH.unshift File.expand_path("#{File.dirname(__FILE__)}/widgets")

require 'Qt4'
require 'mainwindow'

if $0 == __FILE__
    app = Qt::Application.new(ARGV)
    mainwindow = Windows::MainWindow.new
    mainwindow.show
    app.exec
end
