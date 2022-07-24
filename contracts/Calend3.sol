// SPDX-License-Identifier: MIT

/*

-----------------  Appointment Based Funding Portal  --------------------

As users have paid funds to the creators , users get an added advantage to schedule a meet
with the users as a token of love <3


*/


pragma solidity ^0.8.0;

contract Calend3 {
    uint rate;
    address payable public owner;

    struct Appointment {
        string title;     // *** title of the meeting to speak with the creator as a bonus for sending funds to the creator
        address attendee; // *** creator that you are meeting with
        uint startTime;   // start time of meeting with the creator
        uint endTime;     // end time of the meeting with the creator
        uint amountPaid;  // amount paid for the meeting with the creator
    }

    Appointment[] appointments; // *** appointment feature for users because they have paid amount for the creator 
    
    constructor() {
        owner = payable(msg.sender); //payable means upgrading the normal eth address to payable address
    }

    function getRate() public view returns (uint) {
         return rate; // getting the rate value
    }   
    
    function setRate(uint _rate) public {
        require(msg.sender == owner, "Only the owner can set the rate"); 
        rate = _rate;
    }

    function getAppointments() public view returns(Appointment[] memory)
    {
        return appointments; // getting the array of appointments when funds are transferred
    }

    function createAppointment(string memory title,uint startTime, uint endTime ) public payable
    {
        Appointment memory appointment;
        appointment.title = title;
        appointment.startTime = startTime;
        appointment.endTime = endTime;
        appointment.amountPaid = ((endTime - startTime) / 60)*rate; // logic of funds needs to be transferred by the creator

        require(msg.value >= appointment.amountPaid, "We require more ether"); // validate the amount of ETH

        (bool success,) = owner.call{value: msg.value}(""); // send ETH to the creator
        require(success, "Failed to send Ether");

        appointments.push(appointment);
    }
}