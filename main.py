import sys
import random
import asyncio

def main(inputMessage):
  if len(inputMessage) >= 5:
    print(get_message(inputMessage))
  elif inputMessage.startswith("와 랜덤 "):
    print(messageRandomNumber(inputMessage))
  elif inputMessage == "와 니가":
    print(messageYour(inputMessage))

def get_message(strMessage):
  return strMessage.lower()

def messageRandomNumber(inputMessage):
  try:
    number = int(inputMessage.split()[2])
    return random.randint(1, number)
  except (IndexError, ValueError):
    return "올바르지 않은 입력이에요. '와 랜덤 [숫자]' 형식으로 입력해주세요."
  
def messageYour():
  return random.choice(
    [
      "https://youtu.be/SPddvDupQCM?si=lWzujNG5qSbxRO0u",
      "뭘 할 수 있는데"
    ]
  )

if __name__ == "__main__":
  main(sys.argv[1])
