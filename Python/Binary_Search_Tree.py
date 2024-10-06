def create_node(value):
    return {'value': value, 'left': None, 'right': None}

def insert(root, value):
    if root is None:
        return create_node(value)
    if value < root['value']:
        root['left'] = insert(root['left'], value)
    else:
        root['right'] = insert(root['right'], value)
    return root

def search(root, value):
    if root is None:
        return "Not Found"
    if root['value'] == value:
        return "Found"
    if value < root['value']:
        return search(root['left'], value)
    else:
        return search(root['right'], value)

def find_min(root):
    while root['left'] is not None:
        root = root['left']
    return root

def delete(root, value):
    if root is None:
        return root
    if value < root['value']:
        root['left'] = delete(root['left'], value)
    elif value > root['value']:
        root['right'] = delete(root['right'], value)
    else:
        if root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root['left']
        min_node = find_min(root['right'])
        root['value'] = min_node['value']
        root['right'] = delete(root['right'], min_node['value'])
    return root

def in_order(root, result=[]):
    if root is not None:
        in_order(root['left'], result)
        result.append(root['value'])
        in_order(root['right'], result)
    return result

root = None
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 25)

print(search(root, 25)) 

root = delete(root, 10)

print(in_order(root))  
