import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {
    private Map<String, Integer> bookings;

    protected HotelServer() throws RemoteException {
        super();
        bookings = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (!bookings.containsKey(guestName)) {
            bookings.put(guestName, roomNumber);
            System.out.println("Room booked successfully for " + guestName);
            return true;
        } else {
            System.out.println("Room is already booked for " + guestName);
            return false;
        }
    }

    @Override
    public synchronized boolean cancelBooking(String guestName) throws RemoteException {
        if (bookings.containsKey(guestName)) {
            bookings.remove(guestName);
            System.out.println("Booking canceled successfully for " + guestName);
            return true;
        } else {
            System.out.println("No booking found for " + guestName);
            return false;
        }
    }

    public static void main(String[] args) {
        try {
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            HotelServer obj = new HotelServer();
            java.rmi.Naming.rebind("HotelServer", obj);
            System.out.println("Hotel Server ready.");
        } catch (Exception e) {
            System.err.println("Hotel Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
