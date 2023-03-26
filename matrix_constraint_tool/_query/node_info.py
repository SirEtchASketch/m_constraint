import maya.cmds as mc


class node_info():
    
    super()__init__(object):
    self.object = object
    
    """get info about a node
    
    """
    @classmethod
    def from_selection(type:str):
        
        selection = mc.ls(sl=True, type= type, long = True)       
        if selection != 1:
            raise ValueError("select ONE object")
        
        return selection[0]
 
 
    @property
    def type(self, object):
        
        return mc.objType(self.object)
 
    @property
    def shape(self, object):  
    
        if self.type != 'shape':
            return object        
        else:
            return mc.listRelatives(self.object, s=True)[0]
    
    @property
    def has_keys(self):
        """check if object has animation on.

        Args:
            object (_type_): _description_
            
        Returns:
            bool
        """
    
    
    def is_constrained(self);
        """check to see if object transforms are constrained.
        
        
        returns bool
        """
        pass
    
    
    def get_constraint_source(self):
        
        """_summary_
        
        Returns:
            list
        """
        constraint_sources = []
        if not self.is_constrained():
            return constraint_sources
            constraint_objects = []
    
        # get all the connections going into the selected node
        input_connections = mc.listConnections(
            self.object, source=True, destination=False, plugs=False
            )
        
        # iterate over each input connection
        for input_connection in input_connections:
            # if the connection is a constraint connection, 
            # get the source node and add it to the list
            if mc.nodeType(input_connection) == "constraint":
                constraint_object = mc.listConnections(
                        input_connection + ".target", 
                        source=True, 
                        destination=False, 
                        plugs=False)[0]
                
                constraint_sources.append(constraint_object)
        
        return constraint_objects
        
            
    @property
    def get_downstreamNodes(self, type = str):
        """get all the downstream nodes of a specified type:

        Args:
            type (_type_): _description_
            all (_type_): _description_
            
        Returns:
            List
        """
        pass
    @property
    def get_upstreamNodes(self, type = srt, all = bool):
        """get all the upstream nodes of a specified type:

        Args:
            type (_type_): _description_
            all (_type_): _description_
        Returns:
            List
        """
        pass