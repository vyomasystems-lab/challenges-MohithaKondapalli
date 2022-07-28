# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/SPI_Protocol.v Master.v slave.v               # provide your design path

TOPLEVEL := Spi_Protocol         # design file
MODULE   :=  spi_test   # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
