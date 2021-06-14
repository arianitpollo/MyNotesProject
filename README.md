<h2>Në lidhje me projektin</h2>

Eshte nje web app per shenime(notes). Fillimisht per te perdorur kete aplikacion duhet te hapni llogarin(account) tuaj dhe pasi te kyceni(log in), do te
mund te shtoni shenime(add), ti ndryshoni ato(edit) si dhe ti fshini(delete). Mbasi te dilni nga
llogaria juaj, kur te hyni shenimet do ti keni perseri aty, pra cdo llogari dhe cdo perdorues do te
ket qasje te shenimet e tij.

**Teknologjite e perdorura**
<ul>
<li>HTML</li>
<li>Bootstrap</li>
<li>Flask</li>
<li>Flask-Login</li>
<li>Flask SQLAlchemy</li>
<li>SQLite3</li>
</ul>

<h2>Perdorimi</h2>

<ol>
<li>Hani projektin permes PyCharm</li>
<li>Ekzekutoni main.py</li>
<li>Klikoni ne linkun qe do te ju shfaqet ne terminal zakonisht eshte ne formen http://127.0.0.1:5000/ </li>
<li>Logouni nese keni account, ose krijoni te ri nese nuk keni</li>
<li>Tani mund te shfrytezoni mundesite: te krijone shenim te ri, te fshini ndonje shenim si dhe te ndryshoni</li>
<li>Klikoni ne anen e djathe larte dhe do ju shfaqet menyja nga ku mund te dilni nga accounti juaj</li>
<ol>

<h2>Struktura e projektit</h2>
+ Ne "requirements.txt" jane te gjitha librarite me te cilat eshte ndertuar ky projekt
+ Ne folderin "Models" ne filen "models.py" jane dy modelet User dhe Notes prej te cilave jane krijuar edhe 2 tabelat ne database
+ Ne Folderin "routes" jane 2 filet "auth" dhe "views". Ku ne "auth" gjenden te gjitha rruget
+ Ne folderin "templates" jane te gjitha html filet
+ Ne folderin "test" gjenden file "unittest.py" ne te cilen jane kryer disa testime
+ Ne filen "__init__.py" kryhen te  gjitha konfigurimet, krijimi i apliakcionit, krijimi i databases, lidhja e aplikacionit me databasen, importimi dhe regjistrimi i views ose sic quhen ndryshe blueprints, krijimi i instances te Login Manager qe ben lidhjen  mes aplikacionit dhe Flask-login

<h3>DDL/Scripts</h3>

Te gjitha manipulimet me databasen jane bere permes SQLAlchemy(lehteson komunikimin mes aplikacionit tone dhe databases) ne filet views.py(manipulimet me tabelen Notes) dhe auth.py(manipulimet me tabelen User)

<h3>Endpoints</h3>
+ "/" Ju dergon ne faqen kryesore "home.html"
+ "/login" Ju dergon ne faqen ku logoeni ne llogarine tuaj "login.html" 
+ "/signup" Ju dergon ne "signup.html" ku krijon llogari te re
+ "/notes" Per tu kycur duhet te jeni te loguar ne llogarin tuaj. Ketu gjenden te gjitha shenimet tuaja me te cilat mund te manipuloni dhe te krijoni
+ "notes/id/edit" Ju dergon ne "edit.html" ku mund te ndryshoni shenimin tuaj me id e caktuar
+ "notes/id/delete" Ju mundeson qe te fshini shenimin me id te caktuar
+ Nese provoni te qaseni ne "/notes" pa u kycur ne llogarine tuaj, do te ju dergoj ne "/login"






