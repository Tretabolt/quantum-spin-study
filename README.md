<div align="center">

<div align="center">
<img src="assets/banner.svg" alt="Quantum Spin Study Banner" width="100%"/>
</div>

# 🌀 Quantum Spin Study

### *Explorando a Quantização do Momento Angular na Prática*

[![GitHub stars](https://img.shields.io/github/stars/Tretabolt/quantum-spin-study?style=social)](https://github.com/Tretabolt/quantum-spin-study/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Tretabolt/quantum-spin-study?style=social)](https://github.com/Tretabolt/quantum-spin-study/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Tretabolt/quantum-spin-study)](https://github.com/Tretabolt/quantum-spin-study/issues)
[![GitHub license](https://img.shields.io/github/license/Tretabolt/quantum-spin-study)](https://github.com/Tretabolt/quantum-spin-study/blob/main/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/Tretabolt/quantum-spin-study)](https://github.com/Tretabolt/quantum-spin-study/commits/main)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![Physics](https://img.shields.io/badge/Quantum-Physics-purple?logo=atom&logoColor=white)]()
[![Hardware](https://img.shields.io/badge/Hardware-DIY-orange?logo=circuitdiagramdotorg&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

**🔬 Um estudo prático sobre mecânica quântica, spins eletrônicos e aplicações tecnológicas — do experimento de Stern-Gerlach à manipulação de spins em cristais comuns.**

</div>

---

## 📖 Sobre o Projeto

Este repositório documenta uma jornada de estudo e experimentação sobre **quantização do momento angular**, começando pela análise do [Experimento de Stern-Gerlach](https://www.instagram.com/reel/DbWYozSTtPq/) e evoluindo para experimentos práticos com cristais reais.

### 🎯 Objetivos

- ✅ Entender a quantização do momento angular (spin)
- ✅ Construir artefatos para detectar spins em cristais comuns
- ✅ Manipular spins usando micro-ondas e campos magnéticos
- ✅ Explorar aplicações tecnológicas (MRAM, computação quântica)

---

## 🗂️ Estrutura do Repositório

```
quantum-spin-study/
│
├── 📄 README.md                          ← Você está aqui
├── 📄 LICENSE                            ← MIT License
├── 📄 CONTRIBUTING.md                    ← Como contribuir
├── 📄 requirements.txt                   ← Dependências Python
│
├── 📁 docs/                              ← Documentação
│   ├── 01-stern-gerlach.md              ← O experimento original
│   ├── 02-utilidade-quantizacao.md      ← Aplicações da quantização
│   ├── 03-mram.md                       ← MRAM explicado
│   ├── 04-quantum-computing-spin.md     ← Computação quântica
│   ├── 05-spin-medicao.md               ← Como medir spins
│   ├── 06-roteiro-projeto.md            ← Roteiro de estudo
│   ├── 07-teste-cristal-fundo.md        ← Teste com cristais
│   ├── 08-guia-pratico-experimento.md   ← Guia prático
│   ├── 09-home-lab-ai.md                ← Home Lab para IA
│   ├── 10-teste-visual-cristal.md       ← Teste visual simples
│   ├── 11-mram-placa-mae.md             ← MRAM em PC antigo
│   ├── 12-stern-gerlach-cristal.md      ← Stern-Gerlach com cristais
│   ├── 13-montagem-pratica.md           ← Montagem passo a passo
│   ├── 14-manipulacao-spin-cristal.md   ← Manipulação de spins
│   └── 15-epr-com-micro-ondas.md        ← EPR caseiro
│
├── 📁 src/
│   ├── simulacoes/
│   │   ├── simulacao_qubit.py           ← Qubit de spin (QuTiP)
│   │   ├── juncao_tunel.py              ← Junção túnel magnética
│   │   └── stern_gerlach.py             ← Simulação do experimento
│   │
│   └── experimentos/
│       ├── teste_cristal_fundo.md       ← Guia do experimento
│       ├── analise_dados.py             ← Análise de dados
│       └── lista_materiais.md           ← Lista de compras
│
└── 📁 assets/                            ← Imagens e gráficos
    └── .gitkeep
```

---

## 🧪 Experimentos

### Experimento 1: Detecção de Spins em Cristais
> **Status:** 🟢 Pronto para executar

Detectar spins em cristais comuns usando campo magnético.

| Cristal | Tipo | Spins? |
|---------|------|--------|
| Quartzo | Diamagnético | ❌ |
| Sal (NaCl) | Diamagnético | ❌ |
| Pirita | Paramagnético | ✅ Fe²⁺ |
| Granada | Paramagnético | ✅ Fe³⁺ |
| Magnetita | Ferromagnético | ✅✅✅ |

📖 [Documentação completa](docs/07-teste-cristal-fundo.md)

---

### Experimento 2: Stern-Gerlach com Cristais
> **Status:** 🟡 Montagem necessária

Reproduzir o experimento do vídeo com cristais moídos.

```
Materiais: ~R$ 195
Tempo: ~2 horas
Resultado: Separação em 2 trilhas!
```

📖 [Guia de montagem](docs/13-montagem-pratica-stern-gerlach.md)

---

### Experimento 3: EPR Caseiro (Manipulação de Spins)
> **Status:** 🟡 Em planejamento

Usar micro-ondas desmontado para manipular spins em cristal inteiro.

```
Materiais: ~R$ 300-530
Tempo: ~4 horas
Resultado: Ressonância paramagnética detectada!
```

📖 [Montagem completa](docs/15-epr-com-micro-ondas.md)

---

## 💻 Simulações

### Qubit de Spin
```bash
pip install qutip numpy matplotlib
python src/simulacoes/simulacao_qubit.py
```

### Junção Túnel Magnética
```bash
python src/simulacoes/juncao_tunel.py
```

### Experimento de Stern-Gerlach
```bash
python src/simulacoes/stern_gerlach.py
```

---

## 🖥️ Projetos Paralelos

### MRAM em Placa-Mãe Antiga
Como adaptar memória magnética não-volátil em PCs antigos via PCI/SATA.

📖 [Guia completo](docs/11-mram-placa-mae.md)

### Home Lab para IA
Montar um laboratório de IA no quintal com GPUs e refrigeração adequada.

📖 [Guia completo](docs/09-home-lab-ai.md)

---

## 📚 Referências

| Referência | Descrição |
|------------|-----------|
| [Stern & Gerlach (1922)](https://doi.org/10.1007/BF01326983) | Artigo original do experimento |
| [Loss & DiVincenzo (1998)](https://doi.org/10.1103/PhysRevA.57.120) | Qubits com quantum dots |
| [Awschalom et al. (2013)](https://doi.org/10.1126/science.1231364) | Quantum Spintronics |
| [Griffiths - Intro to QM](https://www.cambridge.org/core/books/introduction-to-quantum-mechanics/) | Textbook fundamental |
| [Everspin MRAM](https://www.everspin.com/) | Tecnologia MRAM comercial |

---

## 🛠️ Ferramentas

| Ferramenta | Uso | Instalação |
|------------|-----|------------|
| [QuTiP](https://qutip.org/) | Simulação quântica | `pip install qutip` |
| [NumPy](https://numpy.org/) | Cálculos numéricos | `pip install numpy` |
| [Matplotlib](https://matplotlib.org/) | Visualização | `pip install matplotlib` |

---

## 🤝 Contribuições

Contribuições são bem-vindas! Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit (`git commit -m 'Add nova feature'`)
4. Push (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 📊 Estatísticas

```
📁 Arquivos:     20+
📄 Documentação: 15 artigos
🧪 Simulações:   3 scripts Python
🔬 Experimentos: 3 projetos práticos
📖 Referências:  5 papers/livros
```

---

## 📜 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

---

## 📞 Contato

**Tretabolt** - [GitHub](https://github.com/Tretabolt)

📧 Link do repositório: [https://github.com/Tretabolt/quantum-spin-study](https://github.com/Tretabolt/quantum-spin-study)

---

<div align="center">

**⭐ Se este projeto te ajudou, deixe uma estrela! ⭐**

*Feito com ❤️ e física quântica*

![Visitors](https://api.visitorbadge.io/api/visitors?path=Tretabolt%2Fquantum-spin-study&countColor=%2337d67a&style=flat)

</div>
