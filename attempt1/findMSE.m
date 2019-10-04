%% findMSE

%% Step 0:
% load environment
clear all;
load('2007Drafts.mat');
mockDraft = mockDraft2007;

%% Step 1:
% Finding average BPM:
total = 0;
count = 0;
for i = 1:height(FinalBPM)
    if ~isnan(FinalBPM{i, 1})
        total = total + FinalBPM{i, 1};
        count = count + 1;
    end
end
averageBPM = total / count;

%% Step 2:
% Predict baseline MSE
predictedBPMs = [];
actualBPMs = [];
averageBPMs = [];
for i = 1:height(mockDraft)
    if ~isnan(mockDraft{i, 1})
        predictedBPMs = [predictedBPMs ; mockDraft(i, 7)];
        actualBPMs = [actualBPMs ; mockDraft(i, 5)];
        averageBPMs = [averageBPMs ; averageBPM];
    end
end
%%
%predictedBPMs = table2array(predictedBPMs);
%actualBPMs = table2array(actualBPMs);
%averageBPMs = table2array(averageBPMs);

baselineMSE = mean((predictedBPMs - actualBPMs) .^ 2)
predictionMSE = mean((averageBPMs - actualBPMs) .^ 2)