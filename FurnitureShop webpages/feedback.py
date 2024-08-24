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
    <a class="dropdown-item" href="new product.py">New Arrival</a>
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
 <form class="form-height"><br>
   <center><h2 class="font-style-home">Feedback Form</h2></center><br>
  <div class="form-group row">
    <label for="inputEmail3" class="col-sm-2 col-form-label">Email :</label>
    <div class="col-sm-10">
      <input type="email" class="form-control textbox-color" id="inputEmail3" name="email" placeholder="Enter email address">
    </div>
  </div>
  <div class="form-group row">
    <label for="validationDefault01" class="col-sm-2 col-form-label">Name :</label>
    <div class="col-sm-10">
      <input type="text" class="form-control textbox-color" id="validationDefault01" name="name" placeholder="Enter your name">
    </div>
  </div>
 
<div class="form-group feedback">
    <label for="exampleInputEmail1">Feedback Message :</label>
    <input type="text" class="form-control feedback" id="exampleInputEmail1" name="message" rows="5"></textarea>
    
  </div>

  <div class="form-group row">
    <div class="col-sm-10">
      <input type="submit" class="btn btn-primary" name="sub" data-placement="right" title="Confirm" data-toggle="modal" data-target="#exampleModal">
  

      <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Information</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Are you sure?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
        <button type="button" class="btn btn-primary">OK</button>
      </div>
    </div>
  </div>

    </div>
  </div>
</form>
</form>
</div><br><br><br><br><br>""")
import smtplib
import pymysql
import cgi
import cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="udc")
cur = conn.cursor()

form = cgi.FieldStorage()

pemailid = form.getvalue("email")
pname = form.getvalue("name")
pmessage = form.getvalue("message")
psubmit = form.getvalue("sub")

if psubmit!=None:
    q = """insert into feedback(email,name,message) values('%s','%s','%s')""" % (pemailid,pname,pmessage)
    cur.execute(q)
    conn.commit()

    fromaddr = "arunnallasivam6@gmail.com"
    password = "ejffiypxrxwmeztx"
    toaddr = pemailid
    subject = "We Heard from you "
    body = """Yes you Read that right. MR\MRS  %s \n , Thanks for your feedback\n -UDC Furniture"""% (pname)
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

print("""<div class="footer-bar bg-dark fixed-bottom">
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
