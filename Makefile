.PHONY: all docs

all: docs

docs:
	 jsonschema2md -d . -o docs -f yaml --header false -n -x docs
