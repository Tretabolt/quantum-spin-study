# 🖥️ MRAM em Placa-Mãe de PC Antigo

## Como Funcionaria?

A MRAM (Memória de Acesso Aleatório Magnético) usa **spin dos elétrons** em vez de carga para armazenar dados. Conectando com nosso estudo sobre cristais e spins:

```
MEMÓRIA TRADICIONAL (DRAM)          MRAM
┌─────────────────────┐        ┌─────────────────────┐
│ Capacitor            │        │ Junção Túnel         │
│ ┌───┐               │        │ Magnética (MTJ)      │
│ │   │ ← carga       │        │ ┌───┐               │
│ └───┘               │        │ │ ↑ │ ← spin        │
│                     │        │ └───┘               │
│ Volátil (perde dados│        │ Não-volátil (mantém │
│ sem energia)        │        │ dados sem energia)  │
└─────────────────────┘        └─────────────────────┘
```

---

## Compatibilidade com Placa-Mãe Antiga

### O Problema

```
Placa-mãe antiga (DDR/DDR2/DDR3)
├── Slot: DIMM 184/240 pinos
├── Voltagem: 2.5V / 1.8V / 1.5V
├── Protocolo: DDR/DDR2/DDR3
└── Controlador: integrado na CPU/northbridge

MRAM atual (chips)
├── Interface: SPI, parallel, QSPI
├── Voltagem: 3.3V / 1.8V
├── Tamanho: 4MB - 256MB (chip único)
└── Pacote: SOIC-8, BGA (não DIMM!)
```

**Conclusão direta:** Não existe módulo MRAM em formato DIMM para desktop antigo. Mas dá pra adaptar!

---

## Soluções Práticas

### Solução 1: Módulo SPI MRAM via Adaptador USB

```
┌─────────────────────────────────────────┐
│  MRAM Chip (SPI)                        │
│  ┌─────────────────┐                    │
│  │ Everspin         │                   │
│  │ EM256LX16       │ 256Mb (32MB)       │
│  └────────┬────────┘                    │
│           │ SPI                         │
│  ┌────────┴────────┐                    │
│  │ Adaptador USB    │                   │
│  │ SPI-Master       │                   │
│  └────────┬────────┘                    │
│           │ USB                         │
│  ┌────────┴────────┐                    │
│  │ PC (porta USB)   │                   │
│  └─────────────────┘                    │
│                                         │
│  Velocidade: ~20 MB/s (USB 2.0)        │
│  Uso: armazenamento, logs, swap        │
└─────────────────────────────────────────┘
```

**Material:**
- Chip MRAM Everspin EM256LX16 (~R$ 150-300)
- Adaptador SPI-USB (~R$ 30-80)
- Custo total: ~R$ 200-400

### Solução 2: MRAM como Disco de Boot (SATA)

```
┌─────────────────────────────────────────┐
│  MRAM + Controlador SATA               │
│                                         │
│  ┌─────────────┐    ┌──────────────┐   │
│  │ MRAM Chips   │───│ Controlador  │   │
│  │ 8x 256Mb     │   │ SATA-RAID    │   │
│  │ = 256MB      │   │              │   │
│  └─────────────┘    └──────┬───────┘   │
│                            │ SATA      │
│                     ┌──────┴───────┐   │
│                     │ Placa-mãe    │   │
│                     │ (porta SATA) │   │
│                     └──────────────┘   │
│                                         │
│  Velocidade: ~150 MB/s (SATA I)        │
│  Uso: boot ultra-rápido, OS            │
└─────────────────────────────────────────┘
```

**Material:**
- Controlador SATA-para-SPI (~R$ 100-200)
- 8x chips MRAM 256Mb (~R$ 1.200-2.400)
- Custo total: ~R$ 1.500-2.800

### Solução 3: PCI MRAM Card

```
┌─────────────────────────────────────────┐
│  PCI Card com MRAM                      │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  PCI Card (32-bit, 33MHz)       │    │
│  │  ┌─────────────────────────┐    │    │
│  │  │  Controlador FPGA/ARM   │    │    │
│  │  └───────────┬─────────────┘    │    │
│  │              │                  │    │
│  │  ┌───────────┴─────────────┐    │    │
│  │  │  MRAM Array             │    │    │
│  │  │  16x EM256LX16          │    │    │
│  │  │  = 512MB                │    │    │
│  │  └─────────────────────────┘    │    │
│  └─────────────────────────────────┘    │
│                                         │
│  Velocidade: ~100-200 MB/s             │
│  Uso: RAM não-volátil, cache           │
└─────────────────────────────────────────┘
```

---

## Como a MRAM Funciona na Placa-Mãe

### Arquitetura de um PC Antigo

```
┌─────────────────────────────────────────────────────────┐
│                    PLACA-MÃE ANTIGA                      │
│                                                         │
│  ┌─────────┐      ┌─────────────┐      ┌─────────┐    │
│  │   CPU   │◄────►│ Northbridge │◄────►│  RAM    │    │
│  │ (Pentium│      │ (Intel 865) │      │ (DDR)   │    │
│  │  III/4) │      └──────┬──────┘      └─────────┘    │
│  └─────────┘             │                             │
│                          │                             │
│                   ┌──────┴──────┐                      │
│                   │ Southbridge │                      │
│                   │ (ICH5)      │                      │
│                   └──────┬──────┘                      │
│                          │                             │
│         ┌────────────────┼────────────────┐            │
│         │                │                │            │
│    ┌────┴────┐    ┌─────┴─────┐    ┌─────┴─────┐     │
│    │  PCI    │    │   SATA    │    │   USB     │     │
│    │  Slots  │    │  Ports    │    │  Ports    │     │
│    └─────────┘    └───────────┘    └───────────┘     │
└─────────────────────────────────────────────────────────┘
```

### Onde a MRAM Entra

```
Opção A: Via PCI
┌─────────┐      ┌─────────────┐      ┌─────────┐
│   CPU   │◄────►│ Northbridge │◄────►│  RAM    │ (original)
└─────────┘      └──────┬──────┘      └─────────┘
                        │
                   ┌────┴────┐
                   │   PCI   │
                   │   Bus   │
                   └────┬────┘
                        │
                   ┌────┴────┐
                   │  MRAM   │ (PCI Card)
                   │  512MB  │
                   └─────────┘

Opção B: Via SATA (como disco)
┌─────────┐      ┌─────────────┐      ┌─────────┐
│   CPU   │◄────►│ Southbridge │◄────►│  SATA   │
└─────────┘      └─────────────┘      └────┬────┘
                                           │
                                      ┌────┴────┐
                                      │  MRAM   │ (SATA adapter)
                                      │  256MB  │
                                      └─────────┘

Opção C: Via USB (mais lento)
┌─────────┐      ┌─────────────┐      ┌─────────┐
│   CPU   │◄────►│ Southbridge │◄────►│  USB    │
└─────────┘      └─────────────┘      └────┬────┘
                                           │
                                      ┌────┴────┐
                                      │  MRAM   │ (USB adapter)
                                      │  32MB   │
                                      └─────────┘
```

---

## Vantagens da MRAM vs Memória Original

```
┌────────────────┬────────────┬────────────┬────────────┐
│ Propriedade    │ DDR (antiga)│ MRAM       │ Vantagem   │
├────────────────┼────────────┼────────────┼────────────┤
│ Volatilidade   │ Volátil    │ Não-volátil│ MRAM ✅    │
│ Velocidade     │ ~3 GB/s    │ ~200 MB/s  │ DDR ✅     │
│ Retenção       │ Perde dados│ Mantém     │ MRAM ✅    │
│ Ciclos         │ ∞          │ ∞          │ Empate     │
│ Consumo        │ Alto       │ Baixo      │ MRAM ✅    │
│ Latência       │ ~50ns      │ ~20ns      │ MRAM ✅    │
│ Densidade      │ Alta       │ Baixa      │ DDR ✅     │
│ Custo          │ Baixo      │ Alto       │ DDR ✅     │
└────────────────┴────────────┴────────────┴────────────┘
```

---

## Casos de Uso em PC Antigo

### 1. Boot Ultra-Rápido
```
MRAM como disco de boot:
├── OS: Linux minimal (50MB)
├── Boot: ~2 segundos
├── Sem moving parts
└── Duração: décadas
```

### 2. Swap/RAM Expandida
```
MRAM como swap via PCI:
├── Sistema pensa que é RAM
├── Sem perda de dados em power-off
├── Velocidade: 10-100x mais lento que RAM
└── Mas: não-volátil!
```

### 3. Log/Dados Críticos
```
MRAM para logs industriais:
├── Dados nunca perdidos
├── Escrita ilimitada
├── Temperatura: -40°C a +125°C
└── Ideal para sistemas embarcados
```

---

## Projeto Prático: MRAM em PC Pentium III

### Especificação

```
PC Antigo:
├── CPU: Intel Pentium III 800MHz
├── Chipset: Intel 815/845
├── RAM: 256MB DDR-266
├── Slots: PCI 32-bit, AGP
├── SATA: Não (usar PCI-SATA card)
└── USB: 1.1/2.0

MRAM Add-on:
├── Interface: PCI 32-bit
├── Controlador: FPGA Xilinx Spartan-6
├── MRAM: 8x Everspin EM256LX16
├── Capacidade: 256MB
├── Velocidade: ~100 MB/s
└── Custo: ~R$ 2.000-3.000
```

### Diagrama de Implementação

```
┌─────────────────────────────────────────────────────┐
│  PCI MRAM Card - Design                            │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │  FPGA (Spartan-6)                           │    │
│  │  ┌─────────────────────────────────────┐    │    │
│  │  │  PCI Target Controller              │    │    │
│  │  │  ├── BAR0: MRAM memory window       │    │    │
│  │  │  ├── BAR1: Control registers        │    │    │
│  │  │  └── DMA engine                     │    │    │
│  │  └─────────────────────────────────────┘    │    │
│  │  ┌─────────────────────────────────────┐    │    │
│  │  │  SPI Master (8 channels)            │    │    │
│  │  │  ├── CH0: MRAM chip 0              │    │    │
│  │  │  ├── CH1: MRAM chip 1              │    │    │
│  │  │  ├── ...                            │    │    │
│  │  │  └── CH7: MRAM chip 7              │    │    │
│  │  └─────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                 │
│  │MRAM0│ │MRAM1│ │MRAM2│ │MRAM3│  (lado superior) │
│  └─────┘ └─────┘ └─────┘ └─────┘                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                 │
│  │MRAM4│ │MRAM5│ │MRAM6│ │MRAM7│  (lado inferior) │
│  └─────┘ └─────┘ └─────┘ └─────┘                 │
│                                                     │
│  Conector PCI 32-bit ──────────────────────────    │
└─────────────────────────────────────────────────────┘
```

---

## Peças para Comprar

| Componente | Modelo | Qtd | Preço (R$) | Onde |
|------------|--------|-----|------------|------|
| FPGA Board | Spartan-6 Starter | 1 | 300-500 | Mercado Livre |
| MRAM Chips | Everspin EM256LX16 | 8 | 150-300 cada | Mouser, Digikey |
| PCB Custom | JLCPCB/PCBWay | 5 | 50-100 | JLCPCB |
| Conectores | PCI edge connector | 1 | 20-50 | AliExpress |
| Decoupling | Capacitores 100nF | 32 | 10 | AliExpress |
| Reguladores | LDO 3.3V/1.8V | 2 | 10 | AliExpress |
| **Total** | | | **R$ 1.500-3.000** | |

---

## Software/Firmware

### Driver Linux (exemplo simplificado)

```c
// mram_pci.c - Driver PCI para MRAM
#include <linux/pci.h>
#include <linux/fs.h>

#define MRAM_SIZE (256 * 1024 * 1024)  // 256MB
#define MRAM_BAR  0

static void __iomem *mram_base;

static int mram_probe(struct pci_dev *dev, const struct pci_device_id *id)
{
    pci_enable_device(dev);
    pci_request_regions(dev, "mram_pci");
    mram_base = pci_iomap(dev, MRAM_BAR, MRAM_SIZE);
    
    printk(KERN_INFO "MRAM: 256MB detected at %p\n", mram_base);
    return 0;
}

// Mapear como dispositivo de bloco
// /dev/mram0 - 256MB de memória não-volátil
```

### Montagem como Disco

```bash
# Carregar driver
sudo insmod mram_pci.ko

# Criar dispositivo de bloco
sudo mknod /dev/mram0 b 240 0

# Formatar
sudo mkfs.ext4 /dev/mram0

# Montar
sudo mount /dev/mram0 /mnt/mram

# Resultado: disco de 256MB ultra-rápido e não-volátil!
```

---

## Resumo

```
┌─────────────────────────────────────────────────┐
│  MRAM em PC Antigo: Resumo                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  ❌ Não existe módulo DIMM MRAM                │
│  ✅ Dá pra adaptar via PCI/SATA/USB            │
│  💰 Custo: R$ 1.500-3.000                     │
│  ⚡ Velocidade: ~100-200 MB/s                  │
│  💾 Capacidade: 256MB-512MB                    │
│  🔋 Não-volátil: dados nunca perdidos          │
│                                                 │
│  Melhor uso: boot rápido, logs, swap           │
│  Não substitui: RAM principal (muito lento)    │
└─────────────────────────────────────────────────┘
```

---

## Referências

- Everspin MRAM Products: https://www.everspin.com
- PCI Specification: https://pcisig.com
- Linux PCI Driver: https://www.kernel.org/doc/html/latest/PCI/
