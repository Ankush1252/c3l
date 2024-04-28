package org.example;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) {
        try {
            // Create an instance of the implementation class
            StringConcatenatorImpl concatenator = new StringConcatenatorImpl();

            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.createRegistry(1099); // Default RMI registry port
            registry.rebind("StringConcatenator", concatenator);

            System.out.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}

