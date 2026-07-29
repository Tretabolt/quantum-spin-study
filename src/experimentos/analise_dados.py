"""
Análise de Dados do Teste de Fundo de Cristal
===============================================
Analisa os resultados do experimento de susceptibilidade magnética
e calcula parâmetros de spin.

Autor: Estudo sobre quantização do momento angular
Data: 2026-07-29
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Constantes Físicas
# ============================================================

mu_0 = 4 * np.pi * 1e-7      # Permeabilidade do vácuo (T·m/A)
mu_B = 9.274e-24              # Magneton de Bohr (J/T)
g_e = 2.0023                  # Fator g do elétron
N_A = 6.022e23                # Número de Avogadro
k_B = 1.381e-23               # Constante de Boltzmann (J/K)

# ============================================================
# 2. Funções de Análise
# ============================================================

def calcular_susceptibilidade(delta_m, area, campo_H):
    """
    Calcula a susceptibilidade volumétrica usando o método de Gouy.
    
    Parâmetros:
    -----------
    delta_m : float
        Variação de massa (kg)
    area : float
        Área da seção transversal da amostra (m²)
    campo_H : float
        Intensidade do campo magnético (A/m)
    
    Retorna:
    --------
    chi : float
        Susceptibilidade volumétrica (adimensional)
    """
    g = 9.81  # m/s²
    chi = (2 * delta_m * g) / (area * mu_0 * campo_H**2)
    return chi

def classificar_material(chi):
    """
    Classifica o material baseado na susceptibilidade.
    
    Retorna:
    --------
    tipo : str
        Tipo do material
    spins : bool
        Se possui spins desemparelhados
    """
    if chi < -1e-6:
        return "Diamagnético", False
    elif chi > 1e-6 and chi < 1e-2:
        return "Paramagnético", True
    elif chi > 1e-2:
        return "Ferromagnético", True
    else:
        return "Não magnético", False

def estimar_spins_por_grama(chi_massa, massa_molar, n_atomos_formula):
    """
    Estima o número de spins desemparelhados por grama.
    
    Parâmetros:
    -----------
    chi_massa : float
        Susceptibilidade mássica (m³/kg)
    massa_molar : float
        Massa molar do material (kg/mol)
    n_atomos_formula : int
        Número de átomos por fórmula unitária
    
    Retorna:
    --------
    spins_por_grama : float
        Número estimado de spins por grama
    """
    # Lei de Curie: χ = (N·μ₀·μ²)/(3·k_B·T)
    # Para T = 300K
    T = 300
    mu_eff = np.sqrt(3 * k_B * T * chi_massa / (mu_0 * N_A / massa_molar))
    spins_por_grama = N_A / massa_molar
    return spins_por_grama, mu_eff

def curie_weiss(T, C, Tc=0):
    """
    Lei de Curie-Weiss: χ = C / (T - Tc)
    """
    return C / (T - Tc)

# ============================================================
# 3. Dados Experimentais (Exemplo)
# ============================================================

# Dados do experimento (preencher com dados reais)
experimentos = {
    "Quartzo": {
        "massa_g": 5.0,
        "comprimento_cm": 3.0,
        "largura_cm": 1.0,
        "delta_m_g": -0.0012,
        "campo_T": 0.4,
        "massa_molar": 60.08,  # g/mol
    },
    "Sal (NaCl)": {
        "massa_g": 5.0,
        "comprimento_cm": 3.0,
        "largura_cm": 1.0,
        "delta_m_g": -0.0025,
        "campo_T": 0.4,
        "massa_molar": 58.44,
    },
    "Açúcar": {
        "massa_g": 5.0,
        "comprimento_cm": 3.0,
        "largura_cm": 1.0,
        "delta_m_g": -0.0015,
        "campo_T": 0.4,
        "massa_molar": 342.30,
    },
    "Granada": {
        "massa_g": 5.0,
        "comprimento_cm": 2.0,
        "largura_cm": 1.5,
        "delta_m_g": +0.008,
        "campo_T": 0.4,
        "massa_molar": 497.75,
    },
    "Pirita": {
        "massa_g": 5.0,
        "comprimento_cm": 2.5,
        "largura_cm": 1.2,
        "delta_m_g": +0.005,
        "campo_T": 0.4,
        "massa_molar": 119.98,
    },
    "Magnetita": {
        "massa_g": 5.0,
        "comprimento_cm": 2.0,
        "largura_cm": 1.0,
        "delta_m_g": +0.850,
        "campo_T": 0.4,
        "massa_molar": 231.53,
    },
}

# ============================================================
# 4. Análise dos Resultados
# ============================================================

print("=" * 70)
print("ANÁLISE DE DADOS: TESTE DE FUNDO DE CRISTAL")
print("=" * 70)

resultados = []

for nome, dados in experimentos.items():
    # Converter unidades
    delta_m = dados["delta_m_g"] * 1e-3  # kg
    area = dados["largura_cm"] * 1e-2 * dados["comprimento_cm"] * 1e-2  # m²
    campo_H = dados["campo_T"] / mu_0  # A/m (aproximação)
    
    # Calcular susceptibilidade
    chi = calcular_susceptibilidade(delta_m, area, campo_H)
    
    # Classificar
    tipo, tem_spins = classificar_material(chi)
    
    # Salvar resultados
    resultados.append({
        "nome": nome,
        "chi": chi,
        "tipo": tipo,
        "tem_spins": tem_spins,
        "delta_m_g": dados["delta_m_g"],
    })
    
    print(f"\n--- {nome} ---")
    print(f"  Δm = {dados['delta_m_g']:+.4f} g")
    print(f"  χ = {chi:.2e}")
    print(f"  Tipo: {tipo}")
    print(f"  Spins desemparelhados: {'SIM' if tem_spins else 'NÃO'}")

# ============================================================
# 5. Visualização
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 5.1 Variação de massa
ax1 = axes[0, 0]
nomes = [r["nome"] for r in resultados]
delta_ms = [r["delta_m_g"] for r in resultados]
colors = ['blue' if d < 0 else 'red' for d in delta_ms]
bars = ax1.bar(nomes, delta_ms, color=colors, alpha=0.7, edgecolor='black')
ax1.set_ylabel('Δm (g)', fontsize=12)
ax1.set_title('Variação de Massa no Campo Magnético', fontsize=14)
ax1.axhline(y=0, color='black', linewidth=0.5)
ax1.grid(True, alpha=0.3, axis='y')
ax1.tick_params(axis='x', rotation=45)

# 5.2 Susceptibilidade
ax2 = axes[0, 1]
chis = [r["chi"] for r in resultados]
colors2 = ['blue' if c < 0 else 'red' for c in chis]
bars2 = ax2.bar(nomes, chis, color=colors2, alpha=0.7, edgecolor='black')
ax2.set_ylabel('χ (susceptibilidade)', fontsize=12)
ax2.set_title('Susceptibilidade Magnética', fontsize=14)
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.grid(True, alpha=0.3, axis='y')
ax2.tick_params(axis='x', rotation=45)

# 5.3 Classificação
ax3 = axes[1, 0]
tipos = [r["tipo"] for r in resultados]
tipo_colors = {"Diamagnético": "blue", "Paramagnético": "orange", 
               "Ferromagnético": "red", "Não magnético": "gray"}
bars3 = ax3.bar(nomes, [1]*len(nomes), 
                color=[tipo_colors[t] for t in tipos], alpha=0.7, edgecolor='black')
ax3.set_ylabel('Classificação', fontsize=12)
ax3.set_title('Tipo de Material', fontsize=14)
ax3.set_yticks([])
ax3.tick_params(axis='x', rotation=45)

# Legenda
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=c, label=t) for t, c in tipo_colors.items()]
ax3.legend(handles=legend_elements, loc='upper right')

# 5.4 Diagrama de spins
ax4 = axes[1, 1]
# Gráfico conceitual
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 10)
ax4.set_xticks([])
ax4.set_yticks([])

# Diamagnético (sem spins)
ax4.add_patch(plt.Circle((2, 7), 1.5, color='lightblue', alpha=0.5))
ax4.annotate('', xy=(2, 8.2), xytext=(2, 5.8),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax4.annotate('', xy=(2, 5.8), xytext=(2, 8.2),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax4.text(2, 4, 'Diamagnético\n(χ < 0)', ha='center', fontsize=10)
ax4.text(2, 9.5, '↑↓', ha='center', fontsize=16, fontweight='bold')

# Paramagnético (com spins)
ax4.add_patch(plt.Circle((5, 7), 1.5, color='lightyellow', alpha=0.5))
ax4.annotate('', xy=(5, 8.5), xytext=(5, 5.5),
            arrowprops=dict(arrowstyle='->', color='red', lw=3))
ax4.text(5, 4, 'Paramagnético\n(χ > 0)', ha='center', fontsize=10)
ax4.text(5, 9.5, '↑', ha='center', fontsize=16, fontweight='bold', color='red')

# Ferromagnético (spins alinhados)
ax4.add_patch(plt.Circle((8, 7), 1.5, color='lightyellow', alpha=0.5))
for i in range(3):
    for j in range(3):
        ax4.annotate('', xy=(7.2+i*0.8, 7.8), xytext=(7.2+i*0.8, 6.2),
                    arrowprops=dict(arrowstyle='->', color='darkred', lw=2))
ax4.text(8, 4, 'Ferromagnético\n(χ >> 1)', ha='center', fontsize=10)

ax4.set_title('Spins nos Materiais', fontsize=14)

plt.tight_layout()
plt.savefig('assets/analise_cristal_fundo.png', dpi=150, bbox_inches='tight')
print(f"\n✅ Gráfico salvo em: assets/analise_cristal_fundo.png")

# ============================================================
# 6. Relatório
# ============================================================

print("\n" + "=" * 70)
print("RELATÓRIO FINAL")
print("=" * 70)

print("\nResumo dos Resultados:")
print("-" * 50)
for r in resultados:
    print(f"  {r['nome']:15} | {r['tipo']:15} | Spins: {'✓' if r['tem_spins'] else '✗'}")

print("\nConclusão:")
print("-" * 50)
paramagneticos = [r for r in resultados if r['tem_spins']]
diamagneticos = [r for r in resultados if not r['tem_spins']]

print(f"  Materiais paramagnéticos (com spins): {len(paramagneticos)}")
for r in paramagneticos:
    print(f"    - {r['nome']}: provável impureza de metal de transição")

print(f"\n  Materiais diamagnéticos (sem spins): {len(diamagneticos)}")
for r in diamagneticos:
    print(f"    - {r['nome']}: todos os elétrons emparelhados")

print("\n  → Os cristais paramagnéticos contêm spins desemparelhados")
print("  → Esses spins vêm de impurezas (Fe³⁺, Mn²⁺, etc.)")
print("  → EPR pode detectar e identificar essas impurezas")
print("  → Mesmo cristais 'puros' têm spins detectáveis!")

print("\n✅ Análise completa!")
