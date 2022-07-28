# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock



# Clock Generation
@cocotb.coroutine

def clock_gen(signal):
    while True:
        signal.value <= 1
        yield Timer(10) 
        signal.value <= 0
        yield Timer(10) 

# Sample Test

@cocotb.test()
async def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    # reset
    dut.reset.value <= 1
    await Timer(10, units = 'ns') 
    dut.reset.value <= 0

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    MODE = 0b01
    dut.MODE.value = MODE
    data_in_to_master = 0b10101111
    dut.data_in_to_master.value = data_in_to_master
    data_in_slave1 = 0b11110111
    dut.data_in_slave1.value = data_in_slave1
    await Timer(20,units='ns')
    CS = 0b01
    dut.CS.value = CS
    RW = 0b11
    dut.RW.VALUE = RW
    

    await Timer(120, units='ns')
    CS = 0b00
    dut.CS.value = CS

    print("EXPECTED OUTPUTS")
    cocotb.log.info(f'data_out_from_master={bin(data_in_slave1)}, data_out_slave1 = {bin(data_in_to_master)}')
    cocotb.log.info(f'data_out_from_master={dut.data_out_from_master}, data_out_slave1 = {dut.data_out_slave1}')    
    #cocotb.log.info(f'MOSI={bin(dut.MOSI)}, MISO1 ={bin(dut.MISO1)}')
    
    # comparison
    error_message = "Value mismatch" # DUT = {bin(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert (dut.data_out_from_master == data_in_slave1) & (dut.data_out_slave1 == data_in_to_master), error_message
