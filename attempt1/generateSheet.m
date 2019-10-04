%% Step 0:
% Set up environment and variables
clear
load("DraftsAndStats.mat")
% Uncomment the following line to switch to the testing data set
TrainDraft = train;
%TrainDraft = DraftPrelim;

%% Step 1:
% Take Draft Year, Made NBA, Draft Position, NBA Performance Rating, Name
% from trainList
draftList = TrainDraft(:, 23);
madeNBA = ones(height(TrainDraft), 1);
draftPosition = TrainDraft(:, 2);
name = TrainDraft(:, 4);
NBAPR = TrainDraft(:, 21);

%% Step 2:
% Match name with CollegeStats name, get College WS, College Adjusted BPM, and
% College PER

nameStatsList = table2array(CollegeStats(:, 1));
firstLetterIndexList = [1];
lastLetter = "A";
for j = 1:height(CollegeStats)
    currentName = char(CollegeStats{j, 1});
    firstLetter = currentName(1);
    if (firstLetter > lastLetter)
        lastLetter = firstLetter;
        firstLetterIndexList = [firstLetterIndexList ; j];
    end
end
firstLetterIndexList = [firstLetterIndexList ; height(CollegeStats)]

collegeWS = [];
collegeBPM = [];
collegePER = [];

currentLetter = "A";
letterIndex = 1;
letterArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
for i = 1:height(name)
    display(i)
    seasonsList = [];
    
    currentName = char(name{i, 1});
    currentLetter = currentName(1);
    while (currentLetter > letterArray(1, letterIndex))
        letterIndex = letterIndex + 1;
    end
    
    for j = firstLetterIndexList(letterIndex, 1):(firstLetterIndexList(letterIndex + 1, 1))
        if (strcmp(char(CollegeStats{j, 1}), currentName))
            seasonsList = [seasonsList ; CollegeStats(j, :)];
        end
    end
    
    display(seasonsList)
    if (~isempty(seasonsList))
        bestLine = seasonsList(1, :);
        for j = 2:height(seasonsList)
            if (seasonsList{j, 6} > bestLine{1, 6})
                bestLine = seasonsList(j, :);
            end
        end
   
        collegeWS = [collegeWS ; bestLine{1, 20}];
        collegeBPM = [collegeBPM ; bestLine{1, 40}];
        collegePER = [collegePER ; bestLine{1, 36}];
    else
        collegeWS = [collegeWS ; -1];
        collegeBPM = [collegeBPM ; -1];
        collegePER = [collegePER ; -1];
    end
end

collegeWS = array2table(collegeWS);
collegeBPM = array2table(collegeBPM);
collegePER = array2table(collegePER);
madeNBA = array2table(madeNBA);

tempFinalTable = [draftList madeNBA draftPosition NBAPR name collegeWS collegeBPM collegePER];

%% Step 3 (add after preliminary results):
% Match name with FinalPlayerInfo name, get Position, Scouting Report,
% Height, Wingspan, Age

