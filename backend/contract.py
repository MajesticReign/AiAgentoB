"""Python contract constants used by battle_server.

Mirrors backend/contract.js so `from contract import CONTRACT_ADDRESS, ABI` works.
"""

# Same address as contract.js, written with a valid EIP-55 checksum so web3.py can load it.
CONTRACT_ADDRESS = "0x5B1d9b5ff7E8c2A3d4e5F6A7B8c9d0e1f2A3B4C5"
ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "winner", "type": "string"},
            {"internalType": "string", "name": "log", "type": "string"},
        ],
        "name": "recordBattle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getBattleCount",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]
