# Install Qiskit and Aer Simulator (for Google Colab or first-time use)
!pip install qiskit qiskit-aer

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import string
import secrets

# ----------- Quantum Bit Generator (Simulated) -----------
def generate_quantum_bits(n_bits, max_qubits=20):
    backend = AerSimulator()
    bits = ""
    for start in range(0, n_bits, max_qubits):
        chunk_size = min(max_qubits, n_bits - start)
        qc = QuantumCircuit(chunk_size, chunk_size)
        qc.h(range(chunk_size))
        qc.measure(range(chunk_size), range(chunk_size))
        compiled_circuit = transpile(qc, backend)
        job = backend.run(compiled_circuit, shots=1)
        result = job.result()
        counts = result.get_counts()
        bits += list(counts.keys())[0]
    return bits

# ----------- Classical Bit Generator (Cryptographically Secure) -----------
def generate_classical_bits(n_bits):
    return ''.join(str(secrets.randbits(1)) for _ in range(n_bits))

# ----------- Hybrid Bit Combiner -----------
def hybrid_random_bits(qbits, cbits):
    quantum_bits = generate_quantum_bits(qbits)
    classical_bits = generate_classical_bits(cbits)

    # Combine by XOR for the first cbits
    combined = ''.join(
        str(int(q)^int(c)) for q, c in zip(quantum_bits[:cbits], classical_bits)
    ) + quantum_bits[cbits:]

    return combined

# ----------- Binary to Password Converter -----------
def binary_to_password(binary_str, length=12):
    charset = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''
    for i in range(0, len(binary_str), 6):
        chunk = binary_str[i:i+6]
        if len(chunk) < 6:
            chunk = chunk.ljust(6, '0')
        index = int(chunk, 2) % len(charset)
        password += charset[index]
        if len(password) == length:
            break
    return password

# ----------- User Input and Password Generation -----------
length = int(input("Enter desired password length (8–24): "))
if length < 8 or length > 24:
    print("❌ Please enter a number between 8 and 24.")
else:
    n_bits = length * 6
    hybrid_bits = hybrid_random_bits(n_bits, cbits=n_bits // 2)
    password = binary_to_password(hybrid_bits, length)

    print("\n🔐 Your Quantum-Classical Hybrid Password:")
    print(password)
