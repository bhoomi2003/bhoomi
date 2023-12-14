app = Flask(__name__)


pipe = pickle.load(open("Naive_model.pk1","rb"))

@app.route('/'. methods=["GET","POST"])
def main_function():