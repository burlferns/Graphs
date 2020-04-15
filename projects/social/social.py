import random
from util import Stack, Queue 

def fisher_yates_shuffle(itemList):
    for ii in range(0, len(itemList)):
        random_index = random.randint(ii, len(itemList) - 1)
        temp = itemList[ii]
        itemList[ii] = itemList[random_index]
        itemList[random_index] = temp

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        ###################################
        # Add users
        ###################################
        for i in range(1,(num_users+1)):
            self.add_user(f'person{i}')

        ###################################
        # Create friendships
        ###################################
        # all_bidirectional_edges is a list of all biidirectional edges. 
        # A bidirectional edge goes, for example, person1 to person2. 
        # Note if you already have a bi-di-edge from person1 one to
        # person2, then you don't need to make one from person2 to person1
        all_bidirectional_edges =  []  
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                all_bidirectional_edges.append((user_id, friend_id))

        # print(f'Before shuffle: {all_bidirectional_edges}')

        fisher_yates_shuffle(all_bidirectional_edges)

        # print(f'After shuffle: {all_bidirectional_edges}')

        ####################################################
        # My thoughts:
        # Let's say there are 2 people to consider: person1 &
        # person2. Let's say that they both enjoy each others
        # company. Thus you have 2 friends and 1 friendship
        # A friendship, corresponds to a 2 unidirectional edge,
        # that is p1 likes p2 & p2 likes p1. If the situtation 
        # was that p1 likes p2 but p2 does not like p1, then 
        # you have 0 friends and 0 friendshps
        # So the last parameter of avg_friendships in 
        # populate_graph should be avg_friends as the instructor
        # told us to divide the last parameter by 2 before using it
        #####################################################
        for i in range(num_users * avg_friendships // 2):
            friends = all_bidirectional_edges[i]
            self.add_friendship(friends[0], friends[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # The next line that set self.friendships is for testing/debugging
        # purposes only
        # self.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        
        qq = Queue()
        qq.enqueue([user_id])

        while qq.size() > 0:
            current_path = qq.dequeue()

            # If the vertex at the end of the current path has not
            # been visited then continue building the path forward
            if current_path[-1] not in visited:
                # mark as visited
                visited[current_path[-1]] = current_path
                # enqueue all neightbors
                for next_vert in self.friendships[current_path[-1]]:
                    new_path = list(current_path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'Friendships: {sg.friendships}')
    print('**********************************************************************')
    connections = sg.get_all_social_paths(1)
    print(f'connections: {connections}')


"""
Answers to the questions
Ques1: To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?
Ans1: Total number of friends = 100*10 = 1000 friends. The total number of friendships = friends/2 = 1000/2 = 500
      So we would have to call add_friendship() 500 times

Ques2: If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular
       user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
Ans2: Since it is random, there is a varying number of total users in an extended social network. This varying number can be from 1
      all the way to the total number of users. Thus you cannot specify one figure for the percentage of other users will be in a 
      particular user's extended social network
      Again because of randomness, you cannot say what the average degree of separation between a user and those in his/her 
      extended network is as the number of common friends between users is random
"""



##############################################################
# My test code - comment out before final commit
##############################################################

# Check adding users properly
# sg = SocialGraph()
# sg.populate_graph(10, 2)
# for key in sg.users:
#     print(f'key={key} ---> name={sg.users[key].name}')

# Check adding friends properly
# sg = SocialGraph()
# sg.populate_graph(4, 2)
# print(sg.friendships)
