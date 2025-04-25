# Funciones Principales de la API
Se define como funcionalidad todas las capacidades que tiene este software
1. Extraer datos de redes sociales relacionados a publicaiones hechas por un conjunto de usuarios determinadas
2. Crear y alimentar una base de datos mysql para almacenar estos datos
3. Registrar usuarios de redes sociales a los cuales se les quiera dar seguimiento
4. Crear conjuntos de datos de publicaciones que pueden ser analizados
5. Registrar personas fisicas que manejen usuarios 
6. Registrar clientes y su informacion de contacto
7. Registrar campagnas (conjunto de publicaciones hechas entorno a un hecho y a peticion de un cliente)
8. Creacion y modificacion de Equipos (conjuntos de personas)
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
### Modelos
- Platform 
# Endpoints
# Esquemas
# Servicios
