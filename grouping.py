def main():
    alpha = Group('alpha')
    bravo = Group('bravo')
    members = []
    matchNum = 0
    while True:
        num = input('\n数字を選んでね\n'\
        '1. 人の追加\n'\
        '2. 後衛の人を選択\n'\
        '3. チーム分け\n'\
        '4. 勝敗を記録する\n'\
        '5. 終了\n'\
        )
        if num == '5':
            break
        elif num == '1':
            if len(members) < 8:
                addMember(members)
                print('現在のメンバー')
                for i, m in enumerate(members):
                    print(f'{i + 1}. {m.name}')
            else:
                print('\n8人までだよ！\n')
        elif num == '2':
            setLongRange(members)
        elif num == '3':
            if len(members) < 8:
                print('まだ8人になってないよ！')
            else:
                grouping(members, alpha, bravo)
        elif num == '4':
            if len(members) < 8:
                print('まだ8人になってないよ！')
            else:
                countWin(members, alpha, bravo, matchNum)

def addMember(members):
    name = input('\n名前を入れてね！\n')
    members.append(Member(name))

def setLongRange(members):
    name = input('\n後衛の人の名前を入れてね！\n')
    nameInMembers = False
    for m in members:
        if m.name == name:
            m.havelongRangeWeapon()
            nameInMembers = True
            print(f'\n{name}さんは後衛です！\n')
    if not nameInMembers:
        print(f'\n{name}さんはいませんでした...\n')


def grouping(members, alpha, bravo):
    alpha.dissolution()
    bravo.dissolution()
    sortedByRate = sorted(members, key=lambda m : m.rate)
    for i in range(2):
        alpha.groupingTopRate(sortedByRate)
        alpha.groupingUnderRate(sortedByRate)
        bravo.groupingTopRate(sortedByRate)
        bravo.groupingUnderRate(sortedByRate)
    alpha.printMembers()
    bravo.printMembers()

def countWin(members, alpha, bravo, matchNum):
    wonTeam = input('\nどちらのチームが勝ちましたか？\n'\
    '1. アルファ\n'\
    '2. ブラボー\n'\
    )
    if wonTeam == '1':
        print('アルファが勝ちました！')
        alpha.win()
        matchNum += 1
    elif wonTeam == '2':
        print('ブラボーが勝ちました！')
        bravo.win()
        matchNum += 1
    else:
        print('\n数字を入力してください！')
        return
    for m in members:
        m.calcRate(matchNum)

class Member:

    def __init__(self, name):
        self.name = name
        self.winNum = 0
        self.rate = 0
        self.isLongRange = False
        self.isGrouped = False
    
    def havelongRangeWeapon(self):
        self.isLongRange = True

    def win(self):
        self.winNum += 1

    def calcRate(self, matchNum):
        self.rate = int(self.winNum / matchNum)
    
    def grouped(self):
        self.isGrouped = True

    def isNotGrouped(self):
        self.isGrouped = False


class Group:

    def __init__(self, name):
        self.groupName = name
        self.grooupedMembers = []
        self.hasLongRangeMember = False

    def printMembers(self):
        print(f'\n{self.groupName}:')
        for g in self.grooupedMembers:
            print(g.name)

    def win(self):
        for g in self.grooupedMembers:
            g.win()

    def dissolution(self):
        self.hasLongRangeMember = False
        for g in self.grooupedMembers:
            g.isNotGrouped()
        self.grooupedMembers = []

    def addGroup(self, member):
        self.grooupedMembers.append(member)
        if member.isLongRange:
            self.hasLongRangeMember = True

    def groupingConcideredRange(self, member):
        if not self.hasLongRangeMember:
            self.addGroup(member)
            member.grouped()
            return True
        elif not member.isLongRange:
            self.addGroup(member)
            member.grouped()
            return True
        else:
            return False

    def groupingTopRate(self, members):
        for i in range(len(members)):
            if not members[i].isGrouped:
                if self.groupingConcideredRange(members[i]):
                    break

    def groupingUnderRate(self, members):
        for i in range(len(members))[::-1]:
            if not members[i].isGrouped:
                if self.groupingConcideredRange(members[i]):
                    break


if __name__ == "__main__":
    main()