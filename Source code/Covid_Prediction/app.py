from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return '<html><body  style="background-color: #FCDEC0;"><br> <h1 style=" text-align: center; ">COVID PREDICTION</h1> <br> <p> <h2>If you have found Disease in the test, Then enter  YES . <br> If you have not found Disease in the test, Then enter  NO .</h2></p><br><form name="myForm" onsubmit="return validateForm()" method="post"><h2 style="text-align:center;"><label for="result1">Heart Disease Result:</label><input type="text" id="result1" name="result1"><br><br><label for="result2">Diabetes Result:</label><input type="text" id="result2" name="result2"><br><br><input type="submit" value="Submit"></h2></form> <script>function validateForm() {let x = document.forms["myForm"]["result1"].value;let y = document.forms["myForm"]["result2"].value; if ((x == "YES")&&(y =="YES")){alert(" Danger ! , you are in danger, you will be easily affected by COVID-19, because you are so weak due to heart and Diabetes disease"); } else if ((x == "NO")&&(y =="YES")) {alert("you are likly to be affected by COIVD-19");} else if ((x == "YES")&&(y =="NO")) {alert("you are likly to be affected by COIVD-19");} else if ((x == "NO")&&(y =="NO")) {alert("good ! , your body is in good condition & your healthy, Be safe and maintain your health");} else { alert("Please enter your results"); }   return false; }</script></body></html>'

if __name__ == '__main__':
   app.run(host='localhost' , port=2000)
   
   