import CursoPOO.Java.account;
import CursoPOO.Java.car;

public class uberx extends car{
    String brand; 
    String model; 

    public uberx(String license, account driver, String brand, String model){
        super(license, driver);
        this.brand = brand; 
        this.model = model; 


    }

}


