# p.78

names = ['kim', 'park', 'jim', 'im']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2
msg = 'you'
print(f"{names[0].title()},{msg}")
print(f"{names[1].title()},{msg}")
print(f"{names[2].title()},{msg}")
print(f"{names[3].title()},{msg}")

# 3-3
vehicle = ['car', 'bus', 'taxi', 'airplane']
print(f"{names[0]}는 {vehicle[0]}를 갖고싶습니다.")
print(f"{names[1]}는 {vehicle[1]}를 갖고싶습니다.")
print(f"{names[2]}는 {vehicle[2]}를 갖고싶습니다.")
print(f"{names[3]}는 {vehicle[3]}를 갖고싶습니다.")


# p.85-86

who = []
who.append('abii')
who.append('abEE')
who.append('abTT')
print(f"{who[0]}님, 저녁식사에 초대합니다.")
print(f"{who[1]}님, 저녁식사에 초대합니다.")
print(f"{who[2]}님, 저녁식사에 초대합니다.")

# 3-5

print(f"오지 못하는 사람 : {who[2]}")
who.pop()
who.append('new')
print(f"{who[0]}님, 저녁식사에 초대합니다.")
print(f"{who[1]}님, 저녁식사에 초대합니다.")
print(f"{who[2]}님, 저녁식사에 초대합니다.")

# 3-6

print(f"{who[0]}님, find more big table.")
print(f"{who[1]}님, find more big table.")
print(f"{who[2]}님, find more big table.")

who.insert(0, 'new2')
who.insert(2, 'new3')
who.append('new4')

print(f"{who[0]}님, 저녁식사에 초대합니다.")
print(f"{who[1]}님, 저녁식사에 초대합니다.")
print(f"{who[2]}님, 저녁식사에 초대합니다.")
print(f"{who[3]}님, 저녁식사에 초대합니다.")
print(f"{who[4]}님, 저녁식사에 초대합니다.")
print(f"{who[5]}님, 저녁식사에 초대합니다.")

# 3-7

print(f"{who[0]}님, 저녁식사에 2명만 초대합니다.")
print(f"{who[1]}님, 저녁식사에 2명만 초대합니다.")
print(f"{who[2]}님, 저녁식사에 2명만 초대합니다.")
print(f"{who[3]}님, 저녁식사에 2명만 초대합니다.")
print(f"{who[4]}님, 저녁식사에 2명만 초대합니다.")
print(f"{who[5]}님, 저녁식사에 2명만 초대합니다.")

print(f"{who[5]}님, 저녁식사에 초대를 취소합니다.")
who.pop()
print(f"{who[4]}님, 저녁식사에 초대를 취소합니다.")
who.pop()
print(f"{who[3]}님, 저녁식사에 초대를 취소합니다.")
who.pop()
print(f"{who[2]}님, 저녁식사에 초대를 취소합니다")
who.pop()

print(f"{who[0]}님, 저녁식사에 여전히 초대합니다.")
print(f"{who[1]}님, 저녁식사에 여전히 초대합니다.")

del who[0]
del who[0]
print(who)

# 3-8

where=[]
where.append('korea')
where.append('america')
where.append('singafal')
where.append('indonesia')
print(where)

print(sorted(where))
print(where)

where.reverse()
print(where)

where.reverse()
print(where)

where.sort()
print(where)

where.sort(reverse=True)
print(where)

# 3-9
print(f"{len(who)}명을 초대합니다.")
