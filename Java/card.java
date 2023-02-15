import CursoPOO.Java.payment;

public class card extends payment {
    Integer numberCard; 
    String dateCard; 
    String ccv; 

    public card(Integer id, Integer numberCard, String dateCard, String ccv){
        super(id); 
        this.numberCard = numberCard; 
        this.dateCard = dateCard; 
        this.ccv = ccv; 
    }
    
}
