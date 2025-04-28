# Funciones Principales de la API
Se define como funcionalidad todas las capacidades que tiene este software
1. Extraer datos de redes sociales relacionados a publicaiones hechas por un conjunto de usuarios determinadas
2. Alimentar una base de datos mysql para almacenar estos datos
3. Registrar usuarios de redes sociales a los cuales se les quiera dar seguimiento
4. Registrar personas fisicas que manejen usuarios 
5. Registrar clientes y su informacion de contacto
6. Registrar campagnas (conjunto de publicaciones hechas entorno a un hecho y a peticion de un cliente)
7. Creacion y modificacion de Equipos (conjuntos de personas)
# Objetos que Interactuan con la API
- Dashboard de Seguimiento de Campgna
- Interfaces de registro y modificacion de campagna, cuentas, personas fisicas, clientes y equipos
# Entidades y Modelos
## Plataforma
La entidad de plataforma representa a las redes sociales donde se hacen las publicaciones
### Atributos
- id: identificador unico en el software. De tipo entero ya que es de una cantidad reducida
- nombre: nombre de la red social. De tipo string ya que solo es una cadena de caracteres
- url: la direccion en la cual se encuentra la red social. De tipo string ya que solo suele ser un cadena de caracteres
- descrption: una pequeña descripcion de la red social
### Modelos de clase
- PlatformBase
    - id
    - nombre
- Platform
    - id
    - nombre 
    - descripcion
- PlatformCreate
    - nombre
    - descripcion (opcional)
- PlatformUpdate
    - id 
    - nombre
- PlatformDelete
    - id
### Metodos
- Crear Plataforma: Registra una plataforma una plataforma 
    - Recibe el nombre y la descripcion de la plataforma y los inserta en una fila nueva de la tabla plataforma
    - Retorna el objeto creado
- Actualizar Plataforma: altera un registro de una plataforma 
    - Recibe el id y el nombre de la plataforma que se vaya a cambiar, junto con el cambio con los cambios guardados 
    - Retorna un codigo HTTP 200 y un mensaje que indica que la operacion fue correcta.
# Endpoints
# Esquemas
# Servicios
