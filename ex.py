class parent():
    def first(self):
        print("first fun")
class child(parent):
    def second(self):
        print("second fun")
ob=child()
ob.first()
ob.second()
