DESCRIPCIÓN DE LA IMPLEMENTACIÓN:
Desarrollado para gestionar el acceso y la
seguridad de una plataforma web, utilizando el framework Django. 
La solución se centra en la autenticación de usuarios y la 
autorización basada en permisos específicos sobre el modelo Auth.


1. AUTENTICACIÓN Y SESIONES:
   - Se utilizaron las vistas LoginView y LogoutView de Django.
   - Se implementó un sistema de mensajes (Django Messages) para 
     confirmar el "Registro Exitoso" al redireccionar al Login.
   - Interfaz con visibilidad de contraseña (ojo) vía JavaScript.

2. CONTROL DE ACCESO (LoginRequiredMixin):
   - La vista 'HomeView' requiere autenticación obligatoria.
   - Usuarios no logueados son redirigidos automáticamente al inicio 
     de sesión.

3. AUTORIZACIÓN Y PERMISOS (PermissionRequiredMixin):
   - La vista 'AdminDataView' (Zona de Administración) está protegida 
     y solo es accesible para usuarios con el permiso 'auth.view_user'.
   - Se configuró 'raise_exception = True' para denegar el acceso 
     mediante un error 403 a usuarios sin privilegios.

4. GESTIÓN DE USUARIOS (Tablas del Modelo Auth):
   - Registro extendido: Se utilizó un formulario personalizado 
     (RegistroConEmailForm) para capturar el correo electrónico.
   - Protección de integridad: Se bloqueó la posibilidad de eliminar 
     al superusuario 'admin' desde la interfaz para evitar un caso critico de seguridad
 
INSTRUCCIONES PARA LA EJECUCIÓN:
-----------------------------------------------------------
1. Descomprimir el archivo seguridad_acceso_django.zip.
2. Ejecutar: python manage.py migrate (para asegurar la base de datos).
3. Iniciar servidor: python manage.py runserver.
4. Acceder a http://127.0.0.1:8000/ e iniciar sesión con la cuenta

Cuenta de admin: admin
Clave de acceso: admin1234

se incluye usuarios de prueba para revisar desde el Panel

ACTUALIZACION 

- Se agrega usuario y grupo moderador y usuario modprueba desde panel de adminstracion y se asignan permisos de 
- Usuario: modprueba
- Clave: mod12345
## Gestión Administrativa
Se habilitó el sitio administrativo para el modelo `ConsultaContacto`. 
- **Superusuario:** Acceso total a la base de datos y gestión de staff.
- **Seguridad:** Se aplicó el principio de "menor privilegio", otorgando 'Staff status' solo a usuarios operativos sin darles acceso a la configuración global (is_superuser).







