class LayerListener(object):
     
    def receive(self, data):
        raise NotImplementedError()
 
 
class LayerInterface(object):
 
    def add_listener(self, listener):
        raise NotImplementedError()
 
    def receive(self, data):
        raise NotImplementedError()
 
 
class DebugLayerListener(LayerListener):
 
    def __init__(self, prefix):
        self.prefix = prefix
 
    def receive(self, data):
        print('{}: {}'.format(self.prefix,data))
 
 
class BaseLayerInterface(LayerInterface):
 
    def __init__(self):
        self.listeners = []
 
    def add_listener(self, listener):
        self.listeners.append(listener)
 
    def fire_data(self, data):
        for listener in self.listeners:
            listener.receive(data)
 
    def receive(self, data):
        raise NotImplementedError()
 
class StringLayer():
    top: LayerInterface
    bottom: LayerInterface
 
    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()
 
        def top_receive(data):
            self.bottom.fire_data(data)
 
        self.top.receive = top_receive
 
        def bottom_receive(data):
            self.top.fire_data(data)
       
        self.bottom.receive = bottom_receive
 
 
class ReverseLayer():
    top: LayerInterface
    bottom: LayerInterface
    
    try:
        def __init__(self):
            self.top = BaseLayerInterface()
            self.bottom = BaseLayerInterface()
    
            def top_receive(data):
                result = data[::-1]
                self.bottom.fire_data(result)
    
            self.top.receive = top_receive
    
            def bottom_receive(data):
                result = data[::-1]
                self.top.fire_data(result)
        
            self.bottom.receive = bottom_receive
    
    except TypeError:
        pass

class CharLayer():
    top: LayerInterface
    bottom: LayerInterface
 
    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()
 
        def top_receive(data):
            for c in data:
                self.bottom.fire_data(c)
            self.bottom.fire_data(None)
           
 
        self.top.receive = top_receive
 
        def bottom_receive(data):
            result = data[::-1]
            self.top.fire_data(result)
       
        self.bottom.receive = bottom_receive


def connect_layers(layer_top, layer_bottom):
    layer_top.bottom.add_listener(layer_bottom.top)
    layer_bottom.top.add_listener(layer_top.bottom)
    

def connect_ZZ(layer1,layer2):
    layer1.bottom.add_listener(layer2.bottom)
    layer2.bottom.add_listener(layer1.bottom)

if __name__ == '__main__':
    string_entrado = 'dado por cima'
    
    a_string_layer = StringLayer()
    a_string_layer.top.add_listener(DebugLayerListener('A3 Top'))
    a_string_layer.bottom.add_listener(DebugLayerListener('A3 Bottom'))
    
    a_reverse_layer = ReverseLayer()
    a_reverse_layer.top.add_listener(DebugLayerListener('A2 Top'))
    a_reverse_layer.bottom.add_listener(DebugLayerListener('A2 Bottom'))
    
    a_char_layer = CharLayer()
    a_char_layer.top.add_listener(DebugLayerListener('A1 Top'))
    a_char_layer.bottom.add_listener(DebugLayerListener('A1 Bottom'))
    
    connect_layers(a_string_layer, a_reverse_layer)
    connect_layers(a_reverse_layer, a_char_layer)

    # =====================================================================


    a_reverse_layer.top.add_listener(DebugLayerListener('B2 Top'))
    a_reverse_layer.bottom.add_listener(DebugLayerListener('B2 Bottom'))
    
    a_string_layer.top.add_listener(DebugLayerListener('B3 Top'))
    a_string_layer.bottom.add_listener(DebugLayerListener('B3 Bottom'))

    a_char_layer.top.add_listener(DebugLayerListener('B1 Top'))
    a_char_layer.bottom.add_listener(DebugLayerListener('B1 Bottom'))

    a_string_layer.bottom.add_listener(a_reverse_layer.top)
    a_reverse_layer.bottom.add_listener(a_char_layer.top)

    connect_ZZ(a_char_layer, a_char_layer)
    # b_string_layer.top.receive(string_entrado)
    a_string_layer.top.receive(string_entrado)
    print('-----------------')