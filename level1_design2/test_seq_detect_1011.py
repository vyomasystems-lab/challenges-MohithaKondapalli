# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

##TEST CASE FOR 011011000
@cocotb.test()
async def test_seq_011011000(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    assert dut.seq_seen == 1,"sequence not detected"
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)


###TEST CASE FOR 101111011101110
@cocotb.test()
async def test_seq_101111011101110(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    assert dut.seq_seen == 1,"sequence not detected"
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    assert dut.seq_seen == 1,"sequence not detected"
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    assert dut.seq_seen == 1,"sequence not detected"
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)

##TEST CASE FOR 1010110110110

@cocotb.test()
async def test_seq_1010110110110(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    assert dut.seq_seen == 1,"sequence not detected"
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    assert dut.seq_seen == 1,"sequence not detected"
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)


##TEST CASE FOR 110111011

@cocotb.test()
async def test_seq_1110111011(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    assert dut.seq_seen == 1,"sequence not detected"
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    await RisingEdge(dut.clk)
    assert dut.seq_seen == 1,"sequence not detected"
    dut._log.info("inp_bit= %d, next_state= %d, seq_seen = %d", dut.inp_bit.value, dut.next_state.value, dut.seq_seen.value)
    

##Self Checking
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
    l = random.randint(1,30)
    print(l)
    for i in range(0,l):
        await RisingEdge(dut.clk)
        inp_bit = random.randint(0,1)
        dut.inp_bit.value = inp_bit
        queue.append(inp_bit)
        print(queue)
        while (len(queue)> 3):

            if((queue[0:4]) == [1,0,1,1]):
                queue.pop(0)
                queue.pop(0)
                queue.pop(0)
                queue.pop(0)
                #print(queue)
                
                await RisingEdge(dut.clk)
                #if dut.seq_seen.value != 1 :
                print("sequence should be one")
                await RisingEdge(dut.clk)
                dut._log.info("reset = %d, inp_bit = %d, current_state = %d, next_state = %d, seq_seen = %d", dut.reset.value, inp_bit, dut.current_state.value, dut.next_state, dut.seq_seen)
                assert dut.seq_seen == 1,"sequence not detected"
                    #print("sequence not detected")

            else:
                queue.pop(0)
                #print(queue)
  
  