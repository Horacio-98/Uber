from payment import payment 

class paypal(payment) : 
    email = str
    
    def __init__(self,id,email) -> None:
        super().__init__(id)
        self.email = email
        
    def info(self) : 
        return self.email