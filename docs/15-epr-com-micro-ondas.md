# 🔬 EPR Caseiro com Micro-ondas Desmontado

## Usando Peças do Micro-ondas

Seu micro-ondas tem tudo que precisamos!

```
PEÇAS DO MICRO-ONDAS QUE VAMOS USAR:
┌─────────────────────────────────────────────┐
│                                             │
│  ┌─────────────┐   MAGNETRON               │
│  │ ▓▓▓▓▓▓▓▓▓▓ │   - Gera micro-ondas      │
│  │ ▓▓▓▓▓▓▓▓▓▓ │   - 2.45 GHz              │
│  └──────┬──────┘   - ~800W (vamos usar     │
│         │               menos!)             │
│  ┌──────┴──────┐                            │
│  │ CAPACITOR   │   CAPACITOR DE ALTA       │
│  │  ████  ████ │   TENSÃO                  │
│  └─────────────┘   - 2100V                 │
│                     - CUIDADO!              │
│  ┌─────────────┐                            │
│  │ TRANSFORMADOR│  TRANSFORMADOR            │
│  │  ┌───┐┌───┐ │  - Fornece energia        │
│  │  │   ││   │ │  - 2100V saída            │
│  └──┴───┘┴───┴─┘                            │
│                                             │
│  ┌─────────────┐                            │
│  │  DIODO DE   │  DIODO DE ALTA TENSÃO     │
│  │  ALTA TEN.  │  - Retifica AC→DC         │
│  └─────────────┘                            │
│                                             │
│  ┌─────────────┐                            │
│  │  GUIA DE    │  GUIA DE ONDAS            │
│  │  ONDAS      │  - Conduz micro-ondas     │
│  │  ═════════  │  - Metal oco              │
│  └─────────────┘                            │
│                                             │
│  ┌─────────────┐                            │
│  │  CÂMARA     │  CAVIDADE                  │
│  │  (metal)    │  - Onde colocamos o cristal│
│  └─────────────┘                            │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Diagrama da Montagem Final

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   EPR CASEIRO - VISTA SUPERIOR                                 │
│                                                                 │
│   ┌──────────┐    ┌──────────┐    ┌──────────────────────┐     │
│   │MAGNETRON │───→│GUIA DE   │───→│    CAVIDADE          │     │
│   │ (2.45GHz)│    │ONDAS     │    │  ┌────────────────┐  │     │
│   └──────────┘    └──────────┘    │  │                │  │     │
│                                    │  │   CRISTAL      │  │     │
│                                    │  │   (rubi)       │  │     │
│                                    │  │                │  │     │
│                                    │  └────────────────┘  │     │
│                                    └──────────┬───────────┘     │
│                                               │                  │
│                                    ┌──────────┴───────────┐     │
│                                    │     DETECTOR         │     │
│                                    │  ┌────────────────┐  │     │
│                                    │  │ Diodo Schottky │  │     │
│                                    │  └───────┬────────┘  │     │
│                                    │          │           │     │
│                                    │  ┌───────┴────────┐  │     │
│                                    │  │  Multímetro    │  │     │
│                                    │  │  (tensão DC)   │  │     │
│                                    │  └────────────────┘  │     │
│                                    └──────────────────────┘     │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                   CAMPO MAGNÉTICO                       │   │
│   │                                                         │   │
│   │      ┌─────────────────────────────────────┐            │   │
│   │      │  ÍMÃ 1 (N)              ÍMÃ 2 (N)   │            │   │
│   │      └──────────────────┬──────────────────┘            │   │
│   │                         │                                │   │
│   │                    ┌────┴────┐                           │   │
│   │                    │ CRISTAL │                           │   │
│   │                    └────┬────┘                           │   │
│   │                         │                                │   │
│   │      ┌──────────────────┴──────────────────┐            │   │
│   │      │  ÍMÃ 3 (S)              ÍMÃ 4 (S)   │            │   │
│   │      └─────────────────────────────────────┘            │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Passo 1: Desmontar o Micro-ondas (CUIDADO!)

### ⚠️ SEGURANÇA PRIMEIRO

```
ANTES DE TUDO:
┌─────────────────────────────────────────────┐
│  ⚠️ DESCARREGAR O CAPACITOR!               │
│                                             │
│  O capacitor armazena 2100V - MORTAL!       │
│                                             │
│  COMO DESCARREGAR:                          │
│  1. Desligar da tomada                     │
│  2. Esperar 5 minutos                      │
│  3. Usar chave de fenda isolada            │
│  4. Curto-circuitar os terminais           │
│  5. Verificar com multímetro               │
│                                             │
│  ⚠️ NUNCA toque nos terminais com a máquina│
│     ligada ou recentemente ligada!         │
└─────────────────────────────────────────────┘
```

### Peças para Retirar

```
1. MAGNETRON
   ├── Localização: atrás, dentro de gabinete metálico
   ├── Fixação: parafusos
   ├── Conexão: guia de ondas
   └── ⚠️ Não danificar o filamento!

2. TRANSFORMADOR DE ALTA TENSÃO
   ├── Localização: fundo do micro-ondas
   ├── Fixação: parafusos na base
   ├── Conexão: fios de alimentação
   └── ⚠️ Pesado! (~5kg)

3. CAPACITOR DE ALTA TENSÃO
   ├── Localização: perto do transformador
   ├── Fixação: bracket metálico
   ├── ⚠️ DESCARREGAR ANTES!
   └── Não é essencial (podemos usar fonte externa)

4. DIODO DE ALTA TENSÃO
   ├── Localização: perto do capacitor
   ├── Fixação: fios
   └── Retificador

5. GUIA DE ONDAS
   ├── Localização: tubo metálico saindo do magnetron
   ├── Conexão: magnetron → câmara
   └── Manter inteiro!

6. CÂMARA (PARTE INTERNA)
   ├── Localização: dentro do micro-ondas
   ├── Material: metal (reflete micro-ondas)
   └── Podemos usar como cavidade!
```

---

## Passo 2: Preparar a Cavidade

### Opção A: Usar a Câmara do Micro-ondas (Mais Fácil)

```
CAVIDADE = CÂMARA DO MICRO-ONDAS
┌─────────────────────────────────────┐
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  │   ┌─────────────────────┐   │    │
│  │   │                     │   │    │
│  │   │      CRISTAL        │   │    │
│  │   │   ┌─────────────┐   │   │    │
│  │   │   │    RUBI      │   │   │    │
│  │   │   └─────────────┘   │   │    │
│  │   │                     │   │    │
│  │   └─────────────────────┘   │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  ┌──────────┐    ┌──────────────┐   │
│  │ ENTRADA  │    │    SAÍDA     │   │
│  │ (guia de │    │  (detector)  │   │
│  │  ondas)  │    │              │   │
│  └──────────┘    └──────────────┘   │
│                                     │
└─────────────────────────────────────┘
```

### Opção B: Cavidade Menor (Mais Eficiente)

```
CAVIDADE EM TUBO DE METAL
┌─────────────────────────────────────┐
│  Tubo de alumínio ou cobre          │
│  Diâmetro: 50-80mm                  │
│  Comprimento: 60-100mm              │
│                                     │
│  ┌─────────────────────────────┐    │
│  │  ┌─────────────────────┐    │    │
│  │  │                     │    │    │
│  │  │      CRISTAL        │    │    │
│  │  │   ┌─────────────┐   │    │    │
│  │  │   │    RUBI      │   │    │    │
│  │  │   └─────────────┘   │    │    │
│  │  │                     │    │    │
│  │  └─────────────────────┘    │    │
│  └─────────────────────────────┘    │
│                                     │
│  Furos para acoplamento:            │
│  - Entrada: 10mm (conector)        │
│  - Saída: 10mm (detector)          │
└─────────────────────────────────────┘
```

---

## Passo 3: Conectar o Magnetron

### Circuito de Alimentação

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  CIRCUITO DE ALIMENTAÇÃO DO MAGNETRON                       │
│                                                             │
│  ┌─────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │ TOMADA  │───→│TRANSFORMADOR│───→│  MAGNETRON  │         │
│  │ 220V    │    │  DE ALTA    │    │             │         │
│  └─────────┘    │  TENSÃO     │    │  ┌───────┐  │         │
│                 └──────┬──────┘    │  │FILAMENTO│ │         │
│                        │           │  └───────┘  │         │
│                        │           │             │         │
│                 ┌──────┴──────┐    │  ┌───────┐  │         │
│                 │   DIODO     │    │  │ANTENA │  │──→ ondas│
│                 │   RETIFICADOR│   │  └───────┘  │         │
│                 └──────┬──────┘    └─────────────┘         │
│                        │                                    │
│                 ┌──────┴──────┐                             │
│                 │  CAPACITOR  │                             │
│                 │  (filtragem)│                             │
│                 └─────────────┘                             │
│                                                             │
│  ⚠️ ATENÇÃO:                                               │
│  - Filamento: 3.3V AC (baixa tensão)                       │
│  - Anodo: 2100V DC (ALTA TENSÃO - PERIGOSO!)              │
│  - Corrente: ~300mA                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Como Conectar

```
PASSO A PASSO:
┌─────────────────────────────────────────────┐
│                                             │
│  1. CONECTAR TRANSFORMADOR À REDE           │
│     ├── Fio fase → terminal primário        │
│     ├── Fio neutro → terminal primário      │
│     └── Fio terra → carcaça                 │
│                                             │
│  2. CONECTAR SAÍDA DO TRANSFORMADOR         │
│     ├── Terminal de alta tensão → diodo     │
│     └── Terminal de filamento → magnetron   │
│                                             │
│  3. CONECTAR DIODO                          │
│     ├── Saída → capacitor (+)               │
│     └── Retorno → magnetron (terra)         │
│                                             │
│  4. CONECTAR CAPACITOR                      │
│     ├── (+) → diodo                         │
│     └── (-) → terra/magnetron              │
│                                             │
│  5. CONECTAR MAGNETRON                      │
│     ├── Filamento → transformador           │
│     ├── Anodo → capacitor (+)              │
│     └── Carcaça → terra                    │
│                                             │
└─────────────────────────────────────────────┘
```

---

## Passo 4: Montar o Campo Magnético

### Configuração com 4 Ímãs

```
VISTA FRONTAL:
┌─────────────────────────────────────┐
│                                     │
│  ┌─────────────────────────────┐    │
│  │  ÍMÃ 1 (N)    ÍMÃ 2 (N)    │    │
│  │  50x50x25mm   50x50x25mm   │    │
│  └──────────────┬──────────────┘    │
│                 │                    │
│            ┌────┴────┐               │
│            │ CRISTAL │               │
│            │  (rubi) │               │
│            └────┬────┘               │
│                 │                    │
│  ┌──────────────┴──────────────┐    │
│  │  ÍMÃ 3 (S)    ÍMÃ 4 (S)    │    │
│  │  50x50x25mm   50x50x25mm   │    │
│  └─────────────────────────────┘    │
│                                     │
│  Distância entre ímãs: 4-6cm       │
│  Campo no centro: ~0.3-0.5T        │
│                                     │
└─────────────────────────────────────┘
```

### Suporte para os Ímãs

```
MATERIAL: madeira, MDF, ou acrílico
┌─────────────────────────────────────┐
│                                     │
│  ┌─────────────────────────────┐    │
│  │  Placa superior             │    │
│  │  (com furos para ímãs)      │    │
│  └──────────────┬──────────────┘    │
│                 │                    │
│            parafusos                 │
│                 │                    │
│  ┌──────────────┴──────────────┐    │
│  │  Placa inferior             │    │
│  │  (com furos para ímãs)      │    │
│  └─────────────────────────────┘    │
│                                     │
│  Altura ajustável por parafusos    │
│                                     │
└─────────────────────────────────────┘
```

---

## Passo 5: Montar o Detector

### Circuito do Detector

```
┌─────────────────────────────────────────────┐
│  DETECTOR DE MICRO-ONDAS                    │
│                                             │
│  ENTRADA (da cavidade)                      │
│       │                                     │
│  ┌────┴────┐                                │
│  │  DIODO  │  Schottky 1N5819              │
│  │SCHOTTKY │  (baixa capacitância)          │
│  └────┬────┘                                │
│       │                                     │
│  ┌────┴────┐                                │
│  │ C=100pF │  Capacitor cerâmico           │
│  │  ┌───┐  │  (filtra RF, passa DC)        │
│  └──┴───┴──┘                                │
│       │                                     │
│  ┌────┴────┐                                │
│  │ R=50Ω  │  Resistor de terminação        │
│  └────┬────┘                                │
│       │                                     │
│  ┌────┴────┐                                │
│  │MULTÍMETRO│  Mede tensão DC              │
│  │  (DCV)   │  ∝ potência absorvida        │
│  └─────────┘                                │
│                                             │
└─────────────────────────────────────────────┘
```

### Montagem Física

```
┌─────────────────────────────────────┐
│  ┌─────────────────────────────┐    │
│  │  Placa de circuito (perfboard)│   │
│  │                             │    │
│  │  ┌─────┐  ┌─────┐  ┌─────┐ │    │
│  │  │Diodo│  │ Cap │  │ Res │ │    │
│  │  └──┬──┘  └──┬──┘  └──┬──┘ │    │
│  │     └────────┴────────┘     │    │
│  │              │              │    │
│  │         Conector            │    │
│  │         (para multímetro)   │    │
│  └─────────────────────────────┘    │
│                                     │
│  Conectar com cabo coaxial         │
│  à saída da cavidade               │
└─────────────────────────────────────┘
```

---

## Passo 6: Montar o Cristal

### Cristais que Funcionam

```
MELHORES OPÇÕES:
┌─────────────────────────────────────────────┐
│                                             │
│  1. RUBI (Al₂O₃:Cr³⁺) ← MELHOR!          │
│     ├── Cr³⁺: spin 3/2                    │
│     ├── Fator g ≈ 1.98                     │
│     ├── Sinal forte                        │
│     └── Custo: R$ 20-50                    │
│                                             │
│  2. AMETISTA (SiO₂:Fe³⁺)                  │
│     ├── Fe³⁺: spin 5/2                    │
│     ├── Fator g ≈ 2.00                     │
│     ├── Sinal moderado                     │
│     └── Custo: R$ 15-40                    │
│                                             │
│  3. SAFIRA AZUL (Al₂O₃:Fe,Ti)             │
│     ├── Fe³⁺ + Ti⁴⁺                       │
│     ├── Sinal variável                     │
│     └── Custo: R$ 30-80                    │
│                                             │
│  4. CRISTAL DE SAL IRRADIADO               │
│     ├── Centros cor (F-centers)            │
│     ├── Spin 1/2                           │
│     └── Custo: R$ 5-15                     │
│                                             │
└─────────────────────────────────────────────┘
```

### Posicionamento do Cristal

```
CAVIDADE (vista lateral):
┌─────────────────────────────────────┐
│                                     │
│  ┌─────────────────────────────┐    │
│  │                             │    │
│  │  ┌─────────────────────┐    │    │
│  │  │                     │    │    │
│  │  │  ┌─────────────┐    │    │    │
│  │  │  │   CRISTAL    │    │    │    │
│  │  │  │   (rubi)     │    │    │    │
│  │  │  └─────────────┘    │    │    │
│  │  │                     │    │    │
│  │  └─────────────────────┘    │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  Posição: CENTRO da cavidade       │
│  Orientação: qualquer (campo       │
│  magnético define o eixo)          │
│                                     │
└─────────────────────────────────────┘
```

---

## Passo 7: FAZER O EXPERIMENTO!

### Procedimento Completo

```
ETAPA 1: VERIFICAÇÃO (10 min)
┌─────────────────────────────────────┐
│ [ ] Magnetron desconectado da rede  │
│ [ ] Capacitor descarregado          │
│ [ ] Cristal posicionado na cavidade │
│ [ ] Detector conectado              │
│ [ ] Ímãs posicionados               │
│ [ ] Multímetro no modo DCV          │
└─────────────────────────────────────┘

ETAPA 2: LIGAR (5 min)
┌─────────────────────────────────────┐
│ [ ] Conectar magnetron à rede       │
│ [ ] Verificar filamento (brilho)    │
│ [ ] Multímetro deve marcar tensão   │
│ [ ] Anotar valor inicial            │
└─────────────────────────────────────┘

ETAPA 3: BUSCAR RESSONÂNCIA (30 min)
┌─────────────────────────────────────┐
│ [ ] Mover ímãs lentamente           │
│ [ ] Monitorar multímetro            │
│ [ ] Procurar por QUEDA de tensão    │
│ [ ] Quando cair = RESSONÂNCIA!      │
│ [ ] Anotar posição dos ímãs         │
│ [ ] Medir distância entre eles      │
└─────────────────────────────────────┘

ETAPA 4: REGISTRAR (10 min)
┌─────────────────────────────────────┐
│ [ ] Fotografar posição dos ímãs     │
│ [ ] Medir campo com sensor Hall     │
│ [ ] Anotar tensão do detector       │
│ [ ] Repetir 3 vezes                 │
│ [ ] Calcular campo de ressonância   │
└─────────────────────────────────────┘
```

### O que Observar

```
MULTÍMETRO DURANTE O EXPERIMENTO:

Campo magnético aumentando →
┌─────────────────────────────────────────────────────┐
│                                                     │
│  Tensão                                             │
│    │                                                │
│    │  ─────────────┐                                │
│    │               │                                │
│    │               │                                │
│    │               └─────────────────────────────   │
│    │                                                │
│    └────────────────────────────────────────────→   │
│               B_ressonância       Campo (B₀)        │
│                                                     │
│  A tensão CAI quando:                               │
│  hν = g·μB·B₀                                      │
│                                                     │
│  Isso é RESSONÂNCIA!                                │
│  Os spins estão absorvendo energia!                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Cálculos

### Campo de Ressonância

```
Para rubi (Cr³⁺):
f = g·μB·B₀ / h

B₀ = (f·h) / (g·μB)

Onde:
- f = 2.45 GHz (frequência do magnetron)
- g = 1.98 (fator g do Cr³⁺)
- μB = 9.274×10⁻²⁴ J/T
- h = 6.626×10⁻³⁴ J·s

B₀ = (2.45e9 × 6.626e-34) / (1.98 × 9.274e-24)
B₀ ≈ 0.88 T

Precisamos de campo ~0.88T
Com ímãs de neodímio: ~0.3-0.5T
→ Pode precisar de mais ímãs ou eletroímã
```

### Solução: Ajustar Frequência ou Campo

```
OPÇÃO 1: Usar mais ímãs (empilhar)
├── 8 ímãs empilhados: ~0.6-0.8T
├── 12 ímãs empilhados: ~0.9-1.1T
└── Custo: +R$ 100-200

OPÇÃO 2: Usar eletroímã
├── Bobina com muitas espiras
├── Corrente: 5-10A
├── Campo: 0.5-1.0T ajustável
└── Custo: +R$ 100-300

OPÇÃO 3: Usar cristal com g maior
├── Fe³⁺: g ≈ 2.00 → B₀ ≈ 0.87T
├── Mn²⁺: g ≈ 2.00 → B₀ ≈ 0.87T
└── Mesmo problema

OPÇÃO 4: Usar frequência menor
├── Em vez de 2.45 GHz, usar 900 MHz
├── B₀ ≈ 0.32T (mais fácil!)
├── Precisa de gerador de RF diferente
└── Custo: +R$ 200-400
```

---

## Lista de Compras Final

### Usando Micro-ondas Desmontado

| Item | Custo (R$) | Observação |
|------|------------|------------|
| Micro-ondas desmontado | 0 | Já tem! |
| Rubi natural (5-10g) | 30-50 | Mercado Livre |
| Ímãs neodímio 50x50x25 (8x) | 160-300 | Mercado Livre |
| Diodo Schottky 1N5819 | 5-10 | Eletrônica |
| Capacitor 100pF | 2-5 | Eletrônica |
| Resistor 50Ω | 2-5 | Eletrônica |
| Multímetro digital | 50-80 | Eletrônica |
| Cabo coaxial + conectores | 30-50 | Eletrônica |
| Perfboard + fios | 20-30 | Eletrônica |
| **TOTAL** | **R$ 300-530** | |

### Segurança

| Item | Custo (R$) |
|------|------------|
| Luvas isolantes | 30-50 |
| Óculos proteção | 20-30 |
| **TOTAL** | **R$ 50-80** |

---

## Checklist Final

```
MONTAGEM:
[ ] Micro-ondas desmontado com segurança
[ ] Capacitor descarregado
[ ] Magnetron conectado ao guia de ondas
[ ] Cavidade preparada (câmara do micro-ondas)
[ ] Cristal (rubi) posicionado no centro
[ ] Ímãs montados no suporte
[ ] Detector montado (diodo + multímetro)
[ ] Tudo conectado

EXPERIMENTO:
[ ] Verificações de segurança feitas
[ ] Magnetron ligado
[ ] Campo magnético variado lentamente
[ ] Ressonância encontrada (queda no multímetro)
[ ] Posição dos ímãs registrada
[ ] Campo magnético medido
[ ] Resultado fotografado

ANÁLISE:
[ ] Calcular campo de ressonância
[ ] Calcular fator g
[ ] Comparar com literatura
[ ] Concluir: spins manipulados com sucesso!
[ ] Documentar tudo
[ ] Publicar no GitHub
```

---

## Resumo

```
┌─────────────────────────────────────────────────────┐
│  EPR COM MICRO-ONDAS: RESUMO                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  O QUE FAZ:                                         │
│  - Usa magnetron do micro-ondas como fonte          │
│  - Cristal de rubi como amostra                     │
│  - Ímãs de neodímio como campo magnético            │
│  - Detector simples (diodo + multímetro)            │
│                                                     │
│  O QUE MEDe:                                        │
│  - Absorção de micro-ondas pelo cristal             │
│  - Campo magnético de ressonância                   │
│  - Fator g da impureza magnética                    │
│                                                     │
│  O QUE PROVA:                                       │
│  - Spins são quantizados (só absorvem em B específico)│
│  - Momento angular é real                           │
│  - Mesma física do vídeo de Stern-Gerlach!          │
│                                                     │
│  CUSTO: R$ 300-530                                  │
│  TEMPO: ~4 horas (montagem + experimento)            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

**Bora montar! Me manda foto do micro-ondas desmontado!** 🔬
