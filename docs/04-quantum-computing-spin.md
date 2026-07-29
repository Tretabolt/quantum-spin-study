# 💻 Computação Quântica com Spin

## Visão Geral

A computação quântica com spin usa o **spin de elétrons** como qubits. É uma das abordagens mais promissoras para computação quântica escalável.

---

## Qubit de Spin

### Conceito Básico
- Um **ponto quântico** (quantum dot) confina um único elétron
- O spin desse elétron é o qubit:
  ```
  |↑⟩ = |0⟩  (spin up)
  |↓⟩ = |1⟩  (spin down)
  ```

### Vantagens:
- **Longa coerência** (~ms em silício)
- **Tamanho nanométrico** (~10-100 nm)
- **Compatível com CMOS** (fabricação convencional)
- **Operação em temperatura** relativamente alta (~1K vs ~10mK)

---

## Implementação: Ponto Quântico em Si/SiGe

```
    ┌──────────────────────────┐
    │    Eletrodo de porta      │
    │  ┌───┐     ┌───┐        │
    │  │ QD│─────│QD │        │  QD = Ponto Quântico
    │  │ 1 │     │ 2 │        │  (quantum dot)
    │  └───┘     └───┘        │
    │    ↑          ↑          │
    │  spin ↑    spin ↓        │
    │                          │
    │  Substrato: Si/SiGe      │
    └──────────────────────────┘
```

### Materiais:
- **Substrato:** Si/SiGe heterostructure
- **Portas:** Al/Al₂O₃ (eletrodos de confinamento)
- **Reservatório:** 2DEG (gás de elétrons 2D)

### Condições Operacionais:
- **Temperatura:** ~10-50 mK (dilution refrigerator)
- **Campo magnético:** ~0.1-1 T
- **Controle:** voltagens de porta (~mV)
- **Medição:** corrente de spin (~pA-nA)

---

## Portas Lógicas Quânticas

### Single-Qubit: Rotação de Spin

```python
# Porta de rotação Rₓ(θ)
Rₓ(θ) = cos(θ/2)·I - i·sin(θ/2)·σₓ

# Exemplos:
Rₓ(π) = -iσₓ  # Porta X (NOT quântico)
Rₓ(π/2) = Hadamard-like
```

**Implementação física:**
- Pulso de micro-ondas na frequência de Larmor
- ESR (Ressonância de Spin Eletrônico)
- Frequência típica: ~10-40 GHz

### Two-Qubit: Porta CNOT

```python
# Hamiltoniano de acoplamento
H = J(t) · S₁·S₂

# Onde J(t) é controlado pela voltagem da porta
# Quando J·t = π/4 → CNOT gate
```

**Implementação física:**
- Acoplamento de exchange entre dois spins vizinhos
- Controlado pela voltagem de uma porta de barreira
- Tempo de operação: ~1-100 ns

---

## Circuitos Quânticos com Spin

### Exemplo: Estado de Bell
```
|00⟩ → [H] → [CNOT] → (|00⟩ + |11⟩)/√2

Passo 1: H em qubit 1 → (|0⟩ + |1⟩)/√2 ⊗ |0⟩
Passo 2: CNOT → (|00⟩ + |11⟩)/√2
```

### Exemplo: Teleporte Quântico
```
|ψ⟩ ──●──[H]──M──┐
|0⟩ ──⊕───────M──┤
|0⟩ ─────────────⊕──|ψ⟩
```

---

## Métricas de Performance

| Métrica | Estado Atual | Meta |
|---------|-------------|------|
| Coerência T₂* | ~10 μs (Si) | >1 ms |
| Fidelidade single-qubit | ~99.9% | >99.99% |
| Fidelidade two-qubit | ~99% | >99.9% |
| Qubits conectados | ~6-12 | >1000 |
| Temperatura de operação | ~10 mK | ~1 K |

---

## Empresas e Pesquisadores

| Empresa/Instituição | Abordagem |
|---------------------|-----------|
| Intel | Si/SiGe quantum dots |
| QuTech (Delft) | Si/SiGe e GaAs |
| UNSW (Austrália) | Si:P (fósforo em silício) |
| Google | SQUID-based (outra abordagem) |
| IBM | Supercondutor (outra abordagem) |

---

## Referências Fundamentais

1. **Loss, D. & DiVincenzo, D.P.** (1998). "Quantum computation with quantum dots". *Physical Review A*, 57(1), 120.
2. **Kane, B.E.** (1998). "A silicon-based nuclear spin quantum computer". *Nature*, 393, 133-137.
3. **Vandersypen, L.M.K. et al.** (2017). "Interfacing spin qubits in quantum dots and donors". *npj Quantum Information*, 3, 34.
4. **Zwanenburg, F.A. et al.** (2013). "Silicon quantum electronics". *Reviews of Modern Physics*, 85(3), 961.
