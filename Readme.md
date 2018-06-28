<h1>Boston House Prices Prediction </h1>	
This is a set of regression algorithms from Scikit-Learn applied to Boston House-Prices dataset. 

The dataset has a total of 506 samples with a size of 13, features are real positive values and targets are real between 5. and 50.

<h3> The differents algorithms are: </h3>
	
	1 DecisionTreeRegressor + AdaBoostRegressor 
	2 GradientBoostingRegressor 
	3 DecisionTreeRegressor + BaggingRegressor 
	4 RandomForestRegressor 
	5 LinearRegression + PolynomialFeatures 
	6 LinearRegression + cross validation + shuffle 
	7 TheilSenRegressor	
	8 LinearRegression	
	9 Ridge				
	10 LassoLarsIC			
	11 LassoLarsCV			
	12 BayesianRidge		
	13 KNeighborsRegressor 
	14 LassoCV 			
	15 LassoLars 			
	16 ElasticNet		
	17 ElasticNetCV		
	18 Lasso 				

<h2>Results</h2>

	1 DecisionTreeRegressor + AdaBoostRegressor	0.9058848482560361
	2 GradientBoostingRegressor	0.9004081518446372
	3 DecisionTreeRegressor + BaggingRegressor	0.8883071541276555
	4 RandomForestRegressor	0.8673260573834707
	5 LinearRegression + PolynomialFeatures	0.8594983915127037
	6 cross validation + LinearRegression + shuffle	0.7827154987983166
	7 TheilSenRegressor	0.7517901384800154
	8 LinearRegression	0.7170072626212324
	9 Ridge 	0.7170055142174159
	10 LassoLarsIC	0.7161240975333176
	11 LassoLarsCV	0.7143072566943974
	12 BayesianRidge	0.6860957384645389
	13 KNeighborsRegressor	0.6563295078414701
	14 LassoCV 	0.6431280600783202
	15 LassoLars 	0.6262661585576621
	16 ElasticNet 	0.6204130713553642
	17 ElasticNetCV 0.6011581191235758
	18 Lasso 	0.5233967232760778

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

<h2>Contributing</h2>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.