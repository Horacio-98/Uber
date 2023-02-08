package CursoPOO.Java;
class Main {

    public static void main(String[] args) {
        System.out.println("Hola mundo");

        car car = new car("AMQ123", new account("Horacio GA","123")); 
        car.passenger = 4; 
        car.printDataCar();

    }
}


