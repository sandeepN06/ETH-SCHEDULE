const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("calend3", function () {

  let Contract, contract;
  let owner, addr1, addr2;

  // `beforeEach` will run before each test
  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();

    Contract = await ethers.getContractFactory("Calend3");
    contract = await Contract.deploy();
    await contract.deployed();
  });


  it("Should set the minutely rate ", async function () {
    

    const tx = await contract.setRate(1000);

    // wait until the transaction is mined
    await tx.wait();

    // verify rate is set correctly
    expect(await contract.getRate()).to.equal(1000);

    

    
  });

  it("Should fail if non owner sets rate", async function () {

    // call setRate using a different account address
    // this should fail since this address is not the owner
    await expect(
      contract.connect(addr1).setRate(500)
    ).to.be.revertedWith('Only the owner can set the rate');

  });

  it("Should add two appointments", async function () {
    const tx1 = await contract.setRate(ethers.utils.parseEther("0.00001"));
    await tx1.wait();

    const tx2 = await contract.connect(addr1).createAppointment("Meeting with Part Time Larry", 1644143400, 1644143401, {value: ethers.utils.parseEther("0.001")});
    await tx2.wait();

    const tx3 = await contract.connect(addr2).createAppointment("Breakfast at Tiffany's", 1644154200, 1644154201, {value: ethers.utils.parseEther("0.002")});
    await tx3.wait();

    const appointments = await contract.getAppointments();

    expect(appointments.length).to.equal(2);

    const ownerBalance = await ethers.provider.getBalance(owner.address);
    const addr1Balance = await ethers.provider.getBalance(addr1.address);
    const addr2Balance= await ethers.provider.getBalance(addr2.address);

    console.log(ownerBalance);
    console.log(addr1Balance);
    console.log(addr2Balance);


  });


});