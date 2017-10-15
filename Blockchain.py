import fun
import block


#create the blockchain and the genesis block

blockchain=[fun.create_genesis_block()]
prev_block=blockchain[0]

# How many blocks should we add to the chain
# after the genesis block

tot_num=20

# Add blocks to chain

for i in range(tot_num):
    block_to_add=fun.next_block(prev_block)
    blockchain.append(block_to_add)
    prev_block=block_to_add

    # Tell everyone about it!
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}".format(block_to_add.hash)
    print "Data:{}\n".format(block_to_add.data)







