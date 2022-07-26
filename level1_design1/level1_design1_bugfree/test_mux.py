# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

### TESTCASE for sel input 12
@cocotb.test()
async def testcase_sel12(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')


    sel = 0b01100             
    dut.sel.value = sel                     #driving the sel value to DUT
    inp12 = 0b10
    dut.inp12.value = inp12
       
    await Timer(1)
    out = inp12
    assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = bin(out), output= dut.out.value)


### TESTCASE for sel input 13
@cocotb.test()
async def testcase_sel13(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')


    sel = 0b01101             
    dut.sel.value = sel                     #driving the sel value to DUT
    inp13 = 0b11
    dut.inp13.value = inp13
       
    await Timer(1)
    out = inp13
    assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = bin(out), output= dut.out.value)


### TESTCASE for sel input 30
@cocotb.test()
async def testcase_sel30(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')


    sel = 0b11110             
    dut.sel.value = sel                     #driving the sel value to DUT
    inp30 = 0b11
    dut.inp30.value = inp30
       
    await Timer(1)
    out = inp30
    assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = bin(out), output= dut.out.value)




###SELF CHECKING TESTCASE
@cocotb.test()
async def test_mux_buggy(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    
    
    for i in range(0,30):

        #driving the inputs to dut

        sel = random.getrandbits(5)             #generating random sel value
        dut.sel.value = sel                     #driving the sel value to DUT
        dut.inp1.value = random.getrandbits(2)
        dut.inp2.value = random.getrandbits(2)
        dut.inp0.value = random.getrandbits(2)
        dut.inp3.value = random.getrandbits(2)
        dut.inp4.value = random.getrandbits(2)
        dut.inp5.value = random.getrandbits(2)
        dut.inp6.value = random.getrandbits(2)
        dut.inp7.value = random.getrandbits(2)
        dut.inp8.value = random.getrandbits(2)
        dut.inp9.value = random.getrandbits(2)
        dut.inp10.value = random.getrandbits(2)
        dut.inp11.value = random.getrandbits(2)
        dut.inp12.value = random.getrandbits(2)
        dut.inp13.value = random.getrandbits(2)
        dut.inp14.value = random.getrandbits(2)
        dut.inp15.value = random.getrandbits(2)
        dut.inp16.value = random.getrandbits(2)
        dut.inp17.value = random.getrandbits(2)
        dut.inp18.value = random.getrandbits(2)
        dut.inp19.value = random.getrandbits(2)
        dut.inp20.value = random.getrandbits(2)
        dut.inp21.value = random.getrandbits(2)
        dut.inp22.value = random.getrandbits(2)
        dut.inp23.value = random.getrandbits(2)
        dut.inp24.value = random.getrandbits(2)
        dut.inp25.value = random.getrandbits(2)
        dut.inp26.value = random.getrandbits(2)
        dut.inp27.value = random.getrandbits(2)
        dut.inp28.value = random.getrandbits(2)
        dut.inp29.value = random.getrandbits(2)
        dut.inp30.value = random.getrandbits(2)

        await Timer(2,units='ns')

        if sel == 1:
            out = dut.inp1.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp1.value, out, dut.out.value)
            assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output= dut.out.value)
       
        elif sel == 2:
            out = dut.inp2.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp2.value, out, dut.out.value)
            assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 3:
            out = dut.inp3.value
            dut._log.info("sel = %d input = %d  expected output = %d  actual output = %d", sel, dut.inp3.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        
        elif sel == 4:
            out = dut.inp4.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp4.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        
        elif sel == 5:
            out = dut.inp5.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp5.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 6:
            out = dut.inp6.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp6.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 7:
            out = dut.inp7.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp7.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 8:
            out = dut.inp8.value
            dut._log.info("sel = %d  input = %d expected output = %d  actual output = %d", sel, dut.inp8.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        
        elif sel == 9:
            out = dut.inp9.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp9.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 10:
            out = dut.inp10.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp10.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
            
        elif sel == 11:
            out = dut.inp11.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp11.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 12:
            out = dut.inp12.value
            dut._log.info("sel = %d  input = %d  expected output = %d  actual output = %d", sel, dut.inp12.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 13:
            out = dut.inp13.value
            dut._log.info("sel = %d input = %d  expected output = %d  actual output = %d", sel, dut.inp13.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
            
        elif sel == 14:
            out = dut.inp14.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp14.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
            
        elif sel == 15:
            out = dut.inp15.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp15.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        
        elif sel == 16:
            out = dut.inp16.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp16.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 17:
            out = dut.inp17.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp17.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 18:
            out = dut.inp18.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp18.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 19:
            out = dut.inp19.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp19.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 20:
            out = dut.inp20.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp20.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 21:
            out = dut.inp21.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp21.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 22:
            out = dut.inp22.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp22.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 23:
            out = dut.inp23.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp23.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 24:
            out = dut.inp24.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp24.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 25:
            out = dut.inp25.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp25.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)

        elif sel == 26:
            out = dut.inp26.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp26.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 27:
            out = dut.inp27.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp27.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 28:
            out = dut.inp28.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp28.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 29:
            out = dut.inp29.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp29.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 30:
            out = dut.inp30.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp30.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        elif sel == 0:
            out = dut.inp0.value
            dut._log.info("sel = %d input = %d expected output = %d  actual output = %d", sel, dut.inp30.value, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)
        else :
            out = 0
            dut._log.info("sel = %d  expected output = %d  actual output = %d", sel, out, dut.out.value)
            assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output=dut.out.value)