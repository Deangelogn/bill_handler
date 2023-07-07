import csv


def load_csv(filename : str) -> list:
  table = []
  with open(filename, 'r') as content:
    reader = csv.reader(content)
    for row in reader:
      table.append(row)
  return table


def write_csv(filename, data):
  with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


def count_votes_by_legislator_id(votes_results: list) -> dict:
  legislator_vote_counter = {}
  for row in votes_results[1:]:
    _, legislator_id, _, vote_type = row
    if legislator_id not in legislator_vote_counter:
      legislator_vote_counter[legislator_id] = {'1': 0, '2': 0}

    legislator_vote_counter[legislator_id][vote_type] += 1

  return legislator_vote_counter


def get_legislators_statistcis(vote_counter: dict, legislators: list) -> list:
  legislators_support_oppose_count = [['id', 'name', 'num_supported_bills', 'num_opposed_bills']]

  for row in legislators[1:]:
    legislator_id, legislators_name = row
    
    if legislator_id not in vote_counter:
      vote_counter[legislator_id] = {'1': 0, '2': 0}
      
    legislator_votes = vote_counter[legislator_id]
    legislators_support_oppose_count.append([int(legislator_id), legislators_name, 
                                             int(legislator_votes['1']), int(legislator_votes['2']) 
                                             ])

  return legislators_support_oppose_count


def get_legislators_support_oppose_count(votes_results: list, legislators: list) -> dict:
  votes_counter = count_votes_by_legislator_id(votes_results)
  data = get_legislators_statistcis(votes_counter, legislators)
  return data


def get_bills_data(bills: list) -> dict:
  bills_data = {}
  for row in bills[1:]:
    bill_id, title, primary_sponsor = row
    bills_data[bill_id] = {'title': title, 'primary_sponsor': primary_sponsor}

  return bills_data  

def get_votes_data(votes: list) -> dict:
  votes_data = {}
  for row in votes[1:]:
    vote_id, bull_id = row
    votes_data[vote_id] = bull_id
    
  return votes_data

def get_legislators_data(legislators: list) -> dict:
  legislators_data = {}

  for row in legislators[1:]:
    legislator_id, name = row
    legislators_data[legislator_id] = name
  
  return legislators_data


def count_votes_by_bill(bills: list, votes: list, votes_results: list) -> dict:
  bill_votes_counter = {}

  for row in bills[1:]:
    bill_id, _, _ = row

    if bill_id not in bill_votes_counter:
      bill_votes_counter[bill_id] = {'1': 0, '2': 0}

  votes_data = get_votes_data(votes)

  for row in votes_results[1:]:
    _, _, vote_id, vote_type = row
    bill_votes_counter[votes_data[vote_id]][vote_type] += 1

  return bill_votes_counter


def get_bill_votes_info(votes_counter: dict, bills: list, legislators: list) -> list:
  data = [['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor']]
  
  legislators_data = get_legislators_data(legislators)
  for row in bills[1:]:
    bill_id, title, primary_sponser_id = row
    
    if primary_sponser_id not in legislators_data:
      primary_sponser_name = "Unknown"
    else:
        primary_sponser_name = legislators_data[primary_sponser_id]

    data_row = [bill_id, title, votes_counter[bill_id]['1'], votes_counter[bill_id]['2'], primary_sponser_name]
    data.append(data_row)

  return data 


def get_bills_support_oppose_count(bills: list, votes: list, votes_results: list, legislators: list):
  bill_votes_counter =  count_votes_by_bill(bills, votes, votes_results)
  data = get_bill_votes_info(bill_votes_counter, bills, legislators)
  return data
