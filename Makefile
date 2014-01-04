FORMS = \
	add_patient_form \
	clients_table_widget \
	client_widget \
	main_form \
	measure_widget

FORMS_DIR = ui_forms
DEST_DIR = forms

$(DEST_DIR)/%.py: $(FORMS_DIR)/%.ui
	pyuic4 $^ -o $(DEST_DIR)/$*.bak

all: $(FORMS:%=$(DEST_DIR)/%.py)
