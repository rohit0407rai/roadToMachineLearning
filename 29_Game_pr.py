def game():
    return 600
score=game()
with open("hiscore.text") as f:
    hiscorestr=f.read()
if hiscorestr=='':
    with  open("hiscore.text","w") as f:
        f.write(str(score))
elif int(hiscorestr)<score :
    with open("hiscore.text","w") as f:
        f.write(str(score));
