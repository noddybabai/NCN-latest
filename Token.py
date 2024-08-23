import hashlib

class BlockchainToken:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}

    def transfer(self, sender, recipient, amount):
        if sender not in self.balances:
            self.balances[sender] = 0
        if recipient not in self.balances:
            self.balances[recipient] = 0

        if self.balances[sender] < amount:
            raise ValueError("Insufficient funds")

        self.balances[sender] -= amount
        self.balances[recipient] += amount

    def get_balance(self, address):
        if address not in self.balances:
            return 0
        return self.balances[address]

    def create_block(self, transactions):
        block = {
            "transactions": transactions,
            "previous_hash": self.get_previous_hash()
        }

        block_hash = hashlib.sha256(json.dumps(block).encode()).hexdigest()
        self.blocks.append(block)

        return block_hash

    def get_previous_hash(self):
        if len(self.blocks) == 0:
            return None
        return self.blocks[-1]["hash"]

# Create a new blockchain token
token = BlockchainToken("My Token", "MTK", 1000000)

# Transfer some tokens from one address to another
token.transfer("sender_address", "recipient_address", 100)

# Get the balance of an address
balance = token.get_balance("recipient_address")

# Create a new block
block_hash = token.create_block([transaction])

# Print the block hash
print(block_hash)