class LayersListener(object):

    def receive(self, data):
        raise NotImplementedError()

class LayersInterface(object):

    def add_listener(self, listener):
        raise NotImplementedError()

    def receive(self, data):
        raise NotImplementedError()

class DebugLayer(LayersListener):

    def __init__(self, prefix):
        self.prefix = prefix

    def receive(self, data):
        print("%s:  %s"%(self.prefix, data))

class BaseLayerInterface(LayersInterface):

    def __init__(self):
        self.listeners = []
    
    def add_listener(self, listener):
        self.listeners.append(listener)

    def invite_data(self, data):
        for listener in self.listeners:
            listener.receive(data)

    def receive(self, data):
        raise NotImplementedError()