FORMS_DIR = ui_forms
O_FORMS_DIR = forms
MAIN_FORM = main_form
FORMS = $(MAIN_FORM)
REQUIRES = measurewidget
MAIN_FORM_F = $(O_FORMS_DIR)/$(MAIN_FORM)

all: forms

$(O_FORMS_DIR)/%.rb: $(FORMS_DIR)/%.ui
	@mkdir $(O_FORMS_DIR) -p
	rbuic4 $^ -x > $(O_FORMS_DIR)/$*.rb
forms: $(FORMS:%=$(O_FORMS_DIR)/%.rb)
	@cp $(MAIN_FORM_F).rb $(MAIN_FORM_F).old.rb
	./set_requires.pl $(REQUIRES) < $(MAIN_FORM_F).old.rb > $(MAIN_FORM_F).rb
	@rm -f $(MAIN_FORM_F).old.rb

clean: clean_forms

clean_forms:
	rm -f $(FORMS:%=$(O_FORMS_DIR)/%.rb)
