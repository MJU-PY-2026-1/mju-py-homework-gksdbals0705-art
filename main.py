# 파일이름 : 파이썬 과제 코드
# 작 성 자 : 한유민

import random
party_name = ''
member_count = 0
weeks = 0
target_bmi = 0.0

heights = []
weights = []
bmis = []
total_party_weight = 0.0
max_weight = 0.0

def show_menu():
  print()
  print('1. 파티 기본 정보 입력')
  print('2. 파티원 키, 몸무게 입력')
  print('3. 파티 상태 조회')
  print('4. 파티원 BMI 분석')
  print('5. 이번주 퀘스트 확인')
  print('6. 종료')
  
def setup_party():
  global party_name,member_count,weeks,target_bmi
  
  print('어서오세요 다어어트 용사님들! 이제 당신들은 하나의 팀이 되어 목표를 향해 달려나갈 것입니다!')
  print("우선, 앞으로 사용하게 될 '파티 이름', '목표하는 다이어트 진행 주차', 파티원의 공통 목표인 '목표 BMI'를 입력해주세요!\n")
  
  party_name = input('당신의 파티 이름을 정해주세요 :')
  member_count = int(input(f'{party_name}파티의 총 인원수는 몇 명인가요?(숫자만 적어주세요!) :'))
  weeks = int(input(f'{party_name}파티가 목표하는 다이어트 진행주차를 알려주세요!(숫자만 적어주세요!) :'))
  target_bmi = float(input(f'{party_name}파티의 목표 bmi는 몇인가요? :'))


def calculate_bmi(weight, height):
  return weight/(height*height)

def input_members():
  global total_party_weight, max_weight

  if member_count==0:
    print('먼저 1번 메뉴에서 파티 기본 정보를 입력해 주세요.')
    return
    
  for i in range(member_count):
    print(f'{i+1}번 파티원 정보 입력')
    height = float(input(f'{i+1}번 파티원의 키를 m 단위로 입력하세요(예: 1.75):'))
    weight = float(input(f'{i+1}번 파티원의 체중을 kg 단위로 입력하세요(예: 65.3):'))
    
    heights.append(height)
    weights.append(weight)
    
    bmi = calculate_bmi(weight,height)
    bmis.append(bmi)

    total_party_weight += weight   
  max_weight = max(weights)
  print("모든 파티원의 정보 입력이 완료되었습니다.")

def view_status():
  if not weights:
    print('아직 입력된 파티원이 없습니다. 먼저 2번 메뉴를 통해 입력을 해주세요.')
    return
    
  party_size = len(weights)
  bmis_sort=sorted(bmis)

  print(f'현재 파티의 BMI 랭킹은 다음과 같습니다. \n{bmis_sort}')
  print(f'{party_name}파티의 파티원은 {party_size}명으로, 총 몸무게 합은 {total_party_weight}입니다.')

def analyze_members(target):
  if not weights:
    print('아직 입력된 파티원이 없습니다. 먼저 2번 메뉴를 통해 입력을 해주세요.')
    return

  print('앗 당신의 BMI 등급이 나왔어요!')
  print('특정 조건을 만족하는 사람에게는 히든 문구가 발생하니 기대하세요~!\n')

  for i in range(member_count):
    current_h = heights[i]
    current_w = weights[i]
    current_bmi = bmis[i]

    print(f'{i+1}번 파티원의 분석 결과 -> 키 : {current_h}m, 체중 : {current_w}kg, BMI : {current_bmi}')
    
    if current_bmi<16.0:
      print('당신은 심각한 저체중입니다. 이번 주차 다이어트 평가에서 제외됩니다. 다이어트가 아닌 증량을 목표로 잡으세요!')
      continue
    elif current_bmi < 18.5:
      grade = "B등급(저체중)"
    elif current_bmi < 23.0:
      grade = "S등급(정상)"
    elif current_bmi < 25.0:
      grade = "A등급(과체중)"
    else:
      grade = "F등급(비만)"
    print(f'당신의 등급은 {grade}입니다.')
    
    if current_bmi <= target and grade == "S등급(정상)":
      print("축하합니다! 당신은 [전설의 다이어터] 칭호를 획득했습니다!")
    if grade == "F등급(비만)":
      if current_w == max_weight:
        print("경고! 당신은 [야식의 노예] 칭호를 획득했습니다. 파티 꼴지입니다. 분발하세요!")

def show_weekly_quest():
  quest = random.choice(['배달음식 금지!', '8시 이후로는 물만 마시기!', '하루에 유산소 운동 30분하기!', '패스트푸드 금지!', '3번 헬스장 가기!', '하루에 스쿼트 50개하기!'])
  print(f'\n앞으로 {weeks}주 동안 {party_name} 파티의 건투를 빕니다!')
  print(f'참고로 이번주 파티원들이 지켜야할 퀘스트는 {quest}입니다. 여러분의 양심을 믿겠습니다!')

while True:
  show_menu()
  menu = input('메뉴 번호를 선택해주세요:')

  if menu == '1':
    setup_party()
  elif menu == '2':
    input_members()
  elif menu == '3':
    view_status()
  elif menu == '4':
    analyze_members(target_bmi)
  elif menu == '5':
    show_weekly_quest()
  elif menu == '6':
    print()
    print('다이어트 파티 프로그램을 종료합니다.')
    print('모든 다이어트 용사님들의 목표 달성을 응원합니다!')
    break
  else:
   print()
   print('잘못된 메뉴 번호입니다. 1,2,3,4,5,6 중에서 선택해 주세요.')
  
  



