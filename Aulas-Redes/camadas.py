from typing import List

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
        
class CharLayer():
    top: LayerInterface
    bottom: LayerInterface
    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()
        
        self.buffer = []
        
        def top_receive(data):
           if data is None:
                self.top.fire_data(''.join(self.buffer))
                self.buffer = []
       
           else:
       
                self.buffer.append(data)
        self.bottom.receive = top_receive
 
        def bottom_receive(data):
            for c in data:
                self.bottom.fire_data(c)
            self.bottom.fire_data(None)
           
        self.top.receive = bottom_receive

class Layer:
    top = LayerInterface
    bottom = LayerInterface

    @classmethod
    def connect_all(cls, *layers : List['Layer']):
        for a, b in zip(layers[:-1], layers[1:]):
            a.bottom.add_listener(b.top)
            b.top.add_listener(a.bottom)

    @classmethod
    def crossover(cls, a : 'Layer', b : 'Layer'):
        a.bottom.add_listener(b.bottom)
        b.bottom.add_listener(a.bottom)

if __name__ == '__main__':

    a3 = StringLayer()
    a2 = ReverseLayer()
    a1 = CharLayer()
    
    b3 = StringLayer()
    b2 = ReverseLayer()
    b1 = CharLayer()
    
    a3.top.add_listener(DebugLayerListener('A3 Top'))
    a3.bottom.add_listener(DebugLayerListener('A3 Bottom'))
    b3.top.add_listener(DebugLayerListener('B3 Top'))
    b3.bottom.add_listener(DebugLayerListener('B3 Bottom'))
    
    a2.top.add_listener(DebugLayerListener('A2 Top'))
    a2.bottom.add_listener(DebugLayerListener('A2 Bottom'))
    b2.top.add_listener(DebugLayerListener('B2 Top'))
    b2.bottom.add_listener(DebugLayerListener('B2 Bottom'))
    
    a1.top.add_listener(DebugLayerListener('A1 Top'))
    a1.bottom.add_listener(DebugLayerListener('A1 Bottom'))
    b1.top.add_listener(DebugLayerListener('B1 Top'))
    b1.bottom.add_listener(DebugLayerListener('B1 Bottom'))
    
    Layer.connect_all(a3, a2, a1)
    Layer.connect_all(b3, b2, b1)
    Layer.crossover(b1,a1)
    
   
    b3.top.receive('subinoonibus')
    # b3.top.receive('zezinho')
    # print('-----------------')