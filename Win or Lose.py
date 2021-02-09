''' 
A new fighting game has become popular. There is n number of villains in it, each having some strength. There are n players in the game with each having some energy. The energy is used to kill the villains. A villain can be killed only if the energy of the player is greater than the strength of the villain. 

Maxi is playing the game and at a particular time wants to know if it is possible for him to win the game or not with the given set of energies and strengths of players and villains. Maxi wins the game if his players can kill all the villains with the allotted energy.

Input Format:
The first line of input consists of a number of test cases, T.
The first line of each test case consists of a number of villains and player, N.
The second line of each test case consists of the N space-separated by strengths of Villains.
The third line of each test case consists of N space-separated by the energy of players.
'''

def main():

    t=int(input())
    count=0

    for _ in range(t):
        n = int(input())
        villains = list(map(int, input().strip().split()))      
        players = list(map(int, input().strip().split()))
        villains.sort(reverse=True)
        players.sort(reverse=True)
        
        temp=0
        for i in range(n):
            for j in range(temp, n):
                if players[i] > villains[j]:
                    temp = j+1
                    count += 1
                    break
    
        if (count == n):
            print('WIN')
        else:
            print('LOSE')

        count=0

main()
