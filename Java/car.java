package CursoPOO.Java;

public class car {
    Integer id; 
    String license; 
    account driver; 
    Integer passenger; 

    public car(String license, account driver ){
        this.license = license; 
        this.driver = driver; 
    }

    void printDataCar() {
        System.out.println("License : " + license);
        System.out.println("Name driver : " + driver.name);
        System.out.println("Document driver : " + driver.document);
    }
}

