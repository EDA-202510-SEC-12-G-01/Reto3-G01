import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from DataStructures.List import single_linked_list as sll

def new_stack():
    """
    Crea una nueva pila vacía basada en una lista enlazada simple,
    usando la función al.new_list().
    Returns:
        dict: El diccionario que retorna sll.new_list(), por ejemplo:
              {
                  'size': 0,
                  'elements': []
              }
    """
    return sll.new_list()

def push(my_stack, element):
    """
    Añade el elemento 'element' al tope de la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
        element (any): Elemento que se añadirá a la pila.
    Returns:
        dict: La pila actualizada (my_stack).
    """
    sll.add_first(my_stack, element)
    return my_stack

def pop(my_stack):
    """
    Elimina el elemento en el tope de la pila 'my_stack' y lo retorna.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        any: Elemento eliminado de la pila.
    """
    return sll.remove_first(my_stack)

def is_empty(my_stack):
    """
    Verifica si la pila 'my_stack' está vacía.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 0,
                             'elements': []
                         }
    Returns:
        bool: True si la pila está vacía, False de lo contrario.
    """
    return sll.is_empty(my_stack)

def top(my_stack):
    """
    Retorna el elemento en el tope de la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        any: Elemento en el tope de la pila.
    """
    return sll.first_element(my_stack)

def size(my_stack):
    """
    Retorna la cantidad de elementos en la pila 'my_stack'.
    Parameters:
        my_stack (dict): Estructura de pila que internamente es una array_list,
                         por ejemplo:
                         {
                             'size': 2,
                             'elements': [1,2]
                         }
    Returns:
        int: Cantidad de elementos en la pila.
    """
    return sll.size(my_stack)