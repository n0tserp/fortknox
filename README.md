# Fort Knox • Taproot Vault (Demo)

**Drag → Seal → One-Click Recovery**

A **visual demo** that simulates sealing 3 files into a "90-day timelocked Bitcoin vault".

> **Not for real BTC** — uses a fake address.

---

## Features

- Drag & drop **any 3 files**
- Animated vault door
- Saves `FORTKNOX_RECOVERY.json` to Desktop
- One-click open in Finder/TextEdit (macOS)
- Retro terminal aesthetic

---

## How It Works

1. Drag 3 files → stored in memory
2. After 3rd file → "seal" triggers
3. **Fake address**: `bc1pn0tserp1776`
4. JSON saved with off-chain 90-day note
5. Click button → opens file

---

<img width="899" height="629" alt="511491688-9e755dfd-b44c-4a4b-8e39-75fe773c2ced" src="https://github.com/user-attachments/assets/150784ce-6222-4070-94b9-ed3cd53d003e" /><img width="898" height="627" alt="511491855-d014acac-49e6-4bce-97f8-d5757df98a42" src="https://github.com/user-attachments/assets/0afe6035-bae0-449a-a02c-be2877ca85b1" /><img width="966" height="777" alt="511491966-6f05897a-2e16-4b18-a076-4f825b3d4623" src="https://github.com/user-attachments/assets/150ca475-06c7-4330-999b-2578372b7aa1" />



---
## Installation

```bash
pip install pyqt6
```
## Run

```bash
pip install pyqt6
```

## Warning

- ⚠️ No real Bitcoin logic
- ⚠️ No key derivation
- ⚠️ No on-chain timelock
- ⚠️ Hardcoded fake address
***For education, art, or GUI prototyping only.***

---

## Testnet Prototype in Development
- Real on-chain timelock vault coming soon
- 3 files → real private key
- OP_CHECKLOCKTIMEVERIFY enforced on-chain
- P2WSH testnet address + PSBT + WIF
- Sparrow Wallet compatible
---

## License
**MIT** © n0tserp  
Copy, fork, ship, sell, hire me — Follow @n0tserp for updates.
