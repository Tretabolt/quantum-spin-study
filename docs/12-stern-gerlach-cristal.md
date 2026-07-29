# 🔬 Stern-Gerlach com Cristais: Montagem Completa

## A Ideia

Se nosso experimento com cristais funcionar (detectar spins via atração magnética), podemos ir além e criar algo **parecido com o vídeo** — um feixe de cristal passando por campo magnético não-uniforme.

---

## Diferença do Vídeo vs Nosso Projeto

```
VÍDEO (Stern-Gerlach original):
├── Átomos de prata isolados
├── Feixe de átomos no vácuo
├── Campo magnético não-uniforme
└── Detector: dois pontos separados

NOSSO PROJETO (com cristais):
├── Pó de cristal com impurezas magnéticas
├── Feixe de partículas caindo no ar
├── Campo magnético não-uniforme
└── Detector: duas trilhas de pó separadas
```

---

## Montagem Passo a Passo

### Peça 1: Criar o Feixe de Cristal

```
┌─────────────────────────────┐
│  Funil pequeno (plástico)   │
│  ┌───────────────────┐      │
│  │ Pó de cristal      │     │
│  │ (magnetita, granada)│     │
│  └─────────┬─────────┘      │
│            │                │
│       abertura              │
│       (~2mm)                │
│            │                │
│      feixe de pó            │
│            ↓                │
└─────────────────────────────┘
```

**Material do cristal:**
- **Magnetita moída** (melhor resultado, forte atração)
- **Granada moída** (bom resultado, atração moderada)
- **Quartzo com ferro** (resultado fraco, mas educativo)

**Preparação:**
1. Pegar o cristal (magnetita, granada, pirita)
2. Moer em pó fino (pilão ou liquidificador velho)
3. Peneirar (grão fino ~0.1-0.5mm)
4. Colocar no funil

### Peça 2: Criar o Campo Não-Uniforme

```
┌─────────────────────────────────────────────┐
│  Ímã com Formato de Ponta                   │
│                                             │
│  Visão lateral:                             │
│                                             │
│      ┌─────┐                                │
│      │  S  │  (ponta)                       │
│      └──┬──┘                                │
│         │                                    │
│         │  ← campo concentrado aqui          │
│         │                                    │
│      ┌──┴──┐                                │
│      │  N  │  (plano)                       │
│      └─────┘                                │
│                                             │
│  O formato de ponta cria gradiente!         │
│  ∂B/∂z ≠ 0                                 │
└─────────────────────────────────────────────┘
```

**Como fazer o campo não-uniforme:**

**Opção A: Dois ímãs com formato diferente**
```
Ímã superior: ponta (concentra campo)
Ímã inferior: plano (campo uniforme)
Resultado: gradiente de campo entre eles
```

**Opção B: Ímã + peça de ferro**
```
Ímã: neodímio (forte)
Peça de ferro: cone ou ponta
Resultado: campo concentrado na ponta
```

**Opção C: Eletro enrolado em cone**
```
Bobina cônica: mais espiras na base, menos na ponta
Resultado: gradiente natural
```

### Peça 3: Detector

```
┌─────────────────────────────────────────────┐
│  Detector de Pó                             │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Folha de papel branco               │   │
│  │  (ou superfície plana)               │   │
│  │                                      │   │
│  │     ●●●●●  ← trilha 1 (spin ↑)      │   │
│  │                                      │   │
│  │     ─────  ← separação              │   │
│  │                                      │   │
│  │     ●●●●●  ← trilha 2 (spin ↓)      │   │
│  │                                      │   │
│  └─────────────────────────────────────┘    │
│                                             │
│  Ou: placa de vidro, filme plástico         │
└─────────────────────────────────────────────┘
```

---

## Montagem Completa

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ESTEIRA: MONTAGEM COMPLETA                                │
│                                                             │
│       ┌─────────────┐                                      │
│       │   FUNIL      │  ← pó de cristal                    │
│       │   ┌─────┐    │                                     │
│       │   │ PÓ  │    │                                     │
│       │   └──┬──┘    │                                     │
│       └──────┼───────┘                                     │
│              │                                             │
│              ↓ feixe                                       │
│       ┌──────────────┐                                     │
│       │    PONTA      │  ← ímã superior (S)               │
│       │    ┌────┐     │                                    │
│       └────┼────┼─────┘                                    │
│            │    │                                          │
│            │ ∂B │  ← campo não-uniforme                    │
│            │ ∂z │                                          │
│       ┌────┼────┼─────┐                                    │
│       │    └────┘     │  ← ímã inferior (N)               │
│       │    PLANO      │                                    │
│       └───────┬───────┘                                    │
│               │                                            │
│         ┌─────┴─────┐                                      │
│         │           │                                      │
│      trilha 1    trilha 2                                  │
│      (spin ↑)    (spin ↓)                                  │
│                                                             │
│       ┌─────────────────┐                                  │
│       │    DETECTOR      │  ← papel/vidro                  │
│       └─────────────────┘                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Lista de Materiais

| Item | Qtd | Preço (R$) | Onde |
|------|-----|------------|------|
| Magnetita (pedra) | 100g | 30 | Loja mineralógica |
| Pilão/moedor | 1 | 20 | Supermercado |
| Peneira fina | 1 | 15 | Supermercado |
| Funil plástico | 1 | 5 | Farmácia |
| Ímã neodímio pontiagudo | 2 | 80 | Mercado Livre |
| Suporte/argola | 1 | 30 | Ferragem |
| Folha de papel branco | 10 | 5 | Papelaria |
| Régua/trena | 1 | 10 | Papelaria |
| **Total** | | **~R$ 195** | |

---

## Procedimento Completo

### Passo 1: Preparar o Pó (30 min)
```bash
1. Pegar magnetita (100g)
2. Moer no pilão até virar pó
3. Peneirar (grão ~0.1-0.5mm)
4. Guardar em recipiente seco
```

### Passo 2: Montar o Setup (30 min)
```bash
1. Fixar suporte na mesa
2. Pendurar funil com abertura de 2mm
3. Posicionar ímãs abaixo do funil
   - Superior: ponta (S) → 2cm do feixe
   - Inferior: plano (N) → 4cm do feixe
4. Posicionar detector (papel) a 10cm dos ímãs
```

### Passo 3: Testar SEM Campo (5 min)
```bash
1. Largar pó pelo funil SEM ímãs
2. Observar: deve cair reto (uma trilha)
3. Fotografar como controle
```

### Passo 4: Testar COM Campo (5 min)
```bash
1. Posicionar ímãs
2. Largar pó pelo funil
3. Observar: deve separar em duas trilhas!
4. Fotografar resultado
5. Medir distância entre trilhas
```

### Passo 5: Variar e Documentar (30 min)
```bash
Testar com diferentes cristais:
1. Magnetita (controle positivo)
2. Granada
3. Pirita
4. Quartzo moído (controle negativo)

Para cada cristal:
- Fotografar sem campo
- Fotografar com campo
- Medir separação das trilhas
- Anotar observações
```

---

## Resultados Esperados

```
┌─────────────────────────────────────────────────────────────┐
│  RESULTADOS ESPERADOS                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SEM CAMPO MAGNÉTICO:                                       │
│  ┌─────────────────────────────┐                           │
│  │                             │                           │
│  │         ●●●●●●●            │  ← uma trilha só          │
│  │                             │                           │
│  └─────────────────────────────┘                           │
│                                                             │
│  COM CAMPO MAGNÉTICO (magnetita):                          │
│  ┌─────────────────────────────┐                           │
│  │      ●●●●●                 │  ← trilha 1 (↑)          │
│  │                             │                           │
│  │      ─────                  │  ← separação             │
│  │                             │                           │
│  │      ●●●●●                 │  ← trilha 2 (↓)          │
│  │                             │                           │
│  └─────────────────────────────┘                           │
│                                                             │
│  COM CAMPO MAGNÉTICO (quartzo):                            │
│  ┌─────────────────────────────┐                           │
│  │                             │                           │
│  │         ●●●●●●●            │  ← sem separação          │
│  │                             │                           │
│  └─────────────────────────────┘                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Por Que Funciona?

### Física por Trás

```
Cada partícula de magnetita:
├── Contém ~10²³ átomos de ferro
├── Cada átomo de ferro tem spins desemparelhados
├── Spins alinhados → momento magnético total
└── Campo não-uniforme exerce força

Força no momento magnético:
F = μ · (∂B/∂z)

Para partícula com spin ↑: F para cima
Para partícula com spin ↓: F para baixo
Resultado: separação!
```

### Conexão com o Vídeo

```
VÍDEO (Stern-Gerlach):
├── Átomo de prata: 1 elétron desemparelhado
├── Campo não-uniforme
└── Resultado: 2 pontos

NOSSO EXPERIMENTO:
├── Partícula de magnetita: ~10²³ elétrons desemparelhados
├── Campo não-uniforme
└── Resultado: 2 trilhas

Mesma física! Só muda a escala.
```

---

## Dificuldades e Soluções

### Problema 1: Pó muito fino, dispersa no ar
**Solução:** Usar grão maior (~0.5mm) ou fazer em ambiente sem vento

### Problema 2: Campo não é uniforme o suficiente
**Solução:** Usar ímãs maiores ou mais potentes (empilhar)

### Problema 3: Não vê separação
**Solução:** 
- Verificar se cristal tem spins (teste da agulha antes)
- Usar magnetita (sempre funciona)
- Aproximar mais os ímãs do feixe

### Problema 4: Pó gruda nos ímãs
**Solução:** Afastar um pouco os ímãs (~3-5cm)

---

## Versão Avançada: Com Medição

### Adicionar Sensores

```
┌─────────────────────────────────────────────┐
│  Versão com Sensores                        │
│                                             │
│  Funil → Feixe → Ímãs → Detectores         │
│                          │                  │
│                    ┌─────┴─────┐            │
│                    │           │            │
│              Sensor Hall 1  Sensor Hall 2   │
│              (cima)         (baixo)         │
│                    │           │            │
│                    └─────┬─────┘            │
│                          │                  │
│                    Multímetro/Arduino       │
│                                             │
│  Mede: intensidade do campo em cada trilha  │
│  Conclusão: quantificação do spin!         │
└─────────────────────────────────────────────┘
```

### Material Adicional

| Item | Preço (R$) |
|------|------------|
| Sensor Hall A3144 | 10 |
| Arduino Nano | 50 |
| Display OLED | 30 |
| Jumpers | 10 |
| **Total** | **~R$ 100** |

---

## Checklist Final

```
[ ] Cristal escolhido (magnetita recomendada)
[ ] Pó preparado (grão ~0.3mm)
[ ] Funil montado (abertura 2mm)
[ ] Ímãs posicionados (campo não-uniforme)
[ ] Detector posicionado (papel branco)
[ ] Teste sem campo (controle)
[ ] Teste com campo (experimento)
[ ] Fotos tiradas
[ ] Medidas registradas
[ ] Comparação entre cristais
[ ] Resultado documentado
```

---

## Conclusão

Se der certo (spoiler: com magnetita, vai dar), você estará reproduzindo o **Experimento de Stern-Gerlach em escala macroscópica**!

O que o vídeo mostra com átomos de prata, você estará fazendo com partículas de cristal:
- **Spin quantizado** → momento magnético
- **Campo não-uniforme** → força diferencial
- **Separação em duas trilhas** → prova da quantização!

---

## Próximo Passo

Quer que eu:
1. **Monte a lista de compras** completa?
2. **Crie o código Arduino** para os sensores?
3. **Faça a simulação** do que deve acontecer?
4. **Documente o passo a passo** com fotos?
