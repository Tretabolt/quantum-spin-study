# 🌀 Quantum Spin Study

Estudo sobre **quantização do momento angular**, **MRAM** (Memória de Acesso Aleatório Magnético), **computação quântica com spin** e o **experimento de Stern-Gerlach**.

---

## 📚 Conteúdo

### 1. [Experimento de Stern-Gerlach](docs/01-stern-gerlach.md)
- O experimento que revelou a natureza quântica do spin
- Aparelho experimental, fenômeno observado e interpretação

### 2. [Utilidade da Quantização do Momento Angular](docs/02-utilidade-quantizacao.md)
- Aplicações em física, química, tecnologia e medicina
- Estrutura atômica, espectroscopia, MRI, spintrônica

### 3. [MRAM — Memória de Acesso Aleatório Magnético](docs/03-mram.md)
- Estrutura de Junção Túnel Magnética (MTJ)
- Princípio de funcionamento: TMR e STT
- Comparação com DRAM e Flash
- Roteiro de fabricação

### 4. [Computação Quântica com Spin](docs/04-quantum-computing-spin.md)
- Qubits de spin em pontos quânticos
- Portas lógicas quânticas (Rₓ, Rᵧ, CNOT)
- Implementação prática: Si/SiGe heterostructures

### 5. [Medindo Spins em Cristais](docs/05-spin-medicao.md)
- Técnicas: EPR/ESR, NMR, Difração de Nêutrons, NV Center
- Exemplo prático: medindo spins de quartzo

### 6. [Roteiro de Projeto](docs/06-roteiro-projeto.md)
- Fase 1: Simulação (custo baixo)
- Fase 2: Caracterização (custo médio)
- Fase 3: Fabricação (custo alto)

---

## 🧪 Simulações

| Simulação | Descrição | Arquivo |
|-----------|-----------|---------|
| Qubit de Spin | Simulação de qubit com QuTiP | [simulacao_qubit.py](src/simulacoes/simulacao_qubit.py) |
| Junção Túnel | Modelo de MTJ e cálculo de TMR | [juncao_tunel.py](src/simulacoes/juncao_tunel.py) |
| Stern-Gerlach | Simulação do experimento | [stern_gerlach.py](src/simulacoes/stern_gerlach.py) |

---

## 📖 Referências

1. **Loss, D. & DiVincenzo, D.P.** (1998). "Quantum computation with quantum dots". *Physical Review A*, 57(1), 120.
2. **Stern, O. & Gerlach, W.** (1922). "Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld". *Zeitschrift für Physik*, 9, 349-352.
3. **Slonczewski, J.C.** (1996). "Current-driven excitation of magnetic multilayers". *Journal of Magnetism and Magnetic Materials*, 159, L1-L7.
4. **Awschalom, D.D. et al.** (2013). "Quantum Spintronics: Engineering and Manipulating Atom-Like Spins in Semiconductors". *Science*, 339(6124), 1174-1179.
5. **Degen, C.L. et al.** (2017). "Quantum sensing". *Reviews of Modern Physics*, 89(3), 035002.

---

## 🔧 Ferramentas Recomendadas

| Ferramenta | Uso | Instalação |
|------------|-----|------------|
| [QuTiP](https://qutip.org/) | Simulação de mecânica quântica | `pip install qutip` |
| [Quantum ESPRESSO](https://www.quantum-espresso.org/) | Cálculos DFT | Download no site |
| [Kwant](https://kwant-project.org/) | Transporte quântico | `pip install kwant` |
| [OOMMF](https://math.nist.gov/oommf/) | Dinâmica de spins | Download no site |

---

## 📝 Licença

Este repositório é para fins educacionais. Sinta-se livre para usar e contribuir.

---

*Estudo criado em 29 de julho de 2026*
