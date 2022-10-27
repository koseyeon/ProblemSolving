class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Double_linked_list:
    def __init__(self):
        self.cursor = Node('')
    def cursor_move_left(self):
        left_node = self.cursor.prev
        if(left_node == None):
            return
        else:
            self.cursor = left_node
            return
    def cursor_move_right(self):
        right_node = self.cursor.next
        if(right_node == None):
            return
        else:
            self.cursor = right_node
            return
    def insert(self,node):
        left_node = self.cursor.prev
        if(left_node == None):
            self.cursor.prev = node
            node.next = self.cursor
            return
        else:
            left_node.next = node
            node.prev = left_node
            node.next = self.cursor
            self.cursor.prev = node
            return
    def remove(self):
        left_node = self.cursor.prev
        if(left_node == None):
            return
        else:
            self.cursor.prev = left_node.prev
            if(left_node.prev != None):
                left_node.prev.next = self.cursor
            return
target_str = input()
str_list = Double_linked_list()
for x in target_str:
    str_list.insert(Node(x))
m = int(input())
for _ in range(m):
    cmd = list(input().split())
    if (cmd[0]=='L'):
        str_list.cursor_move_left()
    elif (cmd[0]=='D'):
        str_list.cursor_move_right()
    elif (cmd[0]=='B'):
        str_list.remove()
    elif (cmd[0]=='P'):
        data = cmd[1]
        str_list.insert(Node(data))
answer = []
while str_list.cursor.prev!=None:
    str_list.cursor_move_left()
while str_list.cursor.next!=None:
    answer.append(str_list.cursor.data)
    str_list.cursor_move_right()
answer.append(str_list.cursor.data)
print(''.join(answer))