import maya.cmds as mc

"module to generate nodes for connection"

def make_matrix_node(node_type, node_name):

    """Make a matrix node:
    
    Args:
    
    Return:
    
    Exception:
    """
    
    node = mc.createNode(type, name = node_name)
    
    return node