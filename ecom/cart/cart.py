from store.models import Product

class Cart():
    def __init__(self,request):
        self.session = request.session

        #get the session key if exist
        cart = self.session.get('session_key')

        #if new user, create session key 

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        
        self.cart = cart


    def add(self,product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True

    def cart_total(self):
        # get product ids 
        product_ids = self.cart.keys()
        #use ids to lookup product in db models
        products = Product.objects.filter(id__in = product_ids)
        #get quantities
        quantities = self.cart
        # starr counting at 0
        total = 0
        for key,value in quantities.items():

            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total
    


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #use ids to lookup product in db models
        products = Product.objects.filter(id__in = product_ids)
        #return those looked up prods
        return products 

    def get_quants(self):
        quantities = self.cart
        return quantities
    
    # def update(self,product, quantity):
    #     product_id = str(product)
    #     product_qty = int(quantity)

    #     #get the cart
    #     ourcart = self.cart
    #     #updte cart
    #     ourcart[product_id] = product_qty
    #     self.session.modified = True

    #     thing = self.cart
    #     return thing
    
    def delete(self,product):
        product_id = str(product)
      
        # Delete from cart
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True    