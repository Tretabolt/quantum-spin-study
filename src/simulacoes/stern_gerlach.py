"""
Simulação do Experimento de Stern-Gerlach
==========================================
Simula a deflexão de átomos de prata em campo magnético não-uniforme.

Autor: Estudo sobre quantização do momento angular
Data: 2026-07-29
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.patches as mpatches

# ============================================================
# 1. Parâmetros do Experimento
# ============================================================

# Constantes
mu_B = 9.274e-24  # Magneton de Bohr (J/T)
m_Ag = 1.79e-25  # Massa do átomo de prata (kg)
v_z = 500        # Velocidade do feixe (m/s)
L = 0.2          # Comprimento do ímã (m)
dB_dz = 1.0      # Gradiente do campo (T/m)

# Números quânticos
s = 1/2          # Spin do elétron
ms_values = [-1/2, 1/2]  # Valores possíveis de ms

print("=== Experimento de Stern-Gerlach ===")
print(f"Átomo: Prata (Ag)")
print(f"Spin: s = {s}")
print(f"Valores de ms: {ms_values}")
print(f"Gradiente de campo: {dB_dz} T/m")

# ============================================================
# 2. Cálculo da Deflexão
# ============================================================

def calc_deflection(ms, m_atom, v, L, dB_dz, g_s=2.0023):
    """
    Calcula a deflexão de um átomo no campo não-uniforme.
    
    Fz = ms * g_s * mu_B * (dB/dz)
    Δz = (1/2) * (Fz/m) * (L/v)²
    """
    Fz = ms * g_s * mu_B * dB_dz
    t = L / v
    delta_z = 0.5 * (Fz / m_atom) * t**2
    return delta_z, Fz

# Calcular deflexões
for ms in ms_values:
    delta_z, Fz = calc_deflection(ms, m_Ag, v_z, L, dB_dz)
    print(f"\nms = {ms:+.1f}:")
    print(f"  Força Fz = {Fz:.2e} N")
    print(f"  Deflexão Δz = {delta_z*1e3:.2f} mm")

# ============================================================
# 3. Simulação Monte Carlo (Feixe Clássico vs Quântico)
# ============================================================

N_atoms = 10000  # Número de átomos no feixe

# ---- Cenário Clássico (sem quantização) ----
np.random.seed(42)
# Orientações aleatórias do momento magnético (distribuição uniforme)
theta_classical = np.random.uniform(0, np.pi, N_atoms)
ms_classical = np.cos(theta_classical) * s  # projeção contínua

deflections_classical = []
for ms in ms_classical:
    delta_z, _ = calc_deflection(ms, m_Ag, v_z, L, dB_dz)
    deflections_classical.append(delta_z * 1e3)

# ---- Cenário Quântico (spin quantizado) ----
ms_quantum = np.random.choice(ms_values, N_atoms)

deflections_quantum = []
for ms in ms_quantum:
    delta_z, _ = calc_deflection(ms, m_Ag, v_z, L, dB_dz)
    deflections_quantum.append(delta_z * 1e3)

# ============================================================
# 4. Visualização
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 4.1 Resultado Clássico
ax1 = axes[0, 0]
ax1.hist(deflections_classical, bins=50, color='gray', alpha=0.7, edgecolor='black')
ax1.set_xlabel('Deflexão (mm)', fontsize=12)
ax1.set_ylabel('Contagem', fontsize=12)
ax1.set_title('Previsão Clássica\n(Faixa Borrada)', fontsize=14)
ax1.grid(True, alpha=0.3)

# 4.2 Resultado Quântico
ax2 = axes[0, 1]
ax2.hist(deflections_quantum, bins=50, color='blue', alpha=0.7, edgecolor='black')
ax2.set_xlabel('Deflexão (mm)', fontsize=12)
ax2.set_ylabel('Contagem', fontsize=12)
ax2.set_title('Resultado Quântico\n(Dois Pontos)', fontsize=14)
ax2.grid(True, alpha=0.3)

# 4.3 Diagrama do Aparelho
ax3 = axes[1, 0]
# Fonte
ax3.add_patch(mpatches.Rectangle((0, 0.4), 0.1, 0.2, color='gray'))
ax3.text(0.05, 0.5, 'Fonte\n(Ag)', ha='center', va='center', fontsize=9)
# Ímã
ax3.add_patch(mpatches.FancyBboxPatch((0.3, 0.6), 0.3, 0.15, 
                                       boxstyle="round,pad=0.02", color='blue', alpha=0.7))
ax3.text(0.45, 0.675, 'S', ha='center', va='center', fontsize=14, color='white', fontweight='bold')
ax3.add_patch(mpatches.FancyBboxPatch((0.3, 0.25), 0.3, 0.15, 
                                       boxstyle="round,pad=0.02", color='red', alpha=0.7))
ax3.text(0.45, 0.325, 'N', ha='center', va='center', fontsize=14, color='white', fontweight='bold')
# Detector
ax3.add_patch(mpatches.Rectangle((0.85, 0.1), 0.05, 0.8, color='lightgray'))
ax3.text(0.875, 0.5, 'Detector', ha='center', va='center', fontsize=9, rotation=90)
# Trajetórias
ax3.annotate('', xy=(0.85, 0.7), xytext=(0.1, 0.5),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2, connectionstyle='arc3,rad=0.1'))
ax3.annotate('', xy=(0.85, 0.3), xytext=(0.1, 0.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2, connectionstyle='arc3,rad=-0.1'))
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.set_title('Diagrama do Aparelho', fontsize=14)
ax3.set_xticks([])
ax3.set_yticks([])

# 4.4 Comparação Lado a Lado
ax4 = axes[1, 1]
ax4.hist(deflections_classical, bins=50, color='gray', alpha=0.5, label='Clássico', density=True)
ax4.hist(deflections_quantum, bins=50, color='blue', alpha=0.5, label='Quântico', density=True)
ax4.set_xlabel('Deflexão (mm)', fontsize=12)
ax4.set_ylabel('Densidade', fontsize=12)
ax4.set_title('Comparação: Clássico vs Quântico', fontsize=14)
ax4.legend(fontsize=11)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('assets/stern_gerlach_simulation.png', dpi=150, bbox_inches='tight')
print(f"\n✅ Gráfico salvo em: assets/stern_gerlach_simulation.png")

# ============================================================
# 5. Análise dos Resultados
# ============================================================

print("\n=== Análise dos Resultados ===")
print(f"Média clássica: {np.mean(deflections_classical):.2f} mm")
print(f"Desvio padrão clássico: {np.std(deflections_classical):.2f} mm")
print(f"Média quântica: {np.mean(deflections_quantum):.2f} mm")
print(f"Desvio padrão quântico: {np.std(deflections_quantum):.2f} mm")
print(f"\nSeparação entre picos quânticos: {abs(np.mean([d for d, ms in zip(deflections_quantum, ms_quantum) if ms > 0]) - np.mean([d for d, ms in zip(deflections_quantum, ms_quantum) if ms < 0])):.2f} mm")
print("\n✅ Simulação completa!")
