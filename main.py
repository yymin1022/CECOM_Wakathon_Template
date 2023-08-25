import sys
import random
import asyncio

def main(inputMessage):
  if inputMessage.startswith("와 랜덤 "):
    print(messageRandomNumber(inputMessage))
  elif inputMessage == "와 니가":
    print(messageYour(inputMessage))
  elif inputMessage.startswith("와 예약 "):
    print(asyncio.run(messageReservation(inputMessage)))
  elif len(inputMessage) >= 5:
    print(get_message(inputMessage))

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

async def messageReservation(inputMessage):
  try:
    parts = inputMessage.split()
    message = parts[2]
    delay = int(parts[3])
    repetitions = int(parts[4])

    if delay > 10 or repetitions > 10:
      return "시간과 반복 값은 10 이하의 값만 사용할 수 있어요."

    await asyncio.sleep(delay * 60)

    return (message + '\n') * (repetitions - 1) + message
  except (IndexError, ValueError):
    return "올바르지 않은 입력이에요. '와 예약 [메시지] [분] [반복횟수]' 형식으로 입력해주세요."

if __name__ == "__main__":
  main(sys.argv[1])
