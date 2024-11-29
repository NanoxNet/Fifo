# NanoxNet File Manager FIFO

Un sistema de gestión de archivos FIFO (First In, First Out) con dos versiones: interfaz gráfica moderna y línea de comandos, desarrollado en Python.

## 📋 Descripción

Sistema de gestión de archivos que implementa el principio FIFO con dos versiones disponibles:

1. **Versión GUI (fifo4.1.py)**:
   - 🎨 Interfaz gráfica moderna estilo "hacker"
   - 📊 Barra de progreso dinámica tricolor
   - ⏱️ Estimación de tiempo en tiempo real
   - 📝 Log de actividades detallado

2. **Versión CLI (fifo2.py)**:
   - ⚡ Implementación ligera en consola
   - 🔄 Procesamiento secuencial simple
   - 📋 Salida de estado en tiempo real

## 🚀 Características Principales

### Versión GUI
- 🎯 Interfaz moderna con tema oscuro y detalles en verde
- 📊 Barra de progreso con cambios de color según el avance:
  - 🔴 Rojo (0-33%)
  - 🟡 Amarillo (33-66%)
  - 🟢 Verde (66-100%)
- ⏱️ Estimación de tiempo restante en tiempo real
- 📝 Registro detallado de operaciones
- 🔄 Procesamiento asíncrono con threading

### Versión CLI
- ⚡ Ejecución rápida y eficiente
- 📋 Visualización simple del proceso
- 🔄 Sistema FIFO básico
- 🗑️ Limpieza automática de directorios

## 💻 Requisitos

- Python 3.x
- Módulos incluidos en Python:
  - tkinter (para versión GUI)
  - threading
  - os
  - time

## 🛠️ Instalación

1. Clona el repositorio:
   git clone https://github.com/tu-usuario/nanoxnet-file-manager.git
   
2. Navega al directorio:
   cd nanoxnet-file-manager
   
## 📖 Uso

### Versión GUI (fifo4.1.py)

python fifo4.1.py
1. Configura el directorio de trabajo
2. Selecciona número de archivos (1-20)
3. Presiona "Iniciar"
4. Observa el proceso en tiempo real

### Versión CLI (fifo2.py)

python fifo2.py
- Ejecuta y observa el proceso automático
- Crea y elimina 6 archivos secuencialmente
- Espera 5 segundos entre eliminaciones

## 🔧 Funcionamiento

El sistema:
1. ✨ Crea un directorio temporal
2. 📁 Genera archivos secuencialmente
3. 🔄 Procesa archivos en orden FIFO
4. 📊 Muestra progreso en tiempo real
5. 🗑️ Limpia el directorio al finalizar

## 👨‍💻 Autor

- **NanoEspinoza**
- ID: E00000404309
- Corporación: NanoxNet_Corp

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🎯 Próximas Mejoras

- [ ] Soporte para múltiples directorios
- [ ] Personalización de intervalos de tiempo
- [ ] Exportación de logs
- [ ] Diferentes tipos de archivos
- [ ] Temas visuales adicionales

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork del proyecto
2. Crea tu rama de características
3. Commit de tus cambios
4. Push a la rama
5. Abre un Pull Request

## ⚠️ Notas Importantes

- Sistema diseñado con propósitos educativos
- No usar en directorios con archivos importantes
- Verificar permisos de escritura en el directorio de trabajo

---
*Desarrollado por NanoxNet_Corp © 2024*
