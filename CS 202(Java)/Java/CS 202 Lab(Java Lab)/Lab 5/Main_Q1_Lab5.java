import java.util.*;

public class Main_Q1_Lab5{
	public static void main(String [] args)
	{
		int choice;	
		Scanner sc = new Scanner(System.in);
		do{	
			System.out.println("Enter the key number of the object to be created: ");
			System.out.println("1 = SportsPerson\n2 = Cricketer\n3 = Batsman\n4 = Bowler\n5 = WicketKeeper\n6 = Footballer\n7 = Striker\n8 = Defender\n9 = Goalkeeper\n0 = To exit the program");
			choice = sc.nextInt();

			switch(choice){
				case 1:
					SportsPerson SP = new SportsPerson();
					SP.inputSportsPerson();
					SP.displaySportsPerson();
					break;
				case 2:
					Cricketer Ckt = new Cricketer();
					Ckt.inputCricketer();
					Ckt.displayCricketer();
					break;
				case 3:
					Batsman Bt = new Batsman();
					Bt.inputBatsman();
					Bt.displayBatsman();
					break;
				case 4:
					Bowler Bwl = new Bowler();
					Bwl.inputBowler();
					Bwl.displayBowler();
					break;
				case 5:
					WicketKeeper Wk = new WicketKeeper();
					Wk.inputWK();
					Wk.displayWK();
					break;
				case 6:
					Footballer Fb = new Footballer();
					Fb.inputFootballer();
					Fb.displayFootballer();
					break;
				case 7:
					Striker St = new Striker();
					St.inputStriker();
					St.displayStriker();
					break;
				case 8:
					Defender Def = new Defender();
					Def.inputDefender();
					Def.displayDefender();
					break;
				case 9:	
					Goalkeeper Gk = new Goalkeeper();
					Gk.inputGK();
					Gk.displayGK();
					break;
				case 0:
					System.out.println("Exiting from the program !!!");
					break;
				default:
					System.out.println("Wrong Input: Enter integers from 0-9 !!");
					break;
				}
		}while(choice != 0);
	}					
}

class SportsPerson{
	protected String name;
	protected String address;

	void displaySportsPerson()
	{
		System.out.println("Name: " + name + "\nAddress: " + address + "\n");
	}

	void inputSportsPerson()
	{
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the name: ");
		name = sc.nextLine();
		System.out.println("Enter the address: ");
		address = sc.nextLine();
	}
}

class Cricketer extends SportsPerson{
	static String type = "Cricketer";
	protected int matchesPlayed;
	protected int catches;

	void displayCricketer()
	{
		displaySportsPerson();
		System.out.println("Type: " + type + "\nMatches Played: " + matchesPlayed + "\nCatches: " + catches + "\n");
	}

	void inputCricketer()
	{
		Scanner sc = new Scanner(System.in);
		inputSportsPerson();			

		System.out.println("Enter the number of matches played: ");
		matchesPlayed = sc.nextInt();
		System.out.println("Enter the number of catches taken: ");
		catches = sc.nextInt();
	}
}

class Footballer extends SportsPerson{
	static String type = "Footballer";
	protected int matchesPlayed;
	protected int goals;
	protected int tackles;

	void displayFootballer()
	{
		displaySportsPerson();
		System.out.println("Type: " + type + "\nMatches Played: " + matchesPlayed + "\nGoals: " + goals + "\nTackles: " + tackles + "\n");
	}

	void inputFootballer()
	{
		Scanner sc = new Scanner(System.in);
		inputSportsPerson();	
	
		System.out.println("Enter the number of matches played: ");
		matchesPlayed = sc.nextInt();
		System.out.println("Enter the number of goals scored: ");
		goals = sc.nextInt();
		System.out.println("Enter the number tackles completed: ");
		tackles = sc.nextInt();
	}
}

class Batsman extends Cricketer{
	protected int runs;
	protected double highest;

	void displayBatsman()
	{
		displayCricketer();
		System.out.println("Runs: " + runs + "	\nHighest: " + highest + "\n");
	}

	void inputBatsman()
	{
		Scanner sc = new Scanner(System.in);

		inputCricketer();
		
		System.out.println("Enter the runs scored: ");
		runs = sc.nextInt();
		System.out.println("Enter the highest score: ");
		highest = sc.nextDouble();
	}
}

class Bowler extends Cricketer{
	protected int wickets;
	protected double strikeRate;

	void displayBowler()
	{
		displayCricketer();
		System.out.println("Wickets: " + wickets + "	\nBowling Strike Rate: " + strikeRate + "\n");
	}

	void inputBowler()
	{
		Scanner sc = new Scanner(System.in);
		inputCricketer();

		System.out.println("Enter the wickets taken: ");
		wickets = sc.nextInt();
		System.out.println("Enter the bowling strike rate: ");
		strikeRate = sc.nextDouble();
	}
}

class WicketKeeper extends Cricketer{
	protected int stumpings;

	void displayWK()
	{
		displayCricketer();
		System.out.println("Stumpings: " + stumpings + "\n");
	}

	void inputWK()
	{
		Scanner sc = new Scanner(System.in);
		inputSportsPerson();
		
		System.out.println("Enter the stumpings made: ");
		stumpings = sc.nextInt();
	}
}

class Striker extends Footballer{
	protected int goalsScored;
	protected int assist;
	
	void displayStriker()
	{
		displayFootballer();
		System.out.println("Goals Scored: " + goalsScored + "Assist: " + assist + "\n");
	}

	void inputStriker()
	{
		Scanner sc = new Scanner(System.in);
		inputFootballer();
		System.out.println("Enter number of Goals scored: ");
		goalsScored = sc.nextInt();
		System.out.println("Enter the number of assists made: ");
		assist = sc.nextInt();
	}
}

class Defender extends Footballer{
	protected int tackles;
	protected int headers;
	
	void displayDefender()
	{
		displayFootballer();
		System.out.println("Tackles: " + tackles + "Headers: " + headers + "\n");
	}

	void inputDefender()
	{
		Scanner sc = new Scanner(System.in);
		inputFootballer();
		System.out.println("Enter number of tackles completed: ");
		this.tackles = sc.nextInt();
		System.out.println("Enter the number of headers: ");
		headers = sc.nextInt();
	}
}

class Goalkeeper extends Footballer{
	protected int saves;
	protected int cleanSheets;
	
	void displayGK()
	{
		displayFootballer();
		System.out.println("Saves made: " + saves + "Clean Sheets kept: " + cleanSheets + "\n");
	}

	void inputGK()
	{
		Scanner sc = new Scanner(System.in);
		inputFootballer();
		System.out.println("Enter number of saves made: ");
		saves = sc.nextInt();
		System.out.println("Enter the number of clean sheets kept: ");
		cleanSheets = sc.nextInt();
	}
}
