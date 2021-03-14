#! /usr/bin/python3
from sys import argv, stdin;
import argparse;

if __name__ == "__main__":
  print("NOTE: I hope you've piped-in data, else this script will hang");

  unique_ssh_entries = set();

  for line in stdin:
    if "ssh" in line:
      parts = line.split();
      command_parts = parts[1:];
      if command_parts[0] == "ssh" and len(command_parts) > 1:
        unique_ssh_entries.add(" ".join(command_parts));

  second_filter = set();

  for ssh_entry in unique_ssh_entries:
    command_args = ssh_entry.split()[1:];
    for arg in command_args:
      if "@" in arg:
        second_filter.add(arg);

  for access in second_filter:
    print(access);

  pass;