package CursoPOO.Java;

public class car {
    private Integer id; 
    private String license; 
    private account driver; 
    private Integer passenger; 

    public car(String license, account driver ){
        this.license = license; 
        this.driver = driver; 
    }

    void printDataCar() {
        System.out.println("License : " + license);
        System.out.println("Name driver : " + driver.name);
        System.out.println("Document driver : " + driver.document);
    }

    public Integer getId() {
        return id;
    }

    public String getLicense() {
        return license;
    }

    public account getDriver() {
        return driver;
    }

    public Integer getPassenger() {
        return passenger;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public void setDriver(account driver) {
        this.driver = driver;
    }

    public void setPassenger(Integer passenger) {
        this.passenger = passenger;
    }

    
}

