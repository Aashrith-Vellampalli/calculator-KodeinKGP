// SPDX-License-Identifier: MIT
pragma solidity 0.8.26;
contract calculator{
    uint256 result =0;
    function add(uint256 a) public{
        result+=a;
    }
    function subtract(uint256 a) public{
        result-=a;
    }
    function multiply(uint256 a) public{
        result*=a;
    }
    function divide(uint256 a) public{
        if(a!=0){
            result/=a;
        }
    }
    function power(uint256 a) public{
        result=result**a;
    }
    function show() public view returns (uint256){
        return result;
    }
    
}