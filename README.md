# Sistema de Gestión de Ventas para Vivero 🌿

Este repositorio contiene el desarrollo del proyecto para la materia **Diseño y Aplicaciones en la Web** de la facultad. El sistema está orientado a la gestión de un vivero, abarcando los aspectos de ventas, inventario, productos, empleados y clientes.

## 📌 Información General

- **Materia:** Diseño y Aplicaciones en la Web
- **Iteración:** Proyecto desarrollado hasta la **3ra iteración**
- **Metodología utilizada:** UWE (UML-based Web Engineering)
- **Tecnologías principales:** 
  - [Django](https://www.djangoproject.com/) (back-end)
  - [Tailwind CSS](https://tailwindcss.com/) (front-end)
  - HTML5, JavaScript (uso básico en formularios/modales)

## 📂 Estructura del Proyecto

El sistema se encuentra dividido en los siguientes módulos principales:

- **Ventas:** Registro y seguimiento de ventas realizadas.
- **Inventario:** Control de stock y movimientos de productos.
- **Productos:** Alta, baja y modificación de productos.
- **Clientes:** Gestión de datos personales de los clientes.
- **Empleados:** Administración de los empleados del vivero.

## 🧠 Metodología - UWE

El desarrollo se llevó a cabo aplicando la metodología **UWE**, centrada en el modelado sistemático de aplicaciones web. Las tres primeras iteraciones del proyecto incluyeron:

1. **Gestion de empleados y roles**
2. **Gestion de productos e inventario**
3. **Gestion de ventas y clientes**

> Se incluye la documentacion durante las iteraciones en la carpeta `documentacion/uwe`.

## 🚀 Instalación y Ejecución

### Requisitos

- Python 3.10+
- Django 4.x
- Node.js y npm (para compilar Tailwind, opcional)

### Pasos

1. Clonar el repositorio:

```bash
git clone https://github.com/bialyLT/dise-oweb
cd dise-oweb
```
2. Instalar las dependencias 

```bash
pip3 install -r requirements.txt
npm install
```
3. Creamos las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Ejecutamos el proyecto

```bash
// Esto dejamos ejecutando en otra consola para que funcione tailwind:
npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch

python manage.py runserver
```
