def count_batteries_by_usage(cycles):
  dic = {"lowCount": 0,
    "mediumCount": 0,
    "highCount": 0}
    
  for i in cycles:
    if i < 400:
      dic["lowCount"] += 1
    elif i >= 400 and i <= 919:
      dic["mediumCount"] += 1
    elif i >= 920:
      dic["highCount"] += 1
  return dic


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
