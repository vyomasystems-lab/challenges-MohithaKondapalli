# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock


'''
# Clock Generation
@cocotb.coroutine

def clock_gen(signal):
    while True:
        signal.value <= 1
        yield Timer(10) 
        signal.value <= 0
        yield Timer(10) 
'''
# Sample Test

@cocotb.test()
def run_test(dut):

    # clock
   # cocotb.fork(clock_gen(dut.clk))

    # reset
    #dut.reset.value <= 1
    #await Timer(10, units = 'ns') 
    #dut.reset.value <= 0

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    reset = 0b1
    clk = 0b0
    MODE = 0b1
    data_in_to_master = 0b10101111
    data_in_slave1 = 0b11110111
    dut.reset.value = reset
    dut.clk.value = clk
    dut.MODE.value = MODE
    dut.data_in_to_master.value = data_in_to_master
    dut.data_in_slave1.value = data_in_slave1
    yield Timer(10, units = 'ns')
    reset = 0b0
    dut.reset.value = reset
    yield Timer(10, units = 'ns')
    CS = 0b01
    dut.CS.value = CS
    RW = 0b11
    dut.RW.value = RW
    
    yield Timer(1000, units = 'ns')
    

    print("EXPECTED OUTPUTS")
    cocotb.log.info(f'data_out_from_master={bin(data_in_slave1)}, data_out_slave1 = {bin(data_in_to_master)}')
    yield Timer(10)
    CS = 0b00
    dut.CS.value = CS
    cocotb.log.info(f'data_out_from_master={dut.data_out_from_master}, data_out_slave1 = {dut.data_out_slave1}')    
    #cocotb.log.info(f'MOSI={bin(dut.MOSI)}, MISO1 ={bin(dut.MISO1)}')
    
    # comparison
    error_message = "Value mismatch" # DUT = {bin(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert (dut.data_out_from_master == data_in_slave1) & (dut.data_out_slave1 == data_in_to_master), error_message
