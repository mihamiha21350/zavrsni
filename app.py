from flask import Flask, render_template, request, flash
from music21 import *
import time
import os
##Setup za Music21 i Flask
us = environment.UserSettings()
us['lilypondPath'] = 'static/lilypond/bin/lilypond.exe'
ajmo=stream.Stream()
intervalStream=stream.Stream()
akordStream=stream.Stream()
ljestvicaStream=stream.Stream()

app=Flask(__name__)
app.secret_key="resisestro123"

if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')


##------------ClearAll()------------
def clearAll(): #BRIŠE SVE U /STATIC/NOTE. PRIPREMA PROGRAM ZA RAD.
    poz='static/note'
    for f in os.listdir(poz):
        os.remove(os.path.join(poz,f))


##------------INDEX------------
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


##------------HOME IZBORNIK------------
@app.route("/home")
def izbornik():
    clearAll()
    return render_template("izbornik.html")


##------------INTERVALI------------
@app.route("/intervali", methods=["POST", "GET"])
def intervali():
    clearAll()
    return render_template("intervali.html")

@app.route("/posaljiintervali", methods=["POST", "GET"])
def posaljiintervali():
    ton=request.form.get("ton")+request.form.get("karak")
    toncek=note.Note(pitch.Pitch(ton))
    karint1=request.form.get("karakint1")
    karint2=request.form.get("karakint2")
    ##Provjera tipa intervala (veliki/mali, čisti)
    if karint1 is not None:
        try:
            karint = karint1
        except ValueError:
            pass
    elif karint2 is not None:
        try:
            karint = karint2
        except ValueError:
            pass
    ##Računanje intervala
    i=interval.Interval((request.form.get("interval")+karint))
    toncek2=i.transposeNote(toncek)
    intervalStream.append(toncek)
    intervalStream.append(toncek2)
    ##Ispis i brisanje nepotrebnih datoteka
    intervalStream.write("lilypond.svg", fp="static/note/interval")
    if os.path.exists("static/note/interval"):
        os.remove("static/note/interval")
    intervalStream.clear()
    return render_template("intervali.html")


##------------LJESTVICE------------
@app.route("/ljestvice", methods=["POST", "GET"])
def ljestvice():
    clearAll()
    return render_template("ljestvice.html")

@app.route("/posaljiljestvice", methods=["POST", "GET"])
def posaljiljestvice():
    ljestvicaStream.append(meter.TimeSignature('8/4'))
    lton=request.form.get("ton")+request.form.get("karak")
    ltoncek=note.Note(pitch.Pitch(lton))
    MajSec=interval.Interval("M2")
    MinSec=interval.Interval("m2")
    ##Provjera tipa ljestvice
    if(request.form.get("tip")=="dur"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MajSec.transposeNote(ltoncek))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    if(request.form.get("tip")=="mol"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MajSec.transposeNote(ltoncek))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    if(request.form.get("tip")=="dorska"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MajSec.transposeNote(ltoncek))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    if(request.form.get("tip")=="frigijska"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MinSec.transposeNote(ltoncek))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    if(request.form.get("tip")=="lidijska"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MajSec.transposeNote(ltoncek))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    if(request.form.get("tip")=="miksolidijska"):
        ljestvicaStream.append(ltoncek)
        ljestvicaStream.append(MajSec.transposeNote(ltoncek))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))
        ljestvicaStream.append(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))
        ljestvicaStream.append(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek)))))))
        ljestvicaStream.append(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(MinSec.transposeNote(MajSec.transposeNote(MajSec.transposeNote(ltoncek))))))))
    ljestvicaStream.write("lilypond.svg", fp="static/note/ljestvica")
    if os.path.exists("static/note/ljestvica"):
        os.remove("static/note/ljestvica")
    ljestvicaStream.clear()
    return render_template("ljestvice.html")

@app.route("/kakoizgraditiljestvicu", methods=["POST", "GET"])
def kakoizgraditiljestvicu():
    clearAll()
    return render_template("kakoizgraditiljestvicu.html")


##------------AKORDI------------
@app.route("/akordi", methods=["POST", "GET"])
def akordi():
    clearAll()
    return render_template("akordi.html")

@app.route("/posaljiakordi", methods=["POST", "GET"])
def posaljiakordi():
    aton=request.form.get("ton")+request.form.get("karak")
    atoncek=note.Note(pitch.Pitch(aton))
    MajThird=interval.Interval("M3")
    MinThird=interval.Interval("m3")
    ##Provjera tipa akorda
    if(request.form.get("tip")=="dur"):
        finKord=chord.Chord([atoncek.pitch, MajThird.transposeNote(atoncek).pitch, MinThird.transposeNote(MajThird.transposeNote(atoncek)).pitch])
    elif(request.form.get("tip")=="mol"):
        finKord=chord.Chord([atoncek.pitch, MinThird.transposeNote(atoncek).pitch, MajThird.transposeNote(MinThird.transposeNote(atoncek)).pitch])
    elif(request.form.get("tip")=="sm"):
        finKord=chord.Chord([atoncek.pitch, MinThird.transposeNote(atoncek).pitch, MinThird.transposeNote(MinThird.transposeNote(atoncek)).pitch])
    elif(request.form.get("tip")=="pov"):
        finKord=chord.Chord([atoncek.pitch, MajThird.transposeNote(atoncek).pitch, MajThird.transposeNote(MajThird.transposeNote(atoncek)).pitch])
    ##Provjera obrata kvintakorda
    if(request.form.get("obrat")=="se"):
        finKord.inversion(1)
    if(request.form.get("obrat")=="ks"):
        finKord.inversion(2)
    akordStream.append(finKord)
    ##Ispis i brisanje nepotrebnih datoteka
    akordStream.write("lilypond.svg", fp="static/note/akord")
    if os.path.exists("static/note/akord"):
        os.remove("static/note/akord")
    akordStream.clear()
    return render_template("akordi.html")

@app.route("/kakoizracunatiakord", methods=["POST", "GET"])
def kakoizracunatiakord():
    clearAll()
    return render_template("kakoizracunatiakord.html")
