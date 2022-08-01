# MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/92357357/180820866-59a45347-bce3-4d89-aec6-a14593224472.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs values to the Design Under Test (31-to -1 mux) which takes in 5-bit random input for *sel* 2-bit random inputs for each of the inputs *inp0-inp30 and gives 2-bit output *out* based on the sel input.

The values are assigned to the input port using 
```
dut.sel.value = random.getrandbits(31)
dut.inp0.value = random.getrandbits(1) 
dut.inp1.value = random.getrandbits(1)
.
.
.
dut.inp31.value= random.ranint(1,3)
```

The assert statement is used for comparing the mux output to the expected value.

```
assert out == dut.out.value,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                sel=dut.sel.value, expected = out, output= dut.out.value)
```


The following errors are seen on running the test:
```
assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 01100 is 11 but the design value is 00
                    
assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 01101 is 11 but the design value is 10

assert out == dut.out.value ,"the expected output for input sel line {sel} is {expected} but the design value is {output}".format(
                     AssertionError: the expected output for input sel line 11110 is 01 but the design value is 00


```
## Test Scenario1 
- Test Inputs: sel = 01100, inp12 = 11
- Expected Output: out = 11
- Observed Output in the DUT dut.out=00
![image](https://user-images.githubusercontent.com/92357357/180450336-ddba2411-9d4b-49fd-b626-2e19b0839410.png)

## Test Scenario2
- Test Inputs: sel = 01101, inp13 = 11
- Expected Output: out = 11
- Observed Output in the DUT dut.out=10

This senario appears because in one of the case statement output is assigned to inp12 when sel = 13 ``5'b01101: out = inp12;``
![image](https://user-images.githubusercontent.com/92357357/180827666-681b5d58-3b91-4503-9800-d6408b3f65fc.png)

## Test Scenario3
- Test Inputs: sel = 11110, inp30 = 01
- Expected Output: out = 01
- Observed Output in the DUT dut.out=00

This senario appears as there is no case statement written in the design for sel input 30
![image](https://user-images.githubusercontent.com/92357357/180833612-096e0c3a-c8b9-40b3-a39f-0fe7e37ac3e3.png)


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
In the  design, the case statement for  inp12 is ``5'b01101: out = inp12``  it should be ``5'b01100 : out = inp12``

```
5'b11011: out = inp27;
5'b11100: out = inp28;
5'b11101: out = inp29;      ====>need to add case for sel input 30
default: out = 0;
```
In the  design, the case statement for sel input 11110 is not defined. hence it is giving the default output value 00, it should be defined as ``5'b11110 : out = inp30`` . 


## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/92357357/180451446-7e2b312a-49a6-4f17-ae8e-e74065a34447.png)


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
      5'b01100: out = inp12;       ====>changed
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
      5'b11110: out = inp30;     ======>added
      default: out = 0;
    endcase
    
    


The updated design is checked in as level1_design1/level1_design1_bugfree/mux_fix.v

## Verification Strategy

I used a for loop and assigned random values to all the inputs. If loops are used within the for loop to define the model of design and an assert statement is used to expose the bug in the design by comapring the expected and the actual output value, on running the test its gets terminated if error is detected. so when any error is detected i have go through the output values and the expected values to analyze the design and made changes in the design accordingly and made sure that the design is working properly now . The process is repeated until all the bugs are found and resolved and made sure that the design is covering all the possible input values as its a simple design.

## Is the verification complete ?

The verification is complete as the test case designed is made to run on all possible input values and also made sure that the design is working properly for all the
inputs.
