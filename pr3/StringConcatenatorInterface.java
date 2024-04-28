package org.example;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface StringConcatenator extends Remote {
    String concatenateStrings(String s1, String s2) throws RemoteException;
}

