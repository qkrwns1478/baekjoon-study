from collections import deque
from re import findall

def split_str(s):
    items = findall(r'"[^"]+"|\S+', s)
    result = []
    for item in items:
        if item.startswith('"') and item.endswith('"'):
            result.append(item[1:-1])
        else:
            result.append(item)
    return result

class File:
    def __init__(self, name, content, directory=None):
        self.name = name
        self.content = content
        self.directory = directory
    def update_content(self, content):
        self.content = content

class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = dict()
        self.files = dict()
    def add_child(self, child):
        self.child[child.name] = child
        child.parent = self
    def remove_child(self, child):
        self.child.pop(child.name)
        child.parent = None
    def add_file(self, file):
        self.files[file.name] = file
        file.directory = self
    def remove_file(self, file):
        self.files.pop(file.name)
        file.directory = None

T = int(input())
for t in range(T):
    root = Folder('')
    c = int(input())
    for _ in range(c):
        cmd = split_str(input())
        if cmd[0] == "echo":
            content = cmd[1]
            path = deque(cmd[-1].split('/'))
            cur = root
            
            while len(path) > 1:
                cur = cur.child[path.popleft()]
            
            if path[0] in cur.files:
                cur.files[path[0]].update_content(content)
            else:
                new_file = File(path[0], content)
                cur.add_file(new_file)
        
        elif cmd[0] == "cp":
            s_path = deque(cmd[1].split('/'))
            d_path = deque(cmd[2].split('/'))
            
            cur = root
            while len(s_path) > 1:
                cur = cur.child[s_path.popleft()]
            target = cur.files[s_path[0]]
            
            cur = root
            while len(d_path) > 1:
                cur = cur.child[d_path.popleft()]
                
            if d_path[0] in cur.child: # destination is a directory
                cur = cur.child[d_path[0]]
                new_file = File(target.name, target.content)
            else: # destination is a new filename
                new_file = File(d_path[0], target.content)
            cur.add_file(new_file)
        
        elif cmd[0] == "mv":
            s_path = deque(cmd[1].split('/'))
            d_path = deque(cmd[2].split('/'))
            
            cur = root
            while len(s_path) > 1:
                cur = cur.child[s_path.popleft()]
                
            is_file = True
            if s_path[0] in cur.files:
                target = cur.files[s_path[0]]
            else:
                target = cur.child[s_path[0]]
                is_file = False
            
            cur = root
            while len(d_path) > 1:
                cur = cur.child[d_path.popleft()]
            
            if d_path[0] in cur.child: # destination is a directory
                cur = cur.child[d_path[0]]
                if is_file:
                    new_file = File(target.name, target.content)
                    cur.add_file(new_file)
                    target.directory.remove_file(target)
                else:
                    target.parent.remove_child(target)
                    cur.add_child(target)
            else: # destination is a new filename
                new_file = File(d_path[0], target.content)
                cur.add_file(new_file)
                target.directory.remove_file(target)

        elif cmd[0] == "rm":
            paths = deque(cmd[1].split('/'))
            cur = root
            while len(paths) > 1:
                cur = cur.child[paths.popleft()]
            cur.remove_file(cur.files[paths[0]])

        elif cmd[0] == "mkdir":
            paths = deque(cmd[1].split('/'))
            cur = root
            while len(paths) > 1:
                cur = cur.child[paths.popleft()]
            new_child = Folder(paths[0])
            cur.add_child(new_child)

        elif cmd[0] == "rmdir":
            paths = deque(cmd[1].split('/'))
            cur = root
            while len(paths) > 1:
                cur = cur.child[paths.popleft()]
            cur.remove_child(cur.child[paths[0]])

    q = int(input())
    res = list()
    is_error = False
    for _ in range(q):
        cmd = deque(input().split('/'))
        try:
            cur = root
            while len(cmd) > 1:
                cur = cur.child[cmd.popleft()]
            res.append(cur.files[cmd[0]].content)
        except:
            is_error = True
            break
    if is_error:
        print("invalid!")
    else:
        for r in res:
            print(r)
    if t != T-1:
        print()