package org.example;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringConcatenatorImpl extends UnicastRemoteObject implements StringConcatenator {
    protected StringConcatenatorImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenateStrings(String s1, String s2) throws RemoteException {
        return s1 + s2;
    }
}
