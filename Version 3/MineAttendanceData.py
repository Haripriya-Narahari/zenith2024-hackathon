from blockchain import EdBlock, EdBlockChain, save_blockchain, load_blockchain
from datetime import date
import pickle

def read_attendance_data(datei):
    today = str(date.today())
    file_path = f'AttendanceData/{datei}.txt'

    with open(file_path, 'r') as file:
        attendance_data = file.read()
    return attendance_data

def main():
    # Initialise the Blockchain 
    blockchain = load_blockchain()

    '''
    attendance_data_str_1 = read_attendance_data('2024-04-30')
    attendance_data_1 = eval(attendance_data_str_1)
    blockchain.mine(EdBlock(attendance_data_1, 0))

    attendance_data_str_2 = read_attendance_data('2024-05-01')
    attendance_data_2 = eval(attendance_data_str_2)
    blockchain.mine(EdBlock(attendance_data_2, 1))
    '''

    for block in blockchain.chain:
        print(block)

'''
    blocks_count = len(blockchain.chain)

    attendance_data_str = read_attendance_data()
    attendance_data = eval(attendance_data_str)
    blockchain.mine(EdBlock(attendance_data, blocks_count))

    for block in blockchain.chain:
        print(block)
'''

    #save_blockchain(blockchain)

if __name__ == '__main__':
    main()