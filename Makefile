.PHONY: all docs install

GREEN := \033[1;32m
NC := \033[0m


all: docs

docs/backend/conf.md: backend/conf.schema.json
	@echo -e "${GREEN}Generating docs for backend configuration${NC}"
	 jsonschema2md -d backend -o docs/backend_configuration -f yaml --header false -n -x docs/backend_configuration

docs: docs/backend/conf.md

install:
	@echo -e "${GREEN}Installing Backend:${NC}"
	@cd backend && $(MAKE) install
	@echo -e "${GREEN}Building Backend:${NC}"