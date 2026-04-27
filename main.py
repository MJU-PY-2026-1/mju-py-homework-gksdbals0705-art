# 파일이름 : 파이썬 과제 코드
# 작 성 자 : 한유민
print('어서오세요 다이어트 용사님들! 이제 당신들은 하나의 팀이 되어 목표를 향해 달려나갈 것입니다!')
print("우선, 앞으로 사용하게 될 '파티 이름', '목표하는 다이어트 진행 주차', 파티원의 공통 목표인 '목표 BMI'를 입력해주세요!")
print()

party_name = input('당신의 파티 이름을 정해주세요 :')
member_count = int(input(f'{party_name}파티의 총 인원수는 몇 명인가요? :'))
weeks = int(input(f'{party_name}파티가 목표하는 다이어트 진행주차를 알려주세요! :'))
target_bmi = float(input(f'{party_name}파티의 목표 bmi는 몇인가요? :'))
total_party_weight = 0.0
max_weight = 0.0

heights = []
weights = []

for i in range(member_count):
  hegiht = float(input(f'{member_count+1}번 파티원의 키를 m 단위로 입력하세요(예: 1.75):'))
  weight = float(input(f'{member_count+1}번 파티원의 체중을 kg 단위로 입력하세요(예: 65.3):'))
  heights.append(height)
  weights.append(weight)
