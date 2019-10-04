%% Step 0:
% Set up environment and variables
clear
load("draftData.mat")

%% Step 1:
% Set training set and testing set
trainSet = [draft2003 ; draft2004 ; draft2005 ; draft2006 ; draft2008 ; draft2009 ; draft2010 ; draft2011 ; draft2012 ; draft2013];
testSet = draft2007;

%% Step 2:
% Create model from training data
y = table2array(trainSet(:, 6));
X = table2array([array2table(ones(height(trainSet), 1)) trainSet(:, 7:9)]);

b = regress(y, X);

%% Step 3:
% Test model on test data
testSet = [ testSet (array2table(b(1) + b(2)*table2array(testSet(:, 7)) + b(3)*table2array(testSet(:, 8)) + b(4)*table2array(testSet(:, 9)))) ];