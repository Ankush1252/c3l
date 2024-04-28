package org.example;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            // Get a reference to the remote object from the registry
            Registry registry = LocateRegistry.getRegistry("localhost"); // Assuming server is running on localhost
            StringConcatenator concatenator = (StringConcatenator) registry.lookup("StringConcatenator");

            // Get input strings from the user
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the first string: ");
            String s1 = scanner.nextLine();
            System.out.print("Enter the second string: ");
            String s2 = scanner.nextLine();
            scanner.close();

            // Invoke the remote method
            String result = concatenator.concatenateStrings(s1, s2);

            // Print the result
            System.out.println("Concatenated string: " + result);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}

