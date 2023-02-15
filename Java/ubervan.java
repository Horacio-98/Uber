import java.util.ArrayList;
import java.util.Map;

import CursoPOO.Java.account;
import CursoPOO.Java.car;

public class ubervan extends car{
    Map<String, Map<String, Integer>> typecaraccepted; 
    ArrayList<String> seatsMaterial; 

    public ubervan(String license, account driver, Map<String, Map<String, Integer>> typecaraccepted, ArrayList<String> seatsMaterial){
        super(license, driver);
        this.seatsMaterial = seatsMaterial; 
        this.typecaraccepted = typecaraccepted; 

    }

}


