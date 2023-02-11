"Implement Lisp-like frames in Python"

class Frame():
  "Implement a simple Python frame library"
  frame_counter = 0
  def __init__(self, name = ""):
    Frame.frame_counter += 1
    self.objects = []
    self.depth = 0
    if (len(name)) == 0:
      self.name = f"Frame:{Frame.frame_counter}"
    else:
      self.name = f'"{name}"'

  def add_subframe(self, a_frame):
    a_frame.depth = self.depth + 1
    self.objects.append(a_frame)

  def add_number(self, a_number):
    self.objects.append(a_number)

  def add_string(self, a_string):
    self.objects.append(a_string)

  def __str__(self):
    indent = " " * self.depth * 2
    ret = indent + f"<Frame {self.name}>\n"
    for frm in self.objects:
      if isinstance(frm, (int, float)):
        ret = ret + indent + "  " + f"<Number {frm}>\n"
      if isinstance(frm, str):
        ret = ret + indent + "  " + f'<String "{frm}">\n'
      if isinstance(frm, Frame):
        ret = ret + frm.__str__()
    return ret

f1 = Frame()
f2 = Frame("a sub-frame")
f1.add_subframe(f2)
f1.add_number(3.14)
f2.add_string("a string")
print(f1)
f2.add_subframe(Frame("a sub-sub-frame"))
print(f1)

class BookShelf():
  "A bookshelf is a collection of frames"
  def __init__(self, name = ""):
    self.frames = []
    self.name = name

  def add_frame(self, a_frame):
    self.frames.append(a_frame)

  def search_text(self, search_string):
    ret = []
    for frm in self.frames:
      if str(frm).index(search_string):
        ret.append(frm)
    return ret

bookshelf = BookShelf()
bookshelf.add_frame(f1)
search_results = bookshelf.search_text("sub")
print("Search results: all frames containing 'sub':")
for rs in search_results:
  print(rs)
