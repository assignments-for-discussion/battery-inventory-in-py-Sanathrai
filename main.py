
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  string count=counts
  if count>930:
    print("High")
    assert(counts["highCount"] == 1)
  elif count<310:
    print("Low")
    assert(counts["lowCount"] == 2)
  elif count<310 and count>929:
    print("medium")
    assert(counts["mediumCount"] == 3)
  
  
  
  
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
