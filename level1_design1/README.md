
# MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![gitpod screenshot](https://user-images.githubusercontent.com/92357357/180269862-b4acdb6d-cfe1-4da7-bf00-b5ace04ed753.PNG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives random inputs to the Design Under Test (mux) which takes in 2-bit random inputs for each of 31 inputs and 5-bit random input for *sel* and gives 2-bit output *out* based on the sel input

The values are assigned to the input port using 
```
dut.sel.value = random.ranint(0,31)
dut.inp0.value = random.randint(1,3) 
dut.inp1.value = random.ranint(1,3)
.
.
.
dut.inp31.value= random.ranint(1,3)
```
![](image.png)

The assert statement is used for comparing the mux output to the expected value.



The following errors are seen:
```
assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 01100 is 01 but the design value is 00
                    
 assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 01101 is 10 but the design value is 11

 assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 11110 is 01 but the design value is 00


```
## Test Scenario **(Important)**
- Test Inputs: sel = 12, inp12 = 2
- Expected Output: out = 2
- Observed Output in the DUT dut.out=0
![](image.png)
## Test Scenario
- Test Inputs: sel = 13, inp30 = 3
- Expected Output: out = 3
- Observed Output in the DUT dut.out=2
This senario apperas as the case 5'b01101 is written twice 
![](image.png)
## Test Scenario
- Test Inputs: sel = 30, inp30 = 3
- Expected Output: out = 3
- Observed Output in the DUT dut.out=0
![](image.png)


Output mismatches for the above inputs proves that there are two design bugs

## Design Bugs
Based on the above test input and analysing the design, we see the following bugs

```
5'b01010: out = inp10;
5'b01011: out = inp11;
5'b01101: out = inp12;        ====>BUG1
5'b01101: out = inp13;
5'b01110: out = inp14;
```
In the  design, the case statement for both inp12 and inp13 is same as 5'b01101  it should be ``5'b01100 : out = inp12`` instead of ``5'b01101: out = inp12`` as in the design code. 

```
5'b11011: out = inp27;
5'b11100: out = inp28;
5'b11101: out = inp29;
default: out = 0;
```
In the  design, the case statement for sel input 11110 is not defined. hence it is giving the default output value.  it should be defined as ``5'b11110 : out = inp30`` . 


## Design Fix
Updating the design and re-running the test makes the test pass.

Updated design
 case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01100: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;
      default: out = 0;
    endcase


The updated design is checked in as level1_design1_bugfree/mux.v

## Verification Strategy

## Is the verification complete ?
