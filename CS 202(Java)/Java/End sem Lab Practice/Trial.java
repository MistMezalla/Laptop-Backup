class Shared_resources {
    private String msg;
    private boolean updated = false;
    private boolean isDone = false;

    public synchronized void set_message(String msg) {
        this.msg = msg;
        this.updated = true;
        notify();  // Notify any waiting thread
    }

    public synchronized void setDone() {
        this.isDone = true;
        notify();  // Notify any waiting thread
    }

    public synchronized String get_message() {
        while (!updated && !isDone) {
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println("Message_Printer interrupted while waiting");
            }
        }

        if (isDone && !updated) {
            return null;  // No more messages to process, return null
        }

        this.updated = false;
        return this.msg;
    }
}

class Counter extends Thread {
    private Shared_resources resource;

    public Counter(Shared_resources res) {
        this.resource = res;
    }

    public void run() {
        int i = 0;
        while (i < 5) {
            System.out.println("Current Number: " + ++i);
            resource.set_message("Current cnt: " + i);

            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                System.out.println("Counter Interrupted");
            }
        }
        resource.setDone();  // Mark the counter as done
    }
}

class Display_message implements Runnable {
    Shared_resources resource;

    public Display_message(Shared_resources res) {
        this.resource = res;
    }

    public void run() {
        int i = 0;
        while (i < 5) {
            String message = resource.get_message();
            if (message == null) {
                break;  // Exit if there are no more messages
            }
            System.out.println("Received message: " + message);

            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                System.out.println("Display_message Interrupted");
            }
            i++;
        }
    }
}

public class Trial {
    public static void main(String[] args) {
        Shared_resources resource = new Shared_resources();

        Thread counter = new Counter(resource);
        Thread message_displaye = new Thread(new Display_message(resource));

        message_displaye.setPriority(Thread.MIN_PRIORITY);
        counter.start();
        message_displaye.start();

        try {
            counter.join();
            message_displaye.join();
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted");
        }

        System.out.println("All threads have finished execution.");
    }
}
