def get_diff_tree(dic1, dic2):
    def inner(name, node1, node2):
        if isinstance(node1, dict) and isinstance(node2, dict):
            childs = []
            keys = sorted(set(node1) | set(node2))
            old_keys = set(keys) - set(node2)
            new_keys = set(keys) - set(node1)
            for key in keys:
                if key in old_keys:
                    childs.append({'name': key, 'type': 'deleted',
                                   'value': node1[key]})
                elif key in new_keys:
                    childs.append({'name': key, 'type': 'added',
                                   'value': node2[key]})
                elif (isinstance(node1[key], dict)
                      and isinstance(node2[key], dict)):
                    childs.append(inner(key, node1[key], node2[key]))
                elif node1[key] == node2[key]:
                    childs.append({'name': key, 'type': 'unchanged',
                                   'value': node1[key]})
                else:
                    childs.append({'name': key, 'type': 'changed', 'value':
                                  {'old': node1[key], 'new': node2[key]}})
        return {'name': name, 'type': 'nested', 'childs': childs}
    return inner(None, dic1, dic2)
