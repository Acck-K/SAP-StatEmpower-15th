# SAP-GeoStats-Platform

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-red.svg)](https://pytorch.org)
[![PySAL](https://img.shields.io/badge/PySAL-Spatial_Stats-green.svg)](https://pysal.org/)

## Strategic Context
The **SAP-GeoStats-Platform** is a direct response to China's **"15th Five-Year Plan"** regarding "Building a Modernized Monitoring and Early Warning System" and "Statistical Empowerment for Digital Twin Water Conservancy/Oceanography." It provides a robust, geographically-informed modeling framework to solve "High-Quality Development" challenges by directly addressing data fragmentation and enhancing extreme distribution capture.

## 战略背景 (Strategic Background)
**SAP-GeoStats-Platform** 项目是对国家**“十五五”规划**关于“构建现代化监测预警体系”和“数字孪生水利/海洋的统计赋能”的积极响应。本项目提供了一个鲁棒的、地理信息驱动的建模框架，旨在解决“高质量发展”中的挑战，特别是应对数据碎片化问题并提升对极端分布事件的捕捉能力。

---

## Key Features (核心特性)

1. **Geography-Informed Modeling (地理信息驱动建模)**
   Integrates Spatial Autocorrelation (空间自相关 - Spatial Autocorrelation, SAC) as a guiding statistical constraint for deep neural networks.
   将空间自相关 (SAC) 作为深度神经网络的先验统计约束。

2. **Spatial Strategy: LISA + AM (空间策略)**
   Fuses Local Indicators of Spatial Association (局部空间关联指标 - Local Indicators of Spatial Association, LISA) with Attention Mechanisms (注意力机制 - Attention Mechanism, AM) to adaptively capture spatial heterogeneity and clustering.
   融合 LISA 与注意力机制 (AM)，自适应捕获空间异质性与聚类特征。

3. **Temporal Strategy: PPE + Freq (时间策略)**
   Leverages Physical Phase Encoding (物理相位编码 - Physical Phase Encoding, PPE) in a frequency domain decomposition module to identify dominant physical cycles, maintaining statistical consistency even with 50%+ missing data.
   利用物理相位编码 (PPE) 进行频域分解，识别主导物理周期，即使在 50%+ 缺失率的数据碎片化情况下也能保持统计一致性。

---

## Directory Structure (目录结构)

```
SAP-GeoStats-Platform/
├── configs/            # Configuration files (Database, UI/UX aesthetics)
├── data/               # Synthetic and actual geospatial datasets
├── models/             # Core DL models (SAP_Model.py)
├── scripts/            # Deployment and validation scripts (Case A & B, Dashboard)
└── utils/              # Helper utilities (Data Generators, Fragmentation Injectors)
```

## Quick Start (快速开始)

```bash
# Install dependencies
pip install torch torchvision torchaudio rasterio gdal pysal sqlalchemy streamlit numpy pandas matplotlib seaborn

# Run Case A (Micro-scale Dam Monitoring)
python scripts/case_a_dam_monitoring.py

# Run Case B (Macro-scale Green Tide Monitoring)
python scripts/case_b_green_tide.py

# Launch Streamlit Dashboard
streamlit run scripts/dashboard.py
```

## Case Studies (案例研究)

### Case A: Dam Monitoring Station Networks (大坝监测站网)
- **Scale**: Micro-scale (微观尺度)
- **Target Metrics**: RMSE = 0.0029, GoF = 0.8755

### Case B: Green Tide Remote Sensing Monitoring (绿潮遥感监测)
- **Scale**: Macro-scale (宏观尺度)
- **Target Metrics**: IoU = 0.7869, Classification Accuracy (CA) = 0.9636
