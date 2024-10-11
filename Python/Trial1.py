import csv
import random


# Player class to represent a football player
class Player:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.sold_price = None
        self.team = None


# Team class to represent a team participating in the auction
class Team:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.players = []

    def buy_player(self, player, price):
        if self.balance >= price:
            self.balance -= price
            self.players.append(player)
            print(f"{self.name} successfully bought {player.name} for {price}")
            return True
        else:
            print(f"{self.name} does not have enough balance to buy {player.name}")
            return False


# Auction class to handle the auction process
class Auction:
    def __init__(self):
        self.player_pool = []
        self.sold_players = []
        self.unsold_players = []
        self.teams = []

    # Load players from a CSV file
    def load_players_from_csv(self, file_name):
        try:
            with open(file_name, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    player = Player(row['name'], int(row['base_price']))
                    self.player_pool.append(player)
            print(f"Loaded {len(self.player_pool)} players from {file_name}")
        except FileNotFoundError:
            print("Error: CSV file not found.")

    # Add teams with initial balances
    def add_team(self, name, balance):
        team = Team(name, balance)
        self.teams.append(team)

    # Randomly draw a player from the pool
    def draw_random_player(self):
        if self.player_pool:
            player = random.choice(self.player_pool)
            self.player_pool.remove(player)
            return player
        else:
            print("No more players in the auction pool.")
            return None

    # Manually select a player from the pool
    def draw_player_manually(self, player_name):
        for player in self.player_pool:
            if player.name == player_name:
                self.player_pool.remove(player)
                return player
        print(f"No player named {player_name} in the auction pool.")
        return None

    # Run auction for a player with manual or random drawing
    def auction_player(self, player_name=None):
        if player_name:
            player = self.draw_player_manually(player_name)
        else:
            player = self.draw_random_player()

        if player:
            print(f"\nAuctioning {player.name}, starting at {player.base_price}")
            for team in self.teams:
                choice = input(f"Does {team.name} want to buy {player.name}? (yes/no): ")
                if choice.lower() == 'yes':
                    sold_price = int(input(f"Enter the final sold price for {player.name}: "))
                    if team.buy_player(player, sold_price):
                        player.sold_price = sold_price
                        player.team = team.name
                        self.sold_players.append(player)
                        return
            # If no team buys the player
            self.unsold_players.append(player)
            print(f"{player.name} remained unsold.\n")

    # Display sold players, with optional filters for team or sold price range
    def filter_sold_players(self, team_name=None, price_range=None):
        filtered_players = self.sold_players

        if team_name:
            filtered_players = [p for p in filtered_players if p.team == team_name]
        if price_range:
            min_price, max_price = price_range
            filtered_players = [p for p in filtered_players if min_price <= p.sold_price <= max_price]

        if filtered_players:
            print("\nFiltered Sold Players:")
            for player in filtered_players:
                print(f"{player.name} - Sold to {player.team} for {player.sold_price}")
        else:
            print("No players match the given filter criteria.")

    # Display unsold players
    def display_unsold_players(self):
        if not self.unsold_players:
            print("All players have been sold.")
        else:
            print("\nUnsold Players:")
            for player in self.unsold_players:
                print(player.name)

    # Save auction results to CSV
    def save_results_to_csv(self, sold_file="sold_players.csv", unsold_file="unsold_players.csv"):
        # Write sold players to CSV
        with open(sold_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Sold Price', 'Team'])
            for player in self.sold_players:
                writer.writerow([player.name, player.sold_price, player.team])

        # Write unsold players to CSV
        with open(unsold_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Base Price'])
            for player in self.unsold_players:
                writer.writerow([player.name, player.base_price])

        print(f"Auction results saved to {sold_file} and {unsold_file}")

    # Display team balances
    def display_team_balances(self):
        print("\nTeam Balances:")
        for team in self.teams:
            print(f"{team.name}: {team.balance}")


# Menu-driven interface
def main():
    auction = Auction()
    while True:
        print("\n--- Football Player Auction System ---")
        print("1. Load players from CSV")
        print("2. Add a team")
        print("3. Auction a player (randomly)")
        print("4. Auction a player (manually)")
        print("5. Filter sold players")
        print("6. Display unsold players")
        print("7. Save auction results to CSV")
        print("8. Display team balances")
        print("9. Exit")

        choice = input("Select an option (1-9): ")

        if choice == '1':
            filename = input("Enter CSV file name: ")
            auction.load_players_from_csv(filename)
        elif choice == '2':
            team_name = input("Enter team name: ")
            balance = int(input("Enter team balance: "))
            auction.add_team(team_name, balance)
        elif choice == '3':
            auction.auction_player()  # Random draw
        elif choice == '4':
            player_name = input("Enter the name of the player to auction: ")
            auction.auction_player(player_name)  # Manual draw
        elif choice == '5':
            team_name = input("Enter team name to filter (leave blank for all): ")
            price_range_input = input("Enter price range (min,max) or leave blank: ")
            price_range = None
            if price_range_input:
                min_price, max_price = map(int, price_range_input.split(','))
                price_range = (min_price, max_price)
            auction.filter_sold_players(team_name if team_name else None, price_range)
        elif choice == '6':
            auction.display_unsold_players()
        elif choice == '7':
            auction.save_results_to_csv()
        elif choice == '8':
            auction.display_team_balances()
        elif choice == '9':
            print("Exiting the auction system.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

