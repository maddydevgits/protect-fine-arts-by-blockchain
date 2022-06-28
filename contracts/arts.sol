// SPDX-License-Identifier: MIT
pragma experimental ABIEncoderV2;
pragma solidity >=0.4.22 <0.9.0;

contract arts {
  string[] _artists;
  string[] _hashes;

  mapping(string=>bool) _registered;

  function addArt(string memory artist, string memory hashes) public {

    require(!_registered[hashes]);
    _artists.push(artist);
    _hashes.push(hashes);
    _registered[hashes]=true;
  }
  function viewArts() public view returns(string[] memory, string[] memory) {
    return (_artists,_hashes);
  }
}
