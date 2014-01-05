FORMS = \
	add_patient_form \
	clients_table_widget \
	client_widget \
	main_form \
	measure_widget \
	login_form

FORMS_DIR = ui_forms
DEST_DIR = forms

MACRO = perl -pe 's/^(from.*\.py.*)$$//; if (/^from PyQt4/) { print "$(1)\n"; }' < $(2) > $(3)

$(DEST_DIR)/%.bak: $(FORMS_DIR)/%.ui
	pyuic4 $^ -o $(DEST_DIR)/$*.bak

all: $(FORMS:%=$(DEST_DIR)/%.py)

$(DEST_DIR)/main_form.py: $(DEST_DIR)/main_form.bak
	$(call MACRO,from .measurewindow import MeasureWindow\nfrom .clientswindow import ClientsWindow as ClientsListWindow,\
		$^,$(DEST_DIR)/main_form.py)

$(DEST_DIR)/add_patient_form.py: $(DEST_DIR)/add_patient_form.bak
	cp $^ $(DEST_DIR)/add_patient_form.py

$(DEST_DIR)/login_form.py: $(DEST_DIR)/login_form.bak
	cp $^ $(DEST_DIR)/login_form.py

$(DEST_DIR)/clients_table_widget.py: $(DEST_DIR)/clients_table_widget.bak
	$(call MACRO,from widgets import ClientsTable,$^,$(DEST_DIR)/clients_table_widget.py)

$(DEST_DIR)/client_widget.py: $(DEST_DIR)/client_widget.bak
	$(call MACRO,from widgets import MeasureWidget,$^,$(DEST_DIR)/client_widget.py)

$(DEST_DIR)/measure_widget.py: $(DEST_DIR)/measure_widget.bak
	$(call MACRO,from widgets import MeasureWidget,$^,$(DEST_DIR)/measure_widget.py)

clean:
	rm -f $(FORMS:%=$(DEST_DIR)/%.py) $(FORMS:%=$(DEST_DIR)/%.bak)

