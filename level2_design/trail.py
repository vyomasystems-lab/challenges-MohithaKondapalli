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

# Sample Test
@cocotb.test()
def run_test(dut):
    count = 0;
    val_count = 0
    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    for i in range(0, (2**32)):
        mav_putvalue_src1 =  random.getrandbits(32)
        #val_count = val_count + 1
        #for j in range (0,(2**32)):
        mav_putvalue_src2 = random.getrandbits(32) #0x0
        #val_count = val_count + 1
            #for k in range (0,(2**32)):
        mav_putvalue_src3 = random.getrandbits(32) #0x0
                #val_count = val_count + 1

        mav_putvalue_instr = 0x4005013
                #dut._log.info(f'mav_putvalue_instr={hex(mav_putvalue_instr)}')

                # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

                # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        yield Timer(1) 

                # obtaining the output
        dut_output = dut.mav_putvalue.value

                #cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
                #cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
                # comparison
        if (dut_output !=expected_mav_putvalue ):
            error_message = f'Value mismatch DUT = {bin(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
            print(error_message)
            count = count+1
            #assert dut_output == expected_mav_putvalue, error_message
        else:
            count = count
    print(val_count)
    print(count)  
    assert count == 0, "Failed as error_count > 0"