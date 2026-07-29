"""
Simulação de Qubit de Spin usando QuTiP
========================================
Simula um qubit de spin-1/2 em campo magnético externo.

Autor: Estudo sobre quantização do momento angular
Data: 2026-07-29
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# ============================================================
# 1. Definição dos Estados de Spin
# ============================================================

# Estados base
spin_up = basis(2, 0)    # |↑⟩ = |0⟩
spin_down = basis(2, 1)  # |↓⟩ = |1⟩

print("=== Estados de Spin ===")
print(f"|↑⟩ = {spin_up.trans()}")
print(f"|↓⟩ = {spin_down.trans()}")

# Superposição
psi_plus = (spin_up + spin_down).unit()   # |+⟩ = (|↑⟩ + |↓⟩)/√2
psi_minus = (spin_up - spin_down).unit()  # |−⟩ = (|↑⟩ - |↓⟩)/√2

print(f"|+⟩ = {psi_plus.trans()}")
print(f"|−⟩ = {psi_minus.trans()}")

# ============================================================
# 2. Operadores de Spin
# ============================================================

Sx = sigmax() / 2  # Sx = σx/2
Sy = sigmay() / 2  # Sy = σy/2
Sz = sigmaz() / 2  # Sz = σz/2

print("\n=== Operadores de Spin ===")
print(f"Sx = {Sx}")
print(f"Sy = {Sy}")
print(f"Sz = {Sz}")

# ============================================================
# 3. Hamiltoniano em Campo Magnético
# ============================================================

# Campo magnético B = (Bx, 0, Bz)
Bz = 1.0   # Componente z (T)
Bx = 0.5   # Componente x (T)
gamma = 1.0  # Razão giromagnética (simplificado)

# Hamiltoniano: H = -γ(Sx*Bx + Sz*Bz)
H = -gamma * (Sx * Bx + Sz * Bz)

print(f"\n=== Hamiltoniano ===")
print(f"H = -γ(Sx·Bx + Sz·Bz)")
print(f"H = {H}")

# ============================================================
# 4. Evolução Temporal
# ============================================================

# Estado inicial: |↑⟩
psi0 = spin_up

# Tempo de evolução
tlist = np.linspace(0, 10, 200)

# Evolução unitária
result = sesolve(H, psi0, tlist, [Sx, Sy, Sz])

# Expectation values
exp_Sx = result.expect[0]
exp_Sy = result.expect[1]
exp_Sz = result.expect[2]

# ============================================================
# 5. Visualização
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 5.1 Evolução temporal das componentes de spin
ax1 = axes[0, 0]
ax1.plot(tlist, exp_Sx, 'r-', label='⟨Sx⟩', linewidth=2)
ax1.plot(tlist, exp_Sy, 'g-', label='⟨Sy⟩', linewidth=2)
ax1.plot(tlist, exp_Sz, 'b-', label='⟨Sz⟩', linewidth=2)
ax1.set_xlabel('Tempo', fontsize=12)
ax1.set_ylabel('Valor esperado', fontsize=12)
ax1.set_title('Evolução Temporal do Spin', fontsize=14)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# 5.2 Trajetória na esfera de Bloch
ax2 = axes[0, 1]
b = Bloch(fig=fig, axes=ax2)
b.add_vectors([exp_Sx[0]*2, 0, exp_Sz[0]*2])
b.add_points([exp_Sx*2, exp_Sy*2, exp_Sz*2])
b.render()
ax2.set_title('Esfera de Bloch', fontsize=14)

# 5.3 Probabilidades de medição
ax3 = axes[1, 0]
prob_up = 0.5 + exp_Sz
prob_down = 0.5 - exp_Sz
ax3.fill_between(tlist, 0, prob_up, alpha=0.4, color='blue', label='P(|↑⟩)')
ax3.fill_between(tlist, 0, prob_down, alpha=0.4, color='red', label='P(|↓⟩)')
ax3.set_xlabel('Tempo', fontsize=12)
ax3.set_ylabel('Probabilidade', fontsize=12)
ax3.set_title('Probabilidades de Medição', fontsize=14)
ax3.legend(fontsize=11)
ax3.grid(True, alpha=0.3)

# 5.4 Diagrama de níveis
ax4 = axes[1, 1]
ax4.axhline(y=0.5, color='blue', linewidth=3, label='|↑⟩ Sz = +ℏ/2')
ax4.axhline(y=-0.5, color='red', linewidth=3, label='|↓⟩ Sz = -ℏ/2')
ax4.annotate('', xy=(0.3, 0.45), xytext=(0.3, -0.45),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax4.text(0.35, 0, 'ΔE = γB', fontsize=14, color='green')
ax4.set_xlim(0, 1)
ax4.set_ylim(-1, 1)
ax4.set_title('Diagrama de Níveis', fontsize=14)
ax4.set_ylabel('Energia', fontsize=12)
ax4.legend(fontsize=11)
ax4.set_xticks([])

plt.tight_layout()
plt.savefig('assets/qubit_spin_simulation.png', dpi=150, bbox_inches='tight')
print("\n✅ Gráfico salvo em: assets/qubit_spin_simulation.png")

# ============================================================
# 6. Simulação da Porta CNOT (Two-Qubit)
# ============================================================

print("\n=== Simulação Two-Qubit: Porta CNOT ===")

# Estados base two-qubit
|00⟩ = tensor(basis(2,0), basis(2,0))
|01⟩ = tensor(basis(2,0), basis(2,1))
|10⟩ = tensor(basis(2,1), basis(2,0))
|11⟩ = tensor(basis(2,1), basis(2,1))

# Operadores
Sz1 = tensor(sigmaz(), qeye(2))  # Spin no qubit 1
Sz2 = tensor(qeye(2), sigmaz())  # Spin no qubit 2

# Hamiltoniano de acoplamento: H = J * S1·S2
J = 1.0  # Acoplamento de exchange
H_exchange = J * (tensor(sigmax(), sigmax()) + 
                  tensor(sigmay(), sigmay()) + 
                  tensor(sigmaz(), sigmaz()))

# Evolução para CNOT (t = π/(4J))
t_cnot = np.pi / (4 * J)
U_cnot = (-1j * H_exchange * t_cnot).expm()

# Testar CNOT: |00⟩ → |00⟩
psi_in = |00⟩
psi_out = U_cnot * psi_in
print(f"|00⟩ → {psi_out}")

# Testar CNOT: |10⟩ → |11⟩
psi_in = |10⟩
psi_out = U_cnot * psi_in
print(f"|10⟩ → {psi_out}")

print("\n✅ Simulação completa!")
