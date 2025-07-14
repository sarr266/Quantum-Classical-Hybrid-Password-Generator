# Quantum-Classical-Hybrid-Password-Generator
This project is a secure password generator that combines quantum simulation and classical entropy to produce highly unpredictable and cryptographically strong passwords.

It demonstrates how quantum computing concepts can be applied in practical cybersecurity contexts — such as improving password generation.

---

## 🚀 What It Does

The Python script:
- Generates a binary string using simulated **quantum randomness** (via Qiskit)
- Generates a second binary string using **classical secure randomness** (via Python’s `secrets` module)
- Combines both using XOR to create a **hybrid binary string**
- Converts that binary into a strong, user-defined password

---

## 🧠 How It Works

The code has five main components:

### 1. Quantum Bit Generator
Uses `qiskit` and `AerSimulator` to simulate true randomness via quantum circuits. Hadamard gates are applied to each qubit to place them in superposition, and measurements are taken to collapse the qubits randomly into 0s or 1s.

### 2. Classical Bit Generator
Generates secure random bits using the `secrets` module — ideal for cryptographic applications.

### 3. Hybrid Bit Combiner
XORs quantum bits with classical bits to combine both entropy sources. This leverages the unpredictability of quantum with the speed of classical random generation. Any extra quantum bits are appended to complete the sequence.

### 4. Binary to Password Converter
Splits the hybrid binary into 6-bit chunks, converts each chunk into an index, and maps it to a character from a secure character set (`A-Za-z0-9!@#$%^&*()`).

### 5. User Interaction
Prompts the user for desired password length (between 8 and 24 characters), calculates how many bits are needed, and generates the password.

---

## 🧪 Example Output

```bash
Enter desired password length (8–24): 12

🔐 Your Quantum-Classical Hybrid Password:
fG4#wZ@dLk9Q
