# SPI Protocol Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/92357357/180820866-59a45347-bce3-4d89-aec6-a14593224472.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs values to the Design Under Test which takes in 8-bit input for each *data_in_to_master*, *data_in_slave1*, *data_in_slave2*, *data_in_slave3* , 2-bit inputs *CS*, *RW*, *MODE* and *clk & reset* signals. Depending on CS, RW, MODE the communication i.e read and write between master and three slaves occur.
The values are assigned to the input port using 
```
dut.data_in_to_master.value =0b10101010
dut.data_in_slave1.value =0b11100111
dut.data_in_slave2.value =0b11100111
dut.data_in_slave3.value =0b11100111 
```

The if statement is used for comparing the design output to the expected value.

```
if((dut.data_out_from_master.value == input_vector1) and (dut.data_out_slave1.value == input_vector)):
        cocotb.log.info(" testcase #1  passed successfuly")
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
- Test Inputs: data_in_to_master =0b10101010, .data_in_slave1 =0b11100111
- Expected Output: data_out_from_master = 0b11100111, data_out_slave1 = 0b10101010
- Observed Output in the DUT : data_out_from_master = xxxxxxxx, data_out_slave1 = 0b00000000
![image](https://user-images.githubusercontent.com/92357357/182205080-d2f6c577-b257-4b0e-b73d-f1b59323dceb.png)

Output mismatches for the above inputs proves that there are design bugs

## Design Bugs

## Design Fix

    



## Verification Strategy

A simple read and write operation is performed between master and one slave to validate if the design is having issue and later on different testcases like communication between master and 2 slave with both read and rite operations simultaneously are validated.

## Is the verification complete ?


