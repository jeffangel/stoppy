# Stoppy

**Mantén tu estado en Microsoft Teams (u otras apps similares) siempre en activo 🟢 evitando que se ponga en amarillo 🟡 (inactivo).**  
Funciona en **Windows, Linux y macOS**, ya que utiliza [`pynput`](https://pypi.org/project/pynput/) para simular actividad en el sistema operativo.

[![GitHub Release](https://img.shields.io/github/v/release/jeffangel/stoppy?style=flat-square)](https://github.com/jeffangel/stoppy/releases/latest)

---

## 🚀 Instalación (desde GitHub Release)

Instala `stoppy` directamente desde la última release publicada en GitHub:

```bash
pip install https://github.com/jeffangel/stoppy/releases/download/v0.1.0/stoppy-0.1.0-py3-none-any.whl
```

### 🐍 Recomendación: usa un entorno virtual

Para evitar conflictos con otras dependencias, se recomienda instalar stoppy dentro de un entorno virtual.

#### Python -m venv (estándar)

```bash
python3 -m venv .venv
source .venv/bin/activate   # En Linux / macOS
.venv\Scripts\activate      # En Windows PowerShell

pip install --upgrade pip
pip install https://github.com/jeffangel/stoppy/releases/download/v0.1.0/stoppy-0.1.0-py3-none-any.whl
```


## ▶️ Uso

Una vez instalado, ejecuta:

```bash
stoppy modern   # Usa pynput version
```

Esto simulará actividad en tu sistema (mediante pynput), evitando que Teams y aplicaciones similares cambien tu estado a inactivo.

Para detener la ejecución presiona "clic derecho" o "ctrl + c"