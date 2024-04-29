from blockchain import EdBlock, EdBlockChain
from VariableStorageUtility import VariableStore

attendance_log_vs = VariableStore('attendance_log_vs')

# Initialise the Blockchain 
blockchain = EdBlockChain()
blocks_count = 0

# Initialise the Database of Transactions
database = []


def add_daily_attendance(attendance):
    try:
        data = str(attendance)
        blockchain.mine(EdBlock(data, blocks_count))
        blocks_count += 1
        return True
    except:
        return False
    

def main():
    # Store the attendance data
    temp = attendance_log_vs.get_value()
    
    for i in temp:
        print(i)

    #for block in blockchain.chain:
        #print(block)

if __name__ == '__main__':
    main()