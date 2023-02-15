import CursoPOO.Java.account;
import CursoPOO.Java.car;

public class uberpool extends car{
    String brand; 
    String model; 

    public uberpool(String license, account driver, String brand, String model){
        super(license, driver);
        this.brand = brand; 
        this.model = model; 

    }

}


