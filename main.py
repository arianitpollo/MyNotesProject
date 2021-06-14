from website import create_app

app = create_app()

if __name__ == '__main__':#vetem nese e bejme run dhe jo nese e bejm import do ta ekzekutoj app.run
    app.run(debug=True)#run the web server,debug==true dmth qe sa here ta bejme ndonje ndryshim ne kod donta beje update serverin
