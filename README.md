# Quantum Spin Study

Estudo sobre junções túnel magnéticas (MTJ) e spintrônica.

## Estrutura

```
├── MATERIAIS.md    → Lista completa de materiais, fornecedores e custos
└── README.md       → Este arquivo
```

## Sobre

Este repositório contém documentação técnica para fabricação de junções túnel magnéticas baseadas em **CoFeB/MgO/CoFeB**, utilizadas em:

- **MRAM** (Memória Magnética de Acesso Aleatório)
- **Sensores Magnéticos**
- **Dispositivos Spintrônicos**

## Pilha MTJ

```
┌─────────────────────┐
│   Contato: Ta/W     │  ← Condutores
├─────────────────────┤
│   CoFeB (2-5 nm)    │  ← Camada livre
├─────────────────────┤
│   MgO (1-1.5 nm)    │  ← Barreira túnel
├─────────────────────┤
│   CoFeB (2-5 nm)    │  ← Camada fixa
├─────────────────────┤
│   Substrato Si/SiO₂ │
└─────────────────────┘
```

## Processo de Fabricação

1. **Deposição por sputtering** (DC/RF magnetron) — camada por camada em alto vácuo
2. **Litografia** — definição de padrões (UV para >1µm, e-beam para <100nm)
3. **Ion milling / RIE** — etching para definir a pilha MTJ

## Como Acessar Materiais no Brasil

Consulte [MATERIAIS.md](MATERIAIS.md) para:
- Fornecedores nacionais e internacionais
- Laboratórios com infraestrutura (LNNano, UNICAMP, UFRGS)
- Processo de importação com isenção de impostos
- Estimativas de custo

## Referências

- S. Ikeda et al., *Nature Materials* **9**, 721 (2010)
- Jung et al., *Nanoscale Magnetic Memory*
