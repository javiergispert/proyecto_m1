{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "13ee01c4",
   "metadata": {},
   "source": [
    "# PROJECT 01 DATA README File\n",
    "-----------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba2263a7",
   "metadata": {},
   "source": [
    "\n",
    "## Nombre\n",
    "\n",
    "Visita en bici\n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2de0bd17",
   "metadata": {},
   "source": [
    "---------------"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46c85357",
   "metadata": {},
   "source": [
    "## Status\n",
    "\n",
    "-------------------------------------\n",
    "\n",
    "Alpha, **Beta, 1.1**, Ironhack Data Analytics Final Project\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1163643",
   "metadata": {},
   "source": [
    "## One-liner\n",
    "-----------------\n",
    "La aplicación se conecta a dos bases de datos. Por un lado a la API de la comunidad de Madrid para identificar todos los monumentos de la comunidad de Madrid y por otro lado a una base de datos de Mysql que contiene información sobre las estaciones de BiciMad para ofrecer los puntos de parada más cercanos a cada monumento de la ciudad. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42137077",
   "metadata": {},
   "source": [
    "## Software y Librerías usadas:\n",
    "\n",
    "Para el desarrollo de esta aplicación se ha utilizado el lenguaje de programación [Python](https://www.python.org/downloads/) apoyado a su vez de las siguientes librerías.\n",
    "\n",
    "* [Sqlalchemy](https://www.sqlalchemy.org/).\n",
    "* [Pandas](https://pandas.pydata.org/).\n",
    "* [Requests](https://requests.readthedocs.io/en/latest/).\n",
    "* [Numpy](https://numpy.org/).\n",
    "* [Argparse](https://docs.python.org/3/library/argparse.html).\n",
    "* [Shapely.geometry](https://pypi.org/project/Shapely/)\n",
    "* [Geopandas](https://geopandas.org/en/stable/#:~:text=GeoPandas%20is%20an%20open%20source,access%20and%20matplotlib%20for%20plotting.)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b18deba",
   "metadata": {},
   "source": [
    "## Uso de la aplicación y configuración\n",
    "Existen dos archivos diferentes:\n",
    "* main.py\n",
    "* secuencial.py\n",
    "\n",
    "> El archivo principal es **main.py**, el resto contiene una copia del código puramente secuencial sin ninguna función. Todas las funciones sobre las que se nutre **main.py** se encuentran en la carpeta de **modules**:\n",
    "+ geo_calculations.py: contiene las funciones de mercator para el cálculo de dos puntos en función de sus coordenadas\n",
    "+ macquisition.py: contiene las funciones para la conexión a la bbdd de Mysql y a la Api de la comunidad de Madrid. Para una mejor eficiencia de la aplicación, también contiene la conexión al csv principal con toda la información precargada.\n",
    "+ mexportar.py: contiene una única función para almacenar el resultado en formato csv así como el listado precargado.\n",
    "+ mmanipulaciondf.py: aquí se encuentran todas las operaciones de manipulación de df para seleccionar y limpiar los datos objetivo\n",
    "+ moperacionaritmetica.py: la aplicación directa de mercator a todo el df\n",
    "+ mreporting.py: contiene los resultados que se mostrarán al usuario.\n",
    "\n",
    "> Para arrancar la aplicación en nuestra terminal seguiremos los siguientes pasos:\n",
    "1. Recomendable clonar el repositorio de GitHub en su local\n",
    "2. A través del terminal dirigirse a la carpeta principal donde se encuentra el archivo **main.py**\n",
    "3. Instalar tanto Python como todas las librerías mencionadas anteriormente\n",
    "4. Ejecutar el archivo con el siguiente comando: `python main.py` seguido de `-f` e indicando una de estas dos funciones `one` (en el caso de querer indicar un punto de interés específico) o `all` (si se quiere el punto más cercano a cada punto de interés)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fdefb5d",
   "metadata": {},
   "source": [
    "\n",
    "---------------------\n",
    "![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBrU3-8RkfLnAJrCEKDCJe3n0JO0B1DxC7zNKwlHH-AiTF2H1O6_xIkQeX498tLacqKl0&usqp=CAU)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a06b7196",
   "metadata": {},
   "source": [
    "```\n",
    "└── project_m1\n",
    "    ├── .gitignore\n",
    "    ├── README.md\n",
    "    ├── main.py\n",
    "    ├── secuencial.py\n",
    "    ├── notebooks\n",
    "    │   ├── Main.ipynb\n",
    "    │   ├── Test final.ipynb\n",
    "    │   └── dev_notebook.ipynb\n",
    "    ├── modules\n",
    "    │   ├── geo_calculations.py\n",
    "    │   ├── macquisition.py\n",
    "    │   ├── mexportar.py\n",
    "    │   ├── mmanipulaciondf.py\n",
    "    │   ├── moperacionaritmetica.py\n",
    "    │   └── mreporting.py\n",
    "    └── datasets\n",
    "        ├── bicimad_stations.csv\n",
    "        ├── df.csv\n",
    "        └── results\n",
    "            \n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8f23a43",
   "metadata": {},
   "source": [
    "## Próximos pasos:\n",
    "\n",
    "En versiones futuras, el código está preparado para poder realizar la consulta no solo en base al punto de interés sino también \n",
    "a una parada de BiciMad específica. Del mismo modo, se incluirá la posibilidad de poder indicar un número de estaciones cercanas a un punto de interés para dar más de una solución al usuario.\n",
    "\n",
    "Para versiones posteriores, se tiene previsto ofrecer una imagen visual de recorrido desde el punto de interés a la estación BiciMAD."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f36e848",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:.conda-proyecto_01]",
   "language": "python",
   "name": "conda-env-.conda-proyecto_01-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
