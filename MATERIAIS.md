# Materiais para Junção Túnel Magnética (MTJ)

Estrutura: **CoFeB / MgO / CoFeB** — base para MRAM, sensores magnéticos e spintrônica.

---

## Estrutura da Pilha

```
├── Substrato: Si/SiO₂
├── Camada fixa: CoFeB (2-5 nm)
├── Barreira túnel: MgO (1-1.5 nm)
├── Camada livre: CoFeB (2-5 nm)
├── Contatos: Ta/W (condutores)
└── Processo: deposição por sputtering + litografia
```

---

## Especificações dos Materiais

| Camada | Material | Espessura | Pureza | Tipo de Alvo |
|--------|----------|-----------|--------|--------------|
| Substrato | Si (100) + SiO₂ térmico | SiO₂: 100-300 nm | Prime grade | Wafer 2"-4" |
| Camada fixa | Co₂₀Fe₆₀B₂₀ | 2-5 nm | 99.9%+ | Liga metálica (DC sputtering) |
| Barreira túnel | MgO | 1-1.5 nm | 99.95%+ | Cerâmico (RF sputtering) |
| Camada livre | Co₂₀Fe₆₀B₂₀ | 2-5 nm | 99.9%+ | Liga metálica (DC sputtering) |
| Contato superior | Ta | 5-10 nm | 99.95%+ | Metal puro (DC sputtering) |
| Contato inferior | W | 5-10 nm | 99.95%+ | Metal puro (DC sputtering) |

---

## Fornecedores Internacionais

### Substrato Si/SiO₂
| Fornecedor | Site | Notas |
|---|---|---|
| MSE Supplies | msesupplies.com | Si/SiO₂ térmico, 2"-4", ~$30-80/wafer |
| University Wafer | universitywafer.com | Grande variedade |
| ACS Material | acsmaterial.com | Si/SiO₂ com espessuras variadas |
| Microchemicals | microchemicals.com | Si + SiO₂ seco, 2", entrega global |
| Ted Pella | tedpella.com | Para análise |

### Alvo CoFeB (Co₂₀Fe₆₀B₂₀)
| Fornecedor | Site | Notas |
|---|---|---|
| Kurt J. Lesker | lesker.com | Catálogo online, pedido sob medida |
| Testbourne | testbourne.com | UK, entrega global |
| ACI Alloys | acialloys.com | Ligas customizadas |
| Nanografi | shop.nanografi.com | Alvos de ligas magnéticas |
| Stanford Advanced Materials | sputtertargets.net | 99.9%+ pureza |

> ⚠️ **CoFeB é item customizado** — geralmente não está em estoque. Prazo: 2-6 semanas. Preço: $300-800 USD para alvo 2"-3".

### Alvo MgO
| Fornecedor | Site | Notas |
|---|---|---|
| Stanford Advanced Materials | sputtertargets.net | MgO 99.9%-99.99% |
| Kurt J. Lesker | lesker.com | Catálogo, busca "Magnesium Oxide" |
| QS Advanced Materials | qsrarematerials.com | Vários formatos |
| Heeger Materials | heegermaterials.com | Alvos + substratos cristalinos |
| Infinita Materials | infinitamaterials.com | Fabricante EUA |

### Alvos Ta e W
| Fornecedor | Site | Notas |
|---|---|---|
| Kurt J. Lesker | lesker.com | Ta e W puros, discos 2"-3" |
| Plansee SE | plansee.com | Líder mundial em alvos refratários |
| RD Mathis | rdmathis.com | Ta, W, Mo — loja online |
| Testbourne | testbourne.com | Metais refratários de alta pureza |
| Goodfellow | goodfellow.com | Metais puros, pequenas quantidades |

---

## Fornecedores e Acesso no Brasil

### Distribuidor Nacional
| Fornecedor | Site | Notas |
|---|---|---|
| Ohmini (Angstrom Sciences) | ohmini.com.br | Distribuidor brasileiro de materiais PVD, importação sob demanda |

### Laboratórios com Infraestrutura
| Centro | Localização | O que oferecem |
|---|---|---|
| LNNano / CNPEM | Campinas, SP | Sputtering, litografia, caracterização |
| CCSNano / UNICAMP | Campinas, SP | Deposição, litografia |
| Lab. Filmes Finos / UFRGS | Porto Alegre, RS | Sputtering, magnetismo |
| Lab. Nano / USP São Carlos | São Carlos, SP | Deposição e caracterização |
| LNLS (síncrotron) | Campinas, SP | Caracterização magnética |

### Importação
- **Kurt J. Lesker** tem representante no Brasil (lesker.com/brasil)
- A maioria dos fornecedores internacionais envia para o Brasil

### Isenção de Impostos (Pesquisa)
- **Importação PDI** — isenção de II, IPI, PIS, COFINS para universidades/institutos
- **Convênio 101/97 (CONFAZ)** — isenção de ICMS para materiais científicos
- Requisitos: Declaração de Importação + projeto aprovado (CNPq/FAPESP/CAPES)
- ⚠️ Processo burocrático: 2-6 meses

---

## Estimativa de Custos

### Internacional (USD)
| Item | Preço (USD) |
|---|---|
| Si/SiO₂ wafer 2" (5 un.) | $150-400 |
| Alvo CoFeB 2" (custom) | $400-800 |
| Alvo MgO 2" | $200-500 |
| Alvo Ta 2" | $150-400 |
| Alvo W 2" | $100-300 |
| Frete internacional | $100-300 |
| **Total** | **$1.100-2.700** |

### Brasil (BRL, câmbio ~R$ 6/USD)
| Cenário | Estimativa (BRL) |
|---|---|
| Com impostos (~60-100%) | R$ 6.600-16.200 |
| Com isenção PDI | R$ 3.600-9.000 |

---

## Parâmetros de Sputtering (Referência)

| Material | Tipo de Sputtering | Potência | Pressão Ar | Taxa deposição |
|---|---|---|---|---|
| CoFeB | DC magnetron | 50-150 W | 2-5 mTorr | 0.05-0.2 nm/s |
| MgO | RF magnetron | 100-300 W | 5-10 mTorr | 0.02-0.1 nm/s |
| Ta | DC magnetron | 100-200 W | 2-5 mTorr | 0.1-0.3 nm/s |
| W | DC magnetron | 100-200 W | 2-5 mTorr | 0.1-0.3 nm/s |

Base pressure: ~10⁻⁸ Torr. Deposição sequencial sem quebrar vácuo (interfaces limpas são críticas).

---

## Referências

- S. Ikeda et al., *Nature Materials* **9**, 721 (2010) — MTJ com CoFeB/MgO
- Catálogo técnico Kurt J. Lesker — parâmetros de sputtering recomendados
