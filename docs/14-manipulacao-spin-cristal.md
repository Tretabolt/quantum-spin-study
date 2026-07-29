# 🔮 Manipulação de Spins em Cristal (Sem Pó!)

## O que Você Quer

Manipular spins de um **cristal inteiro**, não pó. Isso é mais avançado — e mais próximo do que os físicos fazem de verdade!

---

## A Ideia

```
CRISTAL INTEIRO com spins
         │
         ↓
┌─────────────────────────────────┐
│  CAMPO MAGNÉTICO ESTÁTICO (B₀) │  ← define eixo de quantização
└────────────────┬────────────────┘
                 │
┌────────────────┴────────────────┐
│  CAMPO OSCILANTE (B₁)          │  ← micro-ondas excitam os spins
│  (bobina + gerador)             │
└────────────────┬────────────────┘
                 │
┌────────────────┴────────────────┐
│  DETECÇÃO                       │  ← mede absorção de energia
│  (diodo + multímetro)           │
└─────────────────────────────────┘
```

**Resultado:** Quando a frequência do campo oscilante coincide com a frequência de ressonância dos spins, o cristal absorve energia. Isso é **Ressonância Paramagnética Eletrônica (EPR)** — manipulação direta de spins!

---

## Cristais que Funcionam

### Melhores Opções (com spins "nativos")

| Cristal | Impureza | Spins | Facilidade | Custo |
|---------|----------|-------|------------|-------|
| **Rubi** (Al₂O₃:Cr³⁺) | Cr³⁺ | 3/2 | ⭐⭐⭐⭐⭐ | R$ 20-50 |
| **Safira azul** (Al₂O₃:Fe,Ti) | Fe³⁺, Ti⁴⁺ | 5/2 | ⭐⭐⭐⭐ | R$ 30-80 |
| **Ametista** (SiO₂:Fe³⁺) | Fe³⁺ | 5/2 | ⭐⭐⭐⭐ | R$ 15-40 |
| **Quartzo rosa** (SiO₂:Ti) | Ti⁴⁺ | variável | ⭐⭐⭐ | R$ 10-30 |
| **Turmalina** | Fe²⁺, Mn²⁺ | variável | ⭐⭐⭐ | R$ 20-50 |
| **Cristal de sal irradiado** | centros cor | 1/2 | ⭐⭐⭐ | R$ 5-15 |

### Melhor escolha: **RUBI**
- Cr³⁺ bem caracterizado
- Sinal forte e fácil de detectar
- Barato e disponível
- Frequência de ressonância conhecida

---

## Montagem do Experimento

### Diagrama Completo

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  MONTAGEM: EPR SIMPLIFICADO                                │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  GERADOR DE MICRO-ONDAS                             │   │
│  │  (magnetron de micro-ondas adaptado)                │   │
│  │  Frequência: ~2.45 GHz                             │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                          │ guia de ondas                    │
│  ┌───────────────────────┴─────────────────────────────┐   │
│  │  CAVIDADE RESSONANTE                                │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │                                             │    │   │
│  │  │         ┌───────────────┐                   │    │   │
│  │  │         │    CRISTAL    │ ← rubi, ametista  │    │   │
│  │  │         │   ┌─────┐    │                    │    │   │
│  │  │         │   │Cr³⁺│    │                    │    │   │
│  │  │         │   └─────┘    │                    │    │   │
│  │  │         └───────────────┘                   │    │   │
│  │  │                                             │    │   │
│  │  │  ┌───┐                           ┌───┐     │    │   │
│  │  │  │ B │ ← campo magnético estático│ B │     │    │   │
│  │  │  │ ₀ │    (ímãs permanentes)     │ ₀ │     │    │   │
│  │  │  └───┘                           └───┘     │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                          │                                  │
│  ┌───────────────────────┴─────────────────────────────┐   │
│  │  DETECTOR                                           │   │
│  │  (diodo Schottky + multímetro)                      │   │
│  │  Mede: potência absorvida pelo cristal              │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Materiais Necessários

### Fonte de Micro-ondas

| Opção | Material | Custo (R$) | Observação |
|-------|----------|------------|------------|
| **A** | Magnetron de micro-ondas velho | 50-100 | ⚠️ PERIGOSO - alta tensão |
| **B** | Módulo micro-ondas 2.4GHz (eBay) | 80-150 | Mais seguro |
| **C** | Gerador de RF + amplificador | 200-400 | Mais controle |

### Cavidade Ressonante

| Opção | Material | Custo (R$) |
|-------|----------|------------|
| **A** | Lata de alumínio (condutor) | 5-10 |
| **B** | Tubo de cobre | 20-40 |
| **C** | Cavidade comercial | 100-300 |

### Campo Magnético

| Opção | Material | Custo (R$) | Campo |
|-------|----------|------------|-------|
| **A** | Ímãs de neodímio (empilhados) | 100-200 | ~0.3T |
| **B** | Bobina + fonte de corrente | 200-400 | ~0.1-0.5T |
| **C** | Eletroímã de motor | 50-150 | ~0.2T |

### Detector

| Opção | Material | Custo (R$) |
|-------|----------|------------|
| **A** | Diodo Schottky + multímetro | 30-60 |
| **B** | Detector de RF comercial | 80-150 |
| **C** | RTL-SDR (radio definido por software) | 100-200 |

### Lista Completa de Compras

```
┌─────────────────────────────────────────────────────┐
│  LISTA DE COMPRAS - EPR CASERO                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  CRISTAL:                                           │
│  [ ] Rubi natural (5-10g)              R$ 30-50    │
│      ou Ametista (10g)                 R$ 15-30    │
│                                                     │
│  FONTES DE MICRO-ONDAS:                            │
│  [ ] Magnetron de micro-ondas velho    R$ 50-100   │
│  [ ] Transformador de alta tensão      (incluso)   │
│  [ ] Diodo de alta tensão              R$ 10       │
│  [ ] Capacitor de alta tensão          (incluso)   │
│                                                     │
│  CAVIDADE:                                          │
│  [ ] Tubo de cobre/alumínio 50mm       R$ 20-40    │
│  [ ] Conectores N-type                 R$ 30-50    │
│  [ ] Guia de ondas (cabo coaxial)      R$ 20-40    │
│                                                     │
│  CAMPO MAGNÉTICO:                                   │
│  [ ] Ímãs neodímio 50x50x25 (4x)      R$ 120-200  │
│  [ ] Suporte de ferro                  R$ 20-40    │
│                                                     │
│  DETECTOR:                                          │
│  [ ] Diodo Schottky 1N5819            R$ 5-10     │
│  [ ] Multímetro digital               R$ 50-80    │
│  [ ] Capacitor 100pF                  R$ 2-5      │
│  [ ] Resistor 50Ω                    R$ 2-5      │
│                                                     │
│  CABOS E CONECTORES:                               │
│  [ ] Cabo coaxial RG58 (2m)           R$ 20-30    │
│  [ ] Conectores SMA/N                 R$ 20-40    │
│  [ ] Fios, solda, fita                R$ 20       │
│                                                     │
│  SEGURANÇA:                                        │
│  [ ] Luvas isolantes                  R$ 30-50    │
│  [ ] Óculos de proteção              R$ 20-30    │
│                                                     │
├─────────────────────────────────────────────────────┤
│  TOTAL ESTIMADO: R$ 400-800                        │
└─────────────────────────────────────────────────────┘
```

---

## Montagem Passo a Passo

### Etapa 1: Preparar a Cavidade

```
CAVIDADE EM TUBO DE COBRE:
┌─────────────────────────────────────┐
│  Tubo de cobre 50mm diâmetro       │
│  Comprimento: 60mm                  │
│                                     │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  │    ┌─────────────────┐      │    │
│  │    │    CRISTAL       │      │    │
│  │    │   (rubi)         │      │    │
│  │    └─────────────────┘      │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  Furos para acoplamento:            │
│  - Entrada: 10mm (conector N)      │
│  - Saída: 10mm (detector)          │
└─────────────────────────────────────┘
```

**Como fazer:**
1. Cortar tubo de cobre (60mm)
2. Soldar tampas nas extremidades
3. Furar para conectores de entrada e saída
4. Inserir cristal no centro
5. Conectar guia de ondas

### Etapa 2: Montar o Campo Magnético

```
CAMPO MAGNÉTICO COM ÍMÃS:
┌─────────────────────────────────────┐
│                                     │
│  ┌─────────────────────────────┐    │
│  │  Ímã 1 (N)    Ímã 2 (N)    │    │
│  └──────────┬──────────────────┘    │
│             │                        │
│         ┌───┴───┐                    │
│         │CRISTAL│                    │
│         └───────┘                    │
│             │                        │
│  ┌──────────┴──────────────────┐    │
│  │  Ímã 3 (S)    Ímã 4 (S)    │    │
│  └─────────────────────────────┘    │
│                                     │
│  Campo B₀ na vertical              │
│  Intensidade: ~0.3T com neodímio   │
│                                     │
└─────────────────────────────────────┘
```

**Posicionamento:**
- Ímãs em configuração de Halbach (campo concentrado)
- Distância do cristal: 2-3cm
- Campo perpendicular ao feixe de micro-ondas

### Etapa 3: Montar o Detector

```
DETECTOR SIMPLIFICADO:
┌─────────────────────────────────────┐
│                                     │
│  Entrada (da cavidade)             │
│       │                             │
│  ┌────┴────┐                        │
│  │ Diodo   │ ← Schottky 1N5819     │
│  │ Schottky│                        │
│  └────┬────┘                        │
│       │                             │
│  ┌────┴────┐                        │
│  │ R=50Ω   │ ← terminação          │
│  └────┬────┘                        │
│       │                             │
│  ┌────┴────┐                        │
│  │ C=100pF │ ← filtro              │
│  └────┬────┘                        │
│       │                             │
│  ┌────┴────┐                        │
│  │Multímetro│ ← mede tensão DC     │
│  └─────────┘                        │
│                                     │
│  Tensão ∝ potência absorvida       │
│                                     │
└─────────────────────────────────────┘
```

---

## Como Manipular os Spins

### Nível 1: Detectar Spins (EPR Passiva)

```
1. Ligar magnetron (micro-ondas)
2. Aplicar campo magnético B₀
3. Varrer B₀ lentamente (mover ímãs)
4. Monitorar detector
5. Quando hν = gμB·B₀ → absorção!
6. Queda no detector = ressonância = spins!
```

### Nível 2: Manipular Spins (EPR Ativa)

```
Para manipular (inverter, criar superposição):

1. Aplicar B₀ (define eixo z)
2. Aplicar pulso de micro-ondas B₁
   - Duração τ = π/(γB₁) → INVERSÃO (flip)
   - Duração τ = π/(2γB₁) → SUPERPOSIÇÃO

3. Resultado:
   - Spin ↑ → ↓ (inversão)
   - Spin ↑ → (↑+↓)/√2 (superposição)
```

### Nível 3: Medir Estado do Spin

```
Após manipulação:

1. Aplicar segundo pulso (rotação de leitura)
2. Medir absorção no detector
3. Absorção alta → spin em superposição
4. Absorção baixa → spin invertido
5. Absorção intermediária → parcialmente invertido
```

---

## Frequência de Ressonância

### Para Rubi (Cr³⁺)

```
Frequência de ressonância EPR:

f = (g·μB·B₀) / h

Onde:
- g ≈ 1.98 (fator g do Cr³⁺)
- μB = 9.274×10⁻²⁴ J/T (magneton de Bohr)
- h = 6.626×10⁻³⁴ J·s (Planck)
- B₀ = campo magnético (T)

Para B₀ = 0.35T:
f = (1.98 × 9.274e-24 × 0.35) / 6.626e-34
f ≈ 9.7 GHz (banda X)

Para B₀ = 0.12T:
f ≈ 3.3 GHz (banda S)
```

### Tabela de Frequências

```
Campo (T) | Frequência | Banda
----------|------------|------
0.05      | 1.4 GHz    | L
0.12      | 3.3 GHz    | S
0.25      | 7.0 GHz    | C
0.35      | 9.7 GHz    | X
0.50      | 14.0 GHz   | Ku
```

---

## Segurança

### ⚠️ PERIGO: Magnetron de Micro-ondas

```
ALTA TENSÃO: 2000-4000V
CORRENTE MORTAL: 500mA+

NUNCA:
❌ Abrir magnetron ligado
❌ Tocar componentes com máquina ligada
❌ Operar sem luvas isolantes
❌ Trabalhar sozinho

SEMPRE:
✅ Desligar e esperar 5 minutos antes de mexer
✅ Usar luvas isolantes
✅ Ter alguém por perto
✅ Usar óculos de proteção
```

### Alternativa Mais Segura

```
Em vez de magnetron:
├── Usar módulo de RF 2.4GHz (mais seguro)
├── Ou gerador de sinais + amplificador
├── Custo: ~R$ 200-400
└── Muito mais controlável e seguro
```

---

## Resultado Esperado

```
QUANDO ENCONTRAR A RESSONÂNCIA:

Detector (multímetro)
    │
    │    ┌───┐
    │    │   │
    │────┘   └────
    │
    └──────────────→ Campo magnético (B₀)
    
         B_resonância
         
    Queda no sinal = spins absorvendo energia!
    
    Isso é manipulação de spins:
    - Micro-ondas excitam os spins
    - Spins absorvem energia
    - Detector vê a absorção
```

---

## Checklist Final

```
COMPONENTES:
[ ] Cristal com spins (rubi ou ametista)
[ ] Fonte de micro-ondas (magnetron ou módulo RF)
[ ] Cavidade ressonante (tubo de cobre)
[ ] Ímãs para campo B₀
[ ] Detector (diodo + multímetro)
[ ] Cabos e conectores

MONTAGEM:
[ ] Cavidade montada com cristal
[ ] Campo magnético posicionado
[ ] Detector conectado
[ ] Tudo testado sem potência

EXPERIMENTO:
[ ] Ligar fonte de micro-ondas (BAIXA POTÊNCIA)
[ ] Varrer campo magnético
[ ] Monitorar detector
[ ] Encontrar ressonância
[ ] Registrar frequência e campo
[ ] Manipular spins (pulsos)

ANÁLISE:
[ ] Calcular fator g
[ ] Comparar com literatura
[ ] Documentar resultados
[ ] Publicar no GitHub
```

---

## Próximo Passo

**Me diz:**
1. **Já tem micro-ondas velho?** (para o magnetron)
2. **Prefere opção mais segura?** (módulo RF)
3. **Quer começar com o quê?**

Aí eu te guio em detalhes! 🔬
