import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class HotelClient {
    private HotelServiceInterface server;
    private Scanner scanner;

    public HotelClient() {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            server = (HotelServiceInterface) registry.lookup("HotelServer");
            scanner = new Scanner(System.in);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void displayMenu() {
        System.out.println("Welcome to Hotel Booking System");
        System.out.println("1. Book a Room");
        System.out.println("2. Cancel Booking");
        System.out.println("3. Exit");
        System.out.print("Enter your choice: ");
    }

    public void bookRoom() {
        System.out.print("Enter guest name: ");
        String guestName = scanner.nextLine();
        System.out.print("Enter room number: ");
        int roomNumber = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        try {
            if (server.bookRoom(guestName, roomNumber)) {
                System.out.println("Room booked successfully for " + guestName);
            } else {
                System.out.println("Room is already booked for " + guestName);
            }
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }

    public void cancelBooking() {
        System.out.print("Enter guest name to cancel booking: ");
        String guestName = scanner.nextLine();
        try {
            if (server.cancelBooking(guestName)) {
                System.out.println("Booking canceled successfully for " + guestName);
            } else {
                System.out.println("No booking found for " + guestName);
            }
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }

    public void start() {
        boolean running = true;
        while (running) {
            displayMenu();
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            switch (choice) {
                case 1:
                    bookRoom();
                    break;
                case 2:
                    cancelBooking();
                    break;
                case 3:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice. Please enter again.");
            }
        }
        System.out.println("Exiting Hotel Booking System.");
        scanner.close();
    }

    public static void main(String[] args) {
        HotelClient client = new HotelClient();
        client.start();
    }
}
