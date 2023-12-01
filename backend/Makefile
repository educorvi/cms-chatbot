.PHONY: all install

GREEN := \033[1;32m
NC := \033[0m


all: install

/etc/cms-chatbot/conf.template.yaml: conf.template.yaml
	mkdir -p /etc/cms-chatbot
	cp -f conf.template.yaml /etc/cms-chatbot/conf.template.yaml

/etc/cms-chatbot/conf.yaml:
	mkdir -p /etc/cms-chatbot
	cp conf.template.yaml /etc/cms-chatbot/conf.yaml

/lib/systemd/system/cms-chatbot.service: cms-chatbot.service
	cp cms-chatbot.service /lib/systemd/system/cms-chatbot.service

install: /etc/cms-chatbot/conf.template.yaml /etc/cms-chatbot/conf.yaml /lib/systemd/system/cms-chatbot.service
	sudo pip install .
	mkdir -p /var/lib/cms-chatbot