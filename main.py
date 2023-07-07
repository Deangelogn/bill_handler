from challenge_packge.bills_handler import load_csv, write_csv
from challenge_packge.bills_handler import get_legislators_support_oppose_count, get_bills_support_oppose_count

def main():
  # Load table of bills
  bills = load_csv('bills.csv')

  # Load table of legislators
  legislators = load_csv('legislators.csv')

  # Load table of votes
  votes = load_csv('votes.csv')

  # Load table of vote results
  votes_results = load_csv('vote_results.csv')

  # Get legislators statistics 
  legislators_data = get_legislators_support_oppose_count(votes_results, legislators)

  # Save legislators statistics
  write_csv('legislators-support-oppose-count.csv', legislators_data)

  # Get bills statistics
  bills_data = get_bills_support_oppose_count(bills, votes, votes_results, legislators)

  # Save bills statistics
  write_csv('bills-support-oppose-count.csv', bills_data)


if __name__ == '__main__':
  main()