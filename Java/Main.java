package CursoPOO.Java; 

class Main {

    public static void main(String[] args) {

        car car_1 = new car("AMQ123", new account("Horacio GA","123")); 
        car_1.printDataCar();

        System.out.println("\n");

        car car_2 = new car("127ZFY", new account("Beatriz GA", "234"));
        car_2.printDataCar();


    }
}


