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

    <div>

      <div id="carouselExampleControls" class="carousel slide carousel-height" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100 carousal-img" src="Images/office.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100 carousal-img" src="Images/sofa1.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100 carousal-img" src="Images/home chair.jpg" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
  </div>

</div>
</form>
  </center>

  <nav class="nav nav-pills nav-justified product-nav">
  <a class="nav-item nav-link font-style" href="sofa.py">Sofa</a>
  <a class="nav-item nav-link font-style" href="office.py">Office</a>
  <a class="nav-item nav-link font-style" href="bedding.py">Bed</a>
  <a class="nav-item nav-link font-style" href="furniture.py">Furniture</a>
</nav>
  
<form class="form-height">
<center>
  <h1 class="font-style-home">Welcome to UDC Furnitures</h1>
  <p>Our company is selling home furniture for you. Our new products are made based on simple, modern and more cortempoary design that concentrates on caving texture and treatment of the wood. Our company is give online service for customer. Moreover, our company have many promotion and gift.</p>
</center>
<div class="album py-5">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <div class="card mb-4 box-shadow zoom">
                <a href="new product.py"><img class="card-img-top" data-src="holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=Thumbnail" <img src="Images/newarrivals.jpg" alt="New product" height ="200px"></a>
                
                <div class="card-body">
                  <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                       <a class="nav-link btn btn-sm btn-outline-secondary" href="new product.py">New Arrivals</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card mb-4 box-shadow zoom">
                <a href="latest promotion.py"><img class="card-img-top" data-src="holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=Thumbnail" <img src="Images/lastestpromotion.jpg" height ="200px" alt="Latest promotion"></a>
                <div class="card-body">
                  <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                       <a class="nav-link btn btn-sm btn-outline-secondary" href="latest promotion.py">Latest promotion</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div class="card mb-4 box-shadow zoom">
                <a href="orderform.py"><img class="card-img-top" data-src="holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=Thumbnail" <img src="Images/onlineorder.png" height ="200px" alt="Online order"></a>
                <div class="card-body">
                  <div class="d-flex justify-content-between align-items-center">
                   <div class="btn-group">
                       <a class="nav-link btn btn-sm btn-outline-secondary" href="orderform.py">Online order</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
    </div>
<center><br><br>
  <div class="company-logo">
  <h2 class="font-style-home">Our company partner</h2><br>
    <a href="#"><img class="zoom" src="Images/sein mya.jpg" alt="Sein Mya" width="200px" height="150px"></a>

    <a href="#"><img class="zoom"  src="Images/Sweety-Home-Logo.jpg" alt="Sweety Home" width="200px" height="150px"></a>

    <a href="#"><img class="zoom"  src="Images/pwint oo.jpg" alt="Pwint OO" width="200px" height="150px"></a>

    <a href=""><img class="zoom"  src="Images/casabella.jpg" alt="Case Bella" width="240px" height="150px"></a>

    <a href=""><img class="zoom"  src="Images/royal logo.jpg" alt="Royal" width="200px" height="150px"></a>
  </div>
</center><br><br><br><br><br><br><br><br><br><br><br><br><br></form>

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