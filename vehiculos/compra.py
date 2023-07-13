

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, vehiculo):
        if vehiculo.patente not in self.carrito.keys():
            self.carrito[vehiculo.patente]={
                "vehiculo_id":vehiculo.patente, 
                "marca": vehiculo.marca,
                "modelo": vehiculo.modelo,
                "precio": str (vehiculo.precio),
                "cantidad": 1,
                "total": vehiculo.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==vehiculo.patente:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = vehiculo.precio
                    value["total"]= value["total"] + vehiculo.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, vehiculo):
        id = vehiculo.patente
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,vehiculo):
        for key, value in self.carrito.items():
            if key == vehiculo.patente:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- vehiculo.precio
                if value["cantidad"] < 1:   
                    self.eliminar(vehiculo)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
