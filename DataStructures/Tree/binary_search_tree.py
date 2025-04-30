from DataStructures.Tree import bst_node
from DataStructures.List import array_list as al

def new_map():
    return {"root": None}

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def insert_node(root, key, value):
    if root is None:
        return bst_node.new_node(key, value)
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def get(my_bst, key):
    found_node = get_node(my_bst["root"], key)
    return found_node["value"] if found_node else None

def get_node(root, key):
    node = None
    if root is not None:
        if key < root["key"]:
            node = get_node(root["left"], key)
        elif key > root["key"]:
            node = get_node(root["right"], key)
        else:
            node = root
    return node         

def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def remove_node(root, key):
    if root is not None:
        if key < root["key"]:
            root["left"] = remove_node(root["left"], key)
        elif key > root["key"]:
            root["right"] = remove_node(root["right"], key)
        else:
            if root["right"] is None:
                return root["left"]
            elif root["left"] is None:
                return root["right"]
            else:
                element = root
                root = get_min_node(element["right"])
                root["right"] = delete_min_tree(element["right"])
                root["left"] = element["left"]
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def contains(my_bst, key):
    return get(my_bst, key) is not None

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])

def is_empty(my_bst):
    return my_bst["root"] is None

def key_set(my_bst):
    keys = al.new_list()
    keys = key_set_tree(my_bst["root"], keys)
    return keys
    
def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        al.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list

def value_set(my_bst):
    values = al.new_list()
    values = value_set_tree(my_bst["root"], values)
    return values
    
def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        al.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list

def get_min(my_bst):
    node = get_min_node(my_bst["root"])
    if node is not None:
        return node["key"]
    return node

def get_min_node(root):
    min = None
    if root is not None:
        if root["left"] is None:
            min = root
        else:
            min = get_min_node(root["left"])
    return min

def get_max(my_bst):
    node = get_max_node(my_bst["root"])
    if node is not None:
        return node["key"]
    return node

def get_max_node(root):
    max = None
    if root is not None:
        if root["right"] is None:
            max = root
        else:
            max = get_max_node(root["right"])
    return max

def delete_min(my_bst):
    return delete_min_tree(my_bst["root"])

def delete_min_tree(root):
    if root is not None:
        if root["left"] is None:
            return root["right"]
        else:
            root["left"] = delete_min_tree(root["left"])
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def delete_max(my_bst):
    return delete_max_tree(my_bst["root"])

def delete_max_tree(root):
    if root is not None:
        if root["right"] is None:
            return root["left"]
        else:
            root["right"] = delete_max_tree(root["right"])
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def floor(my_bst, key):
    node = floor_key(my_bst["root"], key)
    if node is not None:
        return node["key"]
    return node

def floor_key(root, key):
    if root is not None:
        if key < root["key"]:
            return floor_key(root["left"], key)
        elif key > root["key"]:
            candidate = floor_key(root["right"], key)
            if candidate is not None:
                return candidate
            else:
                return root
        else:
            return root
    return root   

def ceiling(my_bst, key):
    node = ceiling_key(my_bst["root"], key)
    if node is not None:
        return node["key"]
    return node

def ceiling_key(root, key):
    if root is not None:
        if key > root["key"]:
            return ceiling_key(root["right"], key)
        elif key < root["key"]:
            candidate = ceiling_key(root["left"], key)
            if candidate is not None:
                return candidate
            else:
                return root
        else:
            return root
    return root 

def select(my_bst, pos):
    node = select_key(my_bst["root"], pos)
    if node is not None:
        return node["key"]
    return node

def select_key(root, key):
    if root is not None:
        count = size_tree(root["left"])
        if count > key:
            return select_key(root["left"], key)
        elif count < key:
            return select_key(root["right"], key - count - 1)
        else:
            return root
    return root

def rank(my_bst, key):
    return rank_keys(my_bst["root"], key)

def rank_keys(root, key):
    if root is not None:
        if key < root["key"]:
            return rank_keys(root["left"], key)
        elif key > root["key"]:
            left_size = size_tree(root["left"])
            rank = rank_keys(root["right"], key)
            total = 1 + left_size + rank
            return total
        else:
            return size_tree(root["left"])
    return 0

def height(my_bst):
    return height_tree(my_bst["root"])

def height_tree(root):
    if root is None:
        return -1
    else:
        return 1 + max(height_tree(root["left"]), height_tree(root["right"]))

def keys(my_bst, key_initial, key_final):
    list_key = al.new_list()
    list_key = keys_range(my_bst["root"], key_initial, key_final, list_key)
    return list_key

def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        if key_initial < root["key"]:
            keys_range(root["left"], key_initial, key_final, list_key)
        if key_initial <= root["key"] and key_final >= root["key"]:
            al.add_last(list_key, root["key"])
        if key_final > root["key"]:
            keys_range(root["right"], key_initial, key_final, list_key)
    return list_key

def values(my_bst, key_initial, key_final):
    list_values = al.new_list()
    list_values = values_range(my_bst["root"], key_initial, key_final, list_values)
    return list_values

def values_range(root, key_initial, key_final, list_value):
    if root is not None:
        if key_initial < root["key"]:
            values_range(root["left"], key_initial, key_final, list_value)
        if key_initial <= root["key"] and key_final >= root["key"]:
            al.add_last(list_value, root["value"])
        if key_final > root["key"]:
            values_range(root["right"], key_initial, key_final, list_value)
    return list_value

def default_compare(key, element):
   if key == bst_node.get_key(element):
      return 0
   elif key > bst_node.get_key(element):
      return 1
   return -1