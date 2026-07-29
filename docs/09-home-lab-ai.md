# 🖥️ Home Lab para IA: Guia Completo

## Visão Geral

Montar um laboratório de IA no quintal exige planejamento em 3 pilares:
1. **Hardware** (GPUs, RAM, CPU)
2. **Infraestrutura** (energia, refrigeração, rede)
3. **Software** (frameworks, modelos)

---

## 💰 Orçamento por Nível

### Nível 1: Iniciante (~R$ 3.000-5.000)
- Roda modelos pequenos (7B-13B)
- Treinar LoRA/fine-tuning básico
- Inferência local

### Nível 2: Intermediário (~R$ 8.000-15.000)
- Roda modelos médios (13B-30B)
- Treinar com quantização
- Múltiplos projetos simultâneos

### Nível 3: Avançado (~R$ 20.000-50.000+)
- Roda modelos grandes (70B+)
- Treinar do zero
- Cluster distribuído

---

## 🛠️ HARDWARE RECOMENDADO

### Opção 1: Setup com GPU NVIDIA (Recomendado para IA)

```
┌─────────────────────────────────────────────┐
│           HOME LAB - GPU SETUP              │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  GPU 1: RTX 3090 (24GB VRAM)        │    │
│  │  GPU 2: RTX 3090 (24GB VRAM)        │    │
│  │  Total VRAM: 48GB                   │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  CPU: Ryzen 9 5900X ou i9-12900K   │    │
│  │  RAM: 128GB DDR4/DDR5              │    │
│  │  SSD: 2TB NVMe                     │    │
│  │  PSU: 1600W (80+ Platinum)         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  Custo estimado: R$ 15.000-25.000          │
└─────────────────────────────────────────────┘
```

| Componente | Modelo | VRAM | Preço (R$) | Onde |
|------------|--------|------|------------|------|
| GPU 1 | RTX 3090 24GB | 24GB | 4.500-6.000 | OLX, Mercado Livre |
| GPU 2 | RTX 3090 24GB | 24GB | 4.500-6.000 | OLX, Mercado Livre |
| CPU | Ryzen 9 5900X | - | 1.200-1.800 | KaBum, Pichau |
| RAM | 128GB DDR4 | - | 1.500-2.500 | KaBum |
| SSD | 2TB NVMe | - | 600-900 | KaBum |
| PSU | 1600W 80+ | - | 800-1.200 | KaBum |
| Placa-mãe | X570/B550 | - | 600-1.000 | KaBum |
| Gabinete | Full Tower | - | 300-500 | KaBum |

### Opção 2: Setup com GPU AMD (Mais barato)

| Componente | Modelo | VRAM | Preço (R$) |
|------------|--------|------|------------|
| GPU | RX 7900 XTX | 24GB | 3.500-5.000 |
| GPU | RX 6800 XT | 16GB | 1.800-2.500 |
| CPU | Ryzen 7 5800X3D | - | 1.000-1.500 |
| RAM | 64GB DDR4 | - | 800-1.200 |

### Opção 3: Server Usado (Melhor custo-benefício)

```
Dell PowerEdge R720/R730
├── 2x Xeon E5-2680 v4 (14 cores cada)
├── 256GB RAM DDR4 ECC
├── 8x bay SSD/HDD
├── PSU redundante
└── Preço: R$ 3.000-6.000 (OLX, eBay)

+ GPU dedicada (RTX 3060 12GB: ~R$ 1.500)
= Setup completo por ~R$ 5.000-8.000
```

---

## ❄️ REFRIGERAÇÃO (Crítico para Quintal)

### Problema: Calor no Brasil

```
Temperatura ambiente: 25-35°C
GPU under load: 80-95°C
Limite seguro: 85°C

Solução: refrigeração adequada!
```

### Opção 1: Ar-Forçado (Simples)

```
┌─────────────────────────────────────┐
│  Gabinete com fluxo de ar          │
│                                     │
│  Frente: 3x fans 120mm (intake)    │
│  Trás: 1x fan 120mm (exhaust)      │
│  Topo: 2x fans 140mm (exhaust)     │
│                                     │
│  Custo: R$ 200-400                  │
│  Eficiência: -10-15°C              │
└─────────────────────────────────────┘
```

### Opção 2: Water Cooling (Melhor)

```
┌─────────────────────────────────────┐
│  Water Cooling Custom Loop          │
│                                     │
│  CPU: Bloco + Radiador 360mm       │
│  GPU: Bloco + Radiador 360mm       │
│  Bomba: D5 ou DDC                  │
│  Reservatório: 200-500ml           │
│                                     │
│  Custo: R$ 1.500-3.000             │
│  Eficiência: -25-35°C              │
└─────────────────────────────────────┘
```

### Opção 3: Ar Condicionado (Para Quintal)

```
┌─────────────────────────────────────┐
│  Mini Split 9.000 BTUs             │
│                                     │
│  Instalar no cômodo do server      │
│  Manter 20-25°C                    │
│  Timer: ligar 30min antes do uso   │
│                                     │
│  Custo: R$ 1.500-2.500             │
│  Energia: ~R$ 100-200/mês          │
└─────────────────────────────────────┘
```

### Opção 4: Imersão em Óleo (DIY Avançado)

```
┌─────────────────────────────────────┐
│  Imersão em óleo mineral           │
│                                     │
│  Banheira plástica + óleo mineral  │
│  Submergir motherboard + GPU       │
│  Trocador de calor + ventilador    │
│                                     │
│  Custo: R$ 500-1.000               │
│  Eficiência: -40-50°C              │
│  ⚠️ Risco alto, avançado apenas    │
└─────────────────────────────────────┘
```

---

## ⚡ ENERGIA (Crítico)

### Consumo Estimado

```
Setup básico (1x RTX 3090):
├── Idle: ~150W
├── Load: ~500W
└── Pico: ~700W

Setup dual GPU (2x RTX 3090):
├── Idle: ~250W
├── Load: ~900W
└── Pico: ~1.200W

Custo mensal (8h/dia, R$ 0.75/kWh):
├── Básico: ~R$ 90/mês
└── Dual: ~R$ 160/mês
```

### Necessidades

```
┌─────────────────────────────────────┐
│  Infraestrutura Elétrica           │
│                                     │
│  Tomada: 220V (preferencial)       │
│  Disjuntor: 20A dedicado           │
│  Fiação: 4mm² (mínimo)            │
│  Nobreak: 1500VA (recomendado)     │
│  Aterramento: obrigatório          │
│                                     │
│  ⚠️ Chame eletricista!             │
└─────────────────────────────────────┘
```

---

## 💻 SOFTWARE

### Sistema Operacional

```
Recomendado: Ubuntu 22.04 LTS
├── Driver NVIDIA: 535+
├── CUDA: 12.x
├── Python: 3.10-3.11
└── Docker: para containers
```

### Frameworks de IA

```
├── PyTorch 2.x (principal)
├── TensorFlow 2.x (alternativa)
├── Hugging Face Transformers
├── vLLM (inferência otimizada)
├── llama.cpp (CPU/GPU misto)
├── Ollama (fácil de usar)
└── Stable Diffusion (imagens)
```

### Modelos que Rodam

```
┌─────────────────────────────────────────────────┐
│  VRAM disponível vs Modelos                    │
├─────────────────────────────────────────────────┤
│  8GB  → Mistral 7B, Llama 2 7B (Q4)           │
│  12GB → Llama 2 13B (Q4), CodeLlama 13B       │
│  24GB → Llama 2 70B (Q4), Mixtral 8x7B (Q4)  │
│  48GB → Llama 2 70B (FP16), modelos maiores   │
└─────────────────────────────────────────────────┘
```

---

## 📋 CHECKLIST - O que Comprar

### Setup Básico (~R$ 5.000)

```
[ ] GPU: RTX 3060 12GB (usada)         R$ 1.500
[ ] CPU: Ryzen 5 5600                   R$ 800
[ ] RAM: 64GB DDR4                     R$ 600
[ ] SSD: 1TB NVMe                      R$ 350
[ ] PSU: 850W 80+ Gold                 R$ 500
[ ] Placa-mãe: B550                    R$ 500
[ ] Gabinete: Mid Tower                R$ 200
[ ] Fans: 6x 120mm                     R$ 150
[ ] Nobreak: 1200VA                    R$ 400
                                    ___________
                                    R$ 5.000
```

### Setup Intermediário (~R$ 12.000)

```
[ ] GPU: RTX 3090 24GB (usada)         R$ 5.000
[ ] CPU: Ryzen 9 5900X                 R$ 1.500
[ ] RAM: 128GB DDR4                    R$ 1.800
[ ] SSD: 2TB NVMe                      R$ 700
[ ] PSU: 1200W 80+ Platinum            R$ 900
[ ] Placa-mãe: X570                    R$ 800
[ ] Gabinete: Full Tower               R$ 400
[ ] Water Cooling AIO 360mm            R$ 600
[ ] Nobreak: 1500VA                    R$ 500
                                    ___________
                                    R$ 12.200
```

### Setup Avançado (~R$ 25.000)

```
[ ] GPU: 2x RTX 3090 24GB             R$ 10.000
[ ] CPU: Ryzen 9 7950X                 R$ 2.500
[ ] RAM: 256GB DDR5                    R$ 4.000
[ ] SSD: 4TB NVMe (2x 2TB)            R$ 1.400
[ ] PSU: 1600W 80+ Platinum            R$ 1.200
[ ] Placa-mãe: X670E                   R$ 1.500
[ ] Gabinete: Super Tower              R$ 600
[ ] Water Cooling Custom               R$ 2.000
[ ] Nobreak: 2000VA                    R$ 800
[ ] Ar Condicionado Split             R$ 2.000
                                    ___________
                                    R$ 26.000
```

---

## 🏗️ MONTAGEM NO QUINTAL

### Estrutura Física

```
┌─────────────────────────────────────────┐
│  Casa/Quarto no Quintal                │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  Rack/Mesa do Server            │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Gabinete Full Tower    │    │    │
│  │  └─────────────────────────┘    │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Nobreak 1500VA         │    │    │
│  │  └─────────────────────────┘    │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Monitor + KVM          │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  Ar Condicionado Split 9000BTU │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  Rede: Cabo Cat6 até roteador  │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### Dicas Importantes

1. **Ventilação:** Deixe espaço entre gabinete e paredes (10cm+)
2. **Poeira:** Use filtros no gabinete, limpe mensalmente
3. **Umidade:** Evite áreas úmidas, use desumidificador se necessário
4. **Segurança:** Tranque o local, evita acesso não autorizado
5. **Ruído:** Fans barulhentos? Considere gabinete com isolamento acústico

---

## 🚀 PRIMEIROS PASSOS

### Dia 1: Compra e Recebimento
```
[ ] Pesquisar preços (KaBum, Pichau, OLX)
[ ] Comprar componentes
[ ] Receber e conferir
```

### Dia 2: Montagem
```
[ ] Montar hardware (placa-mãe, CPU, RAM)
[ ] Instalar GPU(s)
[ ] Conectar PSU
[ ] Testar boot
[ ] Instalar Ubuntu 22.04
```

### Dia 3: Software
```
[ ] Instalar drivers NVIDIA
[ ] Instalar CUDA
[ ] Instalar Python + PyTorch
[ ] Testar com modelo pequeno (Ollama)
[ ] Configurar acesso remoto (SSH)
```

### Dia 4: Primeiro Experimento
```
[ ] Baixar modelo (ex: Mistral 7B)
[ ] Rodar inferência
[ ] Testar fine-tuning (LoRA)
[ ] Monitorar temperaturas
[ ] Ajustar cooling se necessário
```

---

## 📊 Custo-Benefício: Cloud vs Local

```
┌─────────────────────────────────────────────────┐
│  Análise: Cloud GPU vs Home Lab               │
├─────────────────────────────────────────────────┤
│                                                 │
│  Cloud (AWS/Azure/GCP):                       │
│  ├── A100 40GB: ~R$ 50/hora                   │
│  ├── 100 horas/mês: R$ 5.000/mês             │
│  └── 12 meses: R$ 60.000                      │
│                                                 │
│  Home Lab (RTX 3090):                         │
│  ├── Investimento: R$ 12.000                  │
│  ├── Energia: ~R$ 150/mês                     │
│  ├── 12 meses: R$ 13.800                      │
│  └── Break-even: ~3 meses                     │
│                                                 │
│  ✅ Home Lab vence em 3+ meses de uso         │
└─────────────────────────────────────────────────┘
```

---

## 📚 Referências

- r/homelab (Reddit)
- r/LocalLLaMA (Reddit)
- ServeTheHome (reviews de hardware)
- Level1Techs (YouTube)
- WolfgangsChannel (YouTube, water cooling)
