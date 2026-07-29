# 🧲 MRAM — Memória de Acesso Aleatório Magnético

## Visão Geral

MRAM é uma tecnologia de memória não-volátil que usa **propriedades magnéticas** (spin dos elétrons) em vez de carga elétrica para armazenar dados.

---

## Estrutura: Junção Túnel Magnética (MTJ)

```
┌─────────────────────┐
│  Camada Magnética    │ ← "Livre" (spin pode girar)
│  (livre)             │
├─────────────────────┤
│  Barreira de Óxido   │ ← Al₂O₃ ou MgO (~1-2 nm)
│  (túnel)             │
├─────────────────────┤
│  Camada Magnética    │ ← "Referência" (spin fixo)
│  (fixa)              │
└─────────────────────┘
```

### Materiais:
- **Camada fixa:** CoFeB (2-5 nm)
- **Barreira túnel:** MgO (1-1.5 nm)
- **Camada livre:** CoFeB (2-5 nm)
- **Contatos:** Ta/W (condutores)

---

## Princípio de Funcionamento

### Efeito TMR (Tunnel Magnetoresistance)

```
Estado "0" (paralelo):          Estado "1" (antiparalelo):

  ↑        ↑                      ↑        ↓
  │        │                      │        │
  ├────────┤                      ├────────┤
  │ MgO    │                      │ MgO    │
  ├────────┤                      ├────────┤
  │        │                      │        │
  ↑        ↑                      ↑        ↓

Baixa resistência                Alta resistência
Corrente flui                    Corrente dificulta
```

### Escrita por STT (Spin-Transfer Torque)
- Corrente polarizada em spin passa pela junção
- O spin dos elétrons transfere momento para a camada livre
- Se a corrente for forte o suficiente, inverte o spin da camada livre
- **Tempo de escrita:** ~10 ns

---

## Comparação com Outras Memórias

| Propriedade | DRAM | Flash | MRAM |
|---|---|---|---|
| Volatilidade | Volátil | Não-volátil | **Não-volátil** |
| Velocidade de leitura | ~10 ns | ~100 ns | **~10 ns** |
| Velocidade de escrita | ~10 ns | ~100 μs | **~10 ns** |
| Ciclos de escrita | ∞ | ~10⁵ | **~10¹⁵** |
| Densidade | Alta | Muito alta | Média |
| Consumo | Alto | Baixo | **Muito baixo** |
| Retenção | N/A | >10 anos | **>10 anos** |

---

## Parâmetros de Projeto

```
Diâmetro da célula: ~20-50 nm (nó atual)
Razão TMR: >200% (quanto maior, melhor)
Retenção: >10 anos (estabilidade térmica)
Escrita: ~10 ns (velocidade)
Densidade: ~1-16 Gbit (atual)
```

---

## Roteiro de Fabricação (Simplificado)

### Infraestrutura Necessária:
1. **Sputtering system** — deposição de filmes finos
2. **E-beam lithography** — nanolitografia
3. **Ion milling** — gravura
4. **RTA** — annealing térmico
5. **Probe station** — medidas elétricas

### Processo:
1. Depósito da camada fixa (CoFeB) por sputtering
2. Depósito da barreira (MgO) por sputtering reativo
3. Depósito da camada livre (CoFeB)
4. Litografia para definir padrões
5. Gravura ion milling
6. Annealing térmico (RTA) para cristalização
7. Conexões metálicas (Ta/W)

---

## Aplicações

- **Cache de CPU** (substituindo SRAM)
- **IoT e edge computing** (baixo consumo)
- **Armazenamento embarcado** (automotivo, aerospace)
- **Computação neuromórfica** (resistência variável)

---

## Empresas e Produtos

| Empresa | Produto | Densidade |
|---------|---------|-----------|
| Everspin | STT-MRAM | 1-16 Mbit |
| Samsung | Embedded MRAM | 28 nm |
| TSMC | eMRAM | 22 nm |
| Intel | Spin Transfer Torque | R&D |

---

## Referências

- Slonczewski, J.C. (1996). "Current-driven excitation of magnetic multilayers"
- Parkin, S.S.P. et al. (2004). "Giant tunnelling magnetoresistance at room temperature"
- Kent, A.D. & Worledge, D.C. (2015). "A new spin on magnetic memories"
