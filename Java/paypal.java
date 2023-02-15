import CursoPOO.Java.payment;

public class paypal extends payment  {
    String email; 

    public paypal(Integer id, String email){
        super(id); 
        this.email = email; 
    }
}
