FORMS_DIR = ui_forms
O_FORMS_DIR = forms

MAIN_FORMS = main_form client_widget
OTHER_FORMS = add_patient_form
REQUIRES = measurewidget

FORMS = $(MAIN_FORMS) $(OTHER_FORMS)

TARGETS = $(addprefix add_require_, $(MAIN_FORMS))

all: forms

$(TARGETS): add_require_%: $(FORMS_DIR)/%.ui
	./set_requires.pl -i $(O_FORMS_DIR)/$*.rb $(REQUIRES)
$(O_FORMS_DIR)/%.rb: $(FORMS_DIR)/%.ui
	@mkdir $(O_FORMS_DIR) -p
	rbuic4 $^ -x > $(O_FORMS_DIR)/$*.rb
forms: $(FORMS:%=$(O_FORMS_DIR)/%.rb) $(TARGETS)

clean: clean_forms

clean_forms:
	rm -f $(FORMS:%=$(O_FORMS_DIR)/%.rb)
