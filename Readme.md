🚀 Concept : IT Job Finder 2026
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Qt](https://img.shields.io/badge/Qt-PySide6-41cd52?logo=qt)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)


Une application légère, multi‑OS, orientée AdminSys/DevOps, qui centralise les offres d’emploi IT depuis plusieurs plateformes.
🎯 Objectif
# IT Job Finder 2026

IT Job Finder 2026 est une application multi‑plateforme permettant de rechercher,
filtrer et exporter des offres d’emploi IT (AdminSys, DevOps, Cloud, Réseau).

✔ Multi‑sources (LinkedIn, Indeed, WTTJ, Pôle Emploi)  
✔ Filtres intelligents  
✔ Export Excel  
✔ Interface moderne techno/circuit board  
✔ Compatible Windows, Linux, macOS  

Aider les techniciens, admins systèmes, DevOps juniors et confirmés à trouver rapidement des offres pertinentes, filtrées et classées intelligemment.
🏗️ Architecture technique
IT-Job-Finder-2026/
│
├── src/
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── splash_screen.py
│   │   └── styles.qss
│   │
│   ├── core/
│   │   ├── api/
│   │   │   ├── linkedin_client.py
│   │   │   ├── indeed_client.py
│   │   │   ├── wttj_client.py
│   │   │   └── pole_emploi_client.py
│   │   ├── filters.py
│   │   ├── exporter.py
│   │   └── models.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── config_loader.py
│   │
│   └── main.py
│
├── assets/
│   ├── logo.png
│   ├── splash.png
│   └── icons/
│
├── config/
│   └── settings.yaml
│
├── docs/
│   └── README.md
│
└── requirements.txt

Cette structure est propre, modulaire, scalable, et elle correspond parfaitement à ton style AdminSys/DevOps.
🧱 Structure du projet (GitHub)
IT-Job-Finder-2026/
│
├── src/
│   ├── core/
│   │   ├── api_clients/
│   │   ├── filters/
│   │   ├── models/
│   │   └── exporter/
│   ├── ui/
│   ├── cli/
│   └── main.py
│
├── assets/
│   ├── logo.png
│   └── theme/
│
├── config/
│   └── settings.yaml
│
├── docs/
│   └── README.md
│
└── requirements.txt
