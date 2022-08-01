# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Spi_Protocol.v             # provide your design path

TOPLEVEL := Spi_Protocol           # design file
#MODULE   := spi_test.py   # test file
MODULE   := sample_test
include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
