//class Number_Counting extends Thread{
//    public void run(){
//        int i = 0;
//        while (i <= 5){
//            System.out.println(++i);
//            Thread.sleep(5000);
//        }
//    }
//}
//
//class Message implements Runnable{
//    public void run(){
//
//    }
//}
//public class Thread_Qn {
//    public static void main(String [] args){
//        Thread number_counting = new Number_Counting();
//        Runnable msg = new Message();
//
//
//        number_counting.start();
//    }
//}

/*
-> You can see my attempt to write the code which was all erroneous(means not complete)
-> Check the below implementation which makes use of:-
    -> Thread extend
    -> Runnable
    -> setPriority()
    -> join
    -> sleep
    -> wait
    -> notify
 */

// Note:-
/*
-> When the sleep counter < sleep displayer:-
    -> due to exhausted notify() signals from counter and incomplete loop of the displayer
        -> thread of dispayer never completes and hence never joins the main thread and hence the main thread
        never completes as well.
-> This is fixed by adding another boolean vaiable that will keep with the status of whether the counter is finised
or not.
 */

class Shared_resources{
    private String msg;
    private boolean updated = false;
    private boolean isDone = false;

    public synchronized void set_message(String msg){
        this.msg = msg;
        this.updated = true;
        notify();
    }

    public synchronized void setDone(){
        this.isDone = true;
        notify();
    }
    public synchronized String get_message(){
        while (!updated && !isDone){
            try{
                wait();
            }
            catch(InterruptedException e){
                System.out.println("Message_Printer interrupted while waiting");
            }
        }

        if (isDone && !updated){
            return null;
        }
        this.updated = false;
        return this.msg;
    }
}

class Counter extends Thread{
    private Shared_resources resource;

    public Counter(Shared_resources res){
        this.resource = res;
    }

    public void run(){
        int i = 0;
        while (i < 5){
            System.out.println("Current Number: " + ++i);
            resource.set_message("Current cnt: " +  i);

            try {
                Thread.sleep(2000);
            }
            catch(InterruptedException e){
                System.out.println("Counter Interrupted");
            }
        }
        resource.setDone();
    }
}

class Display_message implements Runnable{
    Shared_resources resource;

    public Display_message(Shared_resources res){
        this.resource = res;
    }

    public void run(){
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

public class Thread_Qn{
    public static void main(String [] args){
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
