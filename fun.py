from block import Block
import datetime as date

def create_genesis_block():

    return Block(0,date.datetime.now(),"Genesis Block","0")

def next_block(last_block):
    this_index=last_block.index+1
    this_timestamp=date.datetime.now()
    this_data="block number"+str(this_index)
    this_hash=last_block.hash

    return Block(this_index,this_timestamp,this_data,this_hash)
