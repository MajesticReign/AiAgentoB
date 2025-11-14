// backend/contract.js
export const CONTRACT_ADDRESS = "0x5B1D9b5fF7e8c2a3d4e5f6a7b8c9d0e1f2a3b4c5";
export const ABI = [
  {
    "inputs": [
      { "internalType": "string", "name": "winner", "type": "string" },
      { "internalType": "string", "name": "log", "type": "string" }
    ],
    "name": "recordBattle",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getBattleCount",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  }
];
