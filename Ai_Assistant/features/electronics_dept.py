import txttsp

def new():
    pyobj=txttsp
    file=open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/electronics_dept.txt','r')
    read=file.read()
    pyobj.speak(read)