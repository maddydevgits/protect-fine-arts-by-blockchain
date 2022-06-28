// SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity >=0.4.22 <0.9.0;

contract arts {
  string[] _artists;
  string[] _hashes;

  function addArt(string memory artist, string memory hashes) public {
    _artists.push(artist);
    _hashes.push(hashes);
  }
  function viewArts() public view returns(string[] memory, string[] memory) {
    return (_artists,_hashes);
  }
}
