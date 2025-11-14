from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import uvicorn
from web3 import Web3
from contract import CONTRACT_ADDRESS, ABI  # ← This connects to your file

# === YOUR WALLET (SAFE TO SHOW) ===
WALLET_ADDRESS = "0x791f0c9a61e049fd044f6a7c77f70121b480a339"

# === WEB3 SETUP (Base Sepolia) ===
w3 = Web3(Web3.HTTPProvider("https://sepolia.base.org"))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

app = FastAPI()

class Move(BaseModel):
    name: str
    power: int

class Card(BaseModel):
    name: str
    grade: int
    hp: int
    moves: List[Move]

class BattleLog(BaseModel):
    turn: int
    player_move: str
    opponent_move: str
    damage: int

@app.post("/battle")
def battle(player: Card, opponent: Card):
    log = []
    p_hp = player.hp
    o_hp = opponent.hp
    turn = 1

    while p_hp > 0 and o_hp > 0:
        # AI picks random move
        p_move = player.moves[0].name
        o_move = opponent.moves[0].name
        damage = 60

        o_hp -= damage
        log.append(BattleLog(turn=turn, player_move=p_move, opponent_move=o_move, damage=damage).dict())
        turn += 1

        if o_hp <= 0:
            winner = player.name
            break

        p_hp -= 55
        if p_hp <= 0:
            winner = opponent.name
            break

    # === RECORD ON-CHAIN ===
    try:
        tx_hash = contract.functions.recordBattle(
            winner,
            json.dumps(log)
        ).transact({"from": WALLET_ADDRESS})
        tx_hash = w3.to_hex(tx_hash)
        tx_link = f"https://sepolia.basescan.org/tx/{tx_hash}"
    except:
        tx_link = "Simulated (no gas)"

    return {
        "winner": winner,
        "log": log,
        "on_chain": tx_link
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
