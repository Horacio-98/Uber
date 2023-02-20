import CursoPOO.Java.account;
import CursoPOO.Java.car;

class uberx extends car{
    String brand; 
    String model; 

    public uberx(String license, account driver, String brand, String model){
        super(license, driver); 
        this.brand = brand; 
        this.model = model; 
         
    }


    void data(){
        System.out.println("License : " + brand);
    }

}


