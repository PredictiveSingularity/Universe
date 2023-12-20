# Build, docs release, run, simulation, windows, install and clean can be used multiple times
# How can I edit make file to run the command again? Answer: You need to use a 

.PHONY: help simulation run build install windows release clean docs

help:
	@echo "Makefile Help"
	@echo "To simulate your simulation, type make simulation"
	@echo "To run the simulation, type make run"
	@echo "To build a binary, type make build"
	@echo "To release a newer version, type make release"

simulation:
	@python simulate.py

run:
	@python -m universe

build: setup.py
	@echo "Building Universe..."
	@python setup.py build
	@cython -3 simulate.py -o build/simulate.c --embed
	@mkdir -p dist
	@gcc -Os -I /usr/include/python3.10 -o dist/simulate build/simulate.c -lpython3.10 -lpthread -lm -lutil -ldl
	@echo "Universe has been built."
	@echo "Type make install to use."

install: build
	@echo "Installing Universe..."
	@python setup.py install
	@cp dist/simulate /usr/bin/simulate
	@echo "Universe has been installed."
	@echo "Type simulate --help to begin."

windows:
	@echo "Building Universe on Windows?.."
	@echo "This is highly experimental!"
	@echo "No one has ever tried it."
	@echo "This should compile a Windows binary and create a .bat script to run it."
	@env python -m ursina.build --include_modules universe,numpy .
	@echo "If it worked..."
	@echo "...run dist/(**/)*.bat to begin the simulation."

release:
	@make build
	@python -m twine upload dist/*

clean:
	@rm -rf build
	@rmdir build
	@rm -rf dist
	@rmdir dist
	@rm -rf *.egg-info

docs:
	-@rm -rf docs
	@echo "Generating docs..."
	@bash ./fetch_docs.sh
	@echo "Docs have been generated."