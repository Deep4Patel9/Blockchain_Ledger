#Blockchain Ledger

#Import Libraries and Dependencies
import streamlit as st
import pandas as pd
from hashlib import sha256
from dataclasses import dataclass
from typing import Any, List
import datetime as dt

#Create a Record Data Class with a sender, receiver, and amount attributes

@dataclass
class Record:
    sender: str
    receiver: str
    amount: float



#Create a Block Data Class to store the following attributes:
# record, data, creator_id, prev_hash, timestamp, nonce

@dataclass
class Block:
    record: Record
    creator_id: int
    prev_hash: str = '0'
    timestamp: str = dt.datetime.utcnow().strftime('%H:%M:%S')
    nonce: int = 0

    #Create a Function to hash Block
    
    def hash_block(self):
        sha = sha256()
        record = str(self.record).encode()
        sha.update(record)
        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)
        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)
        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)
        nonce = str(self.nonce).encode()
        sha.update(nonce)
        
        return sha.hexdigest()


#Create a PyChain Data Class with a chain and difficulty attribute

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    #Create a Proof of Work function

    def proof_of_work(self, block):
        calc_hash = block.hash_block()
        num_of_zeros = '0' * self.difficulty

        while not calc_hash.startswith(num_of_zeros):
            block.nonce += 1
            calc_hash = block.hash_block()
        
        print(f'The Winning Hash is {calc_hash}')

        return block 

    #Create an add block function to initiate proof of work

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]
    
    #Create a function to validate blockchain integraty

    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print('Blockchain is Invalid!')
                return False
            block_hash = block.hash_block()
        print('Blockchain is Valid!')
        return True


#Streamlit Code
#Add a cache decorator for Streamlit

@st.cache(allow_output_mutation=True)

def setup():
    print('Initializaing Chain')
    return PyChain([Block('Genesis', 0)])

st.markdown('# PyChain')
st.markdown('## Store a Transaction Record in the PyChain')

pychain = setup()

#Create user inputs for the Streamlit Interface
#Inputs for sender, receiver, amount

sender_in = st.text_input('Sender')
receiver_in = st.text_input('Receiver')
amount_in = st.number_input('Amount to Send', min_value=0.000)

#Create a button to Add New Block to Chain

if st.button('Add Block'):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_record = Record(
        sender= sender_in, 
        receiver= receiver_in,
        amount= amount_in)

    new_block = Block(
        record= new_record,
        creator_id= 42,
        prev_hash= prev_block_hash)

    pychain.add_block(new_block)
    st.balloons()

#Convert pychain to dataframe and display on streamlit

st.markdown('## The PyChain Ledger')
pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

#Add slider on sidebar to select the difficulty for proof of work
difficulty = st.sidebar.slider('Block Difficulty', 1, 5, 2)
pychain.difficulty = difficulty

#Add a block selector to view specific block

st.sidebar.write('# Block Inspector')

selected_block = st.sidebar.selectbox(
    'Which block would you like to view?', pychain.chain
)
st.sidebar.write(selected_block)

#Add a button to vaildate the chain

if st.button('Validate Chain'):
    st.write(pychain.is_valid())