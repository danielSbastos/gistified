import os

from gistified import create_app


# Test for feito
def test(one, 
   two, three

):
   pass 

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
