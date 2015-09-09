pyconve_site
==============================

Sitio web para el PyConVE 2016. Usando la plantilla de Django CookieCutter.


LICENCIA: BSD

Settings
------------



pyconve_site depende extensivamente de configuraciones del entorno (enviroment variables) las cuales **no funcionan en Apache/mode_wsgi**. 

Para la configuración de estas variables, la siguiente tabla muestra la correspondencia entre las variables de entorno y la variable de configuración de Django:

======================================= =========================== ============================================== ======================================================================
Variable de Entorno                     Django Setting              Valor para Desarrollo                          Valor para Producción
======================================= =========================== ============================================== ======================================================================
DJANGO_CACHES                           CACHES (default)            locmem                                         redis
DJANGO_DATABASES                        DATABASES (default)         See code                                       See code
DJANGO_DEBUG                            DEBUG                       True                                           False
DJANGO_SECRET_KEY                       SECRET_KEY                  CHANGEME!!!                                    raises error
DJANGO_SECURE_BROWSER_XSS_FILTER        SECURE_BROWSER_XSS_FILTER   n/a                                            True
DJANGO_SECURE_SSL_REDIRECT              SECURE_SSL_REDIRECT         n/a                                            True
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF      SECURE_CONTENT_TYPE_NOSNIFF n/a                                            True
DJANGO_SECURE_FRAME_DENY                SECURE_FRAME_DENY           n/a                                            True
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS   HSTS_INCLUDE_SUBDOMAINS     n/a                                            True
DJANGO_SESSION_COOKIE_HTTPONLY          SESSION_COOKIE_HTTPONLY     n/a                                            True
DJANGO_SESSION_COOKIE_SECURE            SESSION_COOKIE_SECURE       n/a                                            False
DJANGO_DEFAULT_FROM_EMAIL               DEFAULT_FROM_EMAIL          n/a                                            "pyconve_site <noreply@ve.pycon.org>"
DJANGO_SERVER_EMAIL                     SERVER_EMAIL                n/a                                            "pyconve_site <noreply@ve.pycon.org>"
DJANGO_EMAIL_SUBJECT_PREFIX             EMAIL_SUBJECT_PREFIX        n/a                                            "[pyconve_site] "
DJANGO_ALLOWED_HOSTS                    ALLOWED_HOSTS               ['*']                                          ['ve.pycon.org']
======================================= =========================== ============================================== ======================================================================

La siguiente tabla lista las configuraciones por defecto para las aplicaciones de terceros utilizadas:

======================================= =========================== ============================================== ======================================================================
Variable de Entorno                     Django Setting              Valor para Desarrollo                          Valor para Producción
======================================= =========================== ============================================== ======================================================================
DJANGO_AWS_ACCESS_KEY_ID                AWS_ACCESS_KEY_ID           n/a                                            raises error
DJANGO_AWS_SECRET_ACCESS_KEY            AWS_SECRET_ACCESS_KEY       n/a                                            raises error
DJANGO_AWS_STORAGE_BUCKET_NAME          AWS_STORAGE_BUCKET_NAME     n/a                                            raises error

DJANGO_MAILGUN_API_KEY                  MAILGUN_ACCESS_KEY          n/a                                            raises error
DJANGO_MAILGUN_SERVER_NAME              MAILGUN_SERVER_NAME         n/a                                            raises error
======================================= =========================== ============================================== ======================================================================

Ejecutando el proyecto
----------------------

Inicio
^^^^^^

Debes seguir los siguientes pasos para ejecutar el entorno de desarrollo. Asumimos que las siguientes aplicaciones están instaladas:

* pip
* virtualenv

Primero, asegúrate de crear y activar un virtualenv_, luego en una terminal en la raíz del proyecto instala los requerimientos para el desarrollo local::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Ejecuta ``migrate`` para crear la base de datos inicial::

    $ python manage.py migrate

Ejecuta el servidor local con ``runserver_plus``::

    $ python manage.py runserver_plus

Abre el navegador en http://127.0.0.1:8000/ para ver el site corriendo localmente.

Configuración de Usuarios
^^^^^^^^^^^^^^^^^^^^^^^^^

Para crear una cuenta de **usuario normal**, simplemente se utiliza el formulario de registro. Una vez enviado, verás un mensaje de "Verificar el Email". Ve a tu terminal para recibir una simulación de enlace de verificación.

Para crear una cuenta de **super usuario**, usa el siguiente comando::

    $ python manage.py createsuperuser

Test coverage
^^^^^^^^^^^^^

Para ejecutar las pruebas, verificar el *coverage*, y generar un reporte de alcance::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Live reloading y compilación de Sass CSS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si deseas sacar provecho de *live reloading* y compilación de SASS/Compass a CSS, puedes hacerlo con lo siguiente:

Asegurate de tener nodejs_ instalado. Luego en la raíz del proyecto ejecuta::

    $ npm install

.. _nodejs: http://nodejs.org/download/

Ahora sólamente debes ejecutar::

    $ grunt serve

La aplicación base se ejecutará con el comando usual ``manage.py runserver`` pero tendrá el *live reloading* activado.

Deberás instalar la `extensión del navegador`_

.. _extensión del navegador: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

