# Juego de la Vida (Conway's Game of Life)

Este proyecto es una implementación del **Juego de la Vida de Conway** utilizando **Pygame**. Se trata de una simulación basada en reglas simples que determinan la evolución de una población de células en una grilla.

## Características
- Grilla cuadrada de **25x25**.
- Visualización de la evolución del sistema en **modo gráfico con Pygame**.
- Configuración inicial cargada desde un archivo de texto.
- Controles interactivos:
  - **B** (Begin): Inicia la simulación.
  - **Q** (Quit): Finaliza el programa.
- Soporte para patrones iniciales conocidos: "Still Lifes", "Oscillators" y "Spaceships".

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/leoehz/GameOfLife.git
   cd GameOfLife
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejecuta el siguiente comando para iniciar la simulación dentro de la carpeta src:
```bash
python main.py
```

El archivo de configuración inicial debe seguir el formato:
```
3,4
5,6
7,8
```
Cada línea representa una célula viva en la grilla, con su fila y columna correspondientes.

## Estructura del Proyecto
```
📂 GameOfLife/
├── 📂 assets/              # Recursos gráficos y sonidos
├── 📂 config/              # Archivos de configuración
│   ├── initial_state.txt   # Configuración inicial de la grilla
├── 📂 src/                 # Código fuente
│   ├── game.py            # Lógica del Juego de la Vida
│   ├── conf.py            # Configuracion general del juego
│   ├── renderer.py        # Renderizado con Pygame
│   ├── main.py            # Punto de entrada del programa
├── 📜 README.md           # Documentación del proyecto
├── 📜 requirements.txt     # Dependencias necesarias
```

## Créditos
- Basado en el concepto del "Juego de la Vida" de John Conway.
- Implementado en **Python** utilizando **Pygame**.

## Licencia
Este proyecto está bajo la licencia MIT.

