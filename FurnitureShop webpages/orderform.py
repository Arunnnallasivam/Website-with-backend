#!C:/Users/welcome/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

print("""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/Bootstrap/bootstrap.min.css">

    <!-- Custom css -->
    <link rel="stylesheet" type="text/css" href="css/customer.css">

    <title>UDC Furniture</title>
  </head>

  <body>

    <header>

      <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="home.py"><img src="./Images/UDCLogo.png" class="rounded-circle logo-img"></a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="home.py">HOME</a>
            </li>

            <li class="nav-item active">
                <a class="nav-link" href="about.py">ABOUT</a>
            </li>

            <li class="nav-item active">
                <div class="dropdown show">
  <a class="btn dropdown-toggle product" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown"aria-haspopup="true" aria-expanded="false">
    Product
  </a>

  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
    <a class="dropdown-item" href="new product.py">New Product</a>
    <a class="dropdown-item" href="latest promotion.py">Latest Promotion</a>
    <a class="dropdown-item" href="sofa.py">Sofa</a>
    <a class="dropdown-item" href="office.py">Office</a>
    <a class="dropdown-item" href="bedding.py">Bed</a>
    <a class="dropdown-item" href="furniture.py">Furniture</a>
  </div>
</div>
    </li>
            <li class="nav-item active">
                <a class="nav-link" href="service.py">Service</a>
            </li>
            
            <li class="nav-item active">
                <div class="dropdown show">
  <a class="btn dropdown-toggle product" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown"aria-haspopup="true" aria-expanded="false">
    Contact
  </a>

  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
    <a class="dropdown-item" href="contact.py">Contact</a>
    <a class="dropdown-item" href="feedback.py">Feedback</a>
  </div>
</div>

            </li>

          </ul>
            </div>

    </nav>

    </header>
    </div>
<center>
<div class="body">
 <form class="form-height">

  <div class="form-group">
  <section id="section_2" class="section group">
  <div class="contact_form">
  <center>
<h2 class="font-style-home">Order Form</h2><br>
  <p>"Welcome to UDC Furniture"</p>
</center>

</section>

<center>
<form>
  <div class="form-row">
    <div class="col-md-4 mb-3">
      <label for="validationDefault01">First name</label>
      <input type="text" class="form-control" id="validationDefault01" name="fname" placeholder="Enter First name"  required>
    </div>
    <div class="col-md-4 mb-3">
      <label for="validationDefault02">Last name</label>
      <input type="text" class="form-control" id="validationDefault02" name="lname" placeholder="Enter Last name" required>
    </div>
    <div class="col-md-4 mb-3">
      <label for="validationDefault02">Phone Number</label>
      <input type="int" class="form-control" id="validationDefault02" name="pnumber" placeholder="Enter Phone Number" required>
    </div>
    <div class="form-group col-md-6">
      <label for="inputEmail4">Email</label>
      <input type="email" class="form-control" id="inputEmail4" name="mail" placeholder="Email">
    </div>
   <div class="col-md-4 mb-3">
      <label for="validationDefault02">Quantity</label>
      <input type="int" class="form-control" id="validationDefault02" name="quantity" placeholder="How many do you want?" required>
    </div>
    
  <div class="form-group">
    <label for="inputAddress">Address</label>
    <input type="text" class="form-control" id="inputAddress" name="address" placeholder="1234 Main St">
  </div>
  
  <div class="form-row">
        <div class="col-md-6 mb-3">
      <label for="validationCustom03">City</label>
      <input type="text" class="form-control" id="validationCustom03" name="city" placeholder="City" required>
  </div>
    <div class="col-md-3 mb-3">
      <label for="validationDefault04">State</label>
      <input type="text" class="form-control" id="validationDefault04" name="state" placeholder="State" required>
    </div>
    <div class="form-group col-md-2">
      <label for="validationCustom05">Zip Code</label>
      <input type="text" class="form-control" id="validationCustom05" name="zip" placeholder="Zip" required>
    </div>

  <center><input type="submit" name="sub" class="btn btn-info"></center>
<br><br><br><br><br><br>
</form>""")
import smtplib
import pymysql
import cgi
import cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="udc")
cur = conn.cursor()

form = cgi.FieldStorage()

pfname = form.getvalue("fname")
plname = form.getvalue("lname")
pnumber = form.getvalue("pnumber")
pemailid = form.getvalue("mail")
paddress = form.getvalue("address")
pcity = form.getvalue("city")
pstate = form.getvalue("state")
pzip = form.getvalue("zip")
psubmit = form.getvalue("sub")

if psubmit!=None:
    q = """insert into orderform(firstname,lastname,phonenumber,email,address,city,state,zip) values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (pfname,plname,pnumber, pemailid, paddress,pcity,pstate,pzip)
    cur.execute(q)
    conn.commit()

    fromaddr = "arunnallasivam6@gmail.com"
    password = "ejffiypxrxwmeztx"
    toaddr = pemailid
    subject = "We Heard from you "
    body = """Yes you Read that right. MR  %s \n , We are happy to work with you and our team is currently unavailable to contact you at the moment , we will surely contact you in the next  3 days , thank you for your patience \n -UDC Furniture"""% (pfname)
    msg = """Subject :{}\n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print("""
            <script>
                alert("We Got You, Please Check Your Mail");
            </script>
        """)
conn.close()
print(""" </div>
</center>

<div class="footer-bar bg-dark fixed-bottom">
  <div class="col-6 col-md ">
  <a href="Privacy policy.py"><div class="footer-icon-side"><span style="padding-left:80%;"> Privacy Policy</span></div></a>

  <div class="footer-icon"><center>
    <a class="ex2" href="https://www.facebook.com/"><img src="Images/facebook logo.png" alt="Facebook" width="36px" height="35px"></a>
  </center></div>

  <div class="footer-icon"><center>
    <a class="ex2" href="https://twitter.com/login?lang=en"><img src="Images/twitter.png" alt="Twitter" width="40px" height="40px"></a>
  </center></div>

  <div class="footer-icon"><center>     
    <a class="ex2" href="https://myaccount.google.com/"><img src="Images/google.png" alt="Google" width="30px" height="30px"></a>
  </center></div>

  <div class="footer-icon"><center>
    <a class="ex2" href="https://www.instagram.com/accounts/login/?hl=en"><img src="Images/instagram logo.png" alt="Instagram" width="35px" height="30px"></a>
  </center></div>
  
  <a href="Terms and conditions.py"><div class="footer-icon-side"><span> Terms and Conditions </span></div></a>

     
</div><br> <br> 

  <footer align="center"> 
  
  
   <Span style="padding-left:50px;">   
  Copyright &copy; 2021 UDC Funrniture
  
  </Span>


</footer> 


  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="js/jquery-3.2.1.slim.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>


</body>
</html>""")

