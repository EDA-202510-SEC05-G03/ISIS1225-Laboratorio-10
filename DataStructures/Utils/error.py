"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Estructura utilizada para el manejo de los errores durante la manipulación
  de estructuras de datos y TADs
"""


def reraise(excp, *args):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    excp.args = args + excp.args
    raise excp.with_traceback(excp.__traceback__)


class FunctionNotImplemented(Exception):
    """
    Estructura de error para funciones que no están implementadas
    """

    def __init__(self, function, type="NOT_IMPLEMENTED"):
        self.function = function
        self.type = type
        super().__init__(self.function)

def error_handler(context: str,
                  func_name: str,
                  err: Exception) -> None:
    """*error_handler()* recibe el contexto, nombre de la función y la excepción para lanzar un mensaje de error detallado y el traceback.

    Args:
        context (str): nombre del contexto donde ocurrió el error (paquete/módulo/clase).
        func_name (str): nombre de la función donde ocurrió el error (método).
        err (Exception): excepción lanzada.

    Raises:
        type: excepción con el mensaje de error detallado y el traceback.
    """
    err_msg = f"Error in {context}.{func_name}: {err}"
    raise type(err)(err_msg).with_traceback(err.__traceback__)