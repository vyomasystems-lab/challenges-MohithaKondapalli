
# Bitmanip co-processor Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/92357357/180820866-59a45347-bce3-4d89-aec6-a14593224472.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives four inputs values to the Design Under Test (bitmanip co-processor) which takes in 32-bit input for each *mav_putvalue_instr* , *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3* and perform the operation on mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3 based on mav_putvalue_instr provided and gives an 33 bit output *mav_putvalue* indicating result and valid bit.
The values are assigned to the input port using 
```
mav_putvalue_src1 =  random.getrandbits(32) 
mav_putvalue_src2 = random.getrandbits(32) 
mav_putvalue_src3 = random.getrandbits(32) 
mav_putvalue_instr = val [val is one of the value from list of instructions provided]
```

The if-else statement is used for comparing the mux output to the expected value 

```
if(dut_output != expected_mav_putvalue):
                error_message = f'Value mismatch DUT = {bin(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)} when instruction is mav_putvalue_instr = {hex(mav_putvalue_instr)} '
```


The following errors are seen on running the test:
```
Value mismatch DUT = 0x4b0860b does not match MODEL = 0x280270c1 when instruction is mav_putvalue_instr = 0x40007033 
Value mismatch DUT = 0x1cacb9944 does not match MODEL = 0x0 when instruction is mav_putvalue_instr = 0x40007033
                    
```
## Test Scenario1
 random values are assigned to mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3 and mav_putvalue_instr is assigned to ``ANDN`` instruction 

- Test Inputs:  mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3 and mav_putvalue_instr is assigned to ``ANDN`` instruction = 0x16597b65, mav_putvalue_src2 = 0x4258c31f, mav_putvalue_src3 = 0x2fd6e045, mav_putvalue_instr = 0x40007033
- Expected Output: expected_mav_putvalue = 0x280270c1
- Observed output: dut_output = 0x4b0860b 

![image](https://user-images.githubusercontent.com/92357357/181343462-d0d7eae4-b635-4a87-b602-d98dc02ff959.png)

## Test Scenario2
 Random values are assigned to mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3 and mav_putvalue_instr is assigned to some invalid instruction 
 
- Test Inputs:  mav_putvalue_src1 = 0xe565cca2, mav_putvalue_src2 = 0xf5829c9b, mav_putvalue_src3 = 0x26bac0da, mav_putvalue_instr = 0x4002023
- Expected Output: expected_mav_putvalue = 0x0
- Observed output: dut_output = 0x1cacb9944

![image](https://user-images.githubusercontent.com/92357357/181344234-ff08626e-1401-4bfd-ac4c-df94eb89628a.png)

## Test Scenario3
All the instructions provided in the python model is performed on each combination of src1, src2, src3(these values are generated for a certain rage using for loop) and the value mismatch is seen when ``ANDN`` and ``INVALID`` instructions are provided.
![image](https://user-images.githubusercontent.com/92357357/181347015-6a141042-3005-498c-b138-fb02ffbcb0f4.png)

From the above test scenarios it is detected that the design is failing for ``ANDN`` instruction and according to python model provided when an ``INVALID`` instruction is provided the expected output should be zero but it is returing some value.
Output mismatches for the above inputs proves that there are bugs in the  design

## Design Bugs



## Design Fix


## Verification Strategy
Initially a random set of inputs are assigned to each of src1, src2, src3 and checked if the design is working properly for each instruction provided on the particular combination. Later to make the task simple a test case with a list of instructions is assigned to a variabel and random inputs for src1, src2, src3 are generated till the certain range and each instruction from the provided list is performed on each set of combination and the failure of the design for ``  ANDN`` and ``INVALID`` instructions are detected.  

## Is the verification complete ?
