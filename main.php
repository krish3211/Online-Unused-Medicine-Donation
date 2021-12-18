<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>main</title>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css'><link rel="stylesheet" href="./style.css">
   <style>
     table, th, td {
  border: 5px solid black;
}
     </style>
</head>
<body>
<!-- partial:index.partial.html -->
<nav class="navbar navbar-inverse navbar-global navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Unused Medicine Donation</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav navbar-user navbar-right">
            <li><a href="#about"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>
          </ul>
        </div>
      </div>
    </nav>
<nav class="navbar-primary">
  <a href="#" class="btn-expand-collapse"><span class="glyphicon glyphicon-menu-left"></span></a>
  <ul class="navbar-primary-menu">
    <li>
      <a href="#"><span class="glyphicon glyphicon-envelope"></span><span class="nav-label">Medicine Search</span></a>
      <a href="#"><span class="glyphicon glyphicon-list-alt"></span><span class="nav-label">Upload Medicine Details</span></a>
     
    
    </li>
  </ul>
</nav>
<div class="main-content">
  <form action="ex.py" method="get">
    <input type="search" name="search" >
    <table>
      <tr>
        <th>Person Name</th>
        <th>city/village</th>
        <th>Medicine Name</th>
        <th>Medicine Uses</th>
        <th>Medicine Count</th>
        <th>Expiry Date</th>
        <th>phone NO</th>
      </tr>
      <tbody>
        <?php
        $db = mysqli_connect('localhost','root','','user');
        $que = mysqli_query($db,"SELECT * FROM data");
        while ($row = mysqli_fetch_assoc($que)){
            echo "<tr>";
            echo "<td>".$row['PersonName'].'</td>';
            echo "<td>".$row['city/village'].'</td>';
            echo "<td>".$row['MedicineName'].'</td>';
            echo "<td>".$row['MedicineUses'].'</td>';
            echo "<td>".$row['MedicineCount'].'</td>';
            echo "<td>".$row['ExpiryDate'].'</td>';
            echo "<td>".$row['PhoneNo'].'</td>';
            echo '</tr>';
        }
        ?>
      </tbody>
    </table>
    
  </form>

</div>
<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js'></script><script  src="./script.js"></script>

</body>
</html>
