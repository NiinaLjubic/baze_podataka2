from __init__ import Session

from vozila import Vozilo
from korisnici import Korisnik
from najmovi import Najam
from __init__ import Base
from datetime import datetime
from sqlalchemy.exc import IntegrityError





import os 
from flask import Flask,render_template, request,redirect, url_for,flash,session



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.secret_key = 'ovo-je-moj-tajni-kljuc'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index ():
    vozilo = Session.query(Vozilo).all()
    return render_template('index.html', vozilo=vozilo)


@app.route('/register', methods=['POST'])
def register_user():
    
    ime = request.form['firstName']
    prezime = request.form['lastName']
    email = request.form['email']
    password = request.form['password']
    
    new_user = Korisnik(ime=ime, prezime=prezime, email=email, password=password)
    Session.add(new_user)
    Session.commit()

    flash('Uspjesna registracija.', 'success')
    return redirect(url_for('login'))


@app.route("/login")
def login ():
    return render_template('login.html')

@app.route('/loguser', methods=['GET', 'POST'])
def log_user():
   
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Session.query(Korisnik).filter_by(email=email, password=password).first()
       
        if user:
            session['user_name'] = user.ime
            session['user_id'] = user.ID_korisnika
            flash('Uspjesna prijava!')
            return redirect(url_for('home'))
        else:
            flash('Pogrešan e-mail ili lozinka. Molimo pokušajte ponovno.', 'danger')
            return redirect(url_for('login'))

    


@app.route("/home")
def home ():

    vozilo = Session.query(Vozilo).all()
    najam = Session.query(Najam).all()
    korisnik = Session.query(Korisnik).all()
    provjera = Session.query(Najam).count()
    return render_template('home.html',vozilo=vozilo,najam=najam,korisnik=korisnik, provjera=provjera)


@app.route('/logout')
def logout():
    
    session.pop('user_name', None)
    flash('Uspješna odjava!', 'success')
    return redirect(url_for('login'))


@app.route('/dodaj-vozilo', methods=['POST'])
def dodaj_vozilo():
    marka = request.form.get('marka')
    model = request.form.get('model')
    godina = request.form.get("godina")
    registracijska_oznaka = request.form.get('registracijska_oznaka')
    dostupno = request.form.get("dostupno")
    cijena_najma = request.form.get("cijena_najma")
 
    
    
    novo_vozilo = Vozilo(marka=marka, model=model,godina=godina, registracijska_oznaka=registracijska_oznaka,dostupno=dostupno, cijena_najma=cijena_najma)
    Session.commit()
    Session.add(novo_vozilo)
    flash('Vozilo dodano.', 'success')

    return redirect(url_for('home'))

@app.route('/izbrisi_vozilo/<int:ID_vozila>', methods=['POST'])
def izbrisi_vozilo(ID_vozila):
    vozilo = Session.query(Vozilo).get(ID_vozila)
    
    """    if vozilo:
        
        Session.delete(vozilo)
        Session.commit()  
        flash('Vozilo je uspjesno izbrisano.', 'success') """
    try:
        Session.delete(vozilo)
        Session.commit()  
        flash('Vozilo je uspjesno izbrisano.', 'success')
        return redirect(url_for('home'))
    except IntegrityError as e:
        Session.rollback() 
        flash('Greska pri brisanju. Provjerite postoji li ovaj model u najmu. ', 'success')
        
    return redirect(url_for('home'))

@app.route('/uredi_vozilo/<int:ID_vozila>')
def uredi_vozilo(ID_vozila):
    vozilo = Session.query(Vozilo).get(ID_vozila)
    
    return render_template('uredi_vozilo.html', vozilo=vozilo)

@app.route('/update_vozilo/<int:ID_vozila>', methods=['POST'])
def update_vozilo(ID_vozila):
    vozilo = Session.query(Vozilo).get(ID_vozila)
    if vozilo:
        
        vozilo.marka = request.form.get('marka')
        vozilo.model = request.form.get('model')
        vozilo.godina = request.form.get('godina')
        vozilo.registracijska_oznaka = request.form.get('registracijska_oznaka')
        vozilo.dostupno = request.form.get('dostupno')
        vozilo.cijena_najma = request.form.get('cijena_najma')
        
        
        Session.commit()
    flash("Uspjesno uredjeno! ", "Success")
    return redirect(url_for('home'))






@app.route('/handle_najam', methods=['POST'])
def handle_najam():

    
    ID_vozila = request.form.get('id_vozila')
    korisnik_id = request.form.get('id_korisnika')
    datum_najma = request.form.get('start_date')
    datum_povrata = request.form.get('end_date')
    
    

    datum_najma = datetime.strptime(datum_najma, '%Y-%m-%d')
    datum_povrata = datetime.strptime(datum_povrata, '%Y-%m-%d')

    najam = Najam(vozilo_id=ID_vozila,korisnik_id=korisnik_id,datum_najma=datum_najma,datum_povrata=datum_povrata )
    
    Session.add(najam)
    Session.commit()
    
   
      
    flash("Najam uspjesan","success")
    return redirect(url_for('home'))


@app.route('/izbrisi_najam/<int:ID_najma>', methods=['POST'])
def izbrisi_najam(ID_najma):
    najam = Session.query(Najam).get(ID_najma)
    
    if najam:
        
        Session.delete(najam)
        Session.commit()  
        flash('Najam je uspjesno izbrisan.', 'success')

    return redirect(url_for('home'))

app.debug = True

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)