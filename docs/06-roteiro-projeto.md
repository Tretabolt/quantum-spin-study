# 🚀 Roteiro de Projeto: Do Zero ao MRAM/Qubit

## Fase 1: Simulação (Custo Baixo)

### Ferramentas Gratuitas:
- **Quantum ESPRESSO** → cálculos DFT de estrutura eletrônica
- **Kwant** → transporte quântico em nanoestruturas
- **QuTiP (Python)** → simulação de qubits de spin
- **OOMMF** → simulação de dinâmica de spins magnéticos

### Exercícios Práticos:
1. Simular uma junção túnel CoFeB/MgO/CoFeB
2. Calcular TMR em função da espessura da barreira
3. Modelar um ponto quântico de 2 elétrons
4. Simular porta CNOT com acoplamento de exchange

### Instalação:
```bash
pip install qutip kwant numpy matplotlib
```

---

## Fase 2: Caracterização (Custo Médio)

### Equipamentos Acessíveis:
- **VSM** (Vibrating Sample Magnetometer) → magnetização
- **PPMS** (Physical Property Measurement System) → resistividade
- **AFM/MFM** → imagem de domínios magnéticos
- **EPR benchtop** → espectro de spin

### Materiais para Protótipo:
- Substrato Si/SiO₂ (wafer, ~$50)
- Alvos de sputtering: Co, Fe, B, MgO (~$500-$2000)
- Litografia: e-beam ou UV (~acesso a cleanroom)
- Caracterização: PPMS ou SQUID (~acesso universitário)

---

## Fase 3: Fabricação (Custo Alto)

### Infraestrutura Necessária:
- Sputtering system (deposição de filmes finos)
- E-beam lithography (nanolitografia)
- Ion milling (gravura)
- RTA (annealing térmico)
- Probe station (medidas elétricas)

### Parcerias Recomendadas:
- **Brasil:** LNLS, UNICAMP, USP, UFSC, LNNano, CBPF
- **Internacional:** imec, Leti, NIST, QuTech

---

## Recursos de Aprendizado

### Livros:
1. Griffiths, D.J. — *Introduction to Quantum Mechanics*
2. Awschalom, D.D. et al. — *Semiconductor Spintronics and Quantum Computation*
3. Bandyopadhyay, S. & Cahay, M. — *Introduction to Spintronics*

### Papers Fundamentais:
1. Loss & DiVincenzo (1998) — Qubits com quantum dots
2. Kane (1998) — Silicon-based quantum computer
3. Slonczewski (1996) — Spin-transfer torque
4. Degen et al. (2017) — Quantum sensing

### Online:
- [Qiskit Textbook](https://qiskit.org/learn/) — IBM
- [QuTiP Documentation](https://qutip.org/docs/latest/)
- [arXiv:cond-mat](https://arxiv.org/list/cond-mat.mtrl-sci/recent)
