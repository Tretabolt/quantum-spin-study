"""
Simulação de Junção Túnel Magnética (MTJ)
==========================================
Modela o efeito TMR (Tunnel Magnetoresistance) em uma junção CoFeB/MgO/CoFeB.

Autor: Estudo sobre quantização do momento angular
Data: 2026-07-29
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Parâmetros da Junção Túnel
# ============================================================

# Constantes físicas
hbar = 1.0545718e-34  # J·s
m_e = 9.10938e-31     # kg
e_charge = 1.602176e-19  # C

# Parâmetros da barreira MgO
phi_b = 0.5 * e_charge   # Altura da barreira (eV → J)
d_ox = 1.5e-9             # Espessura da barreira (m)

# Parâmetros das camadas magnéticas
P1 = 0.6   # Polarização da camada fixa
P2 = 0.6   # Polarização da camada livre

# ============================================================
# 2. Modelo de TMR
# ============================================================

def tmr_ratio(P1, P2):
    """
    Calcula a razão TMR usando o modelo de Jullière.
    
    TMR = (R_AP - R_P) / R_P = 2*P1*P2 / (1 - P1*P2)
    """
    return 2 * P1 * P2 / (1 - P1 * P2)

def resistance_parallel(R0, P1, P2):
    """Resistência no estado paralelo."""
    return R0 * (1 - P1 * P2)

def resistance_antiparallel(R0, P1, P2):
    """Resistência no estado antiparalelo."""
    return R0 * (1 + P1 * P2)

# ============================================================
# 3. Cálculos
# ============================================================

# Resistência base (sem polarização)
R0 = 1000  # Ohms

# Razão TMR
TMR = tmr_ratio(P1, P2)
print(f"=== Parâmetros da Junção Túnel ===")
print(f"Camada fixa: CoFeB (P = {P1})")
print(f"Barreira: MgO (d = {d_ox*1e9:.1f} nm)")
print(f"Camada livre: CoFeB (P = {P2})")
print(f"\nRazão TMR: {TMR*100:.1f}%")

# Resistências
R_P = resistance_parallel(R0, P1, P2)
R_AP = resistance_antiparallel(R0, P1, P2)
print(f"R_paralelo: {R_P:.1f} Ω")
print(f"R_antiparalelo: {R_AP:.1f} Ω")

# ============================================================
# 4. Curva I-V
# ============================================================

V = np.linspace(-1.0, 1.0, 200)  # Voltagem (V)

# Modelo simplificado: I = V/R
I_P = V / R_P      # Estado paralelo
I_AP = V / R_AP    # Estado antiparalelo

# ============================================================
# 5. Dependência com Espessura da Barreira
# ============================================================

d_range = np.linspace(0.5e-9, 3.0e-9, 100)  # Espessura (m)

# Coeficiente de tunelamento (WKB approximation)
kappa = np.sqrt(2 * m_e * phi_b) / hbar
T_tunnel = np.exp(-2 * kappa * d_range)

# TMR em função da espessura
TMR_vs_d = 2 * P1 * P2 * T_tunnel / (1 - P1 * P2 * T_tunnel)

# ============================================================
# 6. Visualização
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 6.1 Curva I-V
ax1 = axes[0, 0]
ax1.plot(V, I_P * 1e3, 'b-', linewidth=2, label='Paralelo (P)')
ax1.plot(V, I_AP * 1e3, 'r-', linewidth=2, label='Antiparalelo (AP)')
ax1.set_xlabel('Voltagem (V)', fontsize=12)
ax1.set_ylabel('Corrente (mA)', fontsize=12)
ax1.set_title('Curva I-V da Junção Túnel', fontsize=14)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# 6.2 TMR vs Espessura
ax2 = axes[0, 1]
ax2.plot(d_range * 1e9, TMR_vs_d * 100, 'g-', linewidth=2)
ax2.set_xlabel('Espessura da Barreira (nm)', fontsize=12)
ax2.set_ylabel('TMR (%)', fontsize=12)
ax2.set_title('TMR vs Espessura da Barreira', fontsize=14)
ax2.grid(True, alpha=0.3)

# 6.3 Diagrama de Energia
ax3 = axes[1, 0]
# Barreira
x_barrier = [0.3, 0.3, 0.7, 0.7]
y_barrier = [0, phi_b/e_charge, phi_b/e_charge, 0]
ax3.fill(x_barrier, y_barrier, alpha=0.4, color='orange', label='MgO')
ax3.axhline(y=0, color='blue', linewidth=2, label='CoFeB')
ax3.set_xlabel('Posição', fontsize=12)
ax3.set_ylabel('Energia (eV)', fontsize=12)
ax3.set_title('Diagrama de Energia da MTJ', fontsize=14)
ax3.legend(fontsize=11)
ax3.set_xlim(0, 1)
ax3.set_ylim(0, phi_b/e_charge * 1.5)
ax3.set_xticks([])

# 6.4 Representação dos Estados
ax4 = axes[1, 1]
# Estado Paralelo
ax4.subplot(121)
ax4.bar(['Camada Fixa', 'Camada Livre'], [1, 1], color=['blue', 'blue'])
ax4.set_title('Estado Paralelo\n(Baixa R)', fontsize=12)
ax4.set_ylim(0, 1.5)

# Estado Antiparalelo
ax4.subplot(122)
ax4.bar(['Camada Fixa', 'Camada Livre'], [1, -1], color=['blue', 'red'])
ax4.set_title('Estado Antiparalelo\n(Alta R)', fontsize=12)
ax4.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('assets/juncao_tunel_simulation.png', dpi=150, bbox_inches='tight')
print(f"\n✅ Gráfico salvo em: assets/juncao_tunel_simulation.png")
print(f"\n=== Simulação completa! ===")
