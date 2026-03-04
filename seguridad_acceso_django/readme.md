### Pasos para ejecutar el proyecto

Para levantar el sistema en un entorno local
    Entorno Virtual: Crea y activa tu entorno virtual.
    CMD
    python -m venv venv
    .\venv\Scripts\activate

    Instalación: Instala Django 

    pip install django

    Migraciones: Prepara la base de datos para el sistema de autenticación y el modelo de contactos.
    Bash

    python manage.py migrate

    Servidor: Inicia el servidor de desarrollo.
    Bash

    python manage.py runserver

2. Rutas Principales

El sistema cuenta con las siguientes rutas configuradas en urls.py:

    Registro (registro): Permite la creación de nuevos usuarios mediante el formulario personalizado RegistroConEmailForm, el cual captura y valida el correo electrónico.

    Inicio de Sesión (login): Interfaz de acceso protegida por CSRF que redirige al usuario a la sección interna tras un éxito.

    Vista Protegida (panel): Dashboard interno accesible solo para usuarios autenticados mediante el uso de LoginRequiredMixin o el decorador @login_required.

    Cierre de Sesión (logout): Implementado mediante el método POST para cumplir con los estándares de seguridad.

3. Usuario de Prueba

Para acceder directamente a la vista protegida, puedes utilizar:

    Usuario: admin

    Contraseña: admin1234 

    Usuario: moderador

    Contraseña: mod12345

    