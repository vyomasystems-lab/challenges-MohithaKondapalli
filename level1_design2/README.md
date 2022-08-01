# Sequence Detector(1011) Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![gitpod screenshot](https://user-images.githubusercontent.com/92357357/180269862-b4acdb6d-cfe1-4da7-bf00-b5ace04ed753.PNG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input bit on every positive egde of the clk to the Design Under Test (seq_detect_1011) which takes in 1-bit input for *inp_bit* and gives an 1-bit output *seq_seen" when a 1011 sequencce is seen on the inp_bit 

The values are assigned to the input port using 
```
dut.clk.value = 0 or 1 (assigned 0 or 1 after certain period)
dut.reset.value = 0 or 1(initially 1 and on falling edge of clk  made it 0)
dut.inp_bit.value = 0 or 1 (in few test cases 0 or 1 is directly assigned and in random_testcase random value is assigned)
```


The assert statement is used to find out if sequence 1011 is detected or not.
```
assert dut.seq_seen == 1,"sequence not detected"
```

The following errors are seen:
```
 1. for input values 10111011101110
 AssertionError:  2nd sequence not detected in 10111011101110
 
 2. for input values 1010110110110
  assert dut.seq_seen == 1," 1stsequence not detected in 1010110110110"
                     AssertionError:  1stsequence not detected in 1010110110110
             
 3. assert dut.seq_seen == 1," 1stsequence not detected in 110111011"
                     AssertionError:  1stsequence not detected in 110111011
 
```
## Test Scenario1 
- Test Input: inp_bit = 1,0,1,1,1,0,1,1,1,0,1,1,1,0
- Expected Output: seq_seen = 0,0,0,0,1,0,0,0,1,0,0,0,0,1 
- Observed Output in the DUT seq_seen=0,0,0,0,1,0,0,0,0,0,0,0,1

![image](https://user-images.githubusercontent.com/92357357/180616298-d93869ca-f01e-4d75-9886-9a5705f03e4c.png)

## Test Scenario2

- Test Input: inp_bit= 1,0,1,0,1,1,0,1,1,0,1,1,0
- Expected Output: seq_seen = 0,0,0,0,0,0,1,0,0,0,0,0,0 
- Observed Output in the DUT seq_seen=0,0,0,0,0,0,0,0,0,0,0,0
![image](https://user-images.githubusercontent.com/92357357/180617932-133f2b6a-b106-44dc-ba0d-1091eb782041.png)

## Test Senario3
- Test Input: inp_bit = 1,1,0,1,1,1,0,1,1
- Expected Output: seq_seen = 0,0,0,0,0,1,0,0,0,1 
- Observed Output in the DUT seq_seen= 0,0,0,0,0,0,0,0,1
- 
![image](https://user-images.githubusercontent.com/92357357/180618575-e34b3641-40dc-4b3e-a3b7-471ad8904626.png)


Output mismatches for the above inputs proves that there are three design bugs

## Design Bugs
Based on the above test input and analysing the design, we see the following bugs
1.
```
 SEQ_1011:
      begin
        next_state = IDLE;    ====>BUG1
      end
```
In the  design, when the current_state is SEQ_1011. If inp_bit = 1 it should go to SEQ_1 state but here its is going to IDLE state irrespective of the input hence adjacent sequence after the first sequence is not being detected.

2.
```
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;   ===>BUG2
      end
 ```       
When current_state is SEQ_101=. if input is 1 it should goto next state i.e, SEQ_1011 otherwise it should go to SEQ_1 but here its going to IDLE state

3.
```
 SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   ===>BUG3
        else
          next_state = SEQ_10;
  ```        
 When current_state is state SEQ_1 . if input is 1 then it should remain in the same state but here next_state is IDLE.

## Design Fix
Updated the design for each testsenario and issues are fixed

![image](https://user-images.githubusercontent.com/92357357/180617803-ed161508-cfa2-4ea7-868f-230da5e37c57.png)

Updated the design according to the testsenario 2 and issue is fixed

![image](https://user-images.githubusercontent.com/92357357/180618119-bb340d43-8076-46ad-a87e-3121deb594b2.png)

Updated The design according to test senario3 and the issue is fixed

![image](https://user-images.githubusercontent.com/92357357/180618778-789cb0b9-ba6a-4457-9bef-6cfc30afba00.png)

Upon running all the above testcases and a selfchecking testcase with python logic similar to the design with random input bit after the design fix 

![image](https://user-images.githubusercontent.com/92357357/180638687-52aca1b2-83fa-476b-85b2-3fbfd2d3e75e.png)

Updated design:
```
always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;
      end
      SEQ_1011:
      begin
        if(inp_bit == 0)
          next_state = IDLE;
        else
          next_state = SEQ_1;
      end
    endcase
 ```   
The updated design is checked in as level1_design2_bugfree/seq_detect_1011_fix.v

## Verification Strategy

Initially a simple testcase with single sequence in in the inp_bit is choosen to understand the working of design with the generated output, current_state and next_state values. As the initial testcase failed i have gone though the design and on analyzing the values generated i was able to figure out a bug and fix it. I choose few testcases like overlapping sequence(1010110110110), adjusant sequence(10111011101110). A pattern with no sequence in it is also verified to make sure that the design is giving the expected output even though seqence is not found and upon executing all the above testcase i was able to detect and fix the bugs based on the output, currentstate, nextstate values. 
A self_checking testcase with python logic similar to the working of the design is inserted to verify the design in maximum possible cases.

## Is the verification complete ?
The verification is complete as the testbench developed is ran on a range of random inputs which covers all the corner cases in  the design.
