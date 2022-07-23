# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_random(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    queue = []
    seq_seen = 1
    for i in range(0,10):
        await RisingEdge(dut.clk)
        inp_bit = random.randint(0,1)
        dut.inp_bit.value = inp_bit
        #dut._log.info("inp_bit = %d, next_state = %d, seq_seen = %d",inp_bit, dut.next_state.value, dut.seq_seen.value)
        queue.append(inp_bit)
        print(inp_bit)
        while (len(queue)> 3):

            if((queue[0:4]) == [1,0,1,1]):
                queue.pop(0)
                queue.pop(0)
                queue.pop(0)
                queue.pop(0)
                #print(queue)
                await RisingEdge(dut.clk)
                #if (dut.seq_seen.value == 1) :
                   # dut._log.info("inp_bit = %d, next_state = %d, seq_seen = %d",inp_bit, dut.next_state.value, dut.seq_seen.value)
                    #print("pattern detected")
                    
                assert ut.seq_seen.value == seq_seen,"sequence not detected with {inp_bit}, {current_state}, {seq_see}".format(inp_bit, dut.current_state.value, dut.seq_seen.value)
                #else:
                    #dut._log.info("inp_bit = %d, current_state = %d, seq_seen = %d", inp_bit, dut.current_state.value, dut.seq_seen.value)
                    #print("patter not detected")
                    

                
             
            else:
                queue.pop(0)
                #print(queue)
  

