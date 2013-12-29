require 'Qt4'
require 'add_patient_form'

module Window
    class AddPatientWindow < Qt::Dialog
        def initialize parent = nil
            super
            @ui = Ui::add_patient_form.new
            @ui.setupUi self
        end
    end
end
