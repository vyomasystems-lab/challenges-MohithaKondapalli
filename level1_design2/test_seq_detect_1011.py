# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
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
    for i in range(0,10):
        await RisingEdge(dut.clk)
        inp_bit = random.getrandbits(1)
        dut.inp_bit.value = inp_bit
        queue.append(inp_bit)
    dut._log.info("queue = %b", queue)

    for 
    if queue[0] == 1:
        queue.pop()
        if queue[0] == 0:
            queuue.pop()
            if queue[0] == 1:
                queuue.pop()
                if queue[0] == 0:
                     queuue.pop()
                     assert dut.seq_seen == 1, "sequence not detected"
        
          



    
    
