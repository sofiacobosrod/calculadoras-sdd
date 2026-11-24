# Investigación: Clean Architecture

Herramienta usada: NotebookLM

## ¿Qué es?
Clean Architecture es la forma en donde se escribe un codigo de una aplicación en capas diferentes. La idea de este diseño es que existan dependencias de código que apuntan hacia adentro, es decir, las capas internas no saben lo que ocurre en las capas externas. 

## Capas
- **Domain:** es la esencia de la aplicación en donde está lo protegido dentro del sistema, aquí también están las reglas puras del negocio. 
- **Application:** es el caso de uso, en donde se dictan las acciones concretas que se tienen que realizar. 
- **Infrastructure:** Es la base datos y la interfaz, aquí están las herramientas técnicas.

## Regla de dependencia
Las dependencias apuntan hacía adentro, las capas internas no deben saber que está pasando en las capas externas. Esto es para proteger el nucleo y que se pueda mantener a salvo e intacto ante cualquier cambio en alguna capa externa.

## Cómo lo aplico en mi calculadora
- Domain: las operaciones (Suma, Resta, Multiplicacion, Division) y sus reglas.
- Application: los casos de uso que reciben las teclas y calculan.
- Infrastructure: la ventana con botones y el archivo del historial.
- main.py: conecta todas las piezas.

## Fuentes
- Robert C. Martin, "The Clean Architecture" (blog.cleancoder.com, 2012)
- https://www.youtube.com/watch?v=07JAkHUoSKE