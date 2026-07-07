
class WashingMachine extends Appliance {
    
    public WashingMachine(String brand) {
        super(brand);
    }
    
    @Override
    public void operate() {
        System.out.println("Washing clothes...");
    }
}

class Refrigerator extends Appliance {
    
    public Refrigerator(String brand) {
        super(brand);
    }
    
    @Override
    public void operate() {
        System.out.println("Store food & beverages...");
    }
}

class Microwave extends Appliance {
    
    public Microwave(String brand) {
        super(brand);
    }
    
    @Override
    public void operate() {
        System.out.println("Heating food...");
    }
}

class AirConditioner extends Appliance {
    
    public AirConditioner(String brand) {
        super(brand);
    }
    
    @Override
    public void operate() {
        System.out.println("Cooling the room...");
    }
}

public class Main {

    public static void main(String[] args) {
        
        // First appliance: Washing Machine (LG)
        Appliance washingMachine = new WashingMachine("LG");
        washingMachine.displayBrand();
        washingMachine.turnOn();
        washingMachine.operate();
        washingMachine.turnOff();
        
        System.out.println(); // Empty line for spacing
        
        // Second appliance: Refrigerator (Panasonic)
        Appliance refrigerator = new Refrigerator("Panasonic");
        refrigerator.displayBrand();
        refrigerator.turnOn();
        refrigerator.operate();
        refrigerator.turnOff();
    }
}
