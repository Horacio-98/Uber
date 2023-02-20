public class user extends account {

    public user(String name, String document, String email, String password){
        super(name, document, email, password); 
    }

    public void printDataUser(){
        return super.name; 
    }

    
}
