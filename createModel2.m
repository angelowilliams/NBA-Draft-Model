%% Step 0:
% Set up environment and variables
clear
load("draftData.mat")

%% leave-one-out cross-validation
% Draft Pick

trainSet1 = [draft2011; draft2003; draft2007; draft2012; draft2004; ...
            draft2010; draft2005; draft2006; draft2008; draft2009; ...
            draft2013];
trainSet1 = [trainSet1(:, 8) trainSet1(:, 9:36) trainSet1(:, 40:42) trainSet1(:, 46:48)];

testSet1 = draft2019first;
testSet1 = [testSet1(:, 8) testSet1(:, 9:36) testSet1(:, 40:42) testSet1(:, 46:48)];

predictionMat = []; 
for i = 1:10
    i
    n = 500;
    T = TreeBagger(n, trainSet1(:, 2:width(trainSet1)), trainSet1(:, 1), 'method', 'regression');
    prediction = predict(T, testSet1(:, 2:width(testSet1)));
    predictionMat = [predictionMat prediction];
end
