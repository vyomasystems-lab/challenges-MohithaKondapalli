# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 


@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction

    count = 0   # varaible is used to count the errors 


    #list of all the instructions

    list1 = [0x4005013, 0x4005033, 0x4001033, 0x6005033, 0x6001033,
    0x68005013, 0x28005013, 0x48005013, 0x68001013, 0x28001013,0x48001013,
    0x60005013, 0x20005013, 0x20001013,
    0x68005033, 0x28005033, 0x48005033, 0x68001033, 0x28001033, 0x48001033,
    0x60005033, 0x60001033, 0x20005033, 0x20001033, 0x40004033, 0x40007033, 0x40006033]
    for i in range(0,100):
        mav_putvalue_src1 =  random.getrandbits(32) 
        #dut._log.info(f'mav_putvalue_src1={hex(mav_putvalue_src1)}')
        mav_putvalue_src2 = random.getrandbits(32) 
        #dut._log.info(f'mav_putvalue_src2={hex(mav_putvalue_src2)}')
        mav_putvalue_src3 = random.getrandbits(32) 
        #dut._log.info(f'mav_putvalue_src3={hex(mav_putvalue_src3)}')

        for val in list1:
            mav_putvalue_instr = val
            #dut._log.info(f'mav_putvalue_instr={hex(mav_putvalue_instr)}')

            # expected output from the model
            expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

            # driving the input transaction
            dut.mav_putvalue_src1.value = mav_putvalue_src1
            dut.mav_putvalue_src2.value = mav_putvalue_src2
            dut.mav_putvalue_src3.value = mav_putvalue_src3
            dut.EN_mav_putvalue.value = 1
            dut.mav_putvalue_instr.value = mav_putvalue_instr
  
            yield Timer(2) 

            # obtaining the output
            dut_output = dut.mav_putvalue.value

            #cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
            #cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

            # comparison
            if(dut_output != expected_mav_putvalue):
                error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} when instruction is mav_putvalue_instr = {hex(mav_putvalue_instr)} '
                print(error_message)
                count = count+1
            else:
                count = count
    
            


    print(val_count)  
    assert count == 0, "Failed as error_count > 0"
