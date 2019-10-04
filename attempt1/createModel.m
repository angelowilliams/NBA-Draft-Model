%% Step 0:
% Set up environment and variables
%clear
%load("ModelSets.mat")

%% Step 2:
% Create model from training data
y = table2array(trainSet(:, 4));
X = table2array([array2table(ones(height(trainSet), 1)) trainSet(:, 6:8)]);

%b = regress(trainSet(:, 4), [array2table(ones(height(trainSet), 1)) trainSet(:, 6:8)]);
b = regress(y, X);

%% Step 3:
% Test model on test data
testSet = [ testSet array2table(b(1) + b(2)*table2array(testSet(:, 6)) + b(3)*table2array(testSet(:, 7)) + b(4)*table2array(testSet(:, 8))) ];