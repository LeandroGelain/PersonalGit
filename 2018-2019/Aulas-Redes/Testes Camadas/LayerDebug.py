from BaseLayer import BaseLayerInterface, LayersInterface, DebugLayer
from typing import List

class StringLayer(LayersInterface):

    top: LayersInterface
    bottom: LayersInterface

    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()

        def top_receive(data):
            self.bottom.invite_data(data)

        self.top.receive = top_receive
        
        def bottom_receive(data):
            self.top.invite_data(data)

        self.bottom.receive = bottom_receive

class RevertLayer(LayersInterface):
    
    top: LayersInterface
    bottom: LayersInterface

    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()

        def top_receive(data):
            reverce_data = data[::-1]
            self.bottom.invite_data(reverce_data)

        self.top.receive = top_receive
        
        def bottom_receive(data):
            reverce_data = data[::-1]
            self.top.invite_data(reverce_data)

        self.bottom.receive = bottom_receive

class CharLayer(LayersInterface):
    
    top: LayersInterface
    bottom: LayersInterface

    def __init__(self):
        self.top = BaseLayerInterface()
        self.bottom = BaseLayerInterface()

        self.buffer = []
        
        def top_receive(data):
            if data is None:
                self.top.invite_data(''.join(self.buffer))
                self.buffer = []
            else:
                self.buffer.append(data)
        self.bottom.receive = top_receive
        
        def bottom_receive(data):
            for char in data:
                self.bottom.invite_data(char)
            self.bottom.invite_data(None)

        self.top.receive = bottom_receive


class Layer:
    top = LayersInterface
    bottom = LayersInterface

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
    a2 = RevertLayer()
    a1 = CharLayer()
    
    b3 = StringLayer()
    b2 = RevertLayer()
    b1 = CharLayer()
    
    a3.top.add_listener(DebugLayer('A3 Top'))
    a3.bottom.add_listener(DebugLayer('A3 Bottom'))
    b3.top.add_listener(DebugLayer('B3 Top'))
    b3.bottom.add_listener(DebugLayer('B3 Bottom'))
    
    a2.top.add_listener(DebugLayer('A2 Top'))
    a2.bottom.add_listener(DebugLayer('A2 Bottom'))
    b2.top.add_listener(DebugLayer('B2 Top'))
    b2.bottom.add_listener(DebugLayer('B2 Bottom'))
    
    a1.top.add_listener(DebugLayer('A1 Top'))
    a1.bottom.add_listener(DebugLayer('A1 Bottom'))
    b1.top.add_listener(DebugLayer('B1 Top'))
    b1.bottom.add_listener(DebugLayer('B1 Bottom'))
    
    Layer.connect_all(a3, a2, a1)
    Layer.connect_all(b3, b2, b1)
    Layer.crossover(b1,a1)
    # quit()
   
    # a3.top.receive('leandro')
    b3.top.receive('Leandro Gelain')
    # print('-----------------')