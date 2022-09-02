# Function for calculating the count of usage batteries
def count_batteries_by_usage(cycles):
  # creating dictionary and initiolized category counting variable to zero 
  dic = {"lowCount": 0,
    "mediumCount": 0,
    "highCount": 0}
    
  # Traversing each element in array 
  for i in cycles:
    if i < 400 and i > 0:
      dic["lowCount"] += 1
    elif i >= 400 and i <= 919:
      dic["mediumCount"] += 1
    elif i >= 920:
      dic["highCount"] += 1
    else:
      pass
  
  return dic


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([-100, 100, 300, 400, 500, 600, 900, 919, 920, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 5)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
