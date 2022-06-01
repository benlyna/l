# coding: utf-8

import cgi



html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<style>
*{
	
	
}
body{
    margin: 0;
	padding: 0;
    background-image: url("../TP6/12.jpeg");
    background-size: cover;
background-position: center;
font-family: sans-serif;
	
}
.form-box{
	width: 500px;
	background: rgba(0,0,0,0.8);
	margin:  12% auto; 
	padding: 50px 0;
	color: #fff;
	box-shadow: 0 0 20px 2px rgba(0,0,0,0.5);
}
h1{
	text-align: center;
	margin-bottom: 40px;
}
.input-box{
	margin: 31px auto;
	width: 80%;
	border-bottom: 1px solid #fff;
	padding-top: 10px;
	padding-bottom: 5px;
}
.input-box input{
    width: 90%;
	border: none;
	outline: none;
	background: transparent;
	color: #fff;
}
::placeholder{
	color: #fff;
}
.i{
	margin-right: 10px;
}
.login-btn{
	margin: 40px auto 20px;
	width: 80%;
	display: block;
	padding: 10px 0;
	border: 1px solid #fff;
	cursor: pointer;
	background: transparent;
	color: #fff;
	font-size: 16px;
}
.p {
	color : white;
	background-size: cover;
	
}
h2{
color: #fff;
margin-bottom: 40px;	
}
</style>
<body>

 <div class="form-box">
	<h1>Connexion</h1>
	 <div class="input-box">
		 <i class="fi-xnsuxl-user-solid"></i>
		 <input type="text" name="login" placeholder="login">

	 </div>
	
	 <div class="input-box">
		 <i class="fi-xtluxl-key-alt-thin"></i>
		  <input type="password" name="mdp" placeholder="password">
		
	 </div>
	 <input  type="submit" name="connexion" id="connexion" value="Connexion" class="login-btn"/>

</body>
</html>
"""

print(html)