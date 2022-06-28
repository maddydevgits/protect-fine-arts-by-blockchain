import streamlit as st
from PIL import Image
import ipfsApi
from web3 import Web3,HTTPProvider
import json
from ca import *

def load_img(img):
    return Image.open(img)

def connect_with_blockchain(acc):
    web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
    if(acc==0):
        web3.eth.defaultAccount = web3.eth.accounts[0]
    else:
        web3.eth.defaultAccount=acc
    compiled_contract_path='../build/contracts/arts.json'
    deployed_contract_address=artsContractAddress

    with open(compiled_contract_path) as file:
        contract_json=json.load(file)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=deployed_contract_address,abi=contract_abi)
    return contract, web3

def app():
    st.title('Verify your art')
    img_file=st.file_uploader('Upload your art',type=['jpg','jpeg','png'])
    if img_file is not None:
        file_details={}
        file_details['type']=img_file.type
        file_details['size']=img_file.size
        file_details['name']=img_file.name
        st.write(file_details)

        with open('art.jpg','wb') as f:
            f.write(img_file.getbuffer())
        
        st.image(load_img(img_file),width=250)

        api=ipfsApi.Client('127.0.0.1',5001)
        res=api.add('art.jpg')
        st.write('Hash: '+res['Hash'])
        hash=str(res['Hash'])
        contract,web3=connect_with_blockchain(0)
        _artists,_hashes=contract.functions.viewArts().call()

        if hash in _hashes :
            hashIndex=_hashes.index(hash)
            st.success('Artist: '+_artists[hashIndex])
        else:
            st.error('You can register your art')
