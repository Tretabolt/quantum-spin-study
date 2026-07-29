# 🔧 Guia Prático: Teste de Fundo de Cristal

## Visão Geral

Guia passo a passo para construir e executar um teste de spins em cristais comuns usando o **Método de Gouy** (balança de susceptibilidade magnética).

---

## Método 1: Balança de Gouy (Completo)

### Montagem do Artefato

```
        ┌─────────────────┐
        │   Suporte        │
        │   (argola)       │
        │       │          │
        │       │ fio      │
        │       │          │
        │   ┌───┴───┐      │
        │   │Cristal│      │
        │   └───────┘      │
        │                  │
        │  ┌─────┐ ┌─────┐│
        │  │  S  │ │  N  ││  ← Ímãs neodímio
        │  └─────┘ └─────┘│
        └─────────────────┘
```

### Materiais Necessários

| Item | Preço (R$) | Onde |
|------|-----------|------|
| Balança digital 0.01g | ~80 | Mercado Livre |
| Ímãs neodímio (2x) | ~60 | Mercado Livre |
| Fio de nylon/seda | ~5 | Armarinho |
| Suporte/argola | ~40 | Ferragem |
| Cristais variados | ~50 | Supermercado + Loja mineralógica |
| **Total** | **~R$ 235** | |

### Passo a Passo

#### 1. Preparar o Suporte
```bash
# Material: argola de cortina ou suporte de prateleira
# Fixar em superfície estável (mesa pesada)
# Prender fio de nylon (30-50 cm)
```

#### 2. Preparar as Amostras
```bash
# Cristais para testar:
1. Quartzo (rocha)         → Loja de cristais ou jardim
2. Sal grosso              → Supermercado
3. Açúcar cristal          → Supermercado
4. Magnetita               → Loja mineralógica (controle positivo)
5. Pirita                  → Loja mineralógica

# Preparação:
- Cortar/pesar ~5g de cada
- Medir dimensões (comprimento × largura)
- Embalar em tubo de ensaio ou papel
```

#### 3. Montar o Setup
```python
# Configuração:
distancia_imas = 5 cm      # Entre os dois ímãs
distancia_cristal = 2 cm   # Do cristal aos ímãs
campo_estimado = 0.3-0.5 T # Com neodímio 50mm
```

#### 4. Realizar as Medições
```python
# Para cada cristal:
1. Pesar SEM campo magnético (m0)
2. Posicionar ENTRE os ímãs
3. Pesar COM campo magnético (m1)
4. Calcular Δm = m1 - m0
5. Repetir 3 vezes para cada amostra
```

---

## Método 2: Teste Visual (Sem Equipamento)

### Método da Agulha Magnética

```
Materiais:
- Agulha de costura
- Ímã forte
- Fio fino
- Cristais variados

Procedimento:
1. Magnetizar a agulha (esfregar no ímã)
2. Suspender com fio (bússola improvisada)
3. Aproximar cada cristal da agulha
4. Observar: atrai, repele, ou não faz nada?
```

**Resultado:**
- Atração fraca → Paramagnético (tem spins!)
- Repulsão fraca → Diamagnético (sem spins)
- Nada → Material neutro

### Método da Moeda

```
Materiais:
- Moeda de metal (ferro/níquel)
- Ímã
- Superfície lisa (vidro)
- Cristais

Procedimento:
1. Colocar moeda sobre vidro
2. Posicionar ímã embaixo do vidro
3. Aproximar cristal por cima da moeda
4. Se cristal atrai moeda → Paramagnético
```

---

## Tabela de Resultados Esperados

```
Cristal       | Δm esperado | Tipo         | O que indica
--------------|-------------|--------------|------------------
Quartzo       | -0.001g     | Diamagnético | Sem spins livres
Sal (NaCl)    | -0.002g     | Diamagnético | Sem spins livres
Açúcar        | -0.001g     | Diamagnético | Sem spins livres
Granada       | +0.005g     | Paramagnético| Fe³⁺ presente
Pirita        | +0.003g     | Paramagnético| Fe²⁺ presente
Magnetita     | +0.500g     | Ferromagnético| spins alinhados
```

---

## Análise dos Dados

### Fórmula da Susceptibilidade

```
χ = (2·Δm·g) / (A·μ₀·H²)

Onde:
- Δm = variação de massa (kg)
- g = 9.81 m/s²
- A = área da seção (m²)
- μ₀ = 4π×10⁻⁷ T·m/A
- H = campo magnético (A/m)
```

### Classificação

```
χ < 0 → Diamagnético (sem spins desemparelhados)
χ > 0 → Paramagnético (spins desemparelhados presentes)
χ >> 1 → Ferromagnético (ordenamento magnético)
```

---

## Interpretação Física

### Por que cristais diamagnéticos não têm spins?

- **Quartzo (SiO₂):** Todos os elétrons emparelhados (Si⁴⁺ e O²⁻)
- **Sal (NaCl):** Na⁺ e Cl⁻ com camadas fechadas
- **Açúcar:** Molécula orgânica com ligações covalentes completas

### Por que cristais paramagnéticos têm spins?

- **Granada:** Contém Fe³⁺ (5 elétrons desemparelhados)
- **Pirita:** Contém Fe²⁺ (4 elétrons desemparelhados)
- **Magnetita:** Fe₃O₄ com spins ferromagnéticos

### Relação com o Experimento de Stern-Gerlach

- O experimento mostrou que spins são quantizados (↑ ou ↓)
- Em cristais, esses spins geram momento magnético
- A balança de Gouy mede esse momento magnético
- Portanto, estamos medindo diretamente a **quantização do momento angular**!

---

## Referências

- Kittel, C. *Introduction to Solid State Physics*
- Cullity & Graham. *Introduction to Magnetic Materials*
- Weil & Bolton. *Electron Paramagnetic Resonance*
