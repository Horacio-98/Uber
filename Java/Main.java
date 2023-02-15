package CursoPOO.Java;

import javax.smartcardio.Card;

class Main {

    public static void main(String[] args) {

        car car_1 = new car("AMQ123", new account("Horacio GA","123")); 
        car_1.printDataCar();


    }
}


