# MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![gitpod screenshot](https://user-images.githubusercontent.com/92357357/180269862-b4acdb6d-cfe1-4da7-bf00-b5ace04ed753.PNG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives random inputs to the Design Under Test (mux) which takes in 2-bit random inputs for each of 31 inputs and 5-bit random input for *sel* and gives 2-bit output *out* based on the sel input

The values are assigned to the input port using 
```
dut.clk.value = 0 or 1 (assigned 0 or 1 after certain period)
dut.reset.value = 0 or 1(initially 1 and on falling edge of clk  made it 0)
dut.inp_bit.value = 0 or 1 (in few test cases 0 or 1 is directly assigned and in random_testcase random value is assigned)
```
![image](https://user-images.githubusercontent.com/92357357/180451668-6fbb6f76-e0c0-4fa4-9564-22dce3d9a415.png)


The assert statement is used to find out if sequence 1011 is detected or not.
```
assert dut.seq_seen == 1,"sequence not detected"
```

The following errors are seen:
```
 AssertionError:  2nd sequence not detected in 10111011101110
                    
 
```
## Test Scenario1 
- Test Input: 10111011101110
- Expected Output: seq_seen = 00001000100001 
- Observed Output in the DUT dut.out=0000100000001
![image](https://user-images.githubusercontent.com/92357357/180616298-d93869ca-f01e-4d75-9886-9a5705f03e4c.png)



Output mismatches for the above inputs proves that there are two design bugs

## Design Bugs
Based on the above test input and analysing the design, we see the following bugs

```
 SEQ_1011:
      begin
        next_state = IDLE;    ====>BUG
      end
```
In the  design, when the FSM is in SEQ_1011. If inp_bit = 1 it should go to SEQ_1 state but here its is going to IDLE state irrespective of the input . hence adjacent sequence is not detected.



## Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/92357357/180616665-b20b0969-5419-4dbc-8d80-7bc79aebad52.png)


Updated design:

SEQ_1011:
      begin
        if(inp_bit == 0)
          next_state = IDLE;
        else
          next_state = SEQ_1;
      end
    
    
The updated design is checked in as level1_design2_bugfree/_fix.v

## Verification Strategy

## Is the verification complete ?
