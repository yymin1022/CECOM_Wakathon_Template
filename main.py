import sys
import random
import asyncio
import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

def main(inputMessage):
  if inputMessage.startswith("와 랜덤 "):
    print(messageRandomNumber(inputMessage))
  elif inputMessage == "와 니가":
    print(messageYour(inputMessage))
  elif inputMessage.startswith("와 예약 "):
    print(asyncio.run(messageReservation(inputMessage)))
  elif inputMessage.startswith("와 날씨 "):
    print(messageWeather(inputMessage))
  

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
  
def messageWeather(inputMessage):
  area = inputMessage.split()[1]

  webpage = req.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + urllib.parse.quote(area + ' 날씨'))

  soup = BeautifulSoup(webpage, 'html.parser')
  real_area = soup.select_one('h2.title').text.strip()
  weather = soup.select_one('p.summary').text.strip().replace(soup.select_one('p.summary span').text, '').replace('어제보다', '').strip()
  temp = soup.select_one('div.temperature_text').text.strip().replace(soup.select_one('div.temperature_text span').text, '')
  max_temp = soup.select_one("span.highest").get_text().replace("최고기온", "")
  min_temp = soup.select_one("span.lowest").get_text().replace("최저기온", "")
  body_temp = soup.select_one('dd.desc').text.strip()

  return '\n'.join(
    [
      "현재 " + real_area + "은(는) " + weather + "이며",
      "현재 온도는 " + temp + "이며 " + "체감 온도는 " + body_temp + "입니다.",
      "최고 온도는 " + max_temp + "이며 " + "최저 온도는 " + min_temp + "입니다."
    ]
    )
if __name__ == "__main__":
  main(sys.argv[1])
