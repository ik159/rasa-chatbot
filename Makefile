help:
	@echo "make"
	@echo "    setup"
	@echo "        Installing all requirements for running the bot."
	@echo "	   install"
	@echo "        Bots rise!"
	@echo "        While we set up your bot, go ahead and deploy your action server. 1. Open another server tab and run `rasa run actions` 2. To be able to interact with your bot, open a third server tab and run `rasa shell`"
	@echo "    types"
	@echo "        Check for type errors using pytype."
	@echo "    test-actions"
	@echo "        Run custom action unit tests"
	@echo "    run"
	@echo "		   Setting up your bot"

setup:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	python3 -m spacy download en_core_web_md
	python3 -m spacy link en_core_web_md en 
	pip3 install -e .

types:
	pytype --keep-going actions tests

test-actions:
	pytest . -vv




