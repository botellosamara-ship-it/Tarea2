Api Flash - Gestión de Productos

Hemos realizado un proyecto para gestionar un catálogo de productos en un Api la cual desarrollamos en Flask, usamos Api ya que mediante métodos como GET, POST, PUT y DELETE, podemos realizar operaciones básicas de un CRUD.

Cada método tiene una función: 

GET: consulta la información de los productos.

POST: crea o agrega nuevos productos.

PUT: actualiza la información de un producto existente.

DELETE: elimina un producto.


Antes de todo para poder realizar el programa debemos realizar lo siguiente:
1. Debemos comprobar que Python este instalado ejecutando el comando: python --version
2. También debemos verificar la instalación de Git con el comando: git --version
3. Debemos tener instalado también el postman ya que con el realizaremos las pruebas de los diferentes endpoints.


Proceso para ejecutar el proyecto
1. Clonar el repositorio
   Primero se debe descargar el proyecto desde GitHub utilizando los comandos
   git clone https://github.com/botellosamara-ship-it/Tarea2.git para descargar el repositorio
   cd api para poder ingresar a la carpeta del proyecto

2. Debemos crear el entorno virtual el cual almacenará el entorno virtual del proyecto con el comando: python -m venv .env
   
3. Luego de crear el entorno virtual lo debemos activar con el comando .\env\Scripts\Activate.ps1
4. Ahora las dependencias se deben instalar con el comando pip install flask
5. Ejecutar la aplicación
   Para ejecutar el programa debemos usar el comando python app.py
   la terminal deberá arrojarnos un mensaje el cual seleccionaremos con control y click y correrá, el mensaje es similar a http://127.0.0.1:5000


La terminal deberá estar abierta para realizar las pruebas desde Postman

Las pruebas en Postman con los endpoints se utilizara el URL obtenido anteriormente http://127.0.0.1:5000


GET: Nos ayuda a obtener la lista completa de los productos 

Abrimos Postman.

Creamos una nueva solicitud.

Seleccionamos el método GET.

Escribimos la URL: http://127.0.0.1:5000/api/productos

Presionamos el botón Send.

Postman mostrará la información de los productos registrados.


POST: Nos ayuda a crear o agregar un nuevo producto 

Abrimos una nueva solicitud en Postman.

Seleccionamos el método POST.

Escribimos la URL: http://127.0.0.1:5000/productos

Seleccionamos la pestaña Body.

Seleccionamos raw.

Seleccionamos JSON como tipo de contenido.

Escribimos los datos correspondientes al nuevo producto.

Presionamos Send.

La API procesará la información y creará el nuevo producto.

Ejemplo de la solicitud

{

    "nombre": "Compu",
    
    "precio": 2500000
}


PUT:Nos ayuda a modificar la información de un producto que ya se encuentra registrado 

Abrimos una nueva solicitud en Postman.

Seleccionamos el método PUT.

Escribimos la URL: http://127.0.0.1:5000/productos/3

Seleccionamos Body.

Seleccionamos raw.

Seleccionamos JSON.

Escribimos la nueva información del producto.

Presionamos Send.

La API actualizará la información del producto.

Ejemplo de la solicitud

{

    "id":3, 
    
    "nombre": "Audifonos",
    
        "precio": 150000

}

DELETE: Nos ayuda a eliminar un producto registrado

Abrimos una nueva solicitud en Postman.

Seleccionamos el método DELETE.

Escribimos la URL: http://127.0.0.1:5000/productos/5

Presionamos Send.
La API procesará la solicitud y eliminará el producto.
