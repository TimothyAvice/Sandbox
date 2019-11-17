package Math;

import javax.swing.*;

public class PrimeDetector {

    private PrimeDetector(double number){
        boolean prime = true;
        for(int i = 2; i < (number/2 + 1); i ++){
            if(number % i == 0){
                prime = false;
                break;
            }
        }
        if(prime)
            JOptionPane.showMessageDialog(null, String.format("%.0f is a prime", number));
        else
            JOptionPane.showMessageDialog(null, String.format("%.0f is not a prime", number));
    }

    public static void main(String[] args) {
        double number = -1;
        number = getNumber(number);
        while(number != 0) {
            number = getNumber(number);
        }
        JOptionPane.showMessageDialog(null, "Closing");
    }

    private static double getNumber(double number) {
        String input;
        input = JOptionPane.showInputDialog(null, "Enter number:");
        try {
            number = Double.parseDouble(input);
        } catch (Exception ignored){
            JOptionPane.showMessageDialog(null, "Input Error");
            System.exit(0);
        }
        if(number != 0) {
            new PrimeDetector(number);
        }
        return number;
    }
}
