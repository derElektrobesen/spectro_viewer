FORMS_DIR = ui_forms
O_FORMS_DIR = forms

MAIN_FORMS = client_widget clients_table_widget measure_widget
OTHER_FORMS = add_patient_form main_form
REQUIRES = measurewidget clientstable

SET_REQ = ./set_requires.pl

FORMS = $(MAIN_FORMS) $(OTHER_FORMS)

all: forms

#$(TARGETS): add_require_%: $(FORMS_DIR)/%.ui
#	./set_requires.pl -i $(O_FORMS_DIR)/$*.rb $(REQUIRES)
$(O_FORMS_DIR)/%.rb: $(FORMS_DIR)/%.ui
	@mkdir $(O_FORMS_DIR) -p
	rbuic4 $^ -x > $(O_FORMS_DIR)/$*.rb
forms: $(FORMS:%=$(O_FORMS_DIR)/%.rb)
	$(SET_REQ) -i $(O_FORMS_DIR)/main_form.rb measurewindow clientslistwindow
	$(SET_REQ) -i $(O_FORMS_DIR)/client_widget.rb measurewidget
	$(SET_REQ) -i $(O_FORMS_DIR)/measure_widget.rb measurewidget
	$(SET_REQ) -i $(O_FORMS_DIR)/clients_table_widget.rb clientstable
clean: clean_forms

clean_forms:
	rm -f $(FORMS:%=$(O_FORMS_DIR)/%.rb)
