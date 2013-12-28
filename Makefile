FORMS_DIR = ui_forms
O_FORMS_DIR = forms
FORMS = main
O_FORMS = $(FORMS:%=$(O_FORMS_DIR)/%.rb)

all: forms

$(O_FORMS_DIR)/%.rb: $(FORMS_DIR)/%.ui
	@mkdir $(O_FORMS_DIR) -p
	rbuic4 $^ -x > $(O_FORMS_DIR)/$*.rb
forms: $(FORMS:%=$(O_FORMS_DIR)/%.rb)

clean: clean_forms

clean_forms:
	rm -f $(FORMS:%=$(O_FORMS_DIR)/%.rb)
