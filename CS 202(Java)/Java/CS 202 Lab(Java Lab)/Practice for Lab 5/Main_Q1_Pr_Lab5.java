import java.util.*;

public class Main_Q1_Pr_Lab5 {
    public static void main(String [] args)
    {
        SportsPerson SP = new SportsPerson();
        SP.inputSportsPerson();
        SP.displaySportsPerson();

        Footballer FB = new Footballer();
        FB.inputFootballer();
        FB.displayFootballer();

        Batsman b = new Batsman();
        b.inputBatsman();
        b.displayBatsman();

        Bowler bw = new Bowler();
        bw.inputBowler();
        bw.displayBowler();
        
    }
}

class SportsPerson{
    protected String name;
    protected String address;

    void displaySportsPerson(){
        System.out.println("Name: " + name + "\nAddress: " + address);
    }

    void inputSportsPerson(){
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();
    }
}

class Cricketer extends SportsPerson{
    static String type = "Cricketer";
    protected int matchesPlayed;
    protected int catches;

    void displayCricketer(){
        System.out.println("Name: " + name + "\tAddress: " + address);
        System.out.println("Type: " + type + "\tMatches Played: " + matchesPlayed + "\tCatches: " + catches);
    }

    void inputCricketer() {
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();

        matchesPlayed = sc.nextInt();
        catches = sc.nextInt();
    }
}

class Footballer extends SportsPerson{
    static String type = "Footballer";
    protected int matchesPlayed;
    protected int goals;
    protected int tackles;

    void displayFootballer(){
        System.out.println("Name: " + name + "\tAddress: " + address);
        System.out.println("Type: " + type + "\tMatches Played: " + matchesPlayed + "\tGoals: " + goals + "\tTackles: " + tackles);
    }

    void inputFootballer() {
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();

        matchesPlayed = sc.nextInt();
        goals = sc.nextInt();
        tackles = sc.nextInt();
    }
}

class Batsman extends Cricketer{
    protected int runs;
    protected double highest;

    void displayBatsman(){
        System.out.println("Name: " + name + "\tAddress: " + address);
        System.out.println("Type: " + type + "\tMatches Played: " + matchesPlayed + "\tCatches: " + catches);
        System.out.println("Runs: " + runs + "\tHighest: " + highest);
    }

    void inputBatsman() {
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();

        matchesPlayed = sc.nextInt();
        catches = sc.nextInt();

        runs = sc.nextInt();
        highest = sc.nextDouble();
    }
}

class Bowler extends Cricketer{
    protected int wickets;
    protected double strikeRate;

    void displayBowler(){
        System.out.println("Name: " + name + "\tAddress: " + address);
        System.out.println("Type: " + type + "\tMatches Played: " + matchesPlayed + "\tCatches: " + catches);
        System.out.println("Wickets: " + wickets + "\tStrike Rate: " + strikeRate);
    }

    void inputBowler() {
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();

        matchesPlayed = sc.nextInt();
        catches = sc.nextInt();

        wickets = sc.nextInt();
        strikeRate = sc.nextDouble();
    }
}

class WicketKeeper extends Cricketer{
    protected int stumpings;

    void displayWK(){
        System.out.println("Name: " + name + "\tAddress: " + address);
        System.out.println("Type: " + type + "\tMatches Played: " + matchesPlayed + "\tCatches: " + catches);
        System.out.println("Stumpings: " + stumpings);
    }

    void inputWK() {
        Scanner sc = new Scanner(System.in);

        name = sc.nextLine();
        address = sc.nextLine();

        matchesPlayed = sc.nextInt();
        catches = sc.nextInt();

        stumpings = sc.nextInt();
    }
}

