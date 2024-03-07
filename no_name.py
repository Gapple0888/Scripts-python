import os 
import webbrowser as wb

def starting():
    answer = input("Que souhaitez-vous faire (travailler/se divertir) ? ")
    time = int(input("Pendant combien de temps (en minutes) ? "))
    if answer == "travailler":
        work(time)
    elif answer == "se divertir":
        relax(time)


def work(time):
    print(str(time) + " minutes")
    os.startfile("c:/Users/albin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Anytype.lnk")

def relax(time):
    print(str(time) + " minutes")
    jellyfin = "http://localhost:8096/web/index.html#!/home.html"
    

if __name__ == '__main__' :
    starting()