<h1>Boston House Prices Prediction </h1>	
This is a set of regression algorithms from Scikit-Learn applied to Boston House-Prices dataset. 

The dataset has a total of 506 samples with a size of 13, features are real positive values and targets are real between 5. and 50.		

<h2>Results</h2>

<table>
  <tr>
    <th>Algorithm</th>
    <th>Model performance</th> 
  </tr>
  <tr> <td>DecisionTreeRegressor + AdaBoostRegressor</td>   <td>0.9058848482560361</td> </tr>
  <tr> <td>GradientBoostingRegressor</td>   <td>0.9004081518446372</td> </tr>
  <tr> <td>DecisionTreeRegressor + BaggingRegressor</td>   <td>0.8883071541276555</td> </tr>
  <tr> <td>RandomForestRegressor</td>   <td>0.8673260573834707</td> </tr>
  <tr> <td>LinearRegression + PolynomialFeatures</td>   <td>0.8594983915127037</td> </tr>
  <tr> <td>Cross validation + LinearRegression + shuffle</td>   <td>0.7827154987983166</td> </tr>
  <tr> <td>TheilSenRegressor</td>   <td>0.7517901384800154</td> </tr>
  <tr> <td>LinearRegression</td>   <td>0.7170072626212324</td> </tr>
  <tr> <td>Ridge</td>   <td>0.7170055142174159</td> </tr>
  <tr> <td>LassoLarsIC</td>   <td>0.7161240975333176</td> </tr>
  <tr> <td>LassoLarsCV</td>   <td>0.7143072566943974</td> </tr>
  <tr> <td>BayesianRidge</td>   <td>0.6860957384645389</td> </tr>
  <tr> <td>KNeighborsRegressor</td>   <td>0.6563295078414701</td> </tr>
  <tr> <td>LassoCV</td>   <td>0.6431280600783202</td> </tr>
  <tr> <td>LassoLars</td>   <td>0.6262661585576621</td> </tr>
  <tr> <td>ElasticNet</td>   <td>0.6204130713553642</td> </tr>
  <tr> <td>ElasticNetCV</td>   <td>0.6011581191235758</td> </tr>
  <tr> <td>Lasso</td>   <td>0.5233967232760778</td> </tr>
</table>

<h2>Requirements</h2>
Python 2.7 and up

<h2>Installation</h2>
The followoing are the prerequiste Python modules that needs to be installed to execute main.py:

	sudo pip install pandas
	sudo pip install -U scikit-learn
	sudo pip install numpy

<h2>Downloads</h2>
Clone the repository using the below mentioned command and execute the Python program.
	
	git clone https://github.com/Sehaba95/House-Price-Prediction-Boston-.git
	cd House-Price-Prediction-Boston-/Algorithms
	python AdaBoostRegressor.py

<h2>Authors</h2>

	Sehaba Amine
